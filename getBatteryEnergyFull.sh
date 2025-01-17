#!/bin/bash

batteryFull=$(cat /sys/class/power_supply/BAT0/energy_full)

echo $batteryFull
