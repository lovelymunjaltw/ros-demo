Prerequisite: Need an Ubuntu Machineo or VM

Install ROS, follow the steps mentioned here:
http://wiki.ros.org/melodic/Installation/Ubuntu

catkin is the official build system of ROS.  It combines CMake macros and Python scripts to provide some functionality on top of CMake's normal workflow. Its get installed with ROS.

Follow below steps to create ROS package and nodes:

	Create a workspace for catkin:
		$ mkdir -p ~/catkin_ws/src
		$ cd ~/catkin_ws/
		$ catkin_make

		catkin_make will create three directories: src, build and devel


	Create a package (workspace can have multiple packages):
		$ catkin_create_pkg ros_demo std_msgs roscpp

		Here ros_demo is name of package and after package-name, we can give dependencies
		Above command will create few files and directories:
		directories: src, include
		files: package.xml, CMakeLists.txt