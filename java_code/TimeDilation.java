import java.util.Scanner;
import java.lang.Math;


public class TimeDilation{
	public static void main(String[] args){

	Scanner input = new Scanner(System.in);
	
	System.out.println("\t\t*** Time Dilation Program ***");
	System.out.println();
		
	int ans = 1;
	while (ans == 1){
		
		double v = 1.0;
		while (v >= 1.0){
			System.out.print("Input your velocity (in units of c), [0,1): ");
			v = input.nextDouble();
		}//end WHILE
				
		System.out.print("Input your acceleration (in units of g): ");
		double a = input.nextDouble();
		
		total_trip(v,a);

		System.out.println();
		System.out.print("Repeat? (1 yes, 0 no): ");
		ans = input.nextInt();	
		if (ans != 1) System.exit(0);
	}//end WHILE

	}//end MAIN

	public static void total_trip(double v, double a){
		
		final double C_LITE = 3.00e8;
		final double GRAV = 9.8;
		final double SEC_MONTHS = 2.59e6;		

		double vel = v * C_LITE;
		double gamma = Math.pow((1 - Math.pow(v,2.0)),-0.5);
		double accel = a * GRAV;
		double rel_accel = (1/gamma)*accel; 
	
		double t_earth = vel / rel_accel;
		double A = C_LITE / rel_accel;	
		double inv_A = 1/A;
		double B = Math.sqrt(Math.pow((inv_A * t_earth),2) + 1);

		double t_ship = A * Math.log((inv_A * t_earth) + B);     

		t_earth /= SEC_MONTHS;
		t_ship /= SEC_MONTHS;
	
		System.out.println("********************");
		System.out.println("Phase I,III,IV,VI - Accelerate/Decelerate:");
		System.out.println();	
		System.out.println("Earth time in months:");
		System.out.println("v/a\t\t" + v);
		System.out.println();
		System.out.printf(a + "\t\t%.3f", t_earth); 
		System.out.println();
		System.out.println("Ship time in months:");
		System.out.println("v/a\t\t" + v);
		System.out.println();
		System.out.printf(a + "\t\t%.3f", t_ship); 
		System.out.println();
		System.out.println("********************");
		System.out.println();

		double t_s = t_earth * (1 - Math.pow(v,2.0));
		double t_e = t_s / (1 - Math.pow(v,2.0));
			
		System.out.println("********************");
		System.out.println("Phase II,V - Cruise at constant speed " + v + ":");
		System.out.println();	
		System.out.printf("Earth time in months: %.3f", t_e);
		System.out.println();
		System.out.printf("Ship time in months: %.3f", t_s);			
		System.out.println();
		System.out.println("********************");
		System.out.println();
	
		double total_time_earth = 4*t_earth + 2*t_e;
		double total_time_ship = 4*t_ship + 2*t_s;

		System.out.println();
		System.out.printf("Total Earth time for trip in months: %.3f", total_time_earth);		
		System.out.println();
		System.out.printf("Total ship time for trip in months: %.3f", total_time_ship);
		System.out.println();
	}//end METHOD

}//end CLASS