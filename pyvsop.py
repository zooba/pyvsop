from datetime import timedelta
from vsop import planets
from vsop.util import daterange, SolarSystemMap

print("Loading data...")
PLANETS = [
    ("m", planets.Mercury),
    ("V", planets.Venus),
    ("E", planets.Earth),
    ("M", planets.Mars),
]

for date in daterange(2015, 2016, step=timedelta(days=7)):
    # Create a map of the solar system on a particular day
    ss_map = SolarSystemMap(100, 27, date)
    
    for initial, planet_type in PLANETS:
        planet = planet_type()
        
        ss_map.add_planet(initial, planet)

    print('\n{}\n{}'.format(date, ss_map), end='')
    try:
        input()
    except EOFError:
        break

print()
