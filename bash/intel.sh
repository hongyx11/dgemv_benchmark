#!/bin/bash
make intel
CPUTYPE=$1

if [ -z "$CPUTYPE" ]
then 
echo "CPUTYPE not set. please try agin."
exit
fi


./bin/intelsingle fixed 128 128 100 ${CPUTYPE} 
./bin/intelsingle fixed 256 256 100 ${CPUTYPE} 
./bin/intelsingle fixed 512 512 100 ${CPUTYPE} 
./bin/intelsingle fixed 1024 1024 100 ${CPUTYPE} 
./bin/intelsingle fixed 2048 2048 100 ${CPUTYPE} 
./bin/intelsingle fixed 4096 4096 100 ${CPUTYPE} 
./bin/intelsingle fixed 8192 8192 100 ${CPUTYPE} 


# ./bin/intelsingle fixed 128 10000 100 ${CPUTYPE} 
# ./bin/intelsingle fixed 256 10000 100 ${CPUTYPE} 
# ./bin/intelsingle fixed 512 10000 100 ${CPUTYPE} 
# ./bin/intelsingle fixed 1024 10000 100 ${CPUTYPE} 
# ./bin/intelsingle fixed 2048 10000 100 ${CPUTYPE} 
# ./bin/intelsingle fixed 4096 10000 100 ${CPUTYPE} 
# ./bin/intelsingle fixed 8192 10000 100 ${CPUTYPE} 


# ./bin/intelsingle fixed 10000 128 100 ${CPUTYPE} 
# ./bin/intelsingle fixed 10000 256 100 ${CPUTYPE} 
# ./bin/intelsingle fixed 10000 512 100 ${CPUTYPE} 
# ./bin/intelsingle fixed 10000 1024 100 ${CPUTYPE} 
# ./bin/intelsingle fixed 10000 2048 100 ${CPUTYPE} 
# ./bin/intelsingle fixed 10000 4096 100 ${CPUTYPE} 
# ./bin/intelsingle fixed 10000 8192 100 ${CPUTYPE} 



./bin/inteldouble fixed 128 128 100 ${CPUTYPE} 
./bin/inteldouble fixed 256 256 100 ${CPUTYPE} 
./bin/inteldouble fixed 512 512 100 ${CPUTYPE} 
./bin/inteldouble fixed 1024 1024 100 ${CPUTYPE} 
./bin/inteldouble fixed 2048 2048 100 ${CPUTYPE} 
./bin/inteldouble fixed 4096 4096 100 ${CPUTYPE} 
./bin/inteldouble fixed 8192 8192 100 ${CPUTYPE} 


# ./bin/inteldouble fixed 128 10000 100 ${CPUTYPE} 
# ./bin/inteldouble fixed 256 10000 100 ${CPUTYPE} 
# ./bin/inteldouble fixed 512 10000 100 ${CPUTYPE} 
# ./bin/inteldouble fixed 1024 10000 100 ${CPUTYPE} 
# ./bin/inteldouble fixed 2048 10000 100 ${CPUTYPE} 
# ./bin/inteldouble fixed 4096 10000 100 ${CPUTYPE} 
# ./bin/inteldouble fixed 8192 10000 100 ${CPUTYPE} 


# ./bin/inteldouble fixed 10000 128 100 ${CPUTYPE} 
# ./bin/inteldouble fixed 10000 256 100 ${CPUTYPE} 
# ./bin/inteldouble fixed 10000 512 100 ${CPUTYPE} 
# ./bin/inteldouble fixed 10000 1024 100 ${CPUTYPE} 
# ./bin/inteldouble fixed 10000 2048 100 ${CPUTYPE} 
# ./bin/inteldouble fixed 10000 4096 100 ${CPUTYPE} 
# ./bin/inteldouble fixed 10000 8192 100 ${CPUTYPE} 