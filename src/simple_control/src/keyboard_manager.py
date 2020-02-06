#!/usr/bin/env python
import rospy
import time
import copy
from keyboard.msg import Key
from geometry_msgs.msg import Vector3


# Create a class which we will use to take keyboard commands and convert them to a position
class KeyboardManager():
  # On node initialization
  def __init__(self):
    # Create the publisher and subscriber
    self.position_pub = rospy.Publisher('/keyboardmanager/position', Vector3, queue_size=1)
    self.keyboard_sub = rospy.Subscriber('/keyboard/keydown', Key, self.get_key, queue_size = 1)
    # Create the position message we are going to be sending
    self.pos = Vector3()
    self.prev_pos = Vector3()
    # Start the drone a little bit off the ground
    self.pos.z = 0.5
    # Create a variable we will use to hold the key code
    self.key_code = -1
    # Give the simulation enough time to start
    time.sleep(10)
    # Call the mainloop of our class
    self.mainloop()


  # Callback for the keyboard sub
  def get_key(self, msg):
    self.key_code = msg.code


  # Converts a position to string for printing
  def goalToString(self, msg):
    pos_str = "(" + str(msg.x) 
    pos_str += ", " + str(msg.y)
    pos_str += ", " + str(msg.z) + ")"
    return pos_str


  def mainloop(self):
    # Set the rate of this loop
    rate = rospy.Rate(20)

    # While ROS is still running
    while not rospy.is_shutdown():

      # PASTE CODE FROM LAB 2 Checkpoint 4
 # Check if any key has been pressed
      if self.key_code == 273:
          print("pressed the up arrow key!")
          self.pos.z += .25

      if self.key_code == 274:
          print("pressed the down arrow key")
          self.pos.z -= .25

      if self.key_code == 276:
          print("pressed the left arrow key")
          self.pos.x -= 0.5

      if self.key_code == 275:
          print("pressed the right arrow key")
          self.pos.x += 0.5

        
      # Check if the position has changed
      check_x = self.prev_pos.x != self.pos.x
      check_y = self.prev_pos.y != self.pos.y
      check_z = self.prev_pos.z != self.pos.z
      if check_x or check_y or check_z:
        self.prev_pos = copy.deepcopy(self.pos)
        rospy.loginfo(str(rospy.get_name()) + ": Keyboard: " + self.goalToString(self.pos))

      if self.key_code == 13:
        # Publish the position
        self.position_pub.publish(self.pos)
        rospy.loginfo(str(rospy.get_name()) + ": Sending Position")

      # Reset the code
      if self.key_code != -1:
        self.key_code = -1

      # Sleep for the remainder of the loop
      rate.sleep()


if __name__ == '__main__':
  rospy.init_node('keyboard_manager')
  try:
    ktp = KeyboardManager()
  except rospy.ROSInterruptException:
    pass
