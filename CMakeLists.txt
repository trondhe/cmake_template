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
    find_package(doctest QUIET)
    if(TARGET doctest::doctest)
        # Doctest found via find_package
        # Include doctest.cmake for discover tests, found in CMAKE_MODULE_PATH 
        include(doctest)
    else(NOT TARGET doctest::doctest)
        # else include via subfolder external/doctest, run "git submodule update --init"
        if(EXISTS external/doctest/CMakeLists.txt)
            add_subdirectory(external/doctest)
            include(external/doctest/scripts/cmake/doctest.cmake)
        else()
            message(FATAL_ERROR
            " Doctest was neither found via find_package or in the external folder.\n "
            "Either make sure you have run 'conan install . -if <buildFolder>' and 'conan build . -bf <buildFolder>'\n"
            " or add doctest to the external folder either via git clone or 'git submodule update --init' ")
        endif()
    endif()
    add_subdirectory(test)
endif()

if(BUILD_TOOLS AND NOT BUILD_TESTING)
    add_subdirectory(tools)
endif()
