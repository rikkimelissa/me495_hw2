#!/usr/bin/env python

import rospy
import roslib
import math import sqrt, pi, acos, atan2, cos
from sensor_msgs.msg import JointState

def draw_circle_ik():

	pub = rospy.Publisher('joint_states',Twist, queue_size = 10)
	rospy.init_node('ik', anonymous=True)
	rate = rospy.Rate(50)
	joint_state = JointState()
	joint_state.header = Header()
	joint_state.header.stamp = rospy.Time.now()
	joint_state.name = ['th1','th2']
	joint_state.position = [0,0]
	joint_state.velocity = []
	joint_state.effort = []
	

	while not rospy.is_shutdown():

        # Calculate desired x and y positions
        t = rospy.get_time()
        x = .5*cos(2*pi*t/5) + 1.25
        y = .5*sin(2*pi*t/5)
        
        # Inverse kinematics
        B = sqrt(x**2+y**2)
        q1 = atan2(y,x)
        q2 = acos((B**2+l1**2-l2**2/(2*B*l1))
        th1 = q1-q2
        q3 = acos((l1**2+l2**2-B**2)/(2*l1*l2))
        th2 = pi-q3
		
		# Publish angles
		joint_state.position = [th1,th2]
		rospy.loginfo(angle_cmd)
		pub.publish(angle_cmd)
        rate.sleep()
                                                                                                                         
if __name__ == "__main__":
    try:
        draw_circle_ik()
    except rospy.ROSInterruptException:
        pass
    


