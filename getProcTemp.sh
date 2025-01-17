#!/usr/bin/bash

temperature=$(sensors | grep "Package id 0:" | grep -oP '(?<=\+)\d+(\.\d+)?(?=°C)' | sed -n '1p')
echo $temperature
