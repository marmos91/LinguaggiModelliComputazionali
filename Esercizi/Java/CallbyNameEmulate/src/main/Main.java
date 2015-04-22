package main;
import main.MixedClass;

public class Main 
{
	static void func(Boolean cond, MixedClass a, B b)
	{
		if(cond) 
			System.out.println(a.invoke());
		else
			System.out.println(b.invoke());
	}
	
	public static void main(String[] args) 
	{
		int x = 2, y = 3;
		func((x<3), new MixedClass(), new B());
	}

}
