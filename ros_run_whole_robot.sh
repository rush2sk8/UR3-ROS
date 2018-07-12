#!/bin/bash

pkill roscore
roscore &

echo "Enter name of ft_ros_sensor directory:"
read -p "" ft
echo "Enter name of ros_ur directory:"
read -p "" ur

cd $ft 
source devel/setup.bash
cd ..
./run.sh &
cd .. 
cd $ur
source devel/setup.bash
./run.sh &
cd ..

