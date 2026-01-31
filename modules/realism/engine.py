import os
import shutil
import datetime
import subprocess

class RealismEngine:
    def __init__(self):
        self.input_path = os.path.expanduser("~/observer01-scaffold/inputs/")
        self.output_path = os.path.expanduser("~/observer01-scaffold/outputs/")

    def scan_for_images(self):
        files = os.listdir(self.input_path)
        images = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png'))]
        return images[0] if images else None

    def apply_cinematic_filter(self, image_name):
        input_file = os.path.join(self.input_path, image_name)
        output_file = os.path.join(self.output_path, "cinematic_" + image_name)
        cmd = f"magick {input_file} -brightness-contrast 10x20 {output_file}"
        subprocess.run(cmd, shell=True)

    def generate_report(self, image_name):
        report_file = os.path.join(self.output_path, "vision_report.txt")
        with open(report_file, "w") as f:
            f.write(f"Report for: {image_name}\nStatus: Processed Successfully")

    def archive_session(self, image_name):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        archive_path = os.path.join(self.output_path, f"archive_{timestamp}")
        os.makedirs(archive_path, exist_ok=True)
        
        processed_file = "cinematic_" + image_name
        if os.path.exists(os.path.join(self.output_path, processed_file)):
            shutil.move(os.path.join(self.output_path, processed_file), archive_path)
            print(f"[Observer-01] Archived to: archive_{timestamp}")

