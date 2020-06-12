from conans import ConanFile, tools, CMake

class HelloConan(ConanFile):
    name = "CTK"
    version = "0.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of hello here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "Qt5_DIR": "ANY" ,"VTK_DIR":"ANY"}
    default_options = {"shared": False , "VTK_DIR":""}
    generators = "cmake"
    exports_sources = "*"
    build_requires = "pythonqt/0.1@demo/testing"


    def build(self):
        cmake = CMake(self)
        #self.options.VTK_DIR
        cmake.definitions["Qt5_DIR"] = self.options.Qt5_DIR
        tools.replace_in_file("CMakeLists.txt", "PROJECT(CTK)",'''PROJECT(CTK)
        include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
        conan_basic_setup()''')
        cmake.configure()
        cmake.build()
        cmake.install()

        # Explicit way:
        # self.run('cmake "%s/src" %s' % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["CTKCore","CTKScriptingPythonCore", "CTKWidgets","CTKScriptingPythonWidgets"]
        self.cpp_info.includedirs = ["include/CTKCore","include/CTKScriptingPythonCore", "include/CTKWidgets","include/CTKScriptingPythonWidgets"]
        
