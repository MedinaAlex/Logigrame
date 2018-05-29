:- include('solve-nonogram.pl').
	
main :-
		open('result_prolog.txt',write,Stream2),
		/* Puzzle dinosaure*/
		statistics(walltime, [TimeSinceStart | [TimeSinceLastCall]]),
    open('dinosaure.txt', read, Str),
    read_file(Str,Lines, Stream2),
		statistics(walltime, [NewTimeSinceStart | [ExecutionTime]]),
		write('Execution took '), write(ExecutionTime), write(' ms.'), nl,
		nl(Stream2),
		
		/* Puzzle escargot*/
		statistics(walltime, [TimeSinceStart2 | [TimeSinceLastCall2]]),
		open('escargot.txt', read, Str2),
    read_file(Str2,Lines2, Stream2),
		statistics(walltime, [NewTimeSinceStart2 | [ExecutionTime2]]),
		write('Execution took '), write(ExecutionTime2), write(' ms.'), nl,
		nl(Stream2),
		
		/* Puzzle piano*/
		statistics(walltime, [TimeSinceStart3 | [TimeSinceLastCall3]]),
		open('piano.txt', read, Str3),
    read_file(Str3,Lines3, Stream2),
		statistics(walltime, [NewTimeSinceStart3 | [ExecutionTime3]]),
		write('Execution took '), write(ExecutionTime3), write(' ms.'), nl,
		nl(Stream2),
		
		/* Puzzle bufle*/
		statistics(walltime, [TimeSinceStart4 | [TimeSinceLastCall4]]),
		open('buffle.txt', read, Str4),
    read_file(Str4,Lines4, Stream2),
		statistics(walltime, [NewTimeSinceStart4 | [ExecutionTime4]]),
		write('Execution took '), write(ExecutionTime4), write(' ms.'), nl,
		nl(Stream2),
		
    close(Str),
		close(Str2),
		close(Str3),
		close(Str4),
		close(Stream2).


read_file(Stream,[X|L], Stream2) :-
    read(Stream,X),
		write(X), nl,
		read(Stream,L),
		write(L), nl,
		nonogram(X,L, Stream2).
		
