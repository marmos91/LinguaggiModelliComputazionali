/*
	L = {a^2m b^n, m >=1, n>=1}
*/

regolaS([a|A]) :- regolaA(A).
regolaA([a|B]) :- regolaB(B).
regolaB([a|C]) :- regolaC(C).
regolaC([a|B]) :- regolaB(B).
regolaB([b|F]) :- regolaF(F).
regolaB([b]).
regolaF([b]).