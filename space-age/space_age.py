EARTH_SECONDS = 31557600
PLANETS = {
    'earth': EARTH_SECONDS,
    'mercury': 0.2408467 * EARTH_SECONDS,
    'venus': 0.61519726 * EARTH_SECONDS,
    'mars': 1.8808158 * EARTH_SECONDS,
    'jupiter': 11.862615 * EARTH_SECONDS,
    'saturn': 29.447498 * EARTH_SECONDS,
    'uranus': 84.016846 * EARTH_SECONDS,
    'neptune': 164.79132 * EARTH_SECONDS,
}

class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
        for planet in PLANETS:
            func = lambda p = planet: round(seconds / PLANETS[p], 2)
            setattr(self, 'on_' + planet, func)
