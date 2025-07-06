import random

systems = {
  "navigation": "NAV-01",
  "communications": "COM-02",
  "life_support": "LIFE-03",
  "engines": "ENG-04",
  "deflector_shield": "SHLD-05"
}

def get_system():
    return random.choice([s for s in systems.keys()])
