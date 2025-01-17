#!/bin/bash

temperature=$(sensors | grep 'temp1'  | grep -oP '(?<=\+)\d+(\.\d+)?(?=°C)' | sed -n '2p')
echo $temperature
