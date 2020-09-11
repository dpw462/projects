/* this is the batch file routine */

#include <stdio.h>
#include "batch.h"

void batch()
{
	char plot[26];	
	FILE *fp; 
	
	do{
	    printf("\a\nName the plotting batch file (max 25 characters): ");
	    scanf("%s",plot);
	}while ((fp = fopen(plot,"w")) == NULL);
	
	fprintf(fp,"set terminal postscript landscape enhanced mono \"Helvetica\" 14\n");
	fprintf(fp,"set out \"[NAME_GRAPHIC-FILE].ps\"\n");
	fprintf(fp,"set title \"Magnitude Comparison to Empty Universe as a Function of Redshift\"\n");
	fprintf(fp,"set xlabel \"Redshift - z\"\n");
	fprintf(fp,"set ylabel \"Magnitude - (M_o_u_r - M_e_m_p)\"\n");
	fprintf(fp,"#plot '[DATA_OUTPUT].dat' w lp pointtype 7 pointsize 1,<REPEAT FOR MULTIPLE FILES>");
	printf("\a\nBE SURE TO EDIT THE PLOTTING BATCH FILE TO USE WITH GNUPLOT!\n\a");
	
	fclose(fp);
}
