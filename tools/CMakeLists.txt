set(TOOL ${PROJECT_NAME}tool)

add_executable(${TOOL})

target_sources(${TOOL}
    PRIVATE
        main.cpp
)

target_link_libraries(${TOOL}
    PRIVATE
        ${PROJECT_NAME}::${PROJECT_NAME}
)