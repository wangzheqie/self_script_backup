#!/bin/bash 
# after -x 
#exit 0 
#exit 1

if [ $(id -u) = "0" ]; then 
    echo "superuser"
else
    echo "not"
fi

read text 
echo $text 
# read -s 
# read -t 3 response 

read number 
echo $number 
if [ $((number %2)) -eq 0 ]; then 
    echo "even"
else
    echo "odd"
fi
