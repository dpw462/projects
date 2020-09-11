import java.util.Scanner;
import java.lang.Math;


public class TD{
	public static void main(String[] args){

	Scanner input = new Scanner(System.in);
	
	System.out.println("\t\t*** Time Dilation Program ***");
	System.out.println();
		
	int ans = 1;
	while (ans == 1){
		
		System.out.print("How long is the desired ship travel time (in months!): ");
		double Ts_desired = input.nextDouble();
		double v = 1.0;
		while (v >= 1.0){
			System.out.print("\nInput your velocity (in units of c), [0,1): ");
			v = input.nextDouble();
		}//end WHILE
		System.out.print("Input your acceleration (in units of g): ");
		double a = input.nextDouble();
		
		total_trip(Ts_desired,v,a);

		System.out.println();
		System.out.print("Repeat? (1 yes, 0 no): ");
		ans = input.nextInt();	
		if (ans != 1) System.exit(0);
	}//end WHILE

	}//end MAIN

	public static void total_trip(double T,double v, double a){
		
		final double C_LITE = 3.00e8;
		final double GRAV = 9.81;
		final double SEC_MONTHS = 2.59e6;		

		double vel = v * C_LITE;
		double gamma = Math.pow((1 - Math.pow(v,2.0)),0.5);
		double accel = a * GRAV;
		double rel_accel = gamma*accel; 
	
		double t_earth = vel / rel_accel;
		double A = C_LITE / accel;	
		double inv_A = 1/A;
		double ratio = inv_A * t_earth;
		double B = Math.pow(ratio,2);
		double C = Math.sqrt(B + 1);
		double D = Math.log(ratio + C);     
		double t_ship = A * D;

		t_earth /= SEC_MONTHS;
		t_ship /= SEC_MONTHS;

		double delta = T - (4*t_ship);
		double total_earthtime = 0;
		double total_shiptime = 0;
	
		if (delta > 0){
			double Ts = delta / 2;
			double Te = Ts / Math.pow((1 - Math.pow(v,2.0)),0.5);
			
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
			System.out.println("********************");
			System.out.println("Phase II,V - Cruise at constant speed " + v + ":");
			System.out.println();	
			System.out.printf("Earth time in months: %.3f", Te);
			System.out.println();
			System.out.printf("Ship time in months: %.3f", Ts);			
			System.out.println();
			System.out.println("********************");
			System.out.println();
			
			total_earthtime = 4*t_earth + 2*Te;
			total_shiptime = 4*t_ship + 2*Ts;
			System.out.println("This trip will be a six phase journey. Enjoy your flight!");
			
			System.out.println();
			System.out.printf("Total Earth time for trip in months: %.3f", total_earthtime);		
			System.out.println();
			System.out.printf("Total ship time for trip in months: %.3f", total_shiptime);
			System.out.println();
		}//end IF
		if (delta == 0){
			total_earthtime = 4*t_earth;
			total_shiptime = 4*t_ship;
			
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
			
			System.out.println("No time for cruising! Have a nice flight!");
			System.out.println();
			System.out.printf("Total Earth time for trip in months: %.3f", total_earthtime);		
			System.out.println();
			System.out.printf("Total ship time for trip in months: %.3f", total_shiptime);
			System.out.println();
		}//end IF
		if (delta < 0){
			System.out.println();
			System.out.print("Acceleration to " + v + "c alone, would take longer");
			System.out.println(" than the desired time of the trip!");
			delta_less(delta);
		}//end IF
	}//end METHOD

	public static void delta_less(double delta){

			Scanner input = new Scanner(System.in);
			
			System.out.println();
			System.out.print("How long is the desired ship travel time (in months!): ");
			double Ts_desired = input.nextDouble();
			double v = 1.0;
			while (v >= 1.0){
				System.out.print("\nInput your velocity (in units of c), [0,1): ");
				v = input.nextDouble();
			}//end WHILE
			System.out.print("Input your acceleration (in units of g): ");
			double a = input.nextDouble();
		
			total_trip(Ts_desired,v,a);
	}//end METHOD

}//end CLASS