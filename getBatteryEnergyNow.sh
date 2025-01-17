#!/bin/bash

energyNow=$(cat /sys/class/power_supply/BAT0/energy_now)

echo $energyNow

