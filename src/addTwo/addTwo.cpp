#include "addTwo.h"

int addTwo(int value)
{
    return value + 2;
}

#ifdef BUILD_UNIT_TESTS
#include "doctest/doctest.h"

TEST_CASE("test addTwo")
{
    CHECK(addTwo(2) == 4);
}

#endif
