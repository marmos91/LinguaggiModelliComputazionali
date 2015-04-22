evalExpr(Term, Value) :- evalTerm(Term, Value).
evalExpr(Exp+Term, Value) :- evalExpr(Exp, Value1), evalTerm(Term, Value2), Value is Value1 + Value2.
evalExpr(Exp-Term, Value) :- evalExpr(Exp, Value1), evalTerm(Term, Value2), Value is Value1 - Value2.
evalTerm(Factor, Value) :- evalFactor(Factor, Value).
evalTerm(Term*Factor, Value) :- evalTerm(Term, Value1), evalFactor(Factor, Value2), Value is Value1 * Value2.
evalTerm(Term/Factor) :- evalTerm(Term, Value1), evalFactor(Factor, Value2), Value is Value1 / Value2.
evalFactor([Exp], Value) :- evalExpr(Exp, Value).
evalFactor(Num, Num) :- number(Num).