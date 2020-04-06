from conans import ConanFile, CMake, tools


class ConanRecipe(ConanFile):
    name = "cmake_template"
    version = "0.0.1"
    build_requires = "doctest/2.3.8"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_paths"
    scm = {
        "type": "git",
        "url": "https://github.com/trondhe/cmake_template.git",
        "revision": "auto"
    }

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.test()
        cmake.install()
