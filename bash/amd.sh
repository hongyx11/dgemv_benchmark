#!/bin/bash
make amd
CPUTYPE=$1

if [ -z "$CPUTYPE" ]
then 
echo "CPUTYPE not set. please try agin."
exit
fi

# no transpose 
./bin/amdsingle fixed 5000 10000 1000 ${CPUTYPE} 
./bin/amdsingle fixed 5000 20000 1000 ${CPUTYPE} 
./bin/amdsingle fixed 5000 25000 1000 ${CPUTYPE} 
./bin/amdsingle fixed 8000 80000 1000 ${CPUTYPE} 
./bin/amdsingle fixed 35000 70000 1000 ${CPUTYPE} 

# no transpose 
./bin/amddouble fixed 5000 10000 1000 ${CPUTYPE} 
./bin/amddouble fixed 5000 20000 1000 ${CPUTYPE} 
./bin/amddouble fixed 5000 25000 1000 ${CPUTYPE} 
./bin/amddouble fixed 8000 80000 1000 ${CPUTYPE} 
./bin/amddouble fixed 35000 70000 1000 ${CPUTYPE} 
