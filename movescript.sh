#! /bin/bash

genes="ATP6 ATP8 COX1 COX2 COX3 CYTB ND1 ND2 ND3 ND4L ND4 ND5 ND6"
for i in $genes
do
	if [ -d "./$i" ]
	then
		:
	else
		mkdir $i
	fi
	for n in ./*$i*
	do
		if [ -d $n ]
		then
			:
		elif [ -f $n ]
		then
			mv $n ./$i/
		fi
	done
done
