import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.realism.engine import RealismEngine

def run_vision_inspection():
    print("--- [Observer-01 Vision Phase 4] ---")
    engine = RealismEngine()
    photo = engine.scan_for_images()
    
    if photo:
        # Performing the breakthrough analysis
        engine.apply_cinematic_filter(photo)
        print(f"[Observer-01] Identity Confirmed: {photo}")
        print("[Observer-01] Ready for Neural Enhancement.")
    else:
        print("[Observer-01] Fatal Error: Subject not found in inputs.")

if __name__ == "__main__":
    run_vision_inspection()

