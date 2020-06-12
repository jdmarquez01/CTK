cmake_minimum_required(VERSION 3.10)

set(CMAKE_INSTALL_PREFIX
    "${CMAKE_BINARY_DIR}/install"
    CACHE FILEPATH "${CMAKE_BINARY_DIR}/install")
    
PROJECT(CTK)

include(ExternalProject)
include(GenerateExportHeader)
find_package(Qt5 COMPONENTS Core Widgets Gui Xml Help OpenGL)
find_package(Python3 COMPONENTS Interpreter Development)
find_package(VTK)



if(BUILD_SHARED_LIBS)
    set(LIBRARY_SUFFIX ${CMAKE_STATIC_LIBRARY_SUFFIX})
else()
    set(LIBRARY_SUFFIX ${CMAKE_SHARED_LIBRARY_SUFFIX})
endif()



include(CMake/ctkMacroSimpleTest.cmake)
include(CMake/ctkFunctionCompileSnippets.cmake)
enable_testing()

add_subdirectory(Libs)
