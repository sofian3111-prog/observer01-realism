import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.realism.engine import RealismEngine

def start_observer_auto_mode():
    print("--- [Observer-01: Phase 6 - Active Monitoring] ---")
    engine = RealismEngine()
    
    print("[Observer-01] System is now watching for new visual inputs...")
    
    try:
        while True:
            photo = engine.scan_for_images()
            if photo:
                engine.apply_cinematic_filter(photo)
                engine.generate_report(photo)
                # Correct placement of archiving inside the monitoring loop
                engine.archive_session(photo)
                
                print("[Observer-01] Cycle Complete. Waiting for next input...")
            
            time.sleep(5) 
            
    except KeyboardInterrupt:
        print("\n[Observer-01] Monitoring suspended by user.")

if __name__ == "__main__":
    start_observer_auto_mode()

