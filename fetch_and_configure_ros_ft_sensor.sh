#!/bin/bash

#create directory
echo "Enter Directory Name:"
read -p "" dir_name
mkdir $dir_name/src -p

#setup catkin workspace
cd $dir_name/src
catkin_init_workspace
git clone https://github.com/OptoForce/etherdaq_ros.git
cd ..
catkin_make
source devel/setup.bash

#modify the demo.launch file
echo "$(tput setaf 2)Enter the FT Sensor's IP Address:$(tput sgr0)"
read -p "" ip_addr
sed -i -e "s/192.168.100.12/$ip_addr/g" ./src/etherdaq_ros/launch/demo.launch

#generate a run file
echo "source devel/setup.bash; roslaunch optoforce_etherdaq_driver  demo.launch" > run.sh
chmod +x run.sh
rm -rf ./src/etherdaq_ros/.git

#make sure the new directory isnt pushed to git 
cd ..
echo $dir_name >> .gitignore
