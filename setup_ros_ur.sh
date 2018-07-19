#!/bin/bash

#create directory
echo "Enter Directory Name:"
read -p "" dir_name
mkdir $dir_name/src -p

#setup catkin workspace
cd $dir_name/src
catkin_init_workspace
git clone https://github.com/rushadantia/universal_robot.git
cd universal_robot/
git clone https://github.com/Zagitta/ur_modern_driver
cd ../../
rosdep install --from-paths src --ignore-src -r -y
catkin_make
source devel/setup.bash

#create run 
touch run_server.sh
chmod +x run_server.sh
echo "$(tput setaf 2)Enter the Robot's IP Address:$(tput sgr0)"
read -p "" robot_ip
echo "source devel/setup.bash;roslaunch src/universal_robot/ur_modern_driver/launch/ur3_bringup.launch robot_ip:=$robot_ip" >> run_server.sh

#create move
touch move_robot.sh
chmod +x move_robot.sh
echo "echo \"$(tput setaf 1)Don't forget to start the server!!!$(tput sgr0)\"" > move_robot.sh
echo "source devel/setup.bash" >> move_robot.sh
echo "rosrun ur_driver test_move.py $robot_ip" >> move_robot.sh

#dont add it to git
cd ..
echo $dir_name/ >> .gitignore
