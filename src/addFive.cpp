#include "cmake_template/addFive.h"

#include "addOne/addOne.h"
#include "addTwo/addTwo.h"

int addFive(int value)
{
    int plusOne = addOne(value);
    int plusThree = addTwo(plusOne);
    int plusFive = addTwo(plusThree);
    return plusFive;
}
