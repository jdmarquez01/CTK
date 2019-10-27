project(CTKScriptingPythonWidgets)

#
# See CTK/CMake/ctkMacroBuildLib.cmake for details
#

set(KIT_export_directive "CTK_SCRIPTING_PYTHON_WIDGETS_EXPORT")


# Source files
set(KIT_SRCS
  ctkPythonConsole.cpp
  ctkPythonConsole.h
  )

# Headers that should run through moc
set(KIT_MOC_SRCS
  ctkPythonConsole.h
  )

# UI files
set(KIT_UI_FORMS
)

# Resources
set(KIT_resources
  Resources/ctkScriptingPythonWidgets.qrc
  )

# Target libraries - See CMake/ctkFunctionGetTargetLibraries.cmake
# The following macro will read the target libraries from the file 'target_libraries.cmake'


find_package(PythonLibs)


add_library(
  CTKScriptingPythonWidgets STATIC
  ${KIT_SRCS}
  ${KIT_MOC_SRCS}
    ${INCLUDES}
    ${MY_MOC}
    ${MY_UI_GENERATED_SRC}
    ${KIT_resources}
    ${KIT_GENERATE_MOC_SRCS}
     

)

generate_export_header(CTKScriptingPythonWidgets EXPORT_FILE_NAME "${CMAKE_CURRENT_BINARY_DIR}/ctkScriptingPythonWidgetsExport.h" EXPORT_MACRO_NAME "CTK_SCRIPTING_PYTHON_WIDGETS_EXPORT")  
target_include_directories(CTKScriptingPythonWidgets PUBLIC ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR} ${PYTHON_INCLUDE_DIR}) 


target_link_libraries(CTKScriptingPythonWidgets PUBLIC ${KIT_target_libraries} CTKScriptingPythonCore CTKWidgets CTKCore)




set(ALL_HEADER "ctkPythonConsole.h" "${CMAKE_CURRENT_BINARY_DIR}/ctkScriptingPythonWidgetsExport.h")
set_target_properties(CTKScriptingPythonWidgets PROPERTIES PUBLIC_HEADER "${ALL_HEADER}")




install(TARGETS CTKScriptingPythonWidgets
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        PUBLIC_HEADER DESTINATION include/CTKScriptingPythonWidgets
        ARCHIVE DESTINATION lib
        )



if (false)

ctkFunctionGetTargetLibraries(KIT_target_libraries)

ctkMacroBuildLib(
  NAME ${PROJECT_NAME}
  EXPORT_DIRECTIVE ${KIT_export_directive}
  SRCS ${KIT_SRCS}
  MOC_SRCS ${KIT_MOC_SRCS}
  UI_FORMS ${KIT_UI_FORMS}
  TARGET_LIBRARIES ${KIT_target_libraries}
  RESOURCES ${KIT_resources}
  LIBRARY_TYPE ${CTK_LIBRARY_MODE}
  )

if(CTK_WRAP_PYTHONQT_LIGHT)
  ctkMacroBuildLibWrapper(
    TARGET ${PROJECT_NAME}
    SRCS ${KIT_SRCS}
    WRAPPER_LIBRARY_TYPE ${CTK_LIBRARY_MODE}
    )
endif()
endif()

# Plugins
if(CTK_BUILD_QTDESIGNER_PLUGINS)
  add_subdirectory(Plugins)
endif()

# Testing
#if(BUILD_TESTING)
#  add_subdirectory(Testing)
#endif()
