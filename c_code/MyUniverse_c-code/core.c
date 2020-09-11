/*
* Date: 04-3-12
* Author: Dr. Milan Mijic and Derek Wells							
* Purpose: This is a numerical integration program utilizing        
*          Simpson's Rule. It calculates the co-moving distance to a 	
*          galaxy with redshift z. The information about the matter/radiation 	
*	   content, overall curvature and cosmological constant is contained 
*	   solely in the function we integrate. The program returns two column data: 
*	   redshift and the magnitude.
*/                     

#include <stdio.h>
#include <stdlib.h>
#include "input_integ.h" /* calls the input/integration routine */
#include "batch.h" /* calls the batch file routine */

main()
{
	int redo = 1,ans = 1; 
		
	while (redo == 1) 
	{
		input_integ();
		printf("\a\n\nEnter 1 to repeat program, else any # to continue: ");
		scanf("%i",&redo);
	} /* end of while */
	
	printf("\a\nEnter 1 to create batch file, else any # to exit: ");
	scanf("%i",&ans);
	if (ans == 1)
	{
		batch();
	}
	else
	{
		exit(0);
	}
} /* end of main */
