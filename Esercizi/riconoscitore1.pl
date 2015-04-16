regolaS([a|B]) :- regolaB(B).
regolaB([a|B]) :- regolaB(B).
regolaB([b|S]) :- regolaS(S).
regolaB([a]).