from conans import ConanFile, CMake, tools


class ConanRecipe(ConanFile):
    name = "cmake_template"
    version = "0.0.1"
    # Example requirement on doctest, bincrafters does not have v.2.3.3 as of commit
    # required for doctest_discover_tests
    # newest at current time is "doctest/2.3.1@bincrafters/stable"
    build_requires = "doctest/2.3.3@opensource/stable"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
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
        cmake.install()
        cmake.test()
