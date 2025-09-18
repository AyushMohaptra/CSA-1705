% Monkey Banana Problem in Prolog
% State: state(Monkey_Position, Box_Position, Monkey_Height, Has_Banana)

% Goal state: the monkey has the banana.
canget(state(_, _, _, has_it)).

% Move rules (all in one go for brevity)
canget(state(M, B, H, has_not)) :-
    (
        M \= B, B = at_center,
        ( H = on_floor, move(state(M, B, H, has_not), walk(_, B), NewState);
          H = on_box, move(state(M, B, H, has_not), climb, NewState)
        )
    );
    (
        M = B, B = at_center,
        ( H = on_floor, move(state(M, B, H, has_not), push(_, at_banana), NewState);
          H = on_box, move(state(M, B, H, has_not), grasp, NewState)
        )
    ),
    canget(NewState).

% A rule to find a sequence of moves to the goal.
canget(State) :-
    move(Initial, _, State).
canget(State) :-
    move(Initial, _, Intermediate),
    canget(Intermediate).
