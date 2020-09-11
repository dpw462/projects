/* this is the main program with input/integration done in this routine */

#include <stdio.h>
#include <math.h>
#include "ingrl_simp.h"
#include "input_integ.h"

void input_integ()
{
	double imax,omega_r,omega_m,omega_dm,omega_cs,omega_ct,omega_cc,omega_sum,z,pre_chi,chi,lum_dh,c_radius,dm_ref; /* cosmological parameters */
	char name[26];
	FILE *output;

	do{
	    printf("\a\nName the data output file (max 25 characters): ");
	    scanf("%s",name);
	}while ((output = fopen(name,"w")) == NULL); /* error if file OPENING is bad */

	printf("\nInput Upper Bound z(redshift): \n");
	scanf("%lf",&imax);
	printf("Input Omega_Radiation Parameter: \n");
	scanf("%lf",&omega_r);
	printf("Input Omega_Matter Parameter: \n");
	scanf("%lf",&omega_m);
	printf("Input Omega_DarkMatter Parameter: \n");
	scanf("%lf",&omega_dm);
	printf("Input Omega_CosmicString Parameter: \n");
	scanf("%lf",&omega_cs);
	printf("Input Omega_CosmicTexture Parameter: \n");
	scanf("%lf",&omega_ct);
	printf("Input Omega_Cosmological Constant: \n");
	scanf("%lf",&omega_cc);
		
	omega_sum = omega_r+omega_m+omega_dm+omega_cs+omega_ct+omega_cc;
		
	if (omega_sum == 1)
	{
		printf("\nThose values of Omega correspond to a flat universe.");
	}
	else if (omega_sum > 1)
	{
		printf("\nThose values of Omega correspond to a closed universe.");
	}
	else if (omega_sum < 1)
	{
		printf("\nThose values of Omega correspond to an open universe.");
	}

 	for (z=0.01;z<=imax;z+=0.01) /* loop generates redshifts in 0.01 increments */
  	{ 					 
 		pre_chi = simpson(z,omega_r,omega_m,omega_dm,omega_cs,omega_sum,omega_ct,omega_cc); /* pass omega's */		
 		
		if (omega_sum == 1)
		{
			chi = pre_chi;
			lum_dh = (1+z)*chi;
		}
		else if (omega_sum > 1)
		{
			chi = pre_chi*pow((omega_sum-1),0.5);
			c_radius = sin(chi);
			lum_dh = ((1+z)*c_radius)/(pow((omega_sum-1),0.5));
		}
		else if (omega_sum < 1)
		{
			chi = pre_chi*pow((1-omega_sum),0.5);
			c_radius = sinh(chi);
			lum_dh = ((1+z)*c_radius)/(pow((1-omega_sum),0.5));
		}
	
		dm_ref = 24.167 + log10(lum_dh);
		fprintf(output,"%1.2f\t%E\n",z,dm_ref);
	} /* end of for */
    		
	fclose(output);
}
