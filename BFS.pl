% Best-First Search (BFS) in Prolog

% Example graph with nodes and costs.
% node(Node, Heuristic_Cost).
node(a, 3).
node(b, 2).
node(c, 4).
node(d, 1).
node(e, 0). % Goal node, heuristic cost is 0.

% edge(From_Node, To_Node, Path_Cost).
edge(a, b, 1).
edge(a, c, 5).
edge(b, d, 2).
edge(c, d, 1).
edge(d, e, 3).
edge(d, c, 1).

% Best-First Search predicate.
% search(Initial_Node, Goal_Node, Path)
% The Path is a list of nodes from the initial to the goal.
search(Start, Goal, Path) :-
    search_path([path(Start, [Start], 0)], Goal, Path).

% search_path/3
% Implements the core search logic.
% The queue is a list of paths, ordered by heuristic cost.
search_path([path(Goal, Path, _)|_], Goal, Path).
search_path([path(Current, Path, _)|Queue], Goal, FinalPath) :-
    % Find neighbors of the current node.
    findall(NextState, (edge(Current, Next, Cost)), Neighbors),
    % Create new paths for each neighbor.
    expand(Neighbors, Path, Cost, NewPaths),
    % Merge the new paths into the queue and sort by heuristic cost.
    append(Queue, NewPaths, UnsortedQueue),
    sort_paths(UnsortedQueue, SortedQueue),
    % Continue the search with the best path.
    search_path(SortedQueue, Goal, FinalPath).

% expand/4
% Creates new paths from a list of neighbors.
expand([], _, _, []).
expand([Neighbor|Rest], Path, Cost, [NewPath|RestPaths]) :-
    % Calculate heuristic cost of the new neighbor.
    node(Neighbor, Heuristic),
    NewCost is Cost + Heuristic,
    NewPath = path(Neighbor, [Neighbor|Path], NewCost),
    expand(Rest, Path, Cost, RestPaths).

% sort_paths/2
% Sorts a list of paths by their heuristic cost.
sort_paths(Paths, Sorted) :-
    predsort(compare_paths, Paths, Sorted).

% compare_paths/3
% A comparison predicate for sorting paths.
compare_paths(Result, path(_, _, Cost1), path(_, _, Cost2)) :-
    (   Cost1 < Cost2 -> Result = <
    ;   Cost1 > Cost2 -> Result = >
    ;   Result = = ).