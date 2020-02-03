#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

class Viewer():

  def __init__(self):
    # When this node shutsdown
    rospy.on_shutdown(self.shutdown_sequence)

    # Set the rate
    self.rate = 24.0
    self.dt = 1.0 / self.rate

    # Create the position
    self.x = 0
    self.y = 0
    self.z = 0

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


	# Called on ROS shutdown
  def shutdown_sequence(self):
    rospy.loginfo(str(rospy.get_name()) + ": Shutting Down")


  def view_point(self):
    # self.fig.canvas.restore_region(self.background)
    # self.ax.plot(data, 'o')
    # plt.plot(data, 'o')
    # # plt.draw()
    
    # self.fig.canvas.draw()
    plt.cla()
    self.ax.set_title("Pos: (" + str(int(self.x)) + ", " + str(int(self.y)) + ", " + str(int(self.z)) + ")")
    self.ax.set_xlim([-5, 5])
    self.ax.set_ylim([-5, 5])
    self.ax.set_zlim([0, 5])
    self.ax.set_xlabel("X Axis")
    self.ax.set_ylabel("Y Axis")
    self.ax.set_zlabel("Z Axis")
    self.ax.scatter(self.x, self.y, self.z)
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
