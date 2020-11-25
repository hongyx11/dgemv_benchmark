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
./bin/intelsingle fixed 5000 25000 100 ${CPUTYPE} 
./bin/intelsingle fixed 5000 20000 100 ${CPUTYPE} 
./bin/intelsingle fixed 8000 80000 100 ${CPUTYPE} 
# ./bin/intelsingle fixed 35000 70000 100 ${CPUTYPE} 

# no transpose 
./bin/inteldouble fixed 5000 10000 100 ${CPUTYPE} 
./bin/inteldouble fixed 5000 25000 100 ${CPUTYPE} 
./bin/inteldouble fixed 5000 20000 100 ${CPUTYPE} 
./bin/inteldouble fixed 8000 80000 100 ${CPUTYPE} 
# ./bin/inteldouble fixed 35000 70000 100 ${CPUTYPE} 


# # transpose
# ./bin/intelsingle_transpose fixed 10000 5000 100 ${CPUTYPE} 
# ./bin/intelsingle_transpose fixed 25000 5000 100 ${CPUTYPE} 
# ./bin/intelsingle_transpose fixed 20000 5000 100 ${CPUTYPE} 
# ./bin/intelsingle_transpose fixed 80000 8000 100 ${CPUTYPE} 
# ./bin/intelsingle_transpose fixed 70000 35000 100 ${CPUTYPE} 


# # transpose
# ./bin/inteldouble_transpose fixed 10000 5000 100 ${CPUTYPE} 
# ./bin/inteldouble_transpose fixed 25000 5000 100 ${CPUTYPE} 
# ./bin/inteldouble_transpose fixed 20000 5000 100 ${CPUTYPE} 
# ./bin/inteldouble_transpose fixed 80000 8000 100 ${CPUTYPE} 
# ./bin/inteldouble_transpose fixed 70000 35000 100 ${CPUTYPE} 
