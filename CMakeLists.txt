cmake_minimum_required(VERSION 3.13 FATAL_ERROR)

project(cmake_template CXX)

include(CTest)
option(BUILD_TOOLS "Build tool to run library" On)

# Check if conan_paths file exists such that it can be build
# both with Coann and just with CMake directly
if(EXISTS ${CMAKE_BINARY_DIR}/conan_paths.cmake)
    include(${CMAKE_BINARY_DIR}/conan_paths.cmake)
endif()

add_subdirectory(src)

if(BUILD_TESTING)
    # Search if doctest is installed or added via Conan, else will add from external folder
    # add via submodule
    find_package(doctest CONFIG)
    if(NOT TARGET doctest)
        add_subdirectory(external/doctest)
        include(external/doctest/scripts/cmake/doctest.cmake)
    endif()
    add_subdirectory(test)
endif()

if(BUILD_TOOLS)
    add_subdirectory(tools)
endif()
