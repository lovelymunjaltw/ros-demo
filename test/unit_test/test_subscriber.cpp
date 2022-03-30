#include <gtest/gtest.h>
#include <ros/ros.h>
#include "std_msgs/String.h"
#include <python2.7/Python.h>

// Check status of the subscriber node
bool isSubscriberNodeRunning(std::vector<std::string>& nodeNames) {
	bool returnVal = false;
	for(int i=0; i<nodeNames.size();i++) {
		if(nodeNames[i] == "/subscriber") {
			returnVal = true;
		}
	}
	return returnVal;
}

TEST(BasicTest, IsSubscriberRunning) {
	std::vector<std::string> nodeNames;
	ros::master::getNodes(nodeNames);
	EXPECT_TRUE(isSubscriberNodeRunning(nodeNames));
}

// Call a python script that verified that subscriber is subscribing to a topic called topic1
TEST(BasicTest, HasSubscriberSubscribedToTopic1) {
	std::string path = std::string(	UNITTEST_SRC_DIR) + "/test_subscribers_subscriptions.py";
	FILE* fp = fopen(path.c_str(), "r");
	int returnVal = PyRun_SimpleFile(fp, "test_subscribers_subscriptions.py");
 	EXPECT_EQ(0, returnVal);
 	Py_Finalize();
}


int main(int argc, char** argv){
	testing::InitGoogleTest(&argc, argv);
	Py_Initialize();
	PySys_SetArgv(argc, argv);

	ros::init(argc, argv, "test_subscriber");
	ros::AsyncSpinner spinner(1);
	spinner.start();
	int ret =  RUN_ALL_TESTS();
	spinner.stop();
	ros::shutdown();
	return ret;
}