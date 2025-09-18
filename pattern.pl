% A simple knowledge base of items and their types.
% Format: item(Name, Type).
item(apple, fruit).
item(carrot, vegetable).
item(banana, fruit).
item(broccoli, vegetable).
item(chair, furniture).
item(table, furniture).

% A predicate to find the type of a given item.
% The variable `Type` in the head of the rule matches the second argument of the `item` fact.
find_type(Item, Type) :-
    item(Item, Type).

% A predicate to find all items of a specific type.
% The variable `Item` matches the first argument of the `item` fact.
% The second argument is a specific value, 'fruit', which is a pattern.
find_all_of_type(Item, fruit) :-
    item(Item, fruit).

% Example queries:
% To find the type of 'apple':
% ?- find_type(apple, Type).

% To find all fruits:
% ?- find_all_of_type(Fruit, fruit).

% You can also query directly:
% ?- item(apple, Type).

% To find all furniture items:
% ?- item(Item, furniture).