#!/bin/bash

GENERATE_NUMBER=$1
MODULE=$2

if [ -z $1 ]; then
    GENERATE_NUMBER=6
fi

if [ -z $2 ]; then
    MODULE="light"
fi

python3.13 logic/mt_generator.py --number $GENERATE_NUMBER --device $MODULE

if [ $2 == 'tv' ]; then
    TEMPLATE="tests/test_mt_generator.py.template.tv"
elif [ $2 == 'light' ]; then
    TEMPLATE="tests/test_mt_generator.py.template"
fi

for ((i = 0; i < $GENERATE_NUMBER; i++)); do
    FILE_NAME="tests/test_mt_generator_$i.py"
    echo "generate file $FILE_NAME"
    cp $TEMPLATE $FILE_NAME
    /opt/homebrew/bin/gsed -i "s/\#\#INDEX\#\#/$i/" "$FILE_NAME"
    #sed -i "s/\#\#INDEX\#\#/$i/" "$FILE_NAME"
done

