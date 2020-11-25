#!/bin/bash
make intel
CPUTYPE=$1

if [ -z "$CPUTYPE" ]
then 
echo "CPUTYPE not set. please try agin."
exit
fi

# no transpose 
./bin/intelsingle fixed 5000 10000 100 ${CPUTYPE} 
./bin/intelsingle fixed 5000 20000 100 ${CPUTYPE} 
./bin/intelsingle fixed 5000 25000 100 ${CPUTYPE} 
./bin/intelsingle fixed 8000 80000 100 ${CPUTYPE} 
# ./bin/intelsingle fixed 35000 70000 100 ${CPUTYPE} 

# no transpose 
./bin/inteldouble fixed 5000 10000 100 ${CPUTYPE} 
./bin/inteldouble fixed 5000 20000 100 ${CPUTYPE} 
./bin/inteldouble fixed 5000 25000 100 ${CPUTYPE} 
./bin/inteldouble fixed 8000 80000 100 ${CPUTYPE} 
# ./bin/inteldouble fixed 35000 70000 100 ${CPUTYPE} 

