/* this is the function definition */

#include <math.h>
#include "function.h"

double f(double x,double A,double B,double C,double D,double E,double F, double G)
{ 
	return (1/(pow((A*pow((1+x),4)+(B+C)*pow((1+x),3)+(D+1-E)*pow((1+x),2)+F*(1+x)+G),0.5)));               
}
