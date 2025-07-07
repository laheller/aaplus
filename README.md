# AAPlus

**AAPlus** is a cross-language & cross-platform wrapper library for [AA+ (Astronomical Algorithms+)](http://naughter.com/aa.html), a high-precision C++ implementation of [Jean Meeus's astronomical algorithms](https://www.amazon.com/Astronomical-Algorithms-Jean-Meeus/dp/0943396611) originally developed by **PJ Naughter**. This project provides:

- A **C language interface** to the AA+ C++ framework
- A **C# (P/Invoke) wrapper** for seamless integration with .NET applications

The goal is to make AA+ functionality accessible from C and C# environments, enabling high-precision astronomical calculations in both native and managed codebases.

## Features

- Clean C interface layered over the C++ implementation
- P/Invoke-based C# wrapper for .NET applications
- Access to key AA+ modules: Sun, Moon, planets, coordinate transformations, etc.
- Cross-platform support: Works on both Windows & Linux

## Repository Structure

AAPlus/<br/>
├── AAPlusLib/ -> .NET P/Invoke C# bindings as a .NET netstandard library project<br/>
├── caaplus/ -> Original AA+ C++ source by PJ Naughter extended with C-language wrapper as a Visual C++ project<br/>
├── test/ -> Example C# console application<br/>
├── README.md -> this file<br/>
└── aaplus.sln -> Visual Studio 2022 solution file<br/>

## Getting Started

### Clone the repository:
```bash
git clone https://github.com/laheller/aaplus.git
```

### Build the C++ and C wrapper:
* Windows<br/>
&#9;Simply open `aaplus.sln` in Visual Studio 2022 (Community Edition) that has both C++ and C# workloads installed & build. It should create the `caaplus.dll` library.

* Linux<br/>
&#9;Make sure that the 64bit (and optionally the 32bit) GNU C++ compilers and build tools are installed.
```bash
cd aaplus/caaplus
./build32.sh # builds the 32bit shared library, produces i386/libcaaplus.so
./build64.sh # builds the 64bit shared library, produces amd64/libcaaplus.so
```

### Use in C# Project:
Add the compiled native library (.dll, .so) to your project output directory, where the main output .NET binary is located.

Reference the `AAPlusLib` project or simply include the `AAPlus.cs` source file in your project.

### Check the `test` project for examples, how to use AAPlus library.

## License
This project is licensed under the same terms as the original AA+ library. Please refer to the original [copyright](http://naughter.com/aa.html).

## Credits
AA+ framework by [PJ Naughter](mailto:pjna@naughter.com)

C and C# wrappers by Ladislav Heller
