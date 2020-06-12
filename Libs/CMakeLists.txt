message ("CONAN LIBS = ${CONAN_LIBS}")

add_subdirectory(Core)
add_subdirectory(Widgets)




add_subdirectory(Scripting/Python)


if (VTK_FOUND)
add_subdirectory(Visualization)
endif()

