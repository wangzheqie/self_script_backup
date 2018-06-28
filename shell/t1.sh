#!/bin/bash

count=0
add()
{
    echo "in add"
    count=$((count+$1))
    ((count++))
    return 1
}

#add 10
#or
(add 10)
aa=$?
echo $aa
echo $count

