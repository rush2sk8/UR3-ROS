# UR3 ROS

[```fetch_and_configure_ros_ft_sensor.sh```](https://github.com/rushadantia/UR3-ROS/blob/master/fetch_and_configure_ros_ft_sensor.sh)

This script creates a catkin workspace that is configured and ready to run the [etherdaq_ros](https://github.com/OptoForce/etherdaq_ros.git) module. It also modifies the ```demo.launch``` file so that it uses the ip of YOUR robot. It also generates a ```run.sh``` that will set the ```source devel/setup.bash``` while also making itself executable that will start the ros instance
