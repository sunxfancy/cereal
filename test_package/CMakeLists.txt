project(LibTest)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set (CMAKE_CXX_STANDARD 11)
add_executable(libtest test.cpp)
target_link_libraries(libtest ${CONAN_LIBS})
