project(CTKCore)

#
# 3rd party dependencies
#

# CMake modules
set(CMAKE_MODULE_PATH ${CTKCore_SOURCE_DIR}/CMake ${CMAKE_MODULE_PATH})

# CMake Macros
#include(CMake/ctkMacroBFDCheck.cmake) # HAVE_BFD will be set to True if it applies

#
# See CTK/CMake/ctkMacroBuildLib.cmake for details
#

set(KIT_export_directive "CTK_CORE_EXPORT")


set (HEADERS
ctkAbstractFactory.h                 
ctkBackTrace.h                       
ctkCorePythonQtDecorators.h          
ctkErrorLogFDMessageHandler.h        
ctkException.h                       
ctkPimpl.h                           
ctkWorkflow.h
ctkAbstractFileBasedFactory.h        
ctkBinaryFileDescriptor.h            
ctkCoreTestingMacros.h               
ctkErrorLogFDMessageHandler_p.h      
ctkFileLogger.h                      
ctkScopedCurrentDir.h                
ctkWorkflowStep.h
ctkAbstractLibraryFactory.h          
ctkBooleanMapper.h                   
ctkCoreTestingUtilities.h            
ctkErrorLogLevel.h                   
ctkHighPrecisionTimer.h              
ctkSetName.h                         
ctkWorkflowStep_p.h
ctkAbstractObjectFactory.h           
ctkCallback.h                        
ctkDependencyGraph.h                 
ctkErrorLogQtMessageHandler.h        
ctkLinearValueProxy.h                
ctkSingleton.h                       
ctkWorkflowTransitions.h
ctkAbstractPluginFactory.h           
ctkCommandLineParser.h               
ctkErrorLogAbstractMessageHandler.h  
ctkErrorLogStreamMessageHandler.h    
ctkErrorLogAbstractModel.h
ctkLogger.h                          
ctkUtils.h                           
ctkWorkflow_p.h
ctkAbstractQObjectFactory.h          
ctkCompilerDetections_p.h            
ctkErrorLogContext.h                 
ctkErrorLogTerminalOutput.h          
ctkModelTester.h                     
ctkValueProxy.h
ctkCompatibility_p.h
ctkCoreSettings.h
)




# Source files
set(KIT_SRCS
  ctkCoreSettings.cpp
  ctkAbstractFactory.h
  ctkAbstractFactory.tpp
  ctkAbstractFileBasedFactory.h
  ctkAbstractFileBasedFactory.tpp
  ctkAbstractObjectFactory.h
  ctkAbstractObjectFactory.tpp
  ctkAbstractPluginFactory.h
  ctkAbstractPluginFactory.tpp
  ctkAbstractQObjectFactory.h
  ctkAbstractQObjectFactory.tpp
  ctkAbstractLibraryFactory.h
  ctkAbstractLibraryFactory.tpp
  ctkBackTrace.cpp
  ctkBooleanMapper.cpp
  ctkBooleanMapper.h
  ctkCallback.cpp
  ctkCallback.h
  ctkCommandLineParser.cpp
  ctkCommandLineParser.h
  ctkCoreSettings.cpp
  ctkCoreSettings.h
  ctkCoreTestingUtilities.cpp
  ctkCoreTestingUtilities.tpp
  ctkCoreTestingUtilities.h
  ctkDependencyGraph.cpp
  ctkDependencyGraph.h
  ctkErrorLogAbstractMessageHandler.cpp
  ctkErrorLogAbstractMessageHandler.h
  ctkErrorLogAbstractModel.cpp
  ctkErrorLogAbstractModel.h
  ctkErrorLogContext.h
  ctkErrorLogFDMessageHandler.cpp
  ctkErrorLogFDMessageHandler.h
  ctkErrorLogFDMessageHandler_p.h
  ctkErrorLogLevel.cpp
  ctkErrorLogLevel.h
  ctkErrorLogQtMessageHandler.cpp
  ctkErrorLogQtMessageHandler.h
  ctkErrorLogStreamMessageHandler.cpp
  ctkErrorLogStreamMessageHandler.h
  ctkErrorLogTerminalOutput.cpp
  ctkErrorLogTerminalOutput.h
  ctkException.cpp
  ctkException.h
  ctkFileLogger.cpp
  ctkFileLogger.h
  ctkHighPrecisionTimer.cpp
  ctkLinearValueProxy.cpp
  ctkLinearValueProxy.h
  ctkLogger.cpp
  ctkLogger.h
  ctkModelTester.cpp
  ctkModelTester.h
  ctkPimpl.h
  ctkScopedCurrentDir.cpp
  ctkScopedCurrentDir.h
  ctkSingleton.h
  ctkUtils.cpp
  ctkUtils.h
  ctkValueProxy.cpp
  ctkValueProxy.h
  ctkWorkflow.h
  ctkWorkflow.cpp
  ctkWorkflow_p.h
  ctkWorkflowStep.h
  ctkWorkflowStep.cpp
  ctkWorkflowStep_p.h
  ctkWorkflowTransitions.h
  ctkSetName.cpp
  ctkSetName.h
  )

if(HAVE_BFD)
  list(APPEND KIT_SRCS
    ctkBinaryFileDescriptor.cpp
    ctkBinaryFileDescriptor.h
    )
endif()

# Headers that should run through moc
set(KIT_MOC_SRCS
  ctkBooleanMapper.h
  ctkCallback.h
  ctkCommandLineParser.h
  ctkCoreSettings.h
  ctkErrorLogAbstractMessageHandler.h
  ctkErrorLogAbstractModel.h
  ctkErrorLogFDMessageHandler_p.h
  ctkErrorLogLevel.h
  ctkErrorLogQtMessageHandler.h
  ctkErrorLogTerminalOutput.h
  ctkFileLogger.h
  ctkLinearValueProxy.h
  ctkLogger.h
  ctkModelTester.h
  ctkErrorLogQtMessageHandler.h
  ctkValueProxy.h
  ctkWorkflow.h
  ctkWorkflow_p.h
  ctkWorkflowStep_p.h
  ctkWorkflowTransitions.h
  )

# UI files
set(KIT_UI_FORMS
)

# Resources
set(KIT_resources
)

# Target libraries - See CMake/ctkFunctionGetTargetLibraries.cmake
# The following macro will read the target libraries from the file 'target_libraries.cmake'
set(KIT_target_libraries)

#ctkFunctionGetTargetLibraries(KIT_target_libraries)




SET(CMAKE_AUTOUIC OFF)
SET(CMAKE_AUTOMOC OFF)



qt5_wrap_ui(MY_UI_GENERATED_SRC  ${KIT_UI_FORMS})
qt5_wrap_cpp(MY_MOC  ${KIT_MOC_SRCS})



add_library(
  CTKCore 
  ${KIT_SRCS}
  ${INCLUDES}
  ${KIT_GENERATE_MOC_SRCS}
  ${MY_MOC}
  ${MY_UI_GENERATED_SRC}
  ${KIT_resources}
)

generate_export_header(CTKCore EXPORT_FILE_NAME ${CMAKE_CURRENT_BINARY_DIR}/ctkCoreExport.h EXPORT_MACRO_NAME "CTK_CORE_EXPORT")




target_include_directories(CTKCore PUBLIC 
  $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
  $<INSTALL_INTERFACE:include/CTKCore>
)


set (PUBLIC_HEADERS
    ctkBackTrace.h
    ctkBinaryFileDescriptor.h
    ctkBooleanMapper.h
    ctkCallback.h
    ctkCommandLineParser.h
    ctkCoreTestingUtilities.h
    ctkDependencyGraph.h
    ctkErrorLogAbstractMessageHandler.h
    ctkErrorLogAbstractModel.h
    ctkErrorLogContext.h
    ctkErrorLogFDMessageHandler.h
    ctkErrorLogLevel.h
    ctkErrorLogQtMessageHandler.h
    ctkErrorLogStreamMessageHandler.h
    ctkErrorLogTerminalOutput.h
    ctkException.h
    ctkFileLogger.h
    ctkLinearValueProxy.h
    ctkLogger.h
    ctkModelTester.h
    ctkPimpl.h
    ctkScopedCurrentDir.h
    ctkSetName.h
    ctkUtils.h
    ctkValueProxy.h
    ctkWorkflow.h
    ctkWorkflowStep.h
    ctkWorkflowStep_p.h
    ctkWorkflowTransitions.h
    )



set(ALL_HEADER "${HEADERS}" ${PUBLIC_HEADERS} "${CMAKE_CURRENT_BINARY_DIR}/ctkCoreExport.h")

#message("__> ${ALL_HEADER}")

set_target_properties(CTKCore PROPERTIES PUBLIC_HEADER "${ALL_HEADER}")

target_link_libraries(CTKCore PUBLIC Qt5::Core)

install(TARGETS CTKCore 
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        PUBLIC_HEADER DESTINATION include/CTKCore
        ARCHIVE DESTINATION lib
        )




# Needed for ctkBackTrace
if(UNIX)
  # FreeBSD: The same functionality that is in linux's libdl is provided in FreeBSD's libc
  find_library(HAVE_LIBDL dl)
  if(HAVE_LIBDL)
    target_link_libraries(CTKCore PRIVATE dl)
  endif()
elseif(WIN32 AND NOT MINGW)
  target_link_libraries(CTKCore PRIVATE dbghelp)
endif()

#if(CTK_WRAP_PYTHONQT_LIGHT)
#  ctkMacroBuildLibWrapper(
#    TARGET ${PROJECT_NAME}
#    SRCS ${KIT_SRCS}
#    WRAPPER_LIBRARY_TYPE ${CTK_LIBRARY_MODE}
#    )
#endif()


# Testing
if(BUILD_TESTING)
  add_subdirectory(Testing)
  # Compile source code snippets
  add_subdirectory(Documentation/Snippets)
endif()
