% A simple knowledge base (database) of planets.

% Each fact represents a planet with its name, type, and
% distance from the sun in millions of kilometers.
% Format: planet(name, type, distance_from_sun_in_million_km).

planet(mercury, terrestrial, 58).
planet(venus, terrestrial, 108).
planet(earth, terrestrial, 150).
planet(mars, terrestrial, 228).
planet(jupiter, gas_giant, 778).
planet(saturn, gas_giant, 1427).
planet(uranus, ice_giant, 2871).
planet(neptune, ice_giant, 4498).

% Predicate to represent the number of known moons for each planet.
% Format: has_moons(planet_name, number_of_moons).
has_moons(mercury, 0).
has_moons(venus, 0).
has_moons(earth, 1).
has_moons(mars, 2).
has_moons(jupiter, 95).
has_moons(saturn, 146).
has_moons(uranus, 27).
has_moons(neptune, 14).

% Here are some example queries you could run in a Prolog interpreter:

% To find all terrestrial planets:
% ?- planet(Name, terrestrial, _).

% To find the distance of Saturn from the sun:
% ?- planet(saturn, _, Distance).

% To find all planets with at least 10 moons:
% ?- has_moons(Planet, NumMoons), NumMoons >= 10.
