#!/bin/bash
cd Dependencies/
echo "Installing Snake-Solver Script..."
sudo cp ./snake-solver /usr/bin
echo "Done"
echo "Installing dependency - python-xlib..."
sudo apt-get install python-xlib
sudo python setup.py build
sudo python setup.py install