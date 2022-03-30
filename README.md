Prerequisite: Need an Ubuntu Machineo or VM

Install ROS, follow the steps mentioned here:
http://wiki.ros.org/melodic/Installation/Ubuntu

catkin is the official build system of ROS.  It combines CMake macros and Python scripts to provide some functionality on top of CMake's normal workflow. Its get installed with ROS.


Follow below steps to create ROS package and nodes:

	Create a workspace for catkin:
		$ mkdir -p ~/catkin_ws/src
		$ cd ~/catkin_ws/
		$ source /opt/ros/melodic/setup.bash
		$ catkin_make

		catkin_make will create three directories: src, build and devel
		To set up ctakin directories, command: source devel/setup.bash


	Create a package (workspace can have multiple packages):
		$ catkin_create_pkg ros_demo std_msgs roscpp rospy

		Here `ros_demo` is name of package and after package-name, we can give dependencies
		Above command will create few files and directories:
		directories: src, include
		files: package.xml, CMakeLists.txt


	Publisher and Subscriber are created by cpp files.
	Build the project using command: catkin_make
		Note - Always run build related commands at `catkin_ws` directory.

		It will create nodes execuables with the name mentioned in CMakeLists.txt at path:
		~/catkin_ws/devel/lib/ros_demo 
		Node execuatbles with name: publisher and subscriber

	How to run nodes:
		1. Start rosmaster (through which communicaiton will start): roscore
		2. Start subsciber node: ./publisher
		3. start subscriber node: ./subscriber
		please make sure you run above 2 commands where execubales are present i.e. at ~/catkin_ws/devel/lib/ros_demo 

	Few useful commands related to nodes and topics:
		1. rosnode list
		2. rosnode info <any node name>
		3. rostopic list
		4. rostopic info <any toic name>
		
		Ref for commands:
		http://wiki.ros.org/rostopic
		http://wiki.ros.org/rosservice


Follow below steps to visualise data through Rviz:
	
	1. Create data with any message type supoorted by Rviz. e.g. nav_msgs/Path. We have created data using python script.
	2. start ros master, command: roscore
	3. start rviz, command: rviz
	4. Publish data over a topic (with message type and data file): rostopic pub <any-topic-name> <message-type> -f <file name>
	e.g. rostopic pub topic1 nav_msgs/Path -f shape1_rectangle.yaml
	Run above command where .yaml file is stored
	5. In rviz, Add required display (Path in our case) and select topic name (i.e. /topic1)
	Now we should be able to see the Path in rviz.

	Note:
	Rviz can visualise 3D data as well.
	Data can be create using c++ also. 
	We can write our own plugin to visualise any custom data type.

	Ref: http://wiki.ros.org/rviz/UserGuide