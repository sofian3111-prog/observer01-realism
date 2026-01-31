import sys
import os
import time
import getpass

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.realism.engine import RealismEngine

def start_observer():
    secret = "2026"
    # ANSI Color Codes for Terminal UI
    blue = "\033[94m"
    yellow = "\033[93m"
    green = "\033[92m"
    cyan = "\033[96m"
    red = "\033[91m"
    reset = "\033[0m"

    print(f"{blue}" + "="*40 + f"{reset}")
    print(f"{yellow}OBSERVER-01 CONTROL UNIT{reset}")
    print(f"{blue}" + "="*40 + f"{reset}")
    
    try:
        attempt = getpass.getpass("Auth Token Required: ")
    except Exception:
        attempt = input("Auth Token Required: ")

    if attempt != secret:
        print(f"{red}ACCESS DENIED: Unauthorized User.{reset}")
        return

    print(f"{green}SYSTEM ONLINE: Monitoring Assets...{reset}\n")
    engine = RealismEngine()
    
    try:
        while True:
            photo = engine.scan_for_images()
            if photo:
                print(f"{cyan}[DETECTED]{reset} Target: {photo}")
                # Processing and logging
                data = engine.apply_cinematic_filter(photo)
                # Archiving and returning timestamp
                ts = engine.archive_session(photo)
                
                print(f"{green}[SUCCESS]{reset} Metadata: {data}")
                print(f"{green}[ARCHIVE]{reset} Reference ID: {ts}\n")
                print("\a") # Sound beep
            
            time.sleep(2)
            
    except KeyboardInterrupt:
        print(f"\n{yellow}[HALTED]{reset} System Suspended Safely.")

if __name__ == "__main__":
    start_observer()

