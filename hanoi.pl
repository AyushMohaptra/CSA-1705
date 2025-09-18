% Predicate to solve the Towers of Hanoi problem.
% hanoi(N, A, B, C) moves N discs from peg A to peg C, using peg B as auxiliary.

% Base case: Moving 0 discs requires no steps.
hanoi(0, _, _, _) :-
    !.

% Recursive step:
% To move N discs from A to C:
% 1. Move N-1 discs from A to B (using C).
% 2. Move the largest disc (N) from A to C.
% 3. Move N-1 discs from B to C (using A).
hanoi(N, A, B, C) :-
    N > 0,
    N1 is N - 1,
    hanoi(N1, A, C, B),
    format('Move disc from ~w to ~w~n', [A, C]),
    hanoi(N1, B, A, C).