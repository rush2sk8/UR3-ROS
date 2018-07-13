#!/usr/bin/env python
import rospy
from geometry_msgs.msg import WrenchStamped 


def callback(msg):
	rospy.loginfo(rospy.get_caller_id() + "%u Fx:%.2f Fy:%.2f Fz:%.2f Tx:%.2f Ty:%.2f Tz:%.2f \r\n", msg.header.seq, msg.wrench.force.x, msg.wrench.force.y, msg.wrench.force.z, msg.wrench.torque.x, msg.wrench.torque.y, msg.wrench.torque.z)

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber('ethdaq_data', WrenchStamped , callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
