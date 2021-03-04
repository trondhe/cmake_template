
add_executable(${PROJECT_NAME}Test
    doctest_main.cpp
)

target_link_libraries(${PROJECT_NAME}
    PUBLIC
        doctest::doctest
)

target_link_libraries(${PROJECT_NAME}Test
    PUBLIC
        ${PROJECT_NAME}
)

target_compile_definitions(${PROJECT_NAME}
PRIVATE
    BUILD_UNIT_TESTS
)

doctest_discover_tests(${PROJECT_NAME}Test)
