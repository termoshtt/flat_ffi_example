cmake_minimum_required(VERSION 3.11)
# set(CMAKE_VERBOSE_MAKEFILE 1)

find_package(Boost COMPONENTS python3 numpy3 REQUIRED)
find_package(PythonLibs REQUIRED)
include_directories(${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})

add_library(flat_example SHARED flat.cpp)
target_link_libraries(flat_example ${Boost_LIBRARIES} ${PYTHON_LIBRARY})
set_target_properties(flat_example PROPERTIES PREFIX "")
