person(john_doe, dob(15, 3, 1990)).
person(jane_smith, dob(21, 7, 1985)).
person(peter_jones, dob(10, 1, 2001)).
person(mary_brown, dob(28, 5, 1992)).
person(mike_green, dob(3, 11, 1975)).

% You can query this database to find information.
% Here are some example queries you could run in a Prolog interpreter:

% Query to find the birth year of a specific person:
% ?- person(john_doe, dob(_, _, Year)).

% Query to find everyone born in 1990:
% ?- person(Name, dob(_, _, 1990)).

% Query to find the month someone was born:
% ?- person(peter_jones, dob(_, Month, _)).
