#!/bin/bash
make nec
CPUTYPE=$1

if [ -z "$CPUTYPE" ]
then 
echo "CPUTYPE not set. please try agin."
exit
fi

# no transpose 
./bin/necsingle fixed 5000 10000 1000 ${CPUTYPE} 
./bin/necsingle fixed 5000 20000 1000 ${CPUTYPE} 
./bin/necsingle fixed 5000 25000 1000 ${CPUTYPE} 
./bin/necsingle fixed 8000 80000 1000 ${CPUTYPE} 
./bin/necsingle fixed 35000 70000 1000 ${CPUTYPE} 

# no transpose 
./bin/necdouble fixed 5000 10000 1000 ${CPUTYPE} 
./bin/necdouble fixed 5000 20000 1000 ${CPUTYPE} 
./bin/necdouble fixed 5000 25000 1000 ${CPUTYPE} 
./bin/necdouble fixed 8000 80000 1000 ${CPUTYPE} 
./bin/necdouble fixed 35000 70000 1000 ${CPUTYPE} 

