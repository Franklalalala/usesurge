cmake_minimum_required(VERSION 3.1)

include_directories(${PROJECT_SOURCE_DIR}/include)

add_definitions(-DGENG_MAIN=geng_main)
add_definitions(-DOUTPROC=surgeproc)
add_definitions(-DSURGEPLUGIN="plugin.c")
add_definitions(-DPRUNE=surgeprune)
add_definitions(-DPRUNE=surgepreprune)
add_definitions(-DWORDSIZE=32)
add_definitions(-DMAXN=WORDSIZE)



AUX_SOURCE_DIRECTORY(${CMAKE_CURRENT_SOURCE_DIR} source)

add_executable(surge surge.c geng.c planarity.c ${PROJECT_SOURCE_DIR}/libnauty/times.c)

target_link_libraries(surge nautyW1)