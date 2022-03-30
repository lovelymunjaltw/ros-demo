add_definitions(-DUNITTEST_SRC_DIR="${PROJECT_SOURCE_DIR}/src/tests/unittests")

add_rostest_gtest(test_publisher test_publisher.test test_publisher.cpp)
add_dependencies(test_publisher publisher)
target_link_libraries(test_publisher ${catkin_LIBRARIES} ${GTEST_LIBRARIES})


add_rostest_gtest(test_subscriber test_subscriber.test test_subscriber.cpp)
add_dependencies(test_subscriber subscriber)
target_link_libraries(test_subscriber ${catkin_LIBRARIES} ${GTEST_LIBRARIES} ${PYTHON_LIBRARIES})