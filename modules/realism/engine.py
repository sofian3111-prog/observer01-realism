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
        return result.stdout.strip() if result.returncode == 0 else "Offline-Mode"

    def apply_cinematic_filter(self, image_name):
        input_file = os.path.join(self.input_path, image_name)
        output_file = os.path.join(self.output_path, "cinematic_" + image_name)
        data = self.analyze_image(input_file)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO logs (timestamp, filename, metadata) VALUES (?, ?, ?)", 
                       (datetime.datetime.now().isoformat(), image_name, data))
        conn.commit()
        conn.close()
        cmd = f"magick {input_file} -brightness-contrast 10x20 {output_file}"
        subprocess.run(cmd, shell=True)
        return data

    def archive_session(self, image_name):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        archive_path = os.path.join(self.output_path, f"archive_{timestamp}")
        os.makedirs(archive_path, exist_ok=True)
        processed_file = "cinematic_" + image_name
        original_file = os.path.join(self.input_path, image_name)
        if os.path.exists(os.path.join(self.output_path, processed_file)):
            shutil.move(os.path.join(self.output_path, processed_file), archive_path)
        if os.path.exists(original_file):
            os.remove(original_file)
        return timestamp

