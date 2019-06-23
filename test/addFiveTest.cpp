#include "cmake_template/addFive.h"
#include "doctest.h"

TEST_CASE("test addFive")
{
    CHECK(addFive(5) == 10);
}