cmake_minimum_required(VERSION 4.1.0)

project(glfw_hello)

add_executable(glfw_hello src/main.c)

# set_property(TARGET glfw_hello PROPERTY WIN32_EXECUTABLE TRUE)

target_include_directories(glfw_hello PRIVATE lib/glfw/include)

target_link_libraries(glfw_hello ${CMAKE_CURRENT_SOURCE_DIR}/lib/glfw/libglfw3.a)