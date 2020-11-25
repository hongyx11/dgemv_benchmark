CC=gcc
NVCC=nvcc

intel:
	mkdir -p bin
	mkdir -p log
	mkdir -p plots
	${CC} -O3 dgemv.c  \
	-DUSE_INTEL -DUSE_DOUBLE \
	-DMKL_ILP64 -m64 -I${MKLROOT}/include \
	-o bin/inteldouble \
	-Wl,--start-group ${MKLROOT}/lib/intel64/libmkl_intel_ilp64.a \
	${MKLROOT}/lib/intel64/libmkl_gnu_thread.a ${MKLROOT}/lib/intel64/libmkl_core.a \
	-Wl,--end-group -lgomp -lpthread -lm -ldl

	${CC} -O3 dgemv.c \
	-DUSE_INTEL \
	-DMKL_ILP64 -m64 -I${MKLROOT}/include \
	-o bin/intelsingle \
	-Wl,--start-group ${MKLROOT}/lib/intel64/libmkl_intel_ilp64.a \
	${MKLROOT}/lib/intel64/libmkl_gnu_thread.a ${MKLROOT}/lib/intel64/libmkl_core.a \
	-Wl,--end-group -lgomp -lpthread -lm -ldl

nvidia:
	mkdir -p bin
	mkdir -p log
	mkdir -p plots
	${NVCC} -O3 dgemv.c \
	-DUSE_NVIDIA -DUSE_DOUBLE \
	-o bin/nvidiadouble \
	-I${CUDAROOT}/include -L${CUDAROOT}/lib64 -lcublas -lcudart 

	${NVCC} -g -O3 dgemv.c \
	-DUSE_NVIDIA \
	-o bin/nvidiasingle \
	-I${CUDAROOT}/include -L${CUDAROOT}/lib64 -lcublas -lcudart 

	${NVCC} -O3 dgemv_transpose.c \
	-DUSE_NVIDIA -DUSE_DOUBLE \
	-o bin/nvidiadouble_transpose \
	-I${CUDAROOT}/include -L${CUDAROOT}/lib64 -lcublas -lcudart 

	${NVCC} -g -O3 dgemv_transpose.c \
	-DUSE_NVIDIA \
	-o bin/nvidiasingle_transpose \
	-I${CUDAROOT}/include -L${CUDAROOT}/lib64 -lcublas -lcudart 

amd:
	mkdir -p bin
	mkdir -p log
	mkdir -p plots

all: intel nvidia amd