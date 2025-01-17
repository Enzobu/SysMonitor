#!/bin/bash

temperature=$(sensors | grep 'temp1'  | grep -oP '(?<=\+)\d+(\.\d+)?(?=°C)' | sed -n '1p')
echo $temperature
