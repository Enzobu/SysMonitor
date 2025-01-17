#!/bin/bash

temperature=$(sensors | grep 'Composite' | grep -oP '(?<=\+)\d+(\.\d+)?(?=°C)' | sed -n '1p')
echo $temperature
