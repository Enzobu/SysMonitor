#!/bin/bash

# Récupère la consommation énergétique
consumption=$(cat /sys/class/power_supply/BAT0/power_now)

# Divise par 1 000 000 pour obtenir des watts
consumption_in_watts=$(echo "scale=2; $consumption / 1000000" | bc)

# Affiche la consommation en watts
echo "$consumption_in_watts"
