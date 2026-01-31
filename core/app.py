import sys, os, time, getpass
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.realism.engine import RealismEngine

def start_observer():
    secret = "2026"
    blue, yellow, green, cyan, red, reset = "\033[94m", "\033[93m", "\033[92m", "\033[96m", "\033[91m", "\033[0m"
    
    print(f"{blue}{'='*40}\n{yellow}OBSERVER-01: PHASE 23 ACTIVE\n{'='*40}{reset}")
    
    if getpass.getpass("Auth Token: ") != secret:
        print(f"{red}Access Denied.{reset}"); return
    
    engine = RealismEngine()
    
    # Dashboard Logic
    report_path = engine.generate_daily_report()
    print(f"{cyan}--- SESSION PREVIEW ---")
    with open(report_path, 'r') as f:
        print(f"{f.read()}")
    print(f"-----------------------{reset}")
    
    print(f"{green}System Online. Monitoring inputs...{reset}\n")
    
    try:
        while True:
            target = engine.scan_for_images()
            if target:
                print(f"{cyan}[DETECTED]{reset} {target}")
                if engine.apply_cinematic_filter(target):
                    log_id = engine.archive_session(target)
                    print(f"{green}[SUCCESS]{reset} Archived: {log_id}")
                else:
                    print(f"{yellow}[REJECTED]{reset} Bad file."); os.remove(os.path.join(engine.input_path, target))
            time.sleep(2)
    except KeyboardInterrupt:
        path = engine.generate_daily_report()
        print(f"\n{yellow}[OFFLINE]{reset} Final Report: {path}")

if __name__ == "__main__":
    start_observer()

