import sys
import os
import time
import getpass

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.realism.engine import RealismEngine

def start_observer_auto_mode():
    # Security Layer
    secret_key = "2026"
    print("--- [Observer-01: Security Access] ---")
    user_input = getpass.getpass("Enter Access Key: ")

    if user_input != secret_key:
        print("Access Denied: Unauthorized User.")
        return

    print("Access Granted. Initializing...")
    engine = RealismEngine()
    
    try:
        while True:
            photo = engine.scan_for_images()
            if photo:
                engine.apply_cinematic_filter(photo)
                engine.generate_report(photo)
                engine.archive_session(photo)
            time.sleep(5) 
            
    except KeyboardInterrupt:
        print("\n[Observer-01] Suspended.")

if __name__ == "__main__":
    start_observer_auto_mode()

