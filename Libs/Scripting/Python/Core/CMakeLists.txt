project(CTKScriptingPythonCore)

set(KIT_target_libraries CTKCore PythonQt Qt5::Gui Qt5::Widgets)
#
# See CTK/CMake/ctkMacroBuildLib.cmake for details
#

set(KIT_export_directive "CTK_SCRIPTING_PYTHON_CORE_EXPORT")

# Source files
set(KIT_SRCS
  ctkAbstractPythonManager.cpp
  ctkAbstractPythonManager.h
  )

# Headers that should run through moc
set(KIT_MOC_SRCS
  ctkAbstractPythonManager.h
  )

# UI files
set(KIT_UI_FORMS
)

# Resources
set(KIT_resources
)

#
# Configure file describing which Qt modules are wrapped
#
set(QT_PYTHON_WRAPPED_LIBRARIES_LIST Core Gui Widgets Network OpenGL Sql Svg UiTools WebKit WebKitWidgets Xml XmlPatterns)
foreach(qtlib ${QT_PYTHON_WRAPPED_LIBRARIES_LIST})
  string(TOUPPER ${qtlib} qtlib)
  set(CTK_PYTHONQT_WRAP_QT${qtlib} ${CTK_LIB_Scripting/Python/Core_PYTHONQT_WRAP_QT${qtlib}})
endforeach()

configure_file(
  ctkScriptingPythonCoreConfigure.h.in
  ${CMAKE_CURRENT_BINARY_DIR}/ctkScriptingPythonCoreConfigure.h
  )

# Target libraries - See CMake/ctkFunctionGetTargetLibraries.cmake
# The following macro will read the target libraries from the file 'target_libraries.cmake'
#ctkFunctionGetTargetLibraries(KIT_target_libraries)

#find_package (Python COMPONENTS Interpreter Development)

find_package(PythonLibs)


add_library(
  CTKScriptingPythonCore
  ${KIT_SRCS}
  ${KIT_MOC_SRCS}
    ${INCLUDES}
    ${MY_MOC}
    ${MY_UI_GENERATED_SRC}
    ${KIT_resources}
    ${KIT_GENERATE_MOC_SRCS}
     

)

generate_export_header(CTKScriptingPythonCore EXPORT_FILE_NAME "${CMAKE_CURRENT_BINARY_DIR}/ctkScriptingPythonCoreExport.h" EXPORT_MACRO_NAME "CTK_SCRIPTING_PYTHON_CORE_EXPORT")  
target_include_directories(CTKScriptingPythonCore PUBLIC ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR} ${PYTHON_INCLUDE_DIR}) 


target_link_libraries(CTKScriptingPythonCore PUBLIC ${KIT_target_libraries} PythonQt ${PYTHON_LIBRARY}

    ${QT_PYTHON_WRAPPED_LIBRARIES_LIST}
    )



set(ALL_HEADER "ctkAbstractPythonManager.h" "${CMAKE_CURRENT_BINARY_DIR}/ctkScriptingPythonCoreExport.h")
set_target_properties(CTKScriptingPythonCore PROPERTIES PUBLIC_HEADER "${ALL_HEADER}")



install(TARGETS CTKScriptingPythonCore
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        PUBLIC_HEADER DESTINATION include/CTKScriptingPythonCore
        ARCHIVE DESTINATION lib
        )


if (false)
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
endif()
# Plugins
#if(CTK_BUILD_QTDESIGNER_PLUGINS)
#  add_subdirectory(Plugins)
#endif()

#add_subdirectory(Python)

# Testing
#if(BUILD_TESTING)
#  add_subdirectory(Testing)
#endif()
