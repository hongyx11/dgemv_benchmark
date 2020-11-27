#!/bin/bash
make nec
CPUTYPE=$1

if [ -z "$CPUTYPE" ]
then 
echo "CPUTYPE not set. please try agin."
exit
fi

###########################################################################

# MICADO [1] instrument
# no transpose 
./bin/necsingle fixed 5000 10000 1000 ${VETYPE}  # Dimension for 1 VE
./bin/necsingle fixed 2500 10000 1000 ${VETYPE}  # Dimension for 2 VEs
./bin/necsingle fixed 1250 10000 1000 ${VETYPE}  # Dimension for 4 VEs
./bin/necsingle fixed 625 10000 1000 ${VETYPE}  # Dimension for 8 VEs

./bin/necdouble fixed 5000 10000 1000 ${VETYPE} # Dimension for 1 VE
./bin/necdouble fixed 2500 10000 1000 ${VETYPE} # Dimension for 2 VEs
./bin/necdouble fixed 1250 10000 1000 ${VETYPE} # Dimension for 4 VEs 
./bin/necdouble fixed 625 10000 1000 ${VETYPE} # Dimension for 8 VEs

###########################################################################

# MAVIS instrument
# no transpose 
./bin/necsingle fixed 5000 20000 1000 ${VETYPE} # Dimension for 1 VE
./bin/necsingle fixed 2500 20000 1000 ${VETYPE} # Dimension for 2 VEs
./bin/necsingle fixed 1250 20000 1000 ${VETYPE} # Dimension for 4 VEs
./bin/necsingle fixed 625 20000 1000 ${VETYPE} # Dimension for 8 VEs

./bin/necdouble fixed 5000 20000 1000 ${VETYPE} # Dimension for 1 VE
./bin/necdouble fixed 2500 20000 1000 ${VETYPE} # Dimension for 2 VEs
./bin/necdouble fixed 1250 20000 1000 ${VETYPE} # Dimension for 4 VEs
./bin/necdouble fixed 625 20000 1000 ${VETYPE} # Dimension for 8 VEs

###########################################################################

# SCEXAO [1] instrument
# no transpose 
./bin/necsingle fixed 2000 10000 1000 ${VETYPE} # Dimension for 1 VE
./bin/necsingle fixed 1000 10000 1000 ${VETYPE} # Dimension for 2 VEs
./bin/necsingle fixed 500 10000 1000 ${VETYPE} # Dimension for 4 VEs
./bin/necsingle fixed 200 10000 1000 ${VETYPE} # Dimension for 8 VEs

./bin/necdouble fixed 2000 10000 1000 ${VETYPE} # Dimension for 1 VE
./bin/necdouble fixed 1000 10000 1000 ${VETYPE} # Dimension for 2 VEs
./bin/necdouble fixed 500 10000 1000 ${VETYPE} # Dimension for 4 VEs
./bin/necdouble fixed 200 10000 1000 ${VETYPE} # Dimension for 8 VEs

###########################################################################

# SCEXAO [2] instrument
# no transpose 
./bin/necsingle fixed 2000 14000 1000 ${VETYPE} # Dimension for 1 VE
./bin/necsingle fixed 1000 14000 1000 ${VETYPE} # Dimension for 2 VEs
./bin/necsingle fixed 500 14000 1000 ${VETYPE} # Dimension for 4 VEs
./bin/necsingle fixed 200 14000 1000 ${VETYPE} # Dimension for 8 VEs

./bin/necdouble fixed 2000 14000 1000 ${VETYPE} # Dimension for 1 VE
./bin/necdouble fixed 1000 14000 1000 ${VETYPE} # Dimension for 2 VEs
./bin/necdouble fixed 500 14000 1000 ${VETYPE} # Dimension for 4 VEs
./bin/necdouble fixed 200 14000 1000 ${VETYPE} # Dimension for 8 VEs

###########################################################################

# MICADO [2] instrument
# no transpose 
./bin/necsingle fixed 5000 25000 1000 ${VETYPE} # Dimension for 1 VE
./bin/necsingle fixed 2500 25000 1000 ${VETYPE}  # Dimension for 2 VEs
./bin/necsingle fixed 1250 25000 1000 ${VETYPE}  # Dimension for 4 VEs
./bin/necsingle fixed 625 25000 1000 ${VETYPE}  # Dimension for 8 VEs

./bin/necdouble fixed 5000 25000 1000 ${VETYPE} # Dimension for 1 VE
./bin/necdouble fixed 2500 25000 1000 ${VETYPE}  # Dimension for 2 VEs
./bin/necdouble fixed 1250 25000 1000 ${VETYPE}  # Dimension for 4 VEs
./bin/necdouble fixed 625 25000 1000 ${VETYPE}  # Dimension for 8 VEs

###########################################################################

# MAORY instrument
# no transpose 
./bin/necsingle fixed 8000 80000 1000 ${VETYPE} # Dimension for 1 VE
./bin/necsingle fixed 4000 80000 1000 ${VETYPE} # Dimension for 2 VEs
./bin/necsingle fixed 2000 80000 1000 ${VETYPE} # Dimension for 4 VEs
./bin/necsingle fixed 1000 80000 1000 ${VETYPE} # Dimension for 8 VEs

./bin/necdouble fixed 8000 80000 1000 ${VETYPE} # Dimension for 1 VE
./bin/necdouble fixed 4000 80000 1000 ${VETYPE} # Dimension for 2 VEs
./bin/necdouble fixed 2000 80000 1000 ${VETYPE} # Dimension for 4 VEs
./bin/necdouble fixed 1000 80000 1000 ${VETYPE} # Dimension for 8 VEs

###########################################################################

# EPICS instrument
# no transpose 
./bin/necsingle fixed 35000 70000 1000 ${VETYPE} # Dimension for 1 VE
./bin/necsingle fixed 17500 70000 1000 ${VETYPE} # Dimension for 2 VEs
./bin/necsingle fixed 8750 70000 1000 ${VETYPE} # Dimension for 4 VEs
./bin/necsingle fixed 4375 70000 1000 ${VETYPE} # Dimension for 8 VEs

./bin/necdouble fixed 35000 70000 1000 ${VETYPE} # Dimension for 1 VE
./bin/necdouble fixed 17500 70000 1000 ${VETYPE} # Dimension for 2 VEs
./bin/necdouble fixed 8750 70000 1000 ${VETYPE} # Dimension for 4 VEs
./bin/necdouble fixed 4375 70000 1000 ${VETYPE} # Dimension for 8 VEs

###########################################################################
