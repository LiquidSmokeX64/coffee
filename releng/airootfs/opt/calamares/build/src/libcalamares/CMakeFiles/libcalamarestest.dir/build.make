# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.25

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/fahr/calamares

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/fahr/calamares/build

# Include any dependencies generated for this target.
include src/libcalamares/CMakeFiles/libcalamarestest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/libcalamares/CMakeFiles/libcalamarestest.dir/compiler_depend.make

# Include the progress variables for this target.
include src/libcalamares/CMakeFiles/libcalamarestest.dir/progress.make

# Include the compile flags for this target's objects.
include src/libcalamares/CMakeFiles/libcalamarestest.dir/flags.make

src/libcalamares/CMakeFiles/libcalamarestest.dir/libcalamarestest_autogen/mocs_compilation.cpp.o: src/libcalamares/CMakeFiles/libcalamarestest.dir/flags.make
src/libcalamares/CMakeFiles/libcalamarestest.dir/libcalamarestest_autogen/mocs_compilation.cpp.o: src/libcalamares/libcalamarestest_autogen/mocs_compilation.cpp
src/libcalamares/CMakeFiles/libcalamarestest.dir/libcalamarestest_autogen/mocs_compilation.cpp.o: src/libcalamares/CMakeFiles/libcalamarestest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fahr/calamares/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/libcalamares/CMakeFiles/libcalamarestest.dir/libcalamarestest_autogen/mocs_compilation.cpp.o"
	cd /home/fahr/calamares/build/src/libcalamares && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/libcalamares/CMakeFiles/libcalamarestest.dir/libcalamarestest_autogen/mocs_compilation.cpp.o -MF CMakeFiles/libcalamarestest.dir/libcalamarestest_autogen/mocs_compilation.cpp.o.d -o CMakeFiles/libcalamarestest.dir/libcalamarestest_autogen/mocs_compilation.cpp.o -c /home/fahr/calamares/build/src/libcalamares/libcalamarestest_autogen/mocs_compilation.cpp

src/libcalamares/CMakeFiles/libcalamarestest.dir/libcalamarestest_autogen/mocs_compilation.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/libcalamarestest.dir/libcalamarestest_autogen/mocs_compilation.cpp.i"
	cd /home/fahr/calamares/build/src/libcalamares && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fahr/calamares/build/src/libcalamares/libcalamarestest_autogen/mocs_compilation.cpp > CMakeFiles/libcalamarestest.dir/libcalamarestest_autogen/mocs_compilation.cpp.i

src/libcalamares/CMakeFiles/libcalamarestest.dir/libcalamarestest_autogen/mocs_compilation.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/libcalamarestest.dir/libcalamarestest_autogen/mocs_compilation.cpp.s"
	cd /home/fahr/calamares/build/src/libcalamares && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fahr/calamares/build/src/libcalamares/libcalamarestest_autogen/mocs_compilation.cpp -o CMakeFiles/libcalamarestest.dir/libcalamarestest_autogen/mocs_compilation.cpp.s

src/libcalamares/CMakeFiles/libcalamarestest.dir/Tests.cpp.o: src/libcalamares/CMakeFiles/libcalamarestest.dir/flags.make
src/libcalamares/CMakeFiles/libcalamarestest.dir/Tests.cpp.o: /home/fahr/calamares/src/libcalamares/Tests.cpp
src/libcalamares/CMakeFiles/libcalamarestest.dir/Tests.cpp.o: src/libcalamares/CMakeFiles/libcalamarestest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fahr/calamares/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object src/libcalamares/CMakeFiles/libcalamarestest.dir/Tests.cpp.o"
	cd /home/fahr/calamares/build/src/libcalamares && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/libcalamares/CMakeFiles/libcalamarestest.dir/Tests.cpp.o -MF CMakeFiles/libcalamarestest.dir/Tests.cpp.o.d -o CMakeFiles/libcalamarestest.dir/Tests.cpp.o -c /home/fahr/calamares/src/libcalamares/Tests.cpp

src/libcalamares/CMakeFiles/libcalamarestest.dir/Tests.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/libcalamarestest.dir/Tests.cpp.i"
	cd /home/fahr/calamares/build/src/libcalamares && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fahr/calamares/src/libcalamares/Tests.cpp > CMakeFiles/libcalamarestest.dir/Tests.cpp.i

src/libcalamares/CMakeFiles/libcalamarestest.dir/Tests.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/libcalamarestest.dir/Tests.cpp.s"
	cd /home/fahr/calamares/build/src/libcalamares && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fahr/calamares/src/libcalamares/Tests.cpp -o CMakeFiles/libcalamarestest.dir/Tests.cpp.s

# Object files for target libcalamarestest
libcalamarestest_OBJECTS = \
"CMakeFiles/libcalamarestest.dir/libcalamarestest_autogen/mocs_compilation.cpp.o" \
"CMakeFiles/libcalamarestest.dir/Tests.cpp.o"

# External object files for target libcalamarestest
libcalamarestest_EXTERNAL_OBJECTS =

libcalamarestest: src/libcalamares/CMakeFiles/libcalamarestest.dir/libcalamarestest_autogen/mocs_compilation.cpp.o
libcalamarestest: src/libcalamares/CMakeFiles/libcalamarestest.dir/Tests.cpp.o
libcalamarestest: src/libcalamares/CMakeFiles/libcalamarestest.dir/build.make
libcalamarestest: libcalamares.so.3.3.0
libcalamarestest: /usr/lib/libQt5Test.so.5.15.8
libcalamarestest: /usr/lib/libyaml-cpp.so
libcalamarestest: /usr/lib/libKF5CoreAddons.so.5.101.0
libcalamarestest: /usr/lib/libQt5Core.so.5.15.8
libcalamarestest: src/libcalamares/CMakeFiles/libcalamarestest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/fahr/calamares/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable ../../libcalamarestest"
	cd /home/fahr/calamares/build/src/libcalamares && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/libcalamarestest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/libcalamares/CMakeFiles/libcalamarestest.dir/build: libcalamarestest
.PHONY : src/libcalamares/CMakeFiles/libcalamarestest.dir/build

src/libcalamares/CMakeFiles/libcalamarestest.dir/clean:
	cd /home/fahr/calamares/build/src/libcalamares && $(CMAKE_COMMAND) -P CMakeFiles/libcalamarestest.dir/cmake_clean.cmake
.PHONY : src/libcalamares/CMakeFiles/libcalamarestest.dir/clean

src/libcalamares/CMakeFiles/libcalamarestest.dir/depend:
	cd /home/fahr/calamares/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/fahr/calamares /home/fahr/calamares/src/libcalamares /home/fahr/calamares/build /home/fahr/calamares/build/src/libcalamares /home/fahr/calamares/build/src/libcalamares/CMakeFiles/libcalamarestest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/libcalamares/CMakeFiles/libcalamarestest.dir/depend

