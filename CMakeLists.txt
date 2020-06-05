cmake_minimum_required(VERSION 3.10)

project(CTK)

include(ExternalProject)
include(GenerateExportHeader)
find_package(Qt5 COMPONENTS Core Widgets Gui Xml Help OpenGL)
find_package(Python3 COMPONENTS Interpreter Development)
find_package(VTK)

set(CMAKE_INSTALL_PREFIX
    "${CMAKE_BINARY_DIR}/install"
    CACHE FILEPATH "${CMAKE_BINARY_DIR}/install")

ExternalProject_Add(PythonQt-ep
  GIT_REPOSITORY https://github.com/jdmarquez01/PythonQt.git
  GIT_TAG patched-9
  PREFIX PythonQt
  UPDATE_COMMAND ""
  UPDATE_DISCONNECTED 1
  CMAKE_GENERATOR ${gen}
  CMAKE_ARGS
    ${ep_common_args}
        -DCMAKE_CXX_FLAGS_DEBUG:STRING=${CMAKE_CXX_FLAGS_DEBUG}
        -DCMAKE_CXX_FLAGS_RELEASE:STRING=${CMAKE_CXX_FLAGS_RELEASE}
        -DCMAKE_CXX_FLAGS_MINSIZEREL:STRING=${CMAKE_CXX_FLAGS_MINSIZEREL}
        -DCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING=${CMAKE_CXX_FLAGS_RELWITHDEBINFO}
        -DBUILD_STATIC_LIBS:BOOL=${BUILD_STATIC_LIBS}
        -DBUILD_SHARED_LIBS:BOOL=${BUILD_SHARED_LIBS}
        -DBUILD_TESTING:BOOL=OFF
        -DBUILD_TESTS:BOOL=OFF
        -DQt5_DIR:PATH=${Qt5_DIR}
        -DVTK_DIR:PATH=${VTK5_DIR}
        -DCMAKE_INSTALL_PREFIX:PATH=${CMAKE_INSTALL_PREFIX}
 )



 set(PythonQt_DIR "${CMAKE_INSTALL_PREFIX}")

 file(MAKE_DIRECTORY "${PythonQt_DIR}/include/PythonQt")




message(Lib=> ${PythonQt_DIR}/lib/${CMAKE_SHARED_LIBRARY_PREFIX}CTKCore${CMAKE_SHARED_LIBRARY_SUFFIX})
message(Inc => ${PythonQt_DIR}/include/PythonQt)

if(BUILD_SHARED_LIBS)
    set(LIBRARY_SUFFIX ${CMAKE_STATIC_LIBRARY_SUFFIX})
else()
    set(LIBRARY_SUFFIX ${CMAKE_SHARED_LIBRARY_SUFFIX})
endif()

  add_library(PythonQt IMPORTED UNKNOWN)
  add_dependencies(PythonQt PythonQt-ep)
  set_target_properties( PythonQt PROPERTIES IMPORTED_LOCATION ${PythonQt_DIR}/lib/${CMAKE_SHARED_LIBRARY_PREFIX}PythonQt${LIBRARY_SUFFIX})
  set_target_properties( PythonQt PROPERTIES IMPORTED_IMPLIB_RELEASE ${PythonQt_DIR}/lib/${CMAKE_SHARED_LIBRARY_PREFIX}PythonQt${LIBRARY_SUFFIX})
  set_target_properties( PythonQt PROPERTIES INTERFACE_INCLUDE_DIRECTORIES ${PythonQt_DIR}/include/PythonQt)





include(CMake/ctkMacroSimpleTest.cmake)
include(CMake/ctkFunctionCompileSnippets.cmake)
enable_testing()

add_subdirectory(Libs)
