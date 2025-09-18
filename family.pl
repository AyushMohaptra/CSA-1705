% A simple knowledge base for a family tree.

% Facts about gender.
male(john).
male(bob).
male(dave).
male(joe).
male(tom).
male(harry).
male(charles).
male(william).

female(susan).
female(mary).
female(jane).
female(sally).
female(kate).
female(diana).
female(elizabeth).

% Facts about parent relationships.
parent_of(john, mary).
parent_of(john, bob).
parent_of(susan, mary).
parent_of(susan, bob).
parent_of(bob, joe).
parent_of(bob, sally).
parent_of(jane, joe).
parent_of(jane, sally).
parent_of(joe, tom).
parent_of(joe, kate).
parent_of(sally, harry).
parent_of(sally, william).
parent_of(dave, jane).
parent_of(dave, bob).
parent_of(mary, charles).
parent_of(mary, diana).
parent_of(charles, elizabeth).
parent_of(diana, elizabeth).


% Rules for family relationships
m(X, Y) :- parent_of(X, Y), female(X).
f(X, Y) :- parent_of(X, Y), male(X).
child(X, Y) :- parent_of(Y, X).
d(X, Y) :- child(X, Y), female(X).
grandf(X, Y) :- f(X, Z), parent_of(Z, Y).
grandfm(X, Y) :- m(X, Z), parent_of(Z, Y).
sis(X, Y) :- parent_of(Z, X), parent_of(Z, Y), X \= Y, female(X).
brother(X, Y) :- parent_of(Z, X), parent_of(Z, Y), X \= Y, male(X).