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

# Utility rule file for luksbootkeyfiletest_autogen.

# Include any custom commands dependencies for this target.
include src/modules/luksbootkeyfile/CMakeFiles/luksbootkeyfiletest_autogen.dir/compiler_depend.make

# Include the progress variables for this target.
include src/modules/luksbootkeyfile/CMakeFiles/luksbootkeyfiletest_autogen.dir/progress.make

src/modules/luksbootkeyfile/CMakeFiles/luksbootkeyfiletest_autogen:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/fahr/calamares/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Automatic MOC for target luksbootkeyfiletest"
	cd /home/fahr/calamares/build/src/modules/luksbootkeyfile && /usr/bin/cmake -E cmake_autogen /home/fahr/calamares/build/src/modules/luksbootkeyfile/CMakeFiles/luksbootkeyfiletest_autogen.dir/AutogenInfo.json Debug

luksbootkeyfiletest_autogen: src/modules/luksbootkeyfile/CMakeFiles/luksbootkeyfiletest_autogen
luksbootkeyfiletest_autogen: src/modules/luksbootkeyfile/CMakeFiles/luksbootkeyfiletest_autogen.dir/build.make
.PHONY : luksbootkeyfiletest_autogen

# Rule to build all files generated by this target.
src/modules/luksbootkeyfile/CMakeFiles/luksbootkeyfiletest_autogen.dir/build: luksbootkeyfiletest_autogen
.PHONY : src/modules/luksbootkeyfile/CMakeFiles/luksbootkeyfiletest_autogen.dir/build

src/modules/luksbootkeyfile/CMakeFiles/luksbootkeyfiletest_autogen.dir/clean:
	cd /home/fahr/calamares/build/src/modules/luksbootkeyfile && $(CMAKE_COMMAND) -P CMakeFiles/luksbootkeyfiletest_autogen.dir/cmake_clean.cmake
.PHONY : src/modules/luksbootkeyfile/CMakeFiles/luksbootkeyfiletest_autogen.dir/clean

src/modules/luksbootkeyfile/CMakeFiles/luksbootkeyfiletest_autogen.dir/depend:
	cd /home/fahr/calamares/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/fahr/calamares /home/fahr/calamares/src/modules/luksbootkeyfile /home/fahr/calamares/build /home/fahr/calamares/build/src/modules/luksbootkeyfile /home/fahr/calamares/build/src/modules/luksbootkeyfile/CMakeFiles/luksbootkeyfiletest_autogen.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/modules/luksbootkeyfile/CMakeFiles/luksbootkeyfiletest_autogen.dir/depend

