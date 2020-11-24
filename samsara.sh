export CUDA_VISIBLE_DEVICES=0
make nvidia
GPUTYPE=$1

if [ -z "$GPUTYPE" ]
then 
echo "GPUTYPE not set. please try agin."
exit
fi

./bin/nvidiasingle fixed 128 128 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 256 256 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 512 512 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 1024 1024 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 2048 2048 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 4096 4096 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 8192 8192 100 ${GPUTYPE} ${GPUTYPE}res.txt


# ./bin/nvidiasingle fixed 128 10000 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 256 10000 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 512 10000 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 1024 10000 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 2048 10000 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 4096 10000 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 8192 10000 100 ${GPUTYPE} ${GPUTYPE}res.txt


# ./bin/nvidiasingle fixed 10000 128 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 10000 256 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 10000 512 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 10000 1024 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 10000 2048 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 10000 4096 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiasingle fixed 10000 8192 100 ${GPUTYPE} ${GPUTYPE}res.txt



# ./bin/nvidiadouble fixed 128 128 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 256 256 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 512 512 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 1024 1024 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 2048 2048 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 4096 4096 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 8192 8192 100 ${GPUTYPE} ${GPUTYPE}res.txt


# ./bin/nvidiadouble fixed 128 10000 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 256 10000 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 512 10000 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 1024 10000 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 2048 10000 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 4096 10000 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 8192 10000 100 ${GPUTYPE} ${GPUTYPE}res.txt


# ./bin/nvidiadouble fixed 10000 128 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 10000 256 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 10000 512 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 10000 1024 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 10000 2048 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 10000 4096 100 ${GPUTYPE} ${GPUTYPE}res.txt
# ./bin/nvidiadouble fixed 10000 8192 100 ${GPUTYPE} ${GPUTYPE}res.txt