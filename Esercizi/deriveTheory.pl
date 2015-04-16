/* Generiche */

dExpr(T, DT) :- dTerm(T, DT).
dExpr(E+T, [DE+DT]) :- dExpr(E, DE), dTerm(T, DT).
dExpr(E-T, [DE-DT]) :- dExpr(E, DE), dTerm(T, DT).
dTerm(F, DF) :- dFactor(F, DF).
dTerm(T*F, [[DT*F]+[T*DF]]) :- dTerm(T, DT), dFactor(F, DF).
dTerm(T/F, [[F*DT]-[T*DF]] / [E*F]) :- dTerm(T, DT), dFactor(F, DF).

/* Specifiche */
dFactor(x, 1).
dFactor(N, 0) :- number(N).
dFactor([E], DE) :- dExpr(E, DE).
dFactor(-E, -DE) :- dExpr(E, DE).
dFactor(sin(x), cos(x)) :- !.
dFactor(cos(x), -sin(x)) :- !.
dFactor(sin(E), [cos(E)*DE]) :- dExpr(E, DE).
dFactor(cos(E), [-sin(E)*DE]) :- dExpr(E, DE).
dFactor(x^N, [N*x^(N1)]) :- N1 is N-1, !.
dFactor(E^N, [N*E^(Nm1)*(DE)]) :- dExpr(E, DE), Nm1 is N-1.