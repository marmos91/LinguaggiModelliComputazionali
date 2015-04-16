/*
	L = {(a)^2n b^n 1 <= n <= 2} (limitato superiormente --> tipo 3)
*/

regolaS([a|A]) :- regolaA(A).
regolaA([a|B]) :- regolaB(B).
regolaB([b|C]) :- regolaC(C).
regolaB([a|D]) :- regolaD(D).
regolaD([a|E]) :- regolaE(E).
regolaE([b|F]) :- regolaF(F).
regolaF([b|C]) :- regolaC(C).
regolaB([b]).
regolaF([b]).
