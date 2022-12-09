#!/bin/bash

dir="day$1"
if [ ! -d "$dir" ]; then
    mkdir $dir
    cp solution_template.py $dir/solution.py
    touch $dir/input.txt
    touch $dir/input_simple.txt
fi

