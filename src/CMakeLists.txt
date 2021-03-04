if(BUILD_TESTING)
    # Required for self registrering unit tests for a library target.
    set(PROJECT_TYPE OBJECT) 
else()
    # Without unit tests, build the target as a normal static library.*
    set(PROJECT_TYPE STATIC)
endif()

add_library(${PROJECT_NAME} ${PROJECT_TYPE})
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

target_include_directories(${PROJECT_NAME}
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}
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
