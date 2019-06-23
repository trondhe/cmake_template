#include "addTwo/addTwo.h"
#include "doctest.h"

TEST_CASE("test addTwo")
{
    CHECK(addTwo(2) == 4);
}