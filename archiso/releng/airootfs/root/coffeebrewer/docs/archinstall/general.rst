.. _coffeebrewer.helpers:

.. warning::
	All these helper functions are mostly, if not all, related to outside-installation-instructions. Meaning the calls will affect your current running system - and not touch your installed system.

Profile related helpers
=======================

.. autofunction:: coffeebrewer.list_profiles

Packages
========

.. autofunction:: coffeebrewer.find_package

.. autofunction:: coffeebrewer.find_packages

Locale related
==============

.. autofunction:: coffeebrewer.list_keyboard_languages

.. autofunction:: coffeebrewer.search_keyboard_layout

.. autofunction:: coffeebrewer.set_keyboard_language

.. 
	autofunction:: coffeebrewer.Installer.set_keyboard_layout

Services
========

.. autofunction:: coffeebrewer.service_state

Mirrors
=======

.. autofunction:: coffeebrewer.filter_mirrors_by_region

.. autofunction:: coffeebrewer.add_custom_mirrors

.. autofunction:: coffeebrewer.insert_mirrors

.. autofunction:: coffeebrewer.use_mirrors

.. autofunction:: coffeebrewer.re_rank_mirrors

.. autofunction:: coffeebrewer.list_mirrors

Disk related
============

.. autofunction:: coffeebrewer.BlockDevice

.. autofunction:: coffeebrewer.Partition

.. autofunction:: coffeebrewer.Filesystem

.. autofunction:: coffeebrewer.device_state

.. autofunction:: coffeebrewer.all_blockdevices

Luks (Disk encryption)
======================

.. autofunction:: coffeebrewer.luks2

Networking
==========

.. autofunction:: coffeebrewer.get_hw_addr

.. autofunction:: coffeebrewer.list_interfaces

.. autofunction:: coffeebrewer.check_mirror_reachable

.. autofunction:: coffeebrewer.update_keyring

.. autofunction:: coffeebrewer.enrich_iface_types

.. autofunction:: coffeebrewer.get_interface_from_mac

.. autofunction:: coffeebrewer.wireless_scan

.. autofunction:: coffeebrewer.get_wireless_networks

General
=======

.. autofunction:: coffeebrewer.log

.. autofunction:: coffeebrewer.locate_binary

.. autofunction:: coffeebrewer.SysCommand

.. autofunction:: coffeebrewer.SysCommandWorker

Exceptions
==========

.. autofunction:: coffeebrewer.RequirementError

.. autofunction:: coffeebrewer.DiskError

.. autofunction:: coffeebrewer.ProfileError

.. autofunction:: coffeebrewer.SysCallError

.. autofunction:: coffeebrewer.ProfileNotFound

.. autofunction:: coffeebrewer.HardwareIncompatibilityError

.. autofunction:: coffeebrewer.PermissionError

.. autofunction:: coffeebrewer.UserError

.. autofunction:: coffeebrewer.ServiceException
