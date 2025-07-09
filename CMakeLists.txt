cmake_minimum_required(VERSION 3.28)

project(glfw_hello)

if(WIN32)
	add_library(glfw STATIC IMPORTED)
	set_target_properties(glfw PROPERTIES IMPORTED_LOCATION 
		${CMAKE_CURRENT_SOURCE_DIR}/lib/windows/glfw/libglfw3.a
	)
	target_include_directories(glfw INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/lib/windows/glfw/include)
elseif(LINUX)
    find_package(glfw3 REQUIRED)
endif()

add_executable(glfw_hello src/main.c)
target_link_libraries(glfw_hello PRIVATE glfw)
