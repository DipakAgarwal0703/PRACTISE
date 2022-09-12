package day2;
import java.util.*;
public class Average 
{
	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		double eng,maths,phy,chem,bio,average,total;
		System.out.println("Enter the marks of Student");
		System.out.print("\nEnglish:");
		eng=sc.nextDouble();
		System.out.print("\nPhysics:");
		phy=sc.nextDouble();
		System.out.print("\nMathematics:");
		maths=sc.nextDouble();
		System.out.print("\nChemistry:");
		chem=sc.nextDouble();
		System.out.print("\nBiology:");
		bio=sc.nextDouble();
		total=eng+phy+maths+chem+bio;
		average=total/5;
		System.out.print("\nThe total marks of the student is:"+total);
		System.out.print("\nThe percentage of the student is:"+average);
	}

}
