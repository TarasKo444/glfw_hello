cmake_minimum_required(VERSION 4.1.0)

project(glfw_hello)

if(LINUX)
    find_package(glfw3 REQUIRED)
endif()

add_executable(glfw_hello src/main.c)

if(WIN32)
    target_include_directories(glfw_hello PRIVATE lib/windows/glfw/include)
    target_link_libraries(glfw_hello ${CMAKE_CURRENT_SOURCE_DIR}/lib/windows/glfw/libglfw3.a)
elseif(LINUX)
    target_link_libraries(glfw_hello glfw)
endif()