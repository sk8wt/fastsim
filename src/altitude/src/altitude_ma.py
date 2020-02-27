#!/usr/bin/env python
import rospy
import time
from threading import Lock
from altitude.msg import AltitudeStamped

class AltitudeFusion():

    # Node initialization
    def __init__(self):
        self.pressure_altitude = 0
        self.gps_altitude = 0
        self.last_timestamp = None
        self.changed = False
        self.lock = Lock()        
        # Create the publisher and subscriber
        self.pub = rospy.Publisher('/uav/sensors/altitude_ma',
                                   AltitudeStamped,
                                   queue_size=1)
        self.pa_sub = rospy.Subscriber('/uav/sensors/pressure_altitude_ma',
                                    AltitudeStamped, self.process_pressure_altitude,
                                    queue_size = 1)
        self.pa_sub = rospy.Subscriber('/uav/sensors/gps_altitude_ma',
                                    AltitudeStamped, self.process_gps_altitude,
                                    queue_size = 1)

        self.mainloop()

    def process_pressure_altitude(self, msg):
        self.lock.acquire()
        #TODO
	self.pressure_altitude = msg.value
	self.last_timestamp = msg.stamp
        self.changed = True
        self.lock.release()

    def process_gps_altitude(self, msg):
        self.lock.acquire()
        #TODO
	self.gps_altitude = msg.value
	self.last_timestamp = msg.stamp
        self.changed = True
        self.lock.release()

        
    # The main loop of the function
    def mainloop(self):
        # Set the rate of this loop
        rate = rospy.Rate(10)
        # While ROS is still running
        while not rospy.is_shutdown():
            avg_msg = AltitudeStamped()
            self.lock.acquire()
            if self.changed:
                #TODO initialize avg_msg
		avg_msg.value = (self.gps_altitude + self.pressure_altitude) / 2
		avg_msg.stamp = self.last_timestamp
                self.changed = False
            self.lock.release()
            if avg_msg:
                self.pub.publish(avg_msg)
            # Sleep for the remainder of the loop
            rate.sleep()


if __name__ == '__main__':
    rospy.init_node('altitude_ma_node')
    try:
        AltitudeFusion()
    except rospy.ROSInterruptException:
        pass

