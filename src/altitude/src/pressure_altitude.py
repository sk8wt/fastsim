#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import Float64
from altitude.msg import AltitudeStamped

class PressureAltitude():

    # Node initialization
    def __init__(self):
        # create the message first to avoid race conditions with the 
        # subscriber callback
        self.altitude = AltitudeStamped()
        # Create the publisher 
        self.altitude_pub = #TODO
        # Create the subscriber
        self.pressure_sub = #TODO
        rospy.spin()
        
    # Callback function to calculate the pressure altitude and publish the message
    def set_altitude(self, msg):
        # TODO update self.altitude message with the pressure altitude calculated
        # from the pressure in msg, and with current time stamp
        self.altitude.value = #TODO 
        self.altitude.stamp =  rospy.get_rostime()
        self.altitude_pub.publish(self.altitude)


if __name__ == '__main__':
    rospy.init_node('pressure_altitude_node')
    try:
        PressureAltitude()
    except rospy.ROSInterruptException:
        pass
