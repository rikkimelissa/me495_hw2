#!/usr/bin/env python

import rospy
from math import sqrt, pi, acos, atan2, cos, sin
from sensor_msgs.msg import JointState

def draw_circle_ik():

    # Initialize publisher node
    pub = rospy.Publisher('joint_states', JointState, queue_size = 10)
    rospy.init_node('ik')
    rate = rospy.Rate(50)

    # Initialize JointState message
    joint_state = JointState()
    joint_state.header.stamp = rospy.Time.now()
    joint_state.name = ['joint1','joint2','joint3']
    joint_state.position = [0,0,0]
    joint_state.velocity = []
    joint_state.effort = []
    p = rospy.get_param('~period')
    
    while not rospy.is_shutdown():

        # Calculate desired x and y positions
        t = rospy.get_time()
        x = .5*cos(2*pi*t/p) + 1.25
        y = .5*sin(2*pi*t/p)
        
        # Inverse kinematics
        l1 = 1
        l2 = 1
        B = sqrt(x**2+y**2)
        
        q1 = atan2(y,x)
        q2 = acos((B**2+l1**2-l2**2)/(2*B*l1))
        th1 = q1-q2
        q3 = acos((l1**2+l2**2-B**2)/(2*l1*l2))
        th2 = pi-q3
		
        # Publish angles
        joint_state.header.stamp = rospy.Time.now()
        joint_state.position = [th1,th2,0]
        pub.publish(joint_state)
        rate.sleep()

if __name__ == "__main__":
    try:
        draw_circle_ik()
    except rospy.ROSInterruptException:
        pass
    


