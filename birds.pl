% A simple knowledge base (database) about birds and their flight ability.

% We define two predicates: can_fly/1 and cannot_fly/1.
% Each predicate represents a fact about a specific bird.

% Birds that can fly:
can_fly(eagle).
can_fly(sparrow).
can_fly(pigeon).
can_fly(albatross).
can_fly(hummingbird).

% Birds that cannot fly:
cannot_fly(penguin).
cannot_fly(ostrich).
cannot_fly(kiwi).
cannot_fly(emu).
cannot_fly(cassowary).

% Here are some example queries you could run in a Prolog interpreter to test the program:

% To check if a sparrow can fly:
% ?- can_fly(sparrow).

% To check if a penguin can fly:
% ?- can_fly(penguin).

% To find all birds that can fly:
% ?- can_fly(Bird).

% To find all birds that cannot fly:
% ?- cannot_fly(Bird).

