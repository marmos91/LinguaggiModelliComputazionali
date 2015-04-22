/*
	L = {11(0|1)^m, m > 1} (non deterministico)
*/

regolaS([1|A]) :- regolaA(A).
regolaA([1|C]) :- regolaC(C).
regolaC([0|C]) :- regolaC(C).
regolaC([1|C]) :- regolaC(C).
regolaC([0]).
regolaC([1]).