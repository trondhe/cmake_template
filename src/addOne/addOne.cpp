#include "addOne.h"

int addOne(int value)
{
    return value + 1;
}

#ifdef BUILD_UNIT_TESTS
#include "doctest/doctest.h"

TEST_CASE("test addOne")
{
    CHECK(addOne(1) == 2);
}

#endif
