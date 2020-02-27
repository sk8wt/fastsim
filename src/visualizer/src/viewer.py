#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped, Pose
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from tf.transformations import euler_from_quaternion
from math import sin, cos, degrees

class Viewer():

  def __init__(self):
    # When this node shutsdown
    rospy.on_shutdown(self.shutdown_sequence)

    # Set the rate
    self.rate = 1.0
    self.dt = 1.0 / self.rate

    # Create the position
    self.x = 0
    self.y = 0
    self.z = 0
    self.quaternion = (0, 0, 0, 0)

    self.fig = plt.figure()
    self.ax = self.fig.gca(projection='3d')
    self.ax.set_xlim([-5, 5])
    self.ax.set_ylim([-5, 5])
    self.ax.set_zlim([0, 5])
    plt.ion() 
    plt.show()
    
    # Create the subscribers and publishers
    self.gps_sub = rospy.Subscriber("uav/sensors/gps", PoseStamped, self.get_gps)

    # Run the communication node
    self.DrawLoop()


  # This is the main loop of this class
  def DrawLoop(self):
    # Set the rate
    rate = rospy.Rate(self.rate)

    # While running
    while not rospy.is_shutdown():

        # Display the position
        self.view_point()

        # Sleep any excess time
        rate.sleep()


  # Call back to get the gps data
  def get_gps(self, msg):
    self.x = msg.pose.position.x
    self.y = msg.pose.position.y
    self.z = msg.pose.position.z

    self.quaternion = (msg.pose.orientation.x,
                       msg.pose.orientation.y,
                       msg.pose.orientation.z,
                       msg.pose.orientation.w)


	# Called on ROS shutdown
  def shutdown_sequence(self):
    rospy.loginfo(str(rospy.get_name()) + ": Shutting Down")


  def view_point(self):
    # self.fig.canvas.restore_region(self.background)
    # self.ax.plot(data, 'o')
    # plt.plot(data, 'o')
    # # plt.draw()
    euler = euler_from_quaternion(self.quaternion)
    roll = euler[0]
    pitch = euler[1]
    yaw = euler[2]
    new_x = sin(yaw)
    new_y = cos(yaw)
    
    # self.fig.canvas.draw()
    plt.cla()
    self.ax.set_title("Pos: (" + str(round(self.x,2)) + ", " + str(round(self.y,2)) + ", " + str(round(self.z,2)) + ")")
    self.ax.set_xlim([-5, 5])
    self.ax.set_ylim([-5, 5])
    self.ax.set_zlim([0, 5])
    self.ax.set_xlabel("X Axis")
    self.ax.set_ylabel("Y Axis")
    self.ax.set_zlabel("Z Axis")
    self.ax.quiver(self.x, self.y, self.z, new_x, new_y, 0, color='r')
    plt.draw()
    plt.pause(0.05)



def main():
  rospy.init_node('viewer_node')
  try:
    v = Viewer()
  except rospy.ROSInterruptException:
    pass


if __name__ == '__main__':
  main()
