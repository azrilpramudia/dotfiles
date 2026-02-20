#!/bin/bash

# wait for desktop
sleep 2

# kill picom if it's ready running
pkill picom

# running picom
picom --daemon &
