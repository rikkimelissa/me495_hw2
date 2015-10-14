#!/usr/bin/env python
from visualization_msgs.msg import Marker, MarkerArray
import rospy
import roslib
from math import sqrt, pi, acos, atan2, cos, sin
import tf

# I plotting the marker array with code from this answer: 
# http://answers.ros.org/question/11135/plotting-a-markerarray-of-spheres-with-rviz/

def animate():

    pub = rospy.Publisher('visualization_marker', Marker, queue_size = 10)    
    rospy.init_node('marker_node')
    listener = tf.TransformListener()
    rospy.loginfo('setup')
    rate = rospy.Rate(20)
    markerArray = MarkerArray()
    marker = Marker()
    marker.type = Marker.SPHERE
    marker.color.g = 1
    marker.color.a = 1
    marker.pose.position.x = 1
    marker.pose.position.y = 1
    marker.pose.orientation.w = 1
    marker.scale.x = .05
    marker.scale.y = .05
    marker.scale.z = .05
    marker.header.frame_id = "/link1"
    marker.header.stamp = rospy.Time.now()
    marker.action = Marker.ADD
    count = 0
    MARKERS_MAX = 100
    	
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/link1','/link3',rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        # turn trans,rot into a point
        marker.pose.position.x = trans[0]
        marker.pose.position.y = trans[1]

        # rospy.loginfo(trans[0])
        # rospy.loginfo(trans[1]) 
        
        # Publish marker
        if (count > MARKERS_MAX):
            markerArray.markers.pop(0)
        
        markerArray.markers.append(marker)
        rospy.loginfo(markerArray)

        id = 0
        for m in markerArray.markers:
            m.id = id
            id +=1

        pub.publish(marker)
        count += 1
        rate.sleep()

if __name__ == "__main__":
    try:
        animate()
    except rospy.ROSInterruptException:
        pass
    
