/* this is the integration routine */

#include <math.h>
#include "function.h"
#include "ingrl_simp.h"
#define NO 999 /* maximum points for Simpson's Rule/needs to be ODD so intervals can be EVEN or vice-versa */
#define min 0 /* closest galaxy/initialization point */

double simpson(double max,double A,double B,double C,double D,double E,double F,double G)
{  
	int n;				 
   	double interval,sum = 0.00,x;
   
   	interval = ((max-min)/(NO-1));
   
   	for (n=2;n<NO;n+=2) /* loop for even points  */
   	{
       		x = min+interval*(n-1); /* need the min to adjust if lo is non-0 */
       		sum += 4*f(x,A,B,C,D,E,F,G);
   	}

   	for (n=3;n<NO;n+=2) /* loop for odd points  */
   	{
        	x = min+interval*(n-1); 
      		sum += 2*f(x,A,B,C,D,E,F,G);
   	}   
   	
	sum += f(min,A,B,C,D,E,F,G)+f(max,A,B,C,D,E,F,G); /* add first and last value */          
   	sum *= interval/3.00; /* then multiply by interval */
   
   	return (sum);   
}
