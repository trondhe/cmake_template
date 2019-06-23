add_library(${PROJECT_NAME} STATIC)
add_library(${PROJECT_NAME}::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

target_sources(${PROJECT_NAME}
    PRIVATE
        addFive.cpp
)

target_include_directories(${PROJECT_NAME}
    PUBLIC
        $<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
)

# Using generator expression to give access to internal headers instead of using PRIVATE/PUBLIC
# include directories function. This is to allow unit tests in the test folder to access this
# library's internal headers while also hiding them for other targets when being in a larger
# build tree of multiple libraries linked together.
# Full motivation: https://gitlab.kitware.com/cmake/cmake/issues/19048
target_include_directories(${PROJECT_NAME}
    PUBLIC
        "$<BUILD_INTERFACE:$<$<BOOL:$<TARGET_PROPERTY:${PROJECT_NAME}_PRIVATE>>:${CMAKE_CURRENT_SOURCE_DIR}>>"
)
set_property(TARGET ${PROJECT_NAME} PROPERTY ${PROJECT_NAME}_PRIVATE 1)

add_subdirectory(addOne)
add_subdirectory(addTwo)

###############################################################################
### Installation

include(GNUInstallDirs)
include(CMakePackageConfigHelpers)
set(CMAKE_INSTALL_CONFIGDIR ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME})

# Public headers
install(DIRECTORY ${PROJECT_SOURCE_DIR}/include/ DESTINATION include)

# Library and targets.cmake file
install(TARGETS ${PROJECT_NAME}
    EXPORT ${PROJECT_NAME}-export
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

install(
    EXPORT
        ${PROJECT_NAME}-export
    FILE
        ${PROJECT_NAME}Targets.cmake
    NAMESPACE
        ${PROJECT_NAME}::
    DESTINATION
        ${CMAKE_INSTALL_CONFIGDIR}
)

# Config.cmake file
configure_package_config_file(${PROJECT_SOURCE_DIR}/cmake/Config.cmake.in
  ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake
  INSTALL_DESTINATION ${CMAKE_INSTALL_CONFIGDIR}
)

install(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake
    DESTINATION
        ${CMAKE_INSTALL_CONFIGDIR}
)