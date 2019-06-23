# CMake template project

## Summary

This repo aims to be a simple but complete example of a CMake project. The setup aims to be flexible, allowing being standalone compilable, it can be part of a larger build tree, or a package managed by [Conan](https://conan.io/) (package manager).

## Background and motivation

Due to few complete CMake examples in the wild, I though creating a simple template project anyone can use would be useful to someone.

The project setup tries to adhere to the setup explained in the [vector-of-bool/pitchfork](https://github.com/vector-of-bool/pitchfork) project.
If deviations from this standard, or other better solutions in the CMake files exists, feel free to do a pull request and then we can discuss the solution.

## Structure explanation

**include**  
include folder contains all and only public headers, such that there is no confusion if something is a public header or not. The CMake code also sets up the project in such a way that it makes it harder to use "wrongly".

**src**  
The src/source folder contains all the projects source files and private headers.
The structure is such that cmake includes everything in that directory.
This makes it such that *sub-features* are contained in their own folders which sets up the include statements such that they clearly show where the header file is located.
See how `addFive.cpp` includes the headers from `addOne` and `addTwo` features. These include statements will be valid throughout all files in the src folder, regardless of folder level.

**tools**  
The tools folder compiles a simple main function that links against the library in the src folder and executes the function in the public header.

**test**  
The test folder contains unit tests for the library. It links against the library, but also gets access to the project's internal headers, explained why here: https://gitlab.kitware.com/cmake/cmake/issues/19048

## Compile and Test

The project uses doctest for unit tests. 
If using conan the `find_package(doctest)` should work automatically (not tested as of now).  
If not its source can be gotten by running `git submodule update --init` or be manually downloaded copied into `external/doctest` folder.

All following commands are set up as vscode tasks
`ctrl+shift+p -> Tasks:Run Task`  
Recommended to bind action this to a hotkey.

### Configure

`cmake -GNinja -Bbuild .`

### Build

`cmake --build build`

### Test

`cd build && ctest`
