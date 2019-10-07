project(CTKWidgets)

#
# See CTK/CMake/ctkMacroBuildLib.cmake for details
#

set(KIT_export_directive "CTK_WIDGETS_EXPORT")



set(PUBLIC_HEADERS
    ctkActionsWidget.h
    ctkAddRemoveComboBox.h
    ctkAxesWidget.h
    ctkAxesWidgetEventPlayer.h
    ctkAxesWidgetEventTranslator.h
    ctkBasePopupWidget.h
    ctkBasePopupWidget_p.h
    ctkButtonGroup.h
    ctkCheckBox.h
    ctkCheckBoxPixmaps.h
    ctkCheckableComboBox.h
    ctkCheckableComboBoxEventPlayer.h
    ctkCheckableComboBoxEventTranslator.h
    ctkCheckableHeaderView.h
    ctkCheckableHeaderViewEventPlayer.h
    ctkCheckableHeaderViewEventTranslator.h
    ctkCheckableModelHelper.h
    ctkCheckablePushButton.h
    ctkCollapsibleButton.h
    ctkCollapsibleGroupBox.h
    ctkColorDialog.h
    ctkColorPickerButton.h
    ctkComboBox.h
    ctkCompleter.h
    ctkConsole.h
    ctkConsoleEventPlayer.h
    ctkConsoleEventTranslator.h
    ctkConsole_p.h
    ctkCoordinatesWidget.h
    ctkCoordinatesWidget_p.h
    ctkCrosshairLabel.h
    ctkDateRangeWidget.h
    ctkDirectoryButton.h
    ctkDoubleRangeSlider.h
    ctkDoubleRangeSliderEventPlayer.h
    ctkDoubleRangeSliderEventTranslator.h
    ctkDoubleSlider.h
    ctkDoubleSpinBox.h
    ctkDoubleSpinBox_p.h
    ctkDynamicSpacer.h
    ctkErrorLogModel.h
    ctkErrorLogStatusMessageHandler.h
    ctkErrorLogWidget.h
    ctkExpandButton.h
    ctkExpandableWidget.h
    ctkFileDialog.h
    ctkFileDialogEventPlayer.h
    ctkFileDialogEventTranslator.h
    ctkFittedTextBrowser.h
    ctkFittedTextBrowser_p.h
    ctkFlatProxyModel.h
    ctkFlowLayout.h
    ctkFontButton.h
    ctkFontButtonEventPlayer.h
    ctkFontButtonEventTranslator.h
    ctkHistogram.h
    ctkIconEnginePlugin.h
    ctkIconEnginePlugin_qt4.h
    ctkIconEnginePlugin_qt5.h
    ctkLanguageComboBox.h
    ctkLayoutFactory.h
    ctkLayoutManager.h
    ctkLayoutManager_p.h
    ctkLayoutViewFactory.h
    ctkMaterialPropertyPreviewLabel.h
    ctkMaterialPropertyWidget.h
    ctkMatrixWidget.h
    ctkMatrixWidgetEventPlayer.h
    ctkMatrixWidgetEventTranslator.h
    ctkMenuButton.h
    ctkMenuComboBox.h
    ctkMenuComboBoxEventPlayer.h
    ctkMenuComboBoxEventTranslator.h
    ctkMenuComboBox_p.h
    ctkMessageBox.h
    ctkModalityWidget.h
    ctkPathLineEdit.h
    ctkPathLineEditEventPlayer.h
    ctkPathLineEditEventTranslator.h
    ctkPathListButtonsWidget.h
    ctkPathListButtonsWidget_p.h
    ctkPathListWidget.h
    ctkPixmapIconEngine.h
    ctkPopupWidget.h
    ctkPopupWidgetEventPlayer.h
    ctkPopupWidgetEventTranslator.h
    ctkPopupWidget_p.h
    ctkProxyStyle.h
    ctkPushButton.h
    ctkPushButton_p.h
    ctkQImageView.h
    ctkRangeSlider.h
    ctkRangeSliderEventPlayer.h
    ctkRangeSliderEventTranslator.h
    ctkRangeWidget.h
    ctkScreenshotDialog.h
    ctkScreenshotDialog_p.h
    ctkSearchBox.h
    ctkSettings.h
    ctkSettingsDialog.h
    ctkSettingsPanel.h
    ctkSignalMapper.h
    ctkSizeGrip.h
    ctkSliderWidget.h
    ctkTemplateWidget.h
    ctkTestApplication.h
    ctkThumbnailLabel.h
    ctkThumbnailListWidget.h
    ctkThumbnailListWidget_p.h
    ctkToolTipTrapper.h
    ctkTransferFunction.h
    ctkTransferFunctionBarsItem.h
    ctkTransferFunctionControlPointsItem.h
    ctkTransferFunctionGradientItem.h
    ctkTransferFunctionItem.h
    ctkTransferFunctionNativeItem.h
    ctkTransferFunctionRepresentation.h
    ctkTransferFunctionScene.h
    ctkTransferFunctionView.h
    ctkTreeComboBox.h
    ctkTreeComboBoxEventPlayer.h
    ctkTreeComboBoxEventTranslator.h
    ctkWidgetsPythonQtDecorators.h
    ctkWidgetsTestingUtilities.h
    ctkWidgetsUtils.h
    ctkWorkflowAbstractPagedWidget.h
    ctkWorkflowButtonBoxWidget.h
    ctkWorkflowGroupBox.h
    ctkWorkflowStackedWidget.h
    ctkWorkflowTabWidget.h
    ctkWorkflowWidget.h
    ctkWorkflowWidgetStep.h
    ctkWorkflowWidgetStep_p.h

    )

# add local include directory for FreeBSD
# (QtOpengl can't find GL/gl.h)
# actual bug: https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=195105
if(CMAKE_SYSTEM_NAME STREQUAL FreeBSD)
  include_directories("/usr/local/include")
endif()

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
  ctkActionsWidget.cpp
  ctkActionsWidget.h
  ctkAddRemoveComboBox.cpp
  ctkAddRemoveComboBox.h
  ctkAxesWidget.cpp
  ctkAxesWidget.h
  ctkBasePopupWidget.cpp
  ctkBasePopupWidget.h
  ctkBasePopupWidget_p.h
  ctkButtonGroup.cpp
  ctkButtonGroup.h
  ctkCheckableComboBox.cpp
  ctkCheckableComboBox.h
  ctkCheckableHeaderView.cpp
  ctkCheckableHeaderView.h
  ctkCheckableModelHelper.cpp
  ctkCheckableModelHelper.h
  ctkCheckBox.cpp
  ctkCheckBox.h
  ctkCheckBoxPixmaps.cpp
  ctkCheckBoxPixmaps.h
  ctkCheckablePushButton.cpp
  ctkCheckablePushButton.h
  ctkComboBox.cpp
  ctkComboBox.h
  ctkCompleter.cpp
  ctkCompleter.h
  ctkCollapsibleButton.cpp
  ctkCollapsibleButton.h
  ctkCollapsibleGroupBox.cpp
  ctkCollapsibleGroupBox.h
  ctkColorDialog.cpp
  ctkColorDialog.h
  ctkColorPickerButton.cpp
  ctkColorPickerButton.h
  ctkConsole.cpp
  ctkConsole.h
  ctkConsole_p.h
  ctkCoordinatesWidget.cpp
  ctkCoordinatesWidget.h
  ctkCoordinatesWidget_p.h
  ctkCrosshairLabel.cpp
  ctkCrosshairLabel.h
  ctkDateRangeWidget.cpp
  ctkDateRangeWidget.h
  ctkDirectoryButton.cpp
  ctkDirectoryButton.h
  ctkDoubleRangeSlider.cpp
  ctkDoubleRangeSlider.h
  ctkDoubleSlider.cpp
  ctkDoubleSlider.h
  ctkDoubleSpinBox.cpp
  ctkDoubleSpinBox.h
  ctkDynamicSpacer.cpp
  ctkDynamicSpacer.h
  ctkErrorLogModel.cpp
  ctkErrorLogModel.h
  ctkErrorLogStatusMessageHandler.cpp
  ctkErrorLogStatusMessageHandler.h
  ctkErrorLogWidget.cpp
  ctkErrorLogWidget.h
  ctkExpandButton.cpp
  ctkExpandButton.h
  ctkExpandableWidget.cpp
  ctkExpandableWidget.h
  ctkFileDialog.cpp
  ctkFileDialog.h
  ctkFittedTextBrowser.cpp
  ctkFittedTextBrowser.h
  ctkFlatProxyModel.cpp
  ctkFlatProxyModel.h
  ctkFlowLayout.cpp
  ctkFlowLayout.h
  ctkFontButton.cpp
  ctkFontButton.h
  ctkHistogram.cpp
  ctkHistogram.h
  ctkIconEnginePlugin.cpp
  ctkIconEnginePlugin.h
  #ctkIconEnginePlugin_qt4.h
  ctkIconEnginePlugin_qt5.h
  ctkLanguageComboBox.cpp
  ctkLanguageComboBox.h
  ctkLayoutFactory.cpp
  ctkLayoutFactory.h
  ctkLayoutManager.cpp
  ctkLayoutManager.h
  ctkLayoutViewFactory.cpp
  ctkLayoutViewFactory.h
  ctkMaterialPropertyPreviewLabel.cpp
  ctkMaterialPropertyPreviewLabel.h
  ctkMaterialPropertyWidget.cpp
  ctkMaterialPropertyWidget.h
  ctkMatrixWidget.cpp
  ctkMatrixWidget.h
  ctkMenuButton.cpp
  ctkMenuButton.h
  ctkMenuComboBox.cpp
  ctkMenuComboBox.h
  ctkMenuComboBox_p.h
  ctkMessageBox.cpp
  ctkMessageBox.h
  ctkModalityWidget.cpp
  ctkModalityWidget.h
  ctkPathLineEdit.cpp
  ctkPathLineEdit.h
  ctkPathListButtonsWidget.cpp
  ctkPathListButtonsWidget.h
  ctkPathListButtonsWidget_p.h
  ctkPathListWidget.cpp
  ctkPathListWidget.h
  ctkPixmapIconEngine.cpp
  ctkPixmapIconEngine.h
  ctkPopupWidget.cpp
  ctkPopupWidget.h
  ctkPopupWidget_p.h
  ctkProxyStyle.cpp
  ctkProxyStyle.h
  ctkPushButton.cpp
  ctkPushButton.h
  ctkPushButton_p.h
  ctkQImageView.cpp
  ctkQImageView.h
  ctkRangeSlider.cpp
  ctkRangeSlider.h
  ctkRangeWidget.cpp
  ctkRangeWidget.h
  ctkScreenshotDialog.cpp
  ctkScreenshotDialog.h
  ctkScreenshotDialog_p.h
  ctkSearchBox.cpp
  ctkSearchBox.h
  ctkSettings.cpp
  ctkSettings.h
  ctkSettingsDialog.cpp
  ctkSettingsDialog.h
  ctkSettingsPanel.cpp
  ctkSettingsPanel.h
  ctkSignalMapper.cpp
  ctkSignalMapper.h
  ctkSizeGrip.cpp
  ctkSizeGrip.h
  ctkSliderWidget.cpp
  ctkSliderWidget.h
  ctkTestApplication.cpp
  ctkTestApplication.h
  ctkThumbnailLabel.cpp
  ctkThumbnailLabel.h
  ctkThumbnailListWidget.cpp
  ctkThumbnailListWidget.h
  ctkThumbnailListWidget_p.h
  ctkToolTipTrapper.cpp
  ctkToolTipTrapper.h
  ctkTransferFunction.cpp
  ctkTransferFunction.h
  ctkTransferFunctionBarsItem.cpp
  ctkTransferFunctionBarsItem.h
  ctkTransferFunctionControlPointsItem.cpp
  ctkTransferFunctionControlPointsItem.h
  ctkTransferFunctionGradientItem.cpp
  ctkTransferFunctionGradientItem.h
  ctkTransferFunctionItem.cpp
  ctkTransferFunctionItem.h
  ctkTransferFunctionRepresentation.cpp
  ctkTransferFunctionRepresentation.h
  ctkTransferFunctionScene.cpp
  ctkTransferFunctionScene.h
  ctkTransferFunctionView.cpp
  ctkTransferFunctionView.h
  ctkTreeComboBox.cpp
  ctkTreeComboBox.h
  ctkWidgetsTestingUtilities.cpp
  ctkWidgetsTestingUtilities.h
  ctkWidgetsUtils.cpp
  ctkWidgetsUtils.h
  ctkWorkflowAbstractPagedWidget.cpp
  ctkWorkflowAbstractPagedWidget.h
  ctkWorkflowButtonBoxWidget.cpp
  ctkWorkflowButtonBoxWidget.h
  ctkWorkflowGroupBox.cpp
  ctkWorkflowGroupBox.h
  ctkWorkflowStackedWidget.cpp
  ctkWorkflowStackedWidget.h
  ctkWorkflowTabWidget.cpp
  ctkWorkflowTabWidget.h
  ctkWorkflowWidget.cpp
  ctkWorkflowWidget.h
  ctkWorkflowWidgetStep.cpp
  ctkWorkflowWidgetStep_p.h
  ctkWorkflowWidgetStep.h
  )

# Headers that should run through moc
set(KIT_MOC_SRCS
  ctkActionsWidget.h
  ctkAxesWidget.h
  ctkAddRemoveComboBox.h
  ctkBasePopupWidget.h
  ctkBasePopupWidget_p.h
  ctkButtonGroup.h
  ctkCheckableComboBox.h
  ctkCheckableHeaderView.h
  ctkCheckableModelHelper.h
  ctkCheckablePushButton.h
  ctkCheckBox.h
  ctkCheckBoxPixmaps.h
  ctkComboBox.h
  ctkCompleter.h
  ctkCollapsibleButton.h
  ctkCollapsibleGroupBox.h
  ctkColorDialog.h
  ctkColorPickerButton.h
  ctkConsole.h
  ctkConsole_p.h
  ctkCoordinatesWidget.h
  ctkCoordinatesWidget_p.h
  ctkCrosshairLabel.h
  ctkDateRangeWidget.h
  ctkDirectoryButton.h
  ctkDoubleRangeSlider.h
  ctkDoubleSlider.h
  ctkDoubleSpinBox.h
  ctkDoubleSpinBox_p.h
  ctkDynamicSpacer.h
  ctkErrorLogModel.h
  ctkErrorLogWidget.h
  ctkErrorLogStatusMessageHandler.h
  ctkExpandButton.h
  ctkExpandableWidget.h
  ctkFileDialog.h
  ctkFittedTextBrowser.h
  ctkFlatProxyModel.h
  ctkFlowLayout.h
  ctkFontButton.h
  ctkHistogram.h
  ctkLanguageComboBox.h
  ctkLayoutFactory.h
  ctkLayoutManager.h
  ctkLayoutViewFactory.h
  ctkMaterialPropertyPreviewLabel.h
  ctkMaterialPropertyWidget.h
  ctkMatrixWidget.h
  ctkMenuButton.h
  ctkMenuComboBox.h
  ctkMenuComboBox_p.h
  ctkMessageBox.h
  ctkModalityWidget.h
  ctkPathListButtonsWidget.h
  ctkPathListButtonsWidget_p.h
  ctkPopupWidget.h
  ctkPopupWidget_p.h
  ctkProxyStyle.h
  ctkPushButton.h
  ctkQImageView.h
  ctkRangeSlider.h
  ctkRangeWidget.h
  ctkScreenshotDialog.h
  ctkScreenshotDialog_p.h
  ctkSearchBox.h
  ctkSettings.h
  ctkSettingsDialog.h
  ctkSettingsPanel.h
  ctkSignalMapper.h
  ctkSizeGrip.h
  ctkSliderWidget.h
  ctkTestApplication.h
  ctkThumbnailLabel.h
  ctkThumbnailListWidget.h
  ctkToolTipTrapper.h
  ctkTransferFunction.h
  ctkTransferFunctionBarsItem.h
  ctkTransferFunctionControlPointsItem.h
  ctkTransferFunctionGradientItem.h
  ctkTransferFunctionItem.h
  ctkTransferFunctionRepresentation.h
  ctkTransferFunctionScene.h
  ctkTransferFunctionView.h
  ctkTreeComboBox.h
  ctkWorkflowAbstractPagedWidget.h
  ctkWorkflowButtonBoxWidget.h
  ctkWorkflowGroupBox.h
  ctkWorkflowStackedWidget.h
  ctkWorkflowTabWidget.h
  ctkWorkflowWidget.h
  ctkWorkflowWidgetStep.h
  ctkWorkflowWidgetStep_p.h


  )

#if(CTK_QT_VERSION VERSION_GREATER "4")
  list(APPEND KIT_MOC_SRCS ctkIconEnginePlugin_qt5.h)
#else()
#  list(APPEND KIT_MOC_SRCS ctkIconEnginePlugin_qt4.h)
#endif()

# Headers that should run through moc without adding
# the generated cpp file to the source list
set(KIT_GENERATE_MOC_SRCS
  ctkPathLineEdit.h
  ctkPathListWidget.h
  )

# UI files
set(KIT_UI_FORMS
  Resources/UI/ctkAddRemoveComboBox.ui
  Resources/UI/ctkRangeWidget.ui
  Resources/UI/ctkDateRangeWidget.ui
  Resources/UI/ctkErrorLogWidget.ui
  Resources/UI/ctkMaterialPropertyWidget.ui
  Resources/UI/ctkModalityWidget.ui
  Resources/UI/ctkPathListButtonsWidget.ui
  Resources/UI/ctkScreenshotDialog.ui
  Resources/UI/ctkSettingsDialog.ui
  Resources/UI/ctkSliderWidget.ui
  Resources/UI/ctkThumbnailLabel.ui
  Resources/UI/ctkThumbnailListWidget.ui
  Resources/UI/ctkWorkflowGroupBox.ui
  )

# Resources
set(KIT_resources
  Resources/ctkWidgets.qrc
  )

# Target libraries - See CMake/ctkFunctionGetTargetLibraries.cmake
# The following macro will read the target libraries from the file 'target_libraries.cmake'
#ctkFunctionGetTargetLibraries(KIT_target_libraries)

#if(CTK_QT_VERSION VERSION_GREATER "4")
  list(APPEND KIT_target_libraries Qt5::Widgets Qt5::Xml Qt5::OpenGL)
#endif()

# A player and a translator must be added for custom Qt widgets
if(CTK_USE_QTTESTING)
  list(APPEND KIT_SRCS
    ctkAxesWidgetEventPlayer.cpp
    ctkAxesWidgetEventPlayer.h
    ctkAxesWidgetEventTranslator.cpp
    ctkAxesWidgetEventTranslator.h
    ctkCheckableComboBoxEventPlayer.cpp
    ctkCheckableComboBoxEventPlayer.h
    ctkCheckableComboBoxEventTranslator.cpp
    ctkCheckableComboBoxEventTranslator.h
    ctkCheckableHeaderViewEventPlayer.cpp
    ctkCheckableHeaderViewEventPlayer.h
    ctkCheckableHeaderViewEventTranslator.cpp
    ctkCheckableHeaderViewEventTranslator.h
    ctkConsoleEventPlayer.cpp
    ctkConsoleEventPlayer.h
    ctkConsoleEventTranslator.cpp
    ctkConsoleEventTranslator.h
    ctkDoubleRangeSliderEventPlayer.cpp
    ctkDoubleRangeSliderEventPlayer.h
    ctkDoubleRangeSliderEventTranslator.cpp
    ctkDoubleRangeSliderEventTranslator.h
    ctkFileDialogEventPlayer.cpp
    ctkFileDialogEventPlayer.h
    ctkFileDialogEventTranslator.cpp
    ctkFileDialogEventTranslator.h
    ctkFontButtonEventPlayer.cpp
    ctkFontButtonEventPlayer.h
    ctkFontButtonEventTranslator.cpp
    ctkFontButtonEventTranslator.h
    ctkMatrixWidgetEventPlayer.cpp
    ctkMatrixWidgetEventPlayer.h
    ctkMatrixWidgetEventTranslator.cpp
    ctkMatrixWidgetEventTranslator.h
    ctkMenuComboBoxEventPlayer.cpp
    ctkMenuComboBoxEventPlayer.h
    ctkMenuComboBoxEventTranslator.cpp
    ctkMenuComboBoxEventTranslator.h
    ctkPathLineEditEventPlayer.cpp
    ctkPathLineEditEventPlayer.h
    ctkPathLineEditEventTranslator.cpp
    ctkPathLineEditEventTranslator.h
    ctkPopupWidgetEventPlayer.cpp
    ctkPopupWidgetEventPlayer.h
    ctkPopupWidgetEventTranslator.cpp
    ctkPopupWidgetEventTranslator.h
    ctkRangeSliderEventPlayer.cpp
    ctkRangeSliderEventPlayer.h
    ctkRangeSliderEventTranslator.cpp
    ctkRangeSliderEventTranslator.h
    ctkTreeComboBoxEventPlayer.cpp
    ctkTreeComboBoxEventPlayer.h
    ctkTreeComboBoxEventTranslator.cpp
    ctkTreeComboBoxEventTranslator.h
    )
  list(APPEND KIT_MOC_SRCS
    ctkAxesWidgetEventPlayer.h
    ctkAxesWidgetEventTranslator.h
    ctkCheckableComboBoxEventPlayer.h
    ctkCheckableComboBoxEventTranslator.h
    ctkCheckableHeaderViewEventPlayer.h
    ctkCheckableHeaderViewEventTranslator.h
    ctkCheckableModelHelper.h
    ctkConsoleEventPlayer.h
    ctkConsoleEventTranslator.h
    ctkDoubleRangeSliderEventPlayer.h
    ctkDoubleRangeSliderEventTranslator.h
    ctkFileDialogEventPlayer.h
    ctkFileDialogEventTranslator.h
    ctkFontButtonEventPlayer.h
    ctkFontButtonEventTranslator.h
    ctkMatrixWidgetEventPlayer.h
    ctkMatrixWidgetEventTranslator.h
    ctkMenuComboBoxEventPlayer.h
    ctkMenuComboBoxEventTranslator.h
    ctkPathLineEditEventPlayer.h
    ctkPathLineEditEventTranslator.h
    ctkPopupWidgetEventPlayer.h
    ctkPopupWidgetEventTranslator.h
    ctkRangeSliderEventPlayer.h
    ctkRangeSliderEventTranslator.h
    ctkTreeComboBoxEventPlayer.h
    ctkTreeComboBoxEventTranslator.h
    )
  list(APPEND KIT_target_libraries QtTesting)
endif()




SET(CMAKE_AUTOUIC OFF)
SET(CMAKE_AUTOMOC OFF)

qt5_wrap_ui(MY_UI_GENERATED_SRC  ${KIT_UI_FORMS})
qt5_wrap_cpp(MY_MOC  ${KIT_MOC_SRCS} )


add_library(
  CTKWidgets STATIC
  ${KIT_SRCS}
  ${KIT_MOC_SRCS}
    ${INCLUDES}
    ${MY_MOC}
    ${MY_UI_GENERATED_SRC}
    ${KIT_resources}
    ${KIT_GENERATE_MOC_SRCS}
     

)

generate_export_header(CTKWidgets EXPORT_FILE_NAME "${CMAKE_CURRENT_BINARY_DIR}/ctkWidgetsExport.h" EXPORT_MACRO_NAME "CTK_WIDGETS_EXPORT")  

target_include_directories(CTKWidgets PUBLIC 
  $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}> 
  $<INSTALL_INTERFACE:include/CTKWidgets>
  )



target_link_libraries(CTKWidgets PUBLIC CTKCore ${KIT_target_libraries} ) 

qt5_wrap_cpp(MY_MOC_GENERATED_SRC ${KIT_GENERATE_MOC_SRCS})
add_custom_target(CTKWidgets_mocs DEPENDS  ${MY_MOC_GENERATED_SRC})
add_dependencies(CTKWidgets CTKWidgets_mocs)

set(ALL_HEADER "${PUBLIC_HEADERS}" "${CMAKE_CURRENT_BINARY_DIR}/ctkWidgetsExport.h")

message("__> ${ALL_HEADER}")

set_target_properties(CTKWidgets PROPERTIES PUBLIC_HEADER "${ALL_HEADER}")

install(TARGETS CTKWidgets
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        PUBLIC_HEADER DESTINATION include/CTKWidgets
        ARCHIVE DESTINATION lib
        )


## quitar
if (false)
ctkMacroBuildLib(
  NAME ${PROJECT_NAME}
  EXPORT_DIRECTIVE ${KIT_export_directive}
  SRCS ${KIT_SRCS}
  MOC_SRCS ${KIT_MOC_SRCS}
  GENERATE_MOC_SRCS ${KIT_GENERATE_MOC_SRCS}
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
if(BUILD_TESTING)
  add_subdirectory(Testing)
endif()
