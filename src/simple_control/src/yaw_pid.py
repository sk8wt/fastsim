#!/usr/bin/env python 
import rospy
from threading import Lock
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float64

# Please implement the TODOs after you write the test cases.
class YawPID():
    def __init__(self):
        # this is used to check that a new measurement was received
        # the callback should set it to True
        self.changed = False
        self.output = 0.0
        self.lock = Lock()
        # TODO (3) read param /yaw_pid_node/kp
	self.kp = rospy.get_param("/yaw_pid_node/kp", 0.0)
        # TODO (4) read param /yaw_pid_node/ki
	self.ki = rospy.get_param("/yaw_pid_node/ki", 0.0)
        # TODO (5) read param /yaw_pid_node/kd
	self.kd = rospy.get_param("/yaw_pid_node/kd", 0.0)
	self.setpoint = rospy.get_param("/yaw_pid_node/setpoint", 0.0)
        # TODO (3) create subscriber to the topic '/uav/sensors/attitude' with type Vector3
	self.yaw_sub = rospy.Subscriber('/uav/sensors/attitude', Vector3, self.yaw_angle_callback, queue_size = 1)
        # TODO (2) create publisher on the topic '/uav/input/yaw' with type Float64
	self.yaw_pub  = rospy.Publisher('/uav/input/yaw', Float64, queue_size = 1)
        self.control_loop()

    def yaw_angle_callback(self, msg):
        self.lock.acquire()
        # TODO (3) update the changed flag
	self.changed = True
	self.output= msg.z 
        # TODO (3) record new measurement
        self.lock.release()

    def control_loop(self):
        # TODO initializations for any variables you may use in the control loop
	output = 0.0
	error = 0.0
	integral_helper = 0.0
	derivative_helper = 0.0
	time_interval = 0.01
        # TODO (2) set the rate (use the variable ros_rate)
	ros_rate = rospy.Rate(100)
        while not rospy.is_shutdown():
            # TODO (3) read param /yaw_pid_node/setpoint
            self.lock.acquire()
            if self.changed:
                self.changed = False
                output = 0.0
                # TODO (3) calculate error
		error = self.setpoint - self.output
                # TODO (3) reset self.output
		self.output = 0.0
                # TODO (3) add the proportional term to self.output
		if (self.kp != 0.0):
			output += self.kp * error
                # TODO (4) add the integral term to self.output
		if (self.ki != 0.0):
			output += (self.ki * time_interval * error) + integral_helper
			integral_helper = output
                # TODO (5) add the derivative term to self.output
		if (self.kd != 0.0):
			output += self.kd * ((error - derivative_helper)/time_interval)
			derivative_helper = error
            self.lock.release()    
            # TODO (2) publish the control self.output
            self.yaw_pub.publish(output)
	    ros_rate.sleep()

if __name__ == '__main__':
    rospy.init_node('yaw_pid_node')
    try:
        YawPID()
    except rospy.ROSInterruptException:
        pass
