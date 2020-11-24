CC=gcc
NVCC=nvcc

intel:
	mkdir -p bin

	${CC} -O3 dgemv.c  \
	-DUSE_INTEL -DUSE_DOUBLE \
	-DMKL_ILP64 -m64 -I${MKLROOT}/include \
	-o bin/inteldouble.out \
	-Wl,--start-group ${MKLROOT}/lib/intel64/libmkl_intel_ilp64.a \
	${MKLROOT}/lib/intel64/libmkl_gnu_thread.a ${MKLROOT}/lib/intel64/libmkl_core.a \
	-Wl,--end-group -lgomp -lpthread -lm -ldl

	${CC} -O3 dgemv.c \
	-DUSE_INTEL \
	-DMKL_ILP64 -m64 -I${MKLROOT}/include \
	-o bin/intelsingle.out \
	-Wl,--start-group ${MKLROOT}/lib/intel64/libmkl_intel_ilp64.a \
	${MKLROOT}/lib/intel64/libmkl_gnu_thread.a ${MKLROOT}/lib/intel64/libmkl_core.a \
	-Wl,--end-group -lgomp -lpthread -lm -ldl

nvidia:
	mkdir -p bin

	${NVCC} -O3 dgemv.c \
	-DUSE_NVIDIA -DUSE_DOUBLE \
	-o bin/nvidiadouble.out \
	-I${CUDAROOT}/include -L${CUDAROOT}/lib64 -lcublas -lcudart 

	${NVCC} -O3 dgemv.c \
	-DUSE_NVIDIA \
	-o bin/nvidiasingle.out \
	-I${CUDAROOT}/include -L${CUDAROOT}/lib64 -lcublas -lcudart 

amd:
	mkdir -p bin


all: intel nvidia amd