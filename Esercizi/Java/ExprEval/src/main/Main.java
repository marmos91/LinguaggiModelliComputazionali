package main;
import java.io.FileInputStream;
import java.io.IOException;
import javax.swing.JOptionPane;
import alice.tuprolog.*;

public class Main {

	public static void main(String[] args) 
	{
		Prolog engine = new Prolog();
		try
		{
			Theory t = new Theory(new FileInputStream("theory.pl"));
			engine.setTheory(t);	
		}
		catch(InvalidTheoryException e)
		{
			System.err.println("Teoria non valida");
			System.exit(1);
		}
		catch(IOException e)
		{
			System.err.println("Errore nella lettura della teoria");
			System.exit(1);
		}
		
		String inputString = JOptionPane.showInputDialog("Inserire l'espressione");
		
		//Sostituisco le parentesi tonde con le quadre perchè il parser prolog non accetta 
		//in ingresso le parentesi tonde
		String prologInputString = inputString.replace("(", "[").replace(")", "]");
		
		try
		{
			Term expression = Term.parse(prologInputString);
			Term query = new Struct("evalExpr", expression, new Var("Result"));
			
			SolveInfo info = engine.solve(query);
			
			if(info.isSuccess())
			{
				Term resultTerm = info.getTerm("Result");
				JOptionPane.showMessageDialog(null, ("Il risultato di "+ inputString +" è " + resultTerm), "Risultato", JOptionPane.INFORMATION_MESSAGE);
			}
			else
			{
				JOptionPane.showMessageDialog(null, ("Nessuna soluzione"), "Risultato", JOptionPane.INFORMATION_MESSAGE);
			}
			
			//Termino i thread delle finestre di dialogo
			System.exit(0);
		}
		catch(InvalidTermException e)
		{
			System.err.println("L'espressione non è valida in Prolog");
			System.exit(1);
			
		}
		catch (NoSolutionException e) 
		{
			System.err.println("Errore. Nessuna soluzione all'espressione");
			System.exit(1);
		} 
		catch (UnknownVarException e) 
		{
			System.err.println("Nome della variabile sconosciuto");
			System.exit(1);
		}
	}

}
