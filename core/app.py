import sys
import os

# Adding the modules path to the system
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.realism.engine import RealismEngine

def initialize_observer():
    print("[Observer-01] Initializing System...")
    
    # Initialize the Realism Engine
    engine = RealismEngine()
    
    # Run lighting enhancement
    engine.enhance_lighting(intensity=2.0)
    
    # Apply textures
    engine.apply_textures()
    
    print("[Observer-01] System is now Cinematic and Ready.")

if __name__ == "__main__":
    initialize_observer()

