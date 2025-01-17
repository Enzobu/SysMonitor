#!/bin/bash

batteryFullDesign=$(cat /sys/class/power_supply/BAT0/energy_full_design)

echo $batteryFullDesign
