# include(Catch)

add_executable(${PROJECT_NAME}Test
    doctest_main.cpp
    addOne/addOneTest.cpp
    addTwo/addTwoTest.cpp
    addFiveTest.cpp
)

# Give test target access to projects internal headers
set_property(TARGET ${PROJECT_NAME}Test PROPERTY ${PROJECT_NAME}_PRIVATE 1)

target_link_libraries(${PROJECT_NAME}Test
    PUBLIC
        ${PROJECT_NAME}
        doctest
)


# doctest_discover_tests(${PROJECT_NAME}Test)