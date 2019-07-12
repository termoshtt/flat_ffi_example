cmake_minimum_required(VERSION 3.10.2)
# set(CMAKE_VERBOSE_MAKEFILE 1)

add_subdirectory(flatbuffers EXCLUDE_FROM_ALL)

find_package(Boost COMPONENTS python3 numpy3 REQUIRED)
find_package(PythonLibs REQUIRED)
include_directories(
  ${Boost_INCLUDE_DIRS}
  ${PYTHON_INCLUDE_DIRS}
  ${FLATBUFFERS_INCLUDE_DIRS}
  )

add_library(flat_cpp SHARED
  data_generated.h
  flat.cpp
  )
target_link_libraries(flat_cpp
  ${Boost_LIBRARIES}
  ${PYTHON_LIBRARY}
  flatbuffers
  )
set_target_properties(flat_cpp PROPERTIES PREFIX "")

add_custom_command(
  OUTPUT data_generated.h
  COMMAND flatc --cpp data.fbs
  DEPENDS data.fbs
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  )
add_custom_target(python_binding ALL
  COMMAND flatc --python ${CMAKE_CURRENT_SOURCE_DIR}/data.fbs
  DEPENDS data.fbs
  )
