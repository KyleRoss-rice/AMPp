cmake_minimum_required(VERSION 3.20)
project(AMPpCore)

set(CMAKE_CXX_STANDARD 20)

find_package(Eigen3 3.4 REQUIRED NO_MODULE)
find_package(Bullet REQUIRED)
include_directories(${BULLET_INCLUDE_DIR})

FILE(GLOB_RECURSE SOURCES "src/*.cpp")
add_library(AMPpCore SHARED ${SOURCES})

target_link_libraries(AMPpCore Eigen3::Eigen ${BULLET_LIBRARIES})

message(STATUS "foo include dir: ${BULLET_FOUND}")

