/*
Author: Derek Wells
Date: 09-07-24
Purpose: To try and plot a friggin photon path in Schwarzschild geometry.
*/

#include <stdio.h>
#include <math.h>
#define N 10000
FILE *f1;
FILE *f2;

int main();

float function(float rho, float j);
float cubic(float a, float b, float c, float d);

struct complx solvequad(float p, float q, float r, float s, float t);
struct complx{
	float real;
    	float img;
     	int iscomplex;//0=False, 1 = True
};


/*************************************/
float function(float rho,float j){
		
	float b = 1-1/rho;
	//float c = 1-(((j*j)/(rho*rho))*b);
	float c = ((rho*rho*rho*rho)/(j*j))-((rho*rho)*b);

	//float f = b*sqrt(c);
	float f = sqrt(c);

	//return (abs(f));
	return (f);
}//end RHO FUNCTION declaration
/*************************************/

/*************************************/
float cubic(float a, float b, float c, float d){
	
	int y;
     	float x1,x2;
     	float rhob;
     	struct complx x3;

     	//printf("a=%f b=%f c=%f d=%f\n", a, b, c, d);
     	if (d != 0){
          	x1=0;
          	/*The for loop finds an approximate solution
          	for the equation by using Newton-Raphson Method:
                x1=x0-(f(x0)/f'(x0))
                x2=x1-(f(x1)/f'(x1))
                ...
                ...
          	the solution is more accurate with more iterations*/
          	for(y=0;y<=100;y++){
               		x2=x1-(((a*x1*x1*x1)+(b*x1*x1)+(c*x1)+d)/((3*a*x1*x1)+(2*b*x1)+c));
               		x1=x2;
          	}//end FOR
        }//end IF
     	else
        	/*After one root has been found, we're left
     		with a quadratic equation which can easily be solved
     		using the formula*/
     		x3 = solvequad(a,b,c,d,x2);
     
     	if (x3.real+x3.img>x1) rhob=x3.real+x3.img;
	else rhob=x1;
     	
	return (rhob);
}//end CUBIC equation solution
/*************************************/

/*************************************/
struct complx solvequad(float p, float q, float r, float s, float t){
	
	float a,b,c,i;
     	struct complx x;

     	a=p;
     	b=q+(t*p);
     	c=(-s)/t;
     	x.real =((-b)/(2*a));
     	i=((b*b)-(4*a*c));

     	if (i>=0){
        	x.img =(sqrt(i))/(2*a);
          	x.iscomplex = 0;
     	}//end IF
     	else{
          	x.img =(sqrt(-i))/(2*a);
          	x.iscomplex = 1;
     	}//end ELSE
     
     	return (x);
}//end structure
/*************************************/

/*************************************/
int main(){
	float rho,phi;
	float rhoinit,phivinit,phiinit;
	float rhoout,phiout;
	float phivtxt,phitxt,phidsply;
	//float rhoin,phiin,phistep=0.02;
	float h=0.01;//delta phi
	float j,rhob;
	float x,y;
	int i/*=0*/,k;
	char file[50],test[50];

	printf("\nRho initial (Schwarzchild radii) = ");
	scanf("%f",&rhoinit);
	//printf("\nPhiv initial (deg) = ");
	//scanf("%f",&phivinit);
	printf("\nPhi initial (deg) = ");
	scanf("%f",&phiinit);

	phivtxt = phivinit;
	phivinit = (phivinit/180)*M_PI;
	phitxt = phiinit;
	phiinit = (phiinit/180)*M_PI;

	sprintf(file, "rho%.2fphi%.2f.dat", rhoinit, phitxt);
	f1 = fopen (file, "wt");
	fprintf(f1,"rho\tphi\tx\ty\n");
	sprintf(test, "testing_rho%.2fphi%.2f.dat", rhoinit, phitxt);
	f2 = fopen (test, "wt");
 
	//j = rhoinit*sin(phivinit-phiinit);
	j = 400.0;
	rhob = cubic(1,0,-1*j*j,j*j);//minimum rho computed here; largest of two, positive real roots
	//printf("%f",&rhob);

	rho = rhob;
	phi = M_PI/2;
	for(i=1;i<1000;i++){
		rhoout = rho + h*function(rho,j);
		//printf("%f",function(rho,j));
		phiout = phi + h;	

		phidsply = phiout*180/M_PI;
		x = rhoout*cos(phiout);
		y = rhoout*sin(phiout);
		printf("%.2f\t%.2f\t%.2f\t%.2f%f\t%f\n",rhoout,phidsply,x,y,rhob,function(rho,j));
		fprintf(f2,"%.2f\t%.2f\t%.2f\t%.2f%f\t%f\n",rhoout,phidsply,x,y,rhob,function(rho,j));
		fprintf(f1,"%.2f\t%.2f\t%.2f\t%.2f\n",rhoout,phidsply,x,y);

		/*reinitialize variables*/
		rho = rhoout;
		phi = phiout;
	}//end FOR LEFT BRANCH

	rho = rhob;
	phi = M_PI/2;
	//h = -0.01;
	for(i=1;i<1000;i++){
		h = -0.01;
		rhoout = rho - h*function(rho,j);
		phiout = phi + h;	

		phidsply = phiout*180/M_PI;
		x = rhoout*cos(phiout);
		y = rhoout*sin(phiout);
		printf("%.2f\t%.2f\t%.2f\t%.2f%f\t%f\n",rhoout,phidsply,x,y,rhob,function(rho,j));
		fprintf(f2,"%.2f\t%.2f\t%.2f\t%.2f%f\t%f\n",rhoout,phidsply,x,y,rhob,function(rho,j));
		fprintf(f1,"%.2f\t%.2f\t%.2f\t%.2f\n",rhoout,phidsply,x,y);

		/*reinitialize variables*/
		rho = rhoout;
		phi = phiout;
	}//end FOR RIGHT BRANCH
	
	/********************OLD EULER METHOD********************
	rhoin = rhoinit;
	phiin = phiinit;

	rhoout = rhoin;
	phiout = phiin;
	printf("%f",function(rhoout,j));
	while (function(rhoout,j) > 0){
		rhoout = (rhoin - function(rhoin,j))*phistep;
		phiout = phiin + phistep;
		phidsply = phiout*180/M_PI;
		x = rhoout*cos(phiout);
		y = rhoout*sin(phiout);
		printf("%.2f\t%.2f\t%.2f\t%.2f\n",rhoout,phidsply,x,y);
		fprintf(f1,"%.2f\t%.2f\t%.2f\t%.2f\n",rhoout,phidsply,x,y);
		rhoin = rhoout;
		phiin = phiout;

		i+=1;
	}//end WHILE

	rhoout = rhoin;
	phiout = phiin + phistep;
	phidsply = phiout*180/M_PI;
	x = rhoout*cos(phiout);
	y = rhoout*sin(phiout);
	printf("%.2f\t%.2f\t%.2f\t%.2f\n",rhoout,phidsply,x,y);
	fprintf(f1,"%.2f\t%.2f\t%.2f\t%.2f\n",rhoout,phidsply,x,y);

	for (k=0;k<=i;k++){
		rhoout = (rhoin + function(rhoin,j))*phistep;
		phiout = phiin + phistep;
		phidsply = phiout*180/M_PI;
		x = rhoout*cos(phiout);
		y = rhoout*sin(phiout);
		printf("%.2f\t%.2f\t%.2f\t%.2f\n",rhoout,phidsply,x,y);
		fprintf(f1,"%.2f\t%.2f\t%.2f\t%.2f\n",rhoout,phidsply,x,y);
		rhoin = rhoout;
		phiin = phiout;
	}//end FOR
	/********************OLD EULER METHOD********************/

	fclose (f2);
	fclose (f1);
	printf("\nProgram done.\n");

}//end MAIN
/*************************************/
