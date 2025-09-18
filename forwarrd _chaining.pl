% A simple forward chaining system.

% Initial facts (the working memory).
fact(warm).
fact(wet).

% Rules to infer new facts.
% rule(Conclusion, [Condition1, Condition2, ...]).
rule(rainy, [warm, wet]).
rule(stormy, [rainy, windy]).

% A predicate to infer all possible new facts.
infer :-
    rule(Conclusion, Conditions),
    \+ fact(Conclusion), % The conclusion is not already a fact.
    forall(member(Condition, Conditions), fact(Condition)),
    assertz(fact(Conclusion)),
    infer. % Recursively call to find more facts.

% Base case for the recursion.
infer.

% Predicate to run the forward chaining process.
forward_chaining :-
    % Start by asserting all initial facts.
    % In this simple example, we just call infer.
    write('Initial facts:'), nl,
    findall(F, fact(F), Facts),
    writeln(Facts),
    write('Starting inference...'), nl,
    infer,
    write('Final facts:'), nl,
    findall(F, fact(F), FinalFacts),
    writeln(FinalFacts).

% Example query:
% ?- forward_chaining.
