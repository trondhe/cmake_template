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
The test folder contains unit tests for the library. It links against the library, but also gets access to the project's internal headers, explained why here: <https://gitlab.kitware.com/cmake/cmake/issues/19048>

## Compile and Test

This project has a single dependency on doctest for unit tests.

### With conan package manager

If using conan, `find_package(doctest)` should work automatically.

Install the dependency with `conan install . -if build`.

Build the project with `conan build . -bf build`.

### Without package manager

#### Setup dependencies

The source for the dependency of doctest can be gotten by running `git submodule update --init` or be manually cloned into `external/doctest` folder.

#### Configure and build

All following commands are set up as vscode tasks
`ctrl+shift+p -> Tasks:Run Task`  
Recommended to bind action this to a hotkey.

To configure the project `cmake -GNinja -Bbuild .` and to build `cmake --build build`.

Running tests via ctest can be done with `cd build && ctest`

## Notes

### Unit testing

When having multiple targets in a single build tree, how do you unit test internal classes of a target without making its headers public to other targets?  
This is an issue that occurs when having the unit test files as a standalone executable that you link the target into. You have no reasonable way to access the headers without relative paths upwards
or other types of solutions which create coupledness and becomes harder and harder to maintain.
The original solution used a hack proposed by maintainers of cmake from this issue <https://gitlab.kitware.com/cmake/cmake/issues/19048> which is a reasonable workaround.  
This solution has now been replaced by keeping the unit tests inline in the same compilation unit. This removes the issue with private headers polluting the public includes while also not relying on mostly any hacks. The only requirement is that the library has to be build as an `OBJECT` target instead of `STATIC`.
