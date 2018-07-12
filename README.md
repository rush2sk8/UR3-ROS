# UR3 ROS

[```setup_ros_ft_sensor.sh```](https://github.com/rushadantia/UR3-ROS/blob/master/setup_ros_ft_sensor.sh)

This script creates a catkin workspace that is configured and ready to run the [etherdaq_ros](https://github.com/OptoForce/etherdaq_ros.git) module. It also modifies the ```demo.launch``` file so that it uses the ip of YOUR robot. It also generates a ```run.sh``` that will set the ```source devel/setup.bash``` while also making itself executable that will start the ros instance.


[```setup_ros_ur.sh```](https://github.com/rushadantia/UR3-ROS/blob/master/setup_ros_ur.sh)

Creates the directory to setup the ros packages for the ur3 and uses [my fork](https://github.com/rushadantia/universal_robot) of [Thomas Timm's](https://github.com/ThomasTimm) [universal_robot](https://github.com/ThomasTimm/universal_robot) package. Along with that it uses the [Zagitta](https://github.com/Zagitta/) [ur_modern_driver](https://github.com/Zagitta/ur_modern_driver).
