#!/usr/bin/env python

import rospy
from geometry_msgs.msg import TwistStamped
from altitude.msg import PressureAltitudeStamped

import numpy as np
from Queue import LifoQueue
from enum import Enum 

class MeasurementType(Enum):
  PRESSURE_ALTITUDE = 1
  GPS_ALTITUDE = 2
  VELOCITY = 3

class Measurement:
    def __init__(self, measurement_type, value, timestamp):
        self.measurement_type = measurement_type
        self.value = value
        self.timestamp = timestamp

class KalmanFilter():

    def __init__(self):
        self.last_timestamp = None
        # the variance used in the matrix Q
        self.process_variance = rospy.get_param("/kalman_filter_node/process_variance", 100)
        # the variance used in the matrix R for the GPS measurements
        self.gps_variance = rospy.get_param("/kalman_filter_node/gps_variance", 0.1)
        # the variance used in the matrix R of the pressure altitude measurements
        self.pressure_variance = rospy.get_param("/kalman_filter_node/pressure_variance", 0.1)
        $ the variance used in the matrix R of the vertical velocity measurements
        self.velocity_variance = rospy.get_param("/kalman_filter_node/velocity_variance", 0.1)
        
        self.queue = LifoQueue()

        self.sub_pa = rospy.Subscriber('/uav/sensors/pressure_altitude',
                                      PressureAltitudeStamped, self.process_pressure_altitude,
                                      queue_size = 1)
        self.sub_gps_a = rospy.Subscriber('/uav/sensors/gps_altitude',
                                      PressureAltitudeStamped, self.process_gps_altitude,
                                      queue_size = 1)
        self.sub_vel = rospy.Subscriber('/uav/sensors/velocity',
                                      TwistStamped, self.process_velocity,
                                      queue_size = 1)
        self.pub =  rospy.Publisher('/uav/sensors/kalman_filter_altitude',
                                   PressureAltitudeStamped,
                                   queue_size=1)
        self.mainloop()


    def process_pressure_altitude(self, msg):
        self.queue.put(Measurement(MeasurementType.PRESSURE_ALTITUDE,
                                      msg.value,
                                      msg.stamp))

    def process_gps_altitude(self, msg):
        self.queue.put(Measurement(MeasurementType.GPS_ALTITUDE,
                                      msg.value,
                                      msg.stamp))
        
    def process_velocity(self, msg):
        self.queue.put(Measurement(MeasurementType.VELOCITY,
                                      msg.twist.linear.z,
                                      msg.header.stamp))

    
    # The main loop of the node
    def mainloop(self):
        # Set the rate of this loop
        rate = rospy.Rate(20)
        # state vector
        x = np.zeros((2,1), dtype=float)
        # state transition matrix
        F = np.zeros((2,2), dtype=float)
        F[0][0] = 1
        F[1][1] = 1
        # process covariance matrix
        Q = np.zeros((2,2), dtype=float)
        # initialize P
        P = np.zeros((2,2), dtype=float)
        P[0][0] = 1
        P[1][1] = 1000
        # initialize I
        I = np.zeros((2,2), dtype=float)
        I[0][0] = 1
        I[1][1] = 1 
        # While ROS is still running
        while not rospy.is_shutdown():
            while not self.queue.empty():
                measurement = self.queue.get()
                if self.last_timestamp:
                    ########### predict step
                    delta_t = (measurement.timestamp - self.last_timestamp).to_sec()
                    # TODO: initialize matrices F and Q which depend on the delta_t
           		F[0][1] = delta_t
			F[1][0] = 0
         
                    # TODO: update the state and the process matrix 

			Q[0][0] = (pow(delta_t, 4)) / 4.0
			Q[0][1] = (pow(delta_t, 3)) / 2.0 
			Q[1][0] = (pow(delta_t, 3)) / 2.0
			Q[1][1] = (pow(delta_t, 2)) 

			x = np.matmul(F, x)
			P = np.add(np.matmul(np.matmul(F,P), np.transpose(F)),Q)

                    ########### update step
                    # TODO: initialize H for the measurement type
			H_gps = np.zeros((1,2), dtype=float)
			H_gps[0][0] = 1.0
			H_gps[0][1] = 0.0

			H_vel = np.zeros((1,2), dtype=float)
			H_vel[0][0] = 0.0
			H_vel[0][1] = 1.0

                    # TODO: initialize R for the measurement type
			R_gps = np.zeros((1,1), dtype=float)
			R_gps[0[0] = self.gps_variance

			R_pressure = np.zeros((1,1), dtype=float)
			R_pressure[0][0] = self.pressure_variance

			R_vel = np.zeroes((1,1), dtype=float)
			R_vel[0][0] = self.velocity_variance
			
                    # TODO: initialize the measurement z
                    z = np.zeros((1,1), dtype=float)
                    z[0] = #TODO
                    # TODO: implement the update equations 
                else:
                    # first measurement
                    if measurement.measurement_type == MeasurementType.VELOCITY:
                        x[1] = measurement.value
                    else:
                        x[0] = measurement.value
                # update timestamp
                self.last_timestamp = measurement.timestamp
                    
                # publish message
                msg = PressureAltitudeStamped()
                msg.value = x[0]
                msg.stamp = self.last_timestamp
                self.pub.publish(msg)

            # Sleep for the remainder of the loop
            rate.sleep()


if __name__ == '__main__':
    rospy.init_node('kalman_filter_node')
    try:
        KalmanFilter()
    except rospy.ROSInterruptException:
        pass
