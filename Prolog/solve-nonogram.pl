:- use_module(library(clpfd)).
 
nono(RowSpec, ColSpec, Grid) :-
	rows(RowSpec, Grid),
	transpose(Grid, GridT),
	rows(ColSpec, GridT).
 
rows([], []).
rows([C|Cs], [R|Rs]) :-
	row(C, R),
	rows(Cs, Rs).
 
row(Ks, Row) :-
	sum(Ks, #=, Ones),
	arcs(Ks, Arcs, start, Final),
	append(Row, [0], RowZ),
	automaton(RowZ, [source(start), sink(Final)], [arc(start,0,start) | Arcs]).
 
% Créer la liste de transtion pour arriver à un état fini
arcs([], [], Final, Final).
arcs([K|Ks], Arcs, CurState, Final) :-
	gensym(state, NextState),
	(   K == 0
	->  Arcs = [arc(CurState,0,CurState), arc(CurState,0,NextState) | Rest],
	    arcs(Ks, Rest, NextState, Final)
	;   Arcs = [arc(CurState,1,NextState) | Rest],
	    K1 #= K-1,
	    arcs([K1|Ks], Rest, NextState, Final)).
 
 
make_grid(Grid, X, Y) :-
	length(Grid,X),
	make_rows(Grid, Y).
 
make_rows([], _).
make_rows([R|Rs], Len) :-
	length(R, Len),
	make_rows(Rs, Len).
 
print([], Stream).
print([R|Rs], Stream) :-
	print_row(R, Stream),
	print(Rs, Stream).
 
print_row([], Stream) :- nl(Stream), nl.
print_row([X|R], Stream) :-
	(   X == 0
	->  write('.'),
	write(Stream,'.')
	;   write('x'), 
	write(Stream, 'x')),
	print_row(R, Stream).
 
nonogram(Rows, Cols, Stream) :-
	length(Rows, X),
	length(Cols, Y),
	make_grid(Grid, X, Y),
	nono(Rows, Cols, Grid),
	print(Grid, Stream).
	
	