#!/bin/bash

echo $0
echo $1
echo $2
echo $3
echo $4

# 1 2 3 4
if [ "$1" != "" ]; then 
    echo $1
else
    echo "no flag"
fi

if [ $# -gt 0 ]; then 
    echo $#
else
    echo "no number"
fi

# 
