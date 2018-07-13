# UR3 ROS

[```setup_ros_ft_sensor.sh```](https://github.com/rushadantia/UR3-ROS/blob/master/setup_ros_ft_sensor.sh)

This script creates a catkin workspace that is configured and ready to run [my fork](https://github.com/rushadantia/etherdaq_ros.git) of the [etherdaq_ros](https://github.com/OptoForce/etherdaq_ros.git) module. It also modifies the ```demo.launch``` file so that it uses the ip of YOUR robot. 


[```setup_ros_ur.sh```](https://github.com/rushadantia/UR3-ROS/blob/master/setup_ros_ur.sh)

Creates the directory to setup the ros packages for the ur3 and uses [my fork](https://github.com/rushadantia/universal_robot) of [Thomas Timm's](https://github.com/ThomasTimm) [universal_robot](https://github.com/ThomasTimm/universal_robot) package. Along with that it uses the [Zagitta](https://github.com/Zagitta/) [ur_modern_driver](https://github.com/Zagitta/ur_modern_driver).
