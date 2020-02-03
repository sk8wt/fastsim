# FastSim

This is a point simulator for a drone. The original code was adapted from [FlightGoggles](https://flightgoggles.mit.edu)

## Installing the Simulator

First, we will start by cloning the repo:
```
$ cd ~
$ git clone https://github.com/hildebrandt-carl/fastsim.git
$ cd ~/fastsim
```

Next, install all the prerequisites required for this project:
```
$ sudo apt-get update
$ sudo apt-get install libsdl-dev -y
$ sudo apt-get install python-pip -y
$ python2 -m pip install --upgrade pip
$ python2 -m pip install scipy
```

Now we are going to install the ROS dependent dependencies:
```
$ cd ~/fastsim
$ rosdep install --from-paths src --ignore-src --rosdistro kinetic -y
$ sudo apt-get install ros-kinetic-joy -y
$ sudo apt-get install ros-kinetic-imu-filter-madgwick -y
```

Next, we are going to compile to the workspace.
```
$ cd ~/fastsim
$ catkin build
```

## Using the Simulator

Finally, we can run the simulator
```
$ source ~/fastsim/devel/setup.bash
$ roslaunch flightcontroller fly.launch
```

Inside the rqt_publisher publish messages to:
**Topic:** /uav/input/position 
**Message Type:** geometry_msgs/Vector3
**Frequency:** 1Hz


Set the x,y, and z: the quadrotor will fly to that point.

## Testing the Simulator

To test the simulator, let it run for a minute. Do not provide the simulator with any input x,y, or z position. The default position is (0,0,3). The simulator should look as shown below. If the quadrotor (blue point) falls off the screen, and you have tried improving your VM's performance using the FAQ on the website, please let us know.

![](./sim_running.gif)