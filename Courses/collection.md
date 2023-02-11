Options
Here are a few of the more useful command options when using g++. These compiler flags may be used in any order you wish. However, by convention, we usually group the list of source files together and the list of options together.

Most Common
These are generally most important options for normal use on your VM and in your assignment Makefiles. You’ll probably end up knowing them by heart.

-Wall show all warnings. It turns on all standard C++ warnings about code that might cause unexpected or undefined behavior.
-g provides debugging feature for your program. You will need this when you want to use gdb or valgrind.
--std=c++<##> uses version <##> of C++ when compiling. This will allow you to use specific features of that C++ version. Typically, we have you use --std=c++17.
-o <filename> compiles and links files into an executable named <filename>. The default filename is a.out.
-c compiles and assembles files but doesn’t link them. This is useful when building large projects to separate file compilation and minimize what is re-compiled.