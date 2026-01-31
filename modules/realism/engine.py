import os
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
        
        print(f"[Observer-01] Injecting cinematic contrast into {image_name}...")
        
        # Using system-level command for real image transformation
        # This increases contrast and adds a slight warm tone
        cmd = f"convert {input_file} -brightness-contrast 10x20 -modulate 100,120 {output_file}"
        
        try:
            subprocess.run(cmd, shell=True, check=True)
            print(f"[Observer-01] Transformation Complete! Check outputs/ folder.")
            return True
        except:
            print("[Observer-01] Error: ImageMagick not found.")
            return False

