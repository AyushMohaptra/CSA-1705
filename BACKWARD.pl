% A simple knowledge base with facts and rules.

% Facts (the knowledge base).
fact(has_feathers).
fact(can_fly).
fact(is_small).

% Rules (if-then statements).
rule(is_a_bird, [has_feathers, can_fly]).
rule(is_a_sparrow, [is_a_bird, is_small]).

% Backward chaining predicate.
% A goal is proven if it's a fact.
prove(Goal) :-
    fact(Goal).

% A goal is proven if it's the conclusion of a rule,
% and all of the rule's conditions can be proven.
prove(Goal) :-
    rule(Goal, Conditions),
    forall(member(Condition, Conditions), prove(Condition)).

% Example queries:
% To prove 'is_a_bird':
% ?- prove(is_a_bird).

% To prove 'is_a_sparrow':
% ?- prove(is_a_sparrow).

% To prove something that is not true:
% ?- prove(is_a_mammal).
