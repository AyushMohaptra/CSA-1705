% Predicate to check if a character is a vowel, handling both uppercase and lowercase.
is_vowel(C) :-
    member(C, [a,e,i,o,u,A,E,I,O,U]).

% Base case: The number of vowels in an empty list (string) is 0.
count_vowels([], 0).

% Recursive case:
count_vowels([H|T], Count) :-
    % Recursively count vowels in the rest of the list.
    count_vowels(T, Rest),
    % Check if the head of the list is a vowel.
    (is_vowel(H) ->
        Count is Rest + 1 % If it is, increment the count.
    ;
        Count = Rest % Otherwise, the count is unchanged.
    ).

% Example queries:
% To count vowels in a string:
% ?- count_vowels("Hello World", Vowels).
% Vowels = 3.

% To count vowels in a different string:
% ?- count_vowels("Prolog", Vowels).
% Vowels = 2.
