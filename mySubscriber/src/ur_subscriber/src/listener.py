#!/usr/bin/env python
import time
import roslib; roslib.load_manifest('ur_driver')
import rospy
import actionlib
from control_msgs.msg import *
from trajectory_msgs.msg import *

JOINT_NAMES = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint',
               'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
Q1 = [2.2,0,-1.57,0,0,0]
Q2 = [1.5,0,-1.57,0,0,0]
Q3 = [1.5,-0.2,-1.57,0,0,0]
QQ = [[.79150682,-1.4945254,-1.5666075,-1.6758651,1.558579,1.5475834],[.79133228,-1.6645205,-2.11429186,-0.95836029,1.5617206,1.5460127]]


def eth_callback(msg):
	#rospy.loginfo("%u Fx:%.2f Fy:%.2f Fz:%.2f Tx:%.2f Ty:%.2f Tz:%.2f \r\n", msg.header.seq, msg.wrench.force.x, msg.wrench.force.y, msg.wrench.force.z, msg.wrench.torque.x, msg.wrench.torque.y, msg.wrench.torque.z)
	print("FT",msg.header.seq, msg.wrench.force.x, msg.wrench.force.y, msg.wrench.force.z, msg.wrench.torque.x, msg.wrench.torque.y, msg.wrench.torque.z)

def ur_callback(msg):
	time.sleep(.25)
	for t in msg.transforms:
		#rospy.loginfo("X:%.2f  Y:%.2f  Z:%.2f Rx:%.2f Ry:%.2f Rz:%.2f \r\n", t.transform.translation.x, t.transform.translation.y,  t.transform.translation.z, t.transform.rotation.x, t.transform.rotation.y, t.transform.rotation.z)
		print("UR",t.transform.translation.x, t.transform.translation.y,  t.transform.translation.z, t.transform.rotation.x, t.transform.rotation.y, t.transform.rotation.z)
def move():
	g = FollowJointTrajectoryGoal()
	g.trajectory = JointTrajectory()
	g.trajectory.joint_names = JOINT_NAMES
	d = 2.0
	
	g.trajectory.points = []
	for i in range(10):
		for x in range(len(QQ)):
			g.trajectory.points.append(JointTrajectoryPoint(positions=QQ[x], velocities=[0]*6, time_from_start=rospy.Duration(d)))
			d += 2
	client.send_goal(g)
	try:
		client.wait_for_result()
	except KeyboardInterrupt:
		client.cancel_goal()
		raise

def listener():
	global client
	try:
		rospy.init_node('listener', anonymous=True)
		rospy.init_node('test_move', anonymous=True, disable_signals=True)
		client = actionlib.SimpleActionClient('follow_join_trajectory', FollowJointTrajectoryAction)
		client.wait_for_server()
		move()
		rospy.Subscriber('ethdaq_data', WrenchStamped , eth_callback)
		rospy.Subscriber('tf', tf2_msgs.msg.TFMessage, ur_callback)
		rospy.spin()
	except KeyboardInterrupt:
		rospy.signal_shutdown("KeyboardInterrupt")
		raise
if __name__ == '__main__':
	listener()

