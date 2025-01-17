#!/bin/bash

vitesse=$(sensors | grep 'cpu_fan' | grep -oP ':\s*\K\d+(?=\s+RPM)')
echo $vitesse
