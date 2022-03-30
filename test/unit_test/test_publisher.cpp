#include <gtest/gtest.h>
#include <ros/ros.h>
#include "std_msgs/String.h"


bool isPublisherNameAsExpected = false;
// Call back will be triggered when a message is posted to the topic named "topic1"
void topic1Callback(const ros::MessageEvent<std_msgs::String>& msgEvent) {
	// Node named "publisher" publishes to "topic1"
	// check the name of the node that triggered this event 
	if(msgEvent.getPublisherName() == "/publisher") {
		isPublisherNameAsExpected = true;
	}
}

// Check status of the publisher node
bool isPublisherNodeRunning(std::vector<std::string>& nodeNames) {
	bool returnVal = false;
	for(int i=0; i<nodeNames.size();i++) {
		if(nodeNames[i] == "/publisher") {
			returnVal = true;
		}
	}
	return returnVal;
}

TEST(BasicTest, IsPublisherRunning) {
	std::vector<std::string> nodeNames;
	ros::master::getNodes(nodeNames);
	EXPECT_TRUE(isPublisherNodeRunning(nodeNames));
}

TEST(BasicTest, IsPublisherPublishingToTopic1) {
	ros::NodeHandle nh("");
	// unittest node will subscribe to the topic named "topic1"
	ros::Subscriber sub = nh.subscribe("/topic1", 1, &topic1Callback);
	sleep(5);
	// Verify that the sender of the message is a node named "publisher"
	EXPECT_TRUE(isPublisherNameAsExpected);
	EXPECT_EQ(1, sub.getNumPublishers());
}

int main(int argc, char** argv){
	testing::InitGoogleTest(&argc, argv);
	ros::init(argc, argv, "test_publisher");
	ros::AsyncSpinner spinner(1);
	spinner.start();
	int ret =  RUN_ALL_TESTS();
	spinner.stop();
	ros::shutdown();
	return ret;
}