package For_Testing;
import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.stream.*;

public class AST_Assignment_2 {

	public static List<String> myListresult = new ArrayList<>();
	public static int exercise_5_user_input()
	{	
		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter the value of n:");
		int n = scanner.nextInt();
		scanner.close();
		return n;
	}
	
	public static <T> List<String> primes(long max)
	{
		int min = 1;
		int num=0;
		int i=0;
		List<Integer> list = new ArrayList<>();
		
		String primenumbers="";
		if (max == 2) {System.out.println(2);}
		for (i = 1; i <= max; i++)  	   
		{ 		 		  
		   int counter=0; 		  
		   for(num =i; num>=1; num--)
		   {
		  if(i%num==0)
		  {
			counter = counter + 1;
		  }
		}
		if (counter ==2)
		{
		  //Appended the Prime number to the String
			primenumbers = primenumbers + i + " ";
		}
		//System.out.println(primenumbers);
		}
		List<String> myList = new ArrayList<String>(Arrays.asList(primenumbers.split(" ")));
		return myList;
	}
	
	public static float count_prime(long desired_number) 
	{
		float time1=0;
		float result=0;
		time1= System.nanoTime();
		myListresult = primes(desired_number);
		result= ((System.nanoTime())-(time1));
		//System.out.println(myListresult);
		return result/1000000000;
	} 
	
	public static float fix_int(long desired_number) 
	{	
		long i=0;
		long counting=0;
		for (i=0;i<=desired_number;i++)
		{
			counting = counting +i;
		}
		return counting;
	}
	
	public static float count_fix_int(long desired_number) 
	{
		float time1=0;
		float result=0;
		time1= System.nanoTime();
		fix_int(desired_number);
		result= ((System.nanoTime())-(time1));
		return result/1000000000;
	} 
	
	
	/*Exercise 2
	 *Exercise 6: Doubles, Part I
Write a Java program which performs the following tasks:
1. It first inputs three integers n 1 , n 2 and n 3 from the user: n 1 must be between 1 and 1
million, n 2 and n 3 may be arbitrary, but different and n 2 must be less than n 3 .
2. The program then generates n 1 random floating point numbers and stores them.
3. It computes the sum, the product, the average, the variance, the smallest and the largest
value of these numbers.
4. It outputs, in a nicely formatted way, all the numbers input and the statistics computed. */
	
	
	public static long[] exercise_6_user_input()
	{	
		int i =0;
		System.out.println("Please insert 3 different numbers n 1 , n 2 and n 3");
		System.out.println(" n 1 must be between 1 and million, n 2 must be less than n 3");
		Scanner scanner = new Scanner(System.in);
		long[] n = new long[3];
		for(i = 0; i < 3; i++)
		{
		    n[i] = scanner.nextInt();
		}
		return n;
	}
	
	public static float sum(float[] number_array)
	{
		long i = 0;
		float number=0;
		
		for (float ifloat : number_array)
		    number += ifloat;
		
		return number;
	}
	
	public static float product(float[] number_array)
	{
		long i = 0;
		float number=1;
		
		for (float ifloat : number_array)
		    number = (number * ifloat);
		
		return number;
	}
	
	public static float average(float[] number_array)
	{
		long i = 0;
		float number=1;
		
		for (float ifloat : number_array)
		    number += ifloat;
		
		return number/number_array.length;
	}
	
	public static float variance(float[] number_array)
	{
		long i = 0;
		float number=1;
		float average=0;
		float variance=0;	
		
		for (float ifloat : number_array)
		    number += ifloat;
		
		average = number/number_array.length;
		
		// The variance		
		for (i = 0; i < number_array.length; i++) {
		    variance += (number_array[(int) i] - average) * (number_array[(int) i] - average);
		}
		variance /= number_array.length;
		
		return variance;
	}
	
	
	
	public static float smallest(float[] number_array)
	{
		long i = 0;
		float number=0;
		float comparing = 999999999;
		
		for (float ifloat : number_array)
			if (ifloat<comparing) 
			{comparing = ifloat;}
		    
		
		return comparing;
	}
	
	public static float largest(float[] number_array)
	{
		long i = 0;
		float number=0;
		float comparing = 0;
		
		for (float ifloat : number_array)
			if (ifloat>comparing) 
			{comparing = ifloat;}
		    
		
		return comparing;
	}
	
	
	
	public static void exercise_6(long[] number_array)
	{
		int i =0;
		float number=0;
		float sum = 0;
		float product = 0;
		float average = 0;
		float variance = 0;
		float smallest = 0;
		float largest = 0;
		
		float[] n = new float[(int) number_array[1]];
		
		for (i = 0; i < number_array[1]; i++) 
		{
		    float generatedFloat = new Random().nextFloat();
			n[i]= generatedFloat;
			System.out.println(n[i]);
		}
		
		
		/*Computing the sum*/
		for (float ifloat : n)
		    number += ifloat;
		
		System.out.println("The sum is " +  sum(n));
		System.out.println("The product is " +  product(n));
		System.out.println("The average is " +  average(n));
		System.out.println("The variance is " +  variance(n));
		System.out.println("The smallest is " +  smallest(n));
		System.out.println("The largest is " +  largest(n));	
	}
	
	public static double productoria(int k, int n) 
	{
		long i =0;
		double product=1;
		double o_i =1.0;
		double result= 0 ;
		for (i=1;i<n;i++)
		{
			if(i==1) 
			{o_i=.5;}
			else if((1<i) && (i<k))
			{o_i=.9;}
			else
			{o_i=.1;}
		product = product * (o_i/(1-o_i));
		}
		result = 1-(1/(1+product));
		return result;
	}
	
	public static void exercise_7(long[] number_array)
	{
		
	}
	
	public static void test_prime()
	{

		boolean t = true;
		List<String> p = primes(1000);
		if (p.get(0) != "2") {
			t = false;
		}
		
		if (p.size() > 1000) {
			t = false;
		}
	
		if (Integer.valueOf(p.get(0)) % 2 != 0) {
			t = false;
		}
		
		if (t == false) {
			throw new java.lang.Error("prime test failed");
		}

	}
	
	public static void test_time()
	{
		boolean t = true;

		if (count_fix_int(10) < 0) {
			t = false;
		}

		if (t == false) {
			throw new java.lang.Error("time test failed");
		}
		
		
	}
	
	public static void test_statistic()
	{
		float[] p = new float[]{1,2,3, 8, 4};
		
		
		boolean t = true;

		if (sum(p) != 18) {
			t = false;
		}
		
		if (product(p) != 192) {
			t = false;
		}
		
		if (smallest(p) != 1) {
			t = false;
		}
		
		if (largest(p) != 8) {
			t = false;
		}
		
		if (t == false) {
			throw new java.lang.Error("prime test failed");
		}
	}
	
	public static void test_productoria()
	{
		
		boolean t = true;
		

		
		if (productoria(50, 20) != 1) {
			t = false;
		}
		
		if (productoria(40, 30) != 1) {
			t = false;
		}
		if (productoria(22, 11) != 0.9999999974188252) {
			t = false;
		}
		
		if (t == false) {
			throw new java.lang.Error("prime test failed");
		}
	}
	
	public static void main(String[] args) {
		test_prime();
		test_time();
		test_statistic();
		test_productoria();
		//System.out.println(count_prime(100000) + "seconds"); 
//		int foo = Integer.MAX_VALUE + 1; 
//		System.out.println(Integer.toUnsignedLong(foo));
//		long number=500000000;
//		System.out.println("The time taken to count to desired number = " + count_fix_int(number) + " seconds");
//		System.out.println("The time taken to count to 2 * desired number = " + count_fix_int(2*number) + " seconds");
//		System.out.println("The time taken to count to 10 * desired number = " +count_fix_int(10*number) + " seconds");
//		exercise_6_user_input();
//		exercise_6(exercise_6_user_input());
//		System.out.println(productoria(10,20)); 
//		System.out.println(productoria(10,20)); 
//		System.out.println(productoria(1000,1200)); 
//		System.out.println(productoria(10000,102000)); 
	}
	
	/*That function has a behavior l*/

}


