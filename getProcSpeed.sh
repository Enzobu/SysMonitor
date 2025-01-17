#!/bin/bash

vitessePourcent=$(lscpu | grep "MHz" | grep -oP '(?<=:)\s*\d+(?=\s*%)')
vitesse=$((vitessePourcent * 4800 / 100))
echo $vitesse
