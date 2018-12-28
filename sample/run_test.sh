#!/bin/bash

cd `dirname $0`
if [[ $1 == 'py' || $1 == 'pytest' ]]; then
    echo ">>> pytest"
    pytest py_test
elif [[ $1 == 'unit' || $1 == 'unittest' ]]; then
    echo ">>> pytest with unittest code"
    pytest unit_test
else
    echo ">>> unittest"
    python -m unittest discover -s unit_test
fi
