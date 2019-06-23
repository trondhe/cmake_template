#include "addOne/addOne.h"
#include "doctest.h"

TEST_CASE("test addOne")
{
    CHECK(addOne(1) == 2);
}