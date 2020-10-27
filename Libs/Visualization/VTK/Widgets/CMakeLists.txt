find_package(VTK REQUIRED)
include(${VTK_USE_FILE})

#
# See CTK/CMake/ctkMacroBuildLib.cmake for details
#

set(KIT_export_directive "CTK_VISUALIZATION_VTK_WIDGETS_EXPORT")



set(PUBLIC_HEADER

    ctkVTKAbstractMatrixWidget.h
    ctkVTKAbstractMatrixWidget_p.h
    ctkVTKAbstractView.h
    ctkVTKAbstractView_p.h
    ctkVTKChartView.h
    ctkVTKColorTransferFunction.h
    ctkVTKCompositeFunction.h
    ctkVTKDataSetArrayComboBox.h
    ctkVTKDataSetModel.h
    ctkVTKDiscretizableColorTransferWidget.h
    ctkVTKHistogram.h
    ctkVTKLookupTable.h
    ctkVTKMagnifyView.h
    ctkVTKMagnifyView_p.h
    ctkVTKMatrixWidget.h
    ctkVTKPiecewiseFunction.h
    ctkVTKPropertyWidget.h
    ctkVTKRenderView.h
    ctkVTKRenderViewEventPlayer.h
    ctkVTKRenderViewEventTranslator.h
    ctkVTKRenderView_p.h
    ctkVTKScalarBarWidget.h
    ctkVTKScalarsToColorsComboBox.h
    ctkVTKScalarsToColorsView.h
    ctkVTKScalarsToColorsWidget.h
    ctkVTKSliceView.h
    ctkVTKSliceView_p.h
    ctkVTKSurfaceMaterialPropertyWidget.h
    ctkVTKTextPropertyWidget.h
    ctkVTKThresholdWidget.h
    ctkVTKThumbnailView.h
    ctkVTKVolumePropertyWidget.h
    ctkVTKWidgetsUtils.h
    ctkVisualizationVTKWidgetsPythonQtDecorators.h)
#
# Add the libraries QtTesting
#
if(CTK_USE_QTTESTING)
    find_package(QtTesting REQUIRED)
    include_directories(
        ${QtTesting_INCLUDE_DIRS}
        ${CMAKE_BINARY_DIR} # For ctkConfig.h
        )
endif()

# Source files
set(KIT_SRCS
    ctkVTKAbstractMatrixWidget.cpp
    ctkVTKAbstractMatrixWidget.h
    ctkVTKAbstractMatrixWidget_p.h
    ctkVTKAbstractView.cpp
    ctkVTKAbstractView.h
    ctkVTKAbstractView_p.h
    ctkVTKColorTransferFunction.cpp
    ctkVTKColorTransferFunction.h
    ctkVTKCompositeFunction.cpp
    ctkVTKCompositeFunction.h
    ctkVTKDataSetModel.cpp
    ctkVTKDataSetModel.h
    ctkVTKDataSetArrayComboBox.cpp
    ctkVTKDataSetArrayComboBox.h
    ctkVTKHistogram.cpp
    ctkVTKHistogram.h
    ctkVTKLookupTable.cpp
    ctkVTKLookupTable.h
    ctkVTKMagnifyView.cpp
    ctkVTKMagnifyView.h
    ctkVTKMagnifyView_p.h
    ctkVTKMatrixWidget.cpp
    ctkVTKMatrixWidget.h
    ctkVTKPiecewiseFunction.cpp
    ctkVTKPiecewiseFunction.h
    ctkVTKPropertyWidget.cpp
    ctkVTKPropertyWidget.h
    ctkVTKRenderView.cpp
    ctkVTKRenderView.h
    ctkVTKRenderView_p.h
    ctkVTKScalarBarWidget.cpp
    ctkVTKScalarBarWidget.h
    ctkVTKScalarsToColorsComboBox.cpp
    ctkVTKScalarsToColorsComboBox.h
    ctkVTKSliceView.cpp
    ctkVTKSliceView.h
    ctkVTKSliceView_p.h
    ctkVTKSurfaceMaterialPropertyWidget.cpp
    ctkVTKSurfaceMaterialPropertyWidget.h
    ctkVTKTextPropertyWidget.cpp
    ctkVTKTextPropertyWidget.h
    ctkVTKThresholdWidget.cpp
    ctkVTKThresholdWidget.h
    ctkVTKThumbnailView.cpp
    ctkVTKThumbnailView.h
    ctkVTKWidgetsUtils.cpp
    ctkVTKWidgetsUtils.h
    )

# Headers that should run through moc
set(KIT_MOC_SRCS
    ctkVTKAbstractMatrixWidget_p.h
    ctkVTKAbstractView.h
    ctkVTKAbstractView_p.h
    ctkVTKColorTransferFunction.h
    ctkVTKCompositeFunction.h
    ctkVTKDataSetArrayComboBox.h
    ctkVTKDataSetModel.h
    ctkVTKHistogram.h
    ctkVTKLookupTable.h
    ctkVTKMagnifyView.h
    ctkVTKMagnifyView_p.h
    ctkVTKMatrixWidget.h
    ctkVTKPiecewiseFunction.h
    ctkVTKPropertyWidget.h
    ctkVTKRenderView.h
    ctkVTKRenderView_p.h
    ctkVTKScalarBarWidget.h
    ctkVTKScalarsToColorsComboBox.h
    ctkVTKSliceView.h
    ctkVTKSliceView_p.h
    ctkVTKSurfaceMaterialPropertyWidget.h
    ctkVTKTextPropertyWidget.h
    ctkVTKThresholdWidget.h
    ctkVTKThumbnailView.h
    )

# UI files
set(KIT_UI_FORMS
    Resources/UI/ctkVTKDiscretizableColorTransferWidget.ui
    Resources/UI/ctkVTKScalarBarWidget.ui
    Resources/UI/ctkVTKTextPropertyWidget.ui
    Resources/UI/ctkVTKPropertyWidget.ui
    Resources/UI/ctkVTKThresholdWidget.ui
    )

# Resources
set(KIT_resources
    Resources/ctkVTKWidgets.qrc
    )

# Set VTK_LIBRARIES variable
if(${VTK_VERSION_MAJOR} GREATER 5)
    set(VTK_LIBRARIES
        vtkChartsCore
        vtkCommonMath
        vtkFiltersSources
        vtkImagingGeneral
        vtkImagingStatistics
        vtkInteractionWidgets
        vtkRenderingContext2D
        vtkViewsContext2D
        vtkGUISupportQt
        vtkRenderingFreeType
        vtkRenderingFreeTypeFontConfig
        )
    if(TARGET vtkRenderingContext${VTK_RENDERING_BACKEND})
        list(APPEND VTK_LIBRARIES vtkRenderingContext${VTK_RENDERING_BACKEND})
    endif()
    if(TARGET vtkRenderingGL2PS${VTK_RENDERING_BACKEND})
        list(APPEND VTK_LIBRARIES vtkRenderingGL2PS${VTK_RENDERING_BACKEND})
    endif()
    if(CTK_LIB_Scripting/Python/Core AND CTK_LIB_Scripting/Python/Core_PYTHONQT_USE_VTK)
        set(VTK_LIBRARIES ${VTK_LIBRARIES} vtkWrappingPythonCore)
    endif()
else()
    set(VTK_LIBRARIES
        QVTK
        )
endif()
set(CTK_USE_CHARTS 1)
if(CTK_LIB_Visualization/VTK/Widgets_USE_TRANSFER_FUNCTION_CHARTS)
endif()

if(${CTK_USE_CHARTS})
    set(KIT_SRCS
        ctkVTKChartView.cpp
        ctkVTKChartView.h
        ctkVTKDiscretizableColorTransferWidget.h
        ctkVTKDiscretizableColorTransferWidget.cpp
        ctkVTKVolumePropertyWidget.cpp
        ctkVTKVolumePropertyWidget.h
        ctkVTKScalarsToColorsView.cpp
        ctkVTKScalarsToColorsView.h
        ctkVTKScalarsToColorsWidget.cpp
        ctkVTKScalarsToColorsWidget.h
        ${KIT_SRCS})
    set(KIT_MOC_SRCS
        ctkVTKChartView.h
        ctkVTKDiscretizableColorTransferWidget.h
        ctkVTKVolumePropertyWidget.h
        ctkVTKScalarsToColorsView.h
        ctkVTKScalarsToColorsWidget.h
        ${KIT_MOC_SRCS})
    set(KIT_UI_FORMS
        Resources/UI/ctkVTKVolumePropertyWidget.ui
        Resources/UI/ctkVTKScalarsToColorsWidget.ui
        ${KIT_UI_FORMS})
    if(${VTK_VERSION_MAJOR} GREATER 5)
        set(VTK_LIBRARIES
            vtkChartsCore
            ${VTK_LIBRARIES})
    else()
        set(VTK_LIBRARIES
            vtkCharts
            ${VTK_LIBRARIES})
    endif()
    add_definitions(-DCTK_USE_CHARTS)
endif()

# Target libraries - See CMake/ctkFunctionGetTargetLibraries.cmake
# The following macro will read the target libraries from the file 'target_libraries.cmake'
#ctkFunctionGetTargetLibraries(KIT_target_libraries)
list(APPEND KIT_target_libraries )


# If we use QtTessting, we add all the dependencies
if(CTK_USE_QTTESTING)
    list(APPEND KIT_SRCS
        ctkVTKRenderViewEventPlayer.cpp
        ctkVTKRenderViewEventPlayer.h
        ctkVTKRenderViewEventTranslator.cpp
        ctkVTKRenderViewEventTranslator.h
        )
    list(APPEND KIT_MOC_SRCS
        ctkVTKRenderViewEventPlayer.h
        ctkVTKRenderViewEventTranslator.h
        )
    list(APPEND KIT_target_libraries QtTesting)
endif()

# Prefer QVTKOpenGLWidget to QVTKWidget when using Qt5
set(_use_qvtkopenglwidget 1)
#if(CTK_QT_VERSION VERSION_LESS "5"
#  OR VTK_VERSION VERSION_LESS "8"
#  OR (NOT VTK_RENDERING_BACKEND STREQUAL "OpenGL2"))
#  set(_use_qvtkopenglwidget 0)
#endif()
#if(_use_qvtkopenglwidget)
add_definitions(-DCTK_USE_QVTKOPENGLWIDGET)
#endif()




SET(CMAKE_AUTOUIC OFF)
SET(CMAKE_AUTOMOC OFF)

qt5_wrap_ui(MY_UI_GENERATED_SRC  ${KIT_UI_FORMS})
qt5_wrap_cpp(MY_MOC  ${KIT_MOC_SRCS})


qt5_add_resources (out ${KIT_resources})

add_library(
    CTKVisualizationVTKWidgets STATIC
    ${KIT_SRCS}
    ${INCLUDES}
    ${KIT_GENERATE_MOC_SRCS}
    ${MY_MOC}
    ${MY_UI_GENERATED_SRC}
    ${out}


    )


list(APPEND KIT_target_libraries  ${VTK_LIBRARIES} CTKVisualizationVTKCore CTKWidgets Qt5::Gui)






generate_export_header(CTKVisualizationVTKWidgets EXPORT_FILE_NAME "${CMAKE_CURRENT_BINARY_DIR}/CTKVisualizationVTKWidgetsExport.h" EXPORT_MACRO_NAME "CTK_VISUALIZATION_VTK_WIDGETS_EXPORT")
target_include_directories(CTKVisualizationVTKWidgets PUBLIC ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}) 


target_link_libraries(CTKVisualizationVTKWidgets PUBLIC ${KIT_target_libraries} )


set (PUBLIC_HEADERSS
    ./ctkVTKAbstractMatrixWidget.h
    ./ctkVTKAbstractView.h
    ./ctkVTKChartView.h
    ./ctkVTKColorTransferFunction.h
    ./ctkVTKCompositeFunction.h
    ./ctkVTKDataSetArrayComboBox.h
    ./ctkVTKDataSetModel.h
    ./ctkVTKDiscretizableColorTransferWidget.h
    ./ctkVTKHistogram.h
    ./ctkVTKLookupTable.h
    ./ctkVTKMagnifyView.h
    ./ctkVTKMatrixWidget.h
    ./ctkVTKOpenGLNativeWidget.h
    ./ctkVTKPiecewiseFunction.h
    ./ctkVTKPropertyWidget.h
    ./ctkVTKRenderView.h
    ./ctkVTKRenderViewEventPlayer.h
    ./ctkVTKRenderViewEventTranslator.h
    ./ctkVTKScalarBarWidget.h
    ./ctkVTKScalarsToColorsComboBox.h
    ./ctkVTKScalarsToColorsView.h
    ./ctkVTKScalarsToColorsWidget.h
    ./ctkVTKSliceView.h
    ./ctkVTKSurfaceMaterialPropertyWidget.h
    ./ctkVTKTextPropertyWidget.h
    ./ctkVTKThresholdWidget.h
    ./ctkVTKThumbnailView.h
    ./ctkVTKVolumePropertyWidget.h
    ./ctkVTKWidgetsUtils.h

    )


set(ALL_HEADER "${PUBLIC_HEADER}" "${PUBLIC_HEADERSS}" "${CMAKE_CURRENT_BINARY_DIR}/CTKVisualizationVTKWidgetsExport.h")


set_target_properties(CTKVisualizationVTKWidgets PROPERTIES PUBLIC_HEADER "${ALL_HEADER}")

install(TARGETS CTKVisualizationVTKWidgets
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    PUBLIC_HEADER DESTINATION include/CTKVisualizationVTKWidgets
    ARCHIVE DESTINATION lib
    )






if(_use_qvtkopenglwidget) 
    target_compile_definitions(
        CTKVisualizationVTKWidgets
        INTERFACE
        CTK_USE_QVTKOPENGLWIDGET
        )
endif()

if(CTK_WRAP_PYTHONQT_LIGHT)
    ctkMacroBuildLibWrapper(
        TARGET ${PROJECT_NAME}
        SRCS ${KIT_SRCS}
        WRAPPER_LIBRARY_TYPE ${CTK_LIBRARY_MODE}
        )
endif()

# Plugins
if(CTK_BUILD_QTDESIGNER_PLUGINS)
    add_subdirectory(Plugins)
endif()

# Testing
if(BUILD_TESTING)
    add_subdirectory(Testing)
endif()
