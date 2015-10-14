from visualization_msgs.msg import Marker
import rospy
import roslib
from math import sqrt, pi, acos, atan2, cos, sin
import tf
import geometry_msgs.msg

def animate():

    listener = tf.TransformListener()
    pub = rospy.Publisher('joint_states', Marker, queue_size = 10)    
    rospy.init_node('marker_node', anonymous=True)
    rate = rospy.Rate(20)
   # marker_msg = Marker()
	
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('joint1','joint2',rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        rate.sleep()

        rospy.log_info(trans)
        rospy.log_info(rot)

if __name__ == "__main__":
    try:
        animate()
    except rospy.ROSInterruptException:
        pass
    
