import sys
import os
import time
import getpass

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.realism.engine import RealismEngine

def start_observer():
    secret = "2026"
    blue, yellow, green, cyan, red, reset = "\033[94m", "\033[93m", "\033[92m", "\033[96m", "\033[91m", "\033[0m"

    print(f"{blue}" + "="*40 + f"{reset}")
    print(f"{yellow}OBSERVER-01: PHASE 17 ACTIVE{reset}")
    print(f"{blue}" + "="*40 + f"{reset}")
    
    token = getpass.getpass("Auth Token: ")
    if token != secret:
        print(f"{red}Access Denied.{reset}")
        return

    print(f"{green}Protection Shield: Enabled{reset}\n")
    engine = RealismEngine()
    
    try:
        while True:
            target = engine.scan_for_images()
            if target:
                print(f"{cyan}[DETECTED]{reset} {target}")
                result = engine.apply_cinematic_filter(target)
                
                if result:
                    archive_id = engine.archive_session(target)
                    if archive_id:
                        print(f"{green}[SUCCESS]{reset} Logged as: {archive_id}")
                    else:
                        print(f"{red}[ERROR]{reset} Archiving failed.")
                else:
                    print(f"{yellow}[REJECTED]{reset} File corrupt or empty. Purging...")
                    os.remove(os.path.join(engine.input_path, target))
                
                print("\a")
            time.sleep(2)
    except KeyboardInterrupt:
        print(f"\n{yellow}[OFFLINE]{reset} Standby mode.")

if __name__ == "__main__":
    start_observer()

