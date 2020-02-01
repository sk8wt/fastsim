# FastSim

This is a point simulator for a drone. The original code was adapted from [FlightGoggles](https://flightgoggles.mit.edu)

## Installing the Simulator

First we will start by cloning the repo:
```
$ git clone https://github.com/hildebrandt-carl/fastsim.git
$ cd fastsim
```

Next install all the prerequisits required for this project:
```
$ sudo apt-get update
$ sudo apt-get install libsdl-dev -y
$ sudo apt-get install python-pip -y
$ python2 -m pip install --upgrade pip
$ python2 -m pip install scipy
```

Now we are going to install the ROS dependent dependancies:
```
$ rosdep install --from-paths src --ignore-src --rosdistro kinetic -y
$ sudo apt-get install ros-kineitc-joy -y
$ sudo apt-get install ros-kinetic-imu-filter-madgwick -y
```

Next we are going to compile to workspace.
```
$ catkin build
```

## Using the Simulator

Finally we are able to run the simulator
```
$ source fastsim/devel/setup.bash
$ roslaunch flightcontroller fly.launch
```

Inside the rqt_publisher publish messages to:
**Topic:** /uav/input/position 
**Message Type:** geometry_msgs/Vector3
**Frequency:** 1Hz


Set the x,y and z and the quadrotor will fly to that point.
