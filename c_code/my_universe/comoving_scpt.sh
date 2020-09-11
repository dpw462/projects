#!/bin/sh

#AUTHOR: Derek Wells
#DATE: 06-8-30
#PURPOSE: This is the procedural script for creating the object files, compiling and executing 
#the comoving-luminosity distance program.

echo "Files in same directory? <y,n>"
read ans1
	if [ $ans1 = "y" ]; then
		echo "Creating object files..."
		gcc -c batch.c function.c ingrl_simp.c input_integ.c
		
		echo "Compiling program..."
		gcc -o lum_dist core.c batch.o function.o ingrl_simp.o input_integ.o -lm

		echo "Cleaning up..."
		rm *.o
	elif [ $ans1 = "n" ]; then
		echo "Specify complete path to source files for program i.e. /home/derek etc"
		read dir

		cd $dir 

		echo "Creating object files..."
		gcc -c batch.c function.c ingrl_simp.c input_integ.c

		echo "Compiling program..."
		gcc -o lum_dist core.c batch.o function.o ingrl_simp.o input_integ.o -lm

		echo "Cleaning up..."
		rm *.o
	else
		echo "Exiting... did not recognize answer '<y,n>'"
		exit 1
	fi

echo "Run program? <y,n>"
read ans2
	if [ $ans2 = "y" ]; then
		./lum_dist
	elif [ $ans2 = "n" ]; then
		echo "Bye!"
	else 
		echo "Exiting... did not recognize answer '<y,n>'"
		exit 1
	fi
	
exit 0

