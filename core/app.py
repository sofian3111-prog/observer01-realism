import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.realism.engine import RealismEngine

def run_system():
    print("--- [Observer-01: Phase 5 - Intelligence] ---")
    engine = RealismEngine()
    photo = engine.scan_for_images()
    
    if photo:
        # Step 1: Transformation
        engine.apply_cinematic_filter(photo)
        
        # Step 2: Self-Analysis
        output_name = "cinematic_" + photo
        engine.generate_report(photo, output_name)
        
        print("[Observer-01] Phase 5 complete. System is evolving.")
    else:
        print("[Observer-01] Error: Vision source empty.")

if __name__ == "__main__":
    run_system()

