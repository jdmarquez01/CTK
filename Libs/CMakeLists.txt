add_subdirectory(Scripting/Python)

add_subdirectory(Core)
add_subdirectory(Widgets)
if (VTK_FOUND)
add_subdirectory(Visualization)
endif()

