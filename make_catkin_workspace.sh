#!/bin/bash
read -p "Enter the Workspace Name: " dirname 
mkdir $dirname/src -p
cd $dirname/src
catkin_init_workspace
cd ..
catkin_make
source devel/setup.bash
