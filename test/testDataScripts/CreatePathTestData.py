#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This script generates test data for Path (nav_msgs/Path)"""
import math
import yaml
import yaml
from nav_msgs.msg import Path
from std_msgs.msg import Header
from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped
from tf.transformations import quaternion_from_euler


def createPath(coordinates, pathName):
    print("Creating data for: " + pathName)

    # createing nav_msgs/Path object
    path = Path()

    # Path contains 2 things: 1. header  2. list of PoseStamped (path.poses)
    path.header = Header(frame_id='map')
    path.poses = []

    seq = 0
    for i in range(len(coordinates)):
        # creating Point
        point = Point(coordinates[i][0], coordinates[i][1], 0)

        # creating Quaternion
        if i < len(coordinates) - 1:
            heading = getHeading(coordinates[i][0], coordinates[i][1], coordinates[i + 1][0], coordinates[i + 1][1])
        quaternion = getQuaternion(0, 0, heading)

        # creating Pose with above Point and Quaternion
        pose = Pose(point, quaternion)

        # creating PoseStamped with above Pose and appending in the Path
        poseStamped = createPoseStamped(pose, seq)
        path.poses.append(poseStamped)
        seq = seq + 1

    writeDataToYamlFile(path, pathName)


def createPoseStamped(pose, sequence_number):
    return PoseStamped(
    header=Header(seq=sequence_number, frame_id='map'),
    pose=pose
)


def getHeading(x1, y1, x2, y2):
    # returns heading i.e. direction towards next point on the path
    return math.atan2(y2 - y1, x2 - x1)


def getQuaternion(roll, pitch, yaw):# yaw is same as heading i.e. direction towards next point on the path
    q = quaternion_from_euler(roll, pitch, yaw, 'ryxz')
    qx = q[0]
    qy = q[1]
    qz = q[2]
    qw = q[3]
    return Quaternion(qx, qy, qz, qw)


def writeDataToYamlFile(data, pathName):
    filename = pathName + ".yaml"
    with open(filename, "wb") as yamlFile:
        yaml.dump(
            yaml.load(str(data), Loader=yaml.SafeLoader),
            yamlFile,
            indent=4)
    print("Writing data to file: " + filename + " completed\n")


# create various test data with method: createPath
# test data 1:
coordinates1 = [[10, 10], [30, 10], [60, 10], [60, 35], [55, 60], [30, 60], [15, 60], [30, 30]]
pathName = "shape1_rectangle"
createPath(coordinates1, pathName)

# test data 2:
coordinates2 = [[0, 0], [17, 17], [30, 30], [15, 45], [0, 60], [-15, 45], [-30, 30], [-10, -10]]
pathName = "shape2"
createPath(coordinates2, pathName)

# test data 3:
coordinates3 = [[10, 50], [50, 300], [200, 200], [700, 650], [650, 380], [800, 300], [300, 800], [120, 47]]
pathName = "shape3"
createPath(coordinates3, pathName)