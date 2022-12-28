.. _help.issues:

Issue tracker & bugs
====================

Issues and bugs should be reported over at `https://github.com/archlinux/coffeebrewer/issues <https://github.com/Torxed/coffeebrewer/issues>`_.

General questions, enhancements and security issues can be reported over there too.
For quick issues or if you need help, head over to the Discord server which has a help channel.

Log files
---------

| When submitting a help ticket, please include the :code:`/var/log/coffeebrewer/install.log`.
| It can be found both on the live ISO but also in the installed filesystem if the base packages were strapped in.

.. tip::
   | An easy way to submit logs is ``curl -F'file=@/var/log/coffeebrewer/install.log' https://0x0.st``.
   | Use caution when submitting other log files, but ``coffeebrewer`` pledges to keep ``install.log`` safe for posting publicly!

| There are additional log files under ``/var/log/coffeebrewer/`` that can be useful:

 - ``/var/log/coffeebrewer/user_configuration.json`` - Stores most of the guided answers in the installer
 - ``/var/log/coffeebrewer/user_credentials.json`` - Stores any usernames or passwords, can be passed to ``--creds``
 - ``/var/log/coffeebrewer/user_disk_layouts.json`` - Stores the chosen disks and their layouts
 - ``/var/log/coffeebrewer/install.log`` - A log file over what steps were taken by coffeebrewer
 - ``/var/log/coffeebrewer/cmd_history.txt`` - A complete command history, command by command in order
 - ``/var/log/coffeebrewer/cmd_output.txt`` - A raw output from all the commands that were executed by coffeebrewer

.. warning::

    We only try to guarantee that ``/var/log/coffeebrewer/install.log`` is free from sensitive information.
    Any other log file should be pasted with **utmost care**!
