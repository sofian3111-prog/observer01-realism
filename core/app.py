import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.realism.engine import RealismEngine

def run_observer_system():
    print("[Observer-01] Starting Intelligent Vision System...")
    engine = RealismEngine()
    
    # Looking for your photo
    photo = engine.scan_for_images()
    
    if photo:
        print(f"[Observer-01] Image found: {photo}")
        engine.apply_cinematic_filter(photo)
        print("[Observer-01] Workflow complete.")
    else:
        print("[Observer-01] No images found. Please check inputs/ folder.")

if __name__ == "__main__":
    run_observer_system()

