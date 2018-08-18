# Dummy plugin used by ctkAbstractPluginFactoryTest1
add_definitions( -DCTKDummyPlugin)


qt5_wrap_cpp(TEST_WRAP_CPP ctkDummyPlugin.h)

include_directories(${CMAKE_SOURCE_DIR}/src/ctkCore)
include_directories(${CMAKE_BINARY_DIR}/include/ctkCore)

find_package(Qt5Test REQUIRED)

find_package(Qt5Gui REQUIRED)
add_library(

  CTKDummyPlugin SHARED
  ctkDummyPlugin.h ctkDummyPlugin.cpp

  ${TEST_WRAP_CPP}

  )

generate_export_header(CTKDummyPlugin EXPORT_FILE_NAME "CTKDummyPluginExport.h" EXPORT_MACRO_NAME CTK_DUMMY_EXPORT)


 target_link_libraries(CTKDummyPlugin ${KIT_target_libraries} Qt5::Test Qt5::Gui)

#add_library(
#  CTKDummyPlugin
#CTK_DUMMY_EXPORT
#  ctkDummyPlugin.h ctkDummyPlugin.cpp
#  ctkDummyPlugin.h"
#  TARGETS ${CTK_BASE_LIBRARIES}
#  )


#get_target_property(ctkDummyPluginPATH "CTKDummyPlugin" LOCATION)
remove_definitions(-DCTKDummyPlugin)

set(KIT ${PROJECT_NAME})

#
# Test sources
#
set(KITTests_SRCS
  ctkAbstractFactoryTest1.cpp
  ctkAbstractLibraryFactoryTest1.cpp
  ctkAbstractObjectFactoryTest1.cpp
  ctkAbstractPluginFactoryTest1.cpp
  ctkAbstractQObjectFactoryTest1.cpp
  ctkBackTraceTest.cpp
  ctkBooleanMapperTest.cpp
  ctkCallbackTest1.cpp    
  ctkCommandLineParserTest1.cpp
  ctkExceptionTest.cpp
  ctkHighPrecisionTimerTest.cpp
  ctkLinearValueProxyTest.cpp
  ctkLoggerTest1.cpp
  ctkModelTesterTest1.cpp
  ctkModelTesterTest2.cpp
  ctkUtilsCopyDirRecursivelyTest1.cpp
  ctkUtilsQtHandleToStringTest1.cpp
  ctkUtilsTest.cpp
  ctkUtilsTest1.cpp
  ctkUtilsTest2.cpp
  ctkUtilsTest3.cpp
  ctkUtilsTest4.cpp
  ctkDependencyGraphTest1.cpp
  ctkDependencyGraphTest2.cpp
  ctkPimplTest1.cpp
 # ctkScopedCurrentDirTest1.cpp
  ctkSingletonTest1.cpp
  ctkWorkflowTest1.cpp
  ctkWorkflowTest2.cpp
  ctkWorkflowTest3.cpp
  )

if(HAVE_BFD)
  list(APPEND KITTests_SRCS
    ctkBinaryFileDescriptorTest1.cpp
    )
endif()

include_directories(
  ${CMAKE_SOURCE_DIR}/Libs/Testing
  ${CMAKE_CURRENT_BINARY_DIR}
  )

create_test_sourcelist(Tests ${KIT}CppTests.cpp
  ${KITTests_SRCS}
  #EXTRA_INCLUDE TestingMacros.h
  )

set(TestsToRun ${Tests})
remove(TestsToRun ${KIT}CppTests.cpp)

set(LIBRARY_NAME ${PROJECT_NAME})

#
# Tests Helpers sources
#
set(Tests_Helpers_SRCS
  ctkBranchingWorkflowStep.h
  ctkExampleDerivedWorkflowStep.cpp
  ctkExampleDerivedWorkflowStep.h
  ctkExampleWorkflowStepUsingSignalsAndSlots.cpp
  ctkExampleWorkflowStepUsingSignalsAndSlots.h
  ctkSingletonTestHelper.cpp
  ctkSingletonTestHelper.h
  )

set(Tests_Helpers_MOC_SRCS
  ctkExampleWorkflowStepUsingSignalsAndSlots.h
  )

set(Tests_Helpers_MOC_CPPS
  ctkBooleanMapperTest.cpp
  ctkLinearValueProxyTest.cpp
  ctkUtilsTest.cpp
  )

set(Tests_Helpers_MOC_CPP)

  qt5_wrap_cpp(Tests_Helpers_MOC_CPP ${Tests_Helpers_MOC_CPPS})


  add_custom_target(Tests_Helpers_MOC_CPP_mocs DEPENDS ${Tests_Helpers_MOC_CPP})

 qt5_wrap_cpp(MOCCS ${Tests_Helpers_MOC_SRCS})


if(HAVE_BFD)
  add_executable(ctkBinaryFileDescriptorTestHelper ctkBinaryFileDescriptorTestHelper.cpp)
endif()



#
# Test executable
#
add_executable(${KIT}CppTests ${Tests} ${Tests_Helpers_SRCS} ${MOCCS})

add_dependencies(${KIT}CppTests Tests_Helpers_MOC_CPP_mocs)


target_link_libraries(${KIT}CppTests CTKCore ${CTK_BASE_LIBRARIES} CTKDummyPlugin)

if(CTK_QT_VERSION VERSION_GREATER "4")
  qt5_use_modules(${KIT}CppTests Test Widgets)
endif()

if(UNIX AND NOT APPLE)
  target_link_libraries(${KIT}CppTests rt)
endif()

#
# Add Tests
#

SIMPLE_TEST( ctkAbstractFactoryTest1 )
SIMPLE_TEST( ctkAbstractLibraryFactoryTest1 ${ctkDummyPluginPATH} )
SIMPLE_TEST( ctkAbstractObjectFactoryTest1 )
SIMPLE_TEST( ctkAbstractPluginFactoryTest1 ${ctkDummyPluginPATH} )
SIMPLE_TEST( ctkAbstractQObjectFactoryTest1 )
SIMPLE_TEST( ctkBackTraceTest )
if(HAVE_BFD)
  SIMPLE_TEST( ctkBinaryFileDescriptorTest1 $<TARGET_FILE:ctkBinaryFileDescriptorTestHelper> )
endif()
SIMPLE_TEST( ctkBooleanMapperTest )
SIMPLE_TEST( ctkCallbackTest1 )
SIMPLE_TEST( ctkCommandLineParserTest1 )
SIMPLE_TEST( ctkDependencyGraphTest1 )
SIMPLE_TEST( ctkDependencyGraphTest2 )
SIMPLE_TEST( ctkExceptionTest )
SIMPLE_TEST( ctkHighPrecisionTimerTest )
SIMPLE_TEST( ctkLinearValueProxyTest )
SIMPLE_TEST( ctkLoggerTest1 )
set_property(TEST ctkLoggerTest1 PROPERTY PASS_REGULAR_EXPRESSION "logger.debug\nlogger.info\nlogger.trace\nlogger.warn\nlogger.error\nlogger.fatal")
SIMPLE_TEST( ctkModelTesterTest1 )
SIMPLE_TEST( ctkModelTesterTest2 )
SIMPLE_TEST( ctkPimplTest1 )
#SIMPLE_TEST( ctkScopedCurrentDirTest1 )
SIMPLE_TEST( ctkSingletonTest1 )
SIMPLE_TEST( ctkUtilsCopyDirRecursivelyTest1 )
SIMPLE_TEST( ctkUtilsQtHandleToStringTest1 )
SIMPLE_TEST( ctkUtilsTest )
SIMPLE_TEST( ctkUtilsTest1 )
SIMPLE_TEST( ctkUtilsTest2 )
SIMPLE_TEST( ctkUtilsTest3 )
SIMPLE_TEST( ctkUtilsTest4 )
SIMPLE_TEST( ctkWorkflowTest1 )
SIMPLE_TEST( ctkWorkflowTest2 )
SIMPLE_TEST( ctkWorkflowTest3 )
