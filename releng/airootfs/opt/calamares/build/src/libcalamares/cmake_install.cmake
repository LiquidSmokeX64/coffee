# Install script for directory: /home/fahr/calamares/src/libcalamares

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "0")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "CALAMARES" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcalamares.so.3.3.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcalamares.so.3.3"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fahr/calamares/build/libcalamares.so.3.3.0"
    "/home/fahr/calamares/build/libcalamares.so.3.3"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcalamares.so.3.3.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcalamares.so.3.3"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "CALAMARES" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcalamares.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcalamares.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcalamares.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/fahr/calamares/build/libcalamares.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcalamares.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcalamares.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libcalamares.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "CALAMARES" OR NOT CMAKE_INSTALL_COMPONENT)
  
    file( MAKE_DIRECTORY "$ENV{DESTDIR}//usr/lib/calamares" )
    execute_process( COMMAND "/usr/bin/cmake" -E create_symlink ../libcalamares.so.3.3.0 libcalamares.so WORKING_DIRECTORY "$ENV{DESTDIR}//usr/lib/calamares" )

endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "CALAMARES" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/libcalamares" TYPE FILE FILES
    "/home/fahr/calamares/build/src/libcalamares/CalamaresConfig.h"
    "/home/fahr/calamares/build/src/libcalamares/CalamaresVersion.h"
    "/home/fahr/calamares/src/libcalamares/CalamaresAbout.h"
    "/home/fahr/calamares/src/libcalamares/CppJob.h"
    "/home/fahr/calamares/src/libcalamares/DllMacro.h"
    "/home/fahr/calamares/src/libcalamares/GlobalStorage.h"
    "/home/fahr/calamares/src/libcalamares/Job.h"
    "/home/fahr/calamares/src/libcalamares/JobExample.h"
    "/home/fahr/calamares/src/libcalamares/JobQueue.h"
    "/home/fahr/calamares/src/libcalamares/ProcessJob.h"
    "/home/fahr/calamares/src/libcalamares/PythonHelper.h"
    "/home/fahr/calamares/src/libcalamares/PythonJob.h"
    "/home/fahr/calamares/src/libcalamares/PythonJobApi.h"
    "/home/fahr/calamares/src/libcalamares/Settings.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "CALAMARES" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/libcalamares/geoip" TYPE FILE FILES
    "/home/fahr/calamares/src/libcalamares/geoip/GeoIPFixed.h"
    "/home/fahr/calamares/src/libcalamares/geoip/GeoIPJSON.h"
    "/home/fahr/calamares/src/libcalamares/geoip/GeoIPTests.h"
    "/home/fahr/calamares/src/libcalamares/geoip/GeoIPXML.h"
    "/home/fahr/calamares/src/libcalamares/geoip/Handler.h"
    "/home/fahr/calamares/src/libcalamares/geoip/Interface.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "CALAMARES" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/libcalamares/locale" TYPE FILE FILES
    "/home/fahr/calamares/src/libcalamares/locale/Global.h"
    "/home/fahr/calamares/src/libcalamares/locale/Lookup.h"
    "/home/fahr/calamares/src/libcalamares/locale/TimeZone.h"
    "/home/fahr/calamares/src/libcalamares/locale/TranslatableConfiguration.h"
    "/home/fahr/calamares/src/libcalamares/locale/TranslatableString.h"
    "/home/fahr/calamares/src/libcalamares/locale/Translation.h"
    "/home/fahr/calamares/src/libcalamares/locale/TranslationsModel.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "CALAMARES" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/libcalamares/modulesystem" TYPE FILE FILES
    "/home/fahr/calamares/src/libcalamares/modulesystem/Actions.h"
    "/home/fahr/calamares/src/libcalamares/modulesystem/Config.h"
    "/home/fahr/calamares/src/libcalamares/modulesystem/Descriptor.h"
    "/home/fahr/calamares/src/libcalamares/modulesystem/InstanceKey.h"
    "/home/fahr/calamares/src/libcalamares/modulesystem/Module.h"
    "/home/fahr/calamares/src/libcalamares/modulesystem/Preset.h"
    "/home/fahr/calamares/src/libcalamares/modulesystem/Requirement.h"
    "/home/fahr/calamares/src/libcalamares/modulesystem/RequirementsChecker.h"
    "/home/fahr/calamares/src/libcalamares/modulesystem/RequirementsModel.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "CALAMARES" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/libcalamares/network" TYPE FILE FILES
    "/home/fahr/calamares/src/libcalamares/network/Manager.h"
    "/home/fahr/calamares/src/libcalamares/network/Tests.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "CALAMARES" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/libcalamares/partition" TYPE FILE FILES
    "/home/fahr/calamares/src/libcalamares/partition/AutoMount.h"
    "/home/fahr/calamares/src/libcalamares/partition/FileSystem.h"
    "/home/fahr/calamares/src/libcalamares/partition/Global.h"
    "/home/fahr/calamares/src/libcalamares/partition/KPMHelper.h"
    "/home/fahr/calamares/src/libcalamares/partition/KPMManager.h"
    "/home/fahr/calamares/src/libcalamares/partition/Mount.h"
    "/home/fahr/calamares/src/libcalamares/partition/PartitionIterator.h"
    "/home/fahr/calamares/src/libcalamares/partition/PartitionQuery.h"
    "/home/fahr/calamares/src/libcalamares/partition/PartitionSize.h"
    "/home/fahr/calamares/src/libcalamares/partition/Sync.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "CALAMARES" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/libcalamares/utils" TYPE FILE FILES
    "/home/fahr/calamares/src/libcalamares/utils/BoostPython.h"
    "/home/fahr/calamares/src/libcalamares/utils/CalamaresUtilsSystem.h"
    "/home/fahr/calamares/src/libcalamares/utils/CommandList.h"
    "/home/fahr/calamares/src/libcalamares/utils/Dirs.h"
    "/home/fahr/calamares/src/libcalamares/utils/Entropy.h"
    "/home/fahr/calamares/src/libcalamares/utils/Logger.h"
    "/home/fahr/calamares/src/libcalamares/utils/NamedEnum.h"
    "/home/fahr/calamares/src/libcalamares/utils/NamedSuffix.h"
    "/home/fahr/calamares/src/libcalamares/utils/Permissions.h"
    "/home/fahr/calamares/src/libcalamares/utils/PluginFactory.h"
    "/home/fahr/calamares/src/libcalamares/utils/RAII.h"
    "/home/fahr/calamares/src/libcalamares/utils/Retranslator.h"
    "/home/fahr/calamares/src/libcalamares/utils/Runner.h"
    "/home/fahr/calamares/src/libcalamares/utils/String.h"
    "/home/fahr/calamares/src/libcalamares/utils/StringExpander.h"
    "/home/fahr/calamares/src/libcalamares/utils/Traits.h"
    "/home/fahr/calamares/src/libcalamares/utils/UMask.h"
    "/home/fahr/calamares/src/libcalamares/utils/Units.h"
    "/home/fahr/calamares/src/libcalamares/utils/Variant.h"
    "/home/fahr/calamares/src/libcalamares/utils/Yaml.h"
    "/home/fahr/calamares/src/libcalamares/utils/moc-warnings.h"
    )
endif()

