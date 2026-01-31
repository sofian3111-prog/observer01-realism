import os
import shutil
import datetime
import subprocess
import sqlite3

class RealismEngine:
    def __init__(self):
        self.input_path = os.path.expanduser("~/observer01-scaffold/inputs/")
        self.output_path = os.path.expanduser("~/observer01-scaffold/outputs/")
        self.db_path = os.path.expanduser("~/observer01-scaffold/observer.db")
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS logs 
                          (id INTEGER PRIMARY KEY, timestamp TEXT, filename TEXT, metadata TEXT)''')
        conn.commit()
        conn.close()

    def scan_for_images(self):
        if not os.path.exists(self.input_path):
            os.makedirs(self.input_path)
        files = os.listdir(self.input_path)
        images = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png'))]
        return images[0] if images else None

    def analyze_image(self, image_path):
        cmd = f"magick identify -format '%m | %wx%h' {image_path}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip() if result.returncode == 0 else "Analysis Error"

    def apply_cinematic_filter(self, image_name):
        input_file = os.path.join(self.input_path, image_name)
        output_file = os.path.join(self.output_path, "cinematic_" + image_name)
        
        if not os.path.exists(input_file) or os.path.getsize(input_file) < 100:
            return None

        hour = datetime.datetime.now().hour
        if 6 <= hour < 18:
            effect = "-modulate 100,120,100 -fill orange -colorize 10%"
            mode = "DAY_MODE"
        else:
            effect = "-modulate 80,110,100 -fill blue -colorize 15%"
            mode = "NIGHT_MODE"

        data = f"{self.analyze_image(input_file)} | {mode}"
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO logs (timestamp, filename, metadata) VALUES (?, ?, ?)", 
                       (datetime.datetime.now().isoformat(), image_name, data))
        conn.commit()
        conn.close()

        # Watermark and Filter Command
        cmd = f"magick {input_file} {effect} -fill white -gravity SouthEast -pointsize 25 -annotate +20+20 'OBSERVER-01' {output_file}"
        subprocess.run(cmd, shell=True)
        return data

    def archive_session(self, image_name):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        archive_path = os.path.join(self.output_path, f"archive_{timestamp}")
        processed_file = os.path.join(self.output_path, "cinematic_" + image_name)
        original_file = os.path.join(self.input_path, image_name)
        if os.path.exists(processed_file):
            os.makedirs(archive_path, exist_ok=True)
            shutil.move(processed_file, archive_path)
            if os.path.exists(original_file): os.remove(original_file)
            return timestamp
        return None

    def generate_daily_report(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM logs")
        total = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM logs WHERE metadata LIKE '%DAY_MODE%'")
        day = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM logs WHERE metadata LIKE '%NIGHT_MODE%'")
        night = cursor.fetchone()[0]
        report = f"OBSERVER-01 REPORT\nTotal: {total}\nDay: {day}\nNight: {night}"
        report_path = os.path.join(self.output_path, "daily_report.txt")
        with open(report_path, "w") as f: f.write(report)
        conn.close()
        return report_path

