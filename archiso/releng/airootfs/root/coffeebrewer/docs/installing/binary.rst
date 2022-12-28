.. _installing.binary:

Binary executable
=================

coffeebrewer can be compiled into a standalone executable.
For Arch Linux based systems, there's a package for this called `coffeebrewer <https://archlinux.org/packages/extra/any/coffeebrewer/>`_.

.. warning::
    This is not required if you're running coffeebrewer on a pre-built ISO. The installation is only required if you're creating your own scripted installations.

Using pacman
------------

coffeebrewer is on the `official repositories <https://wiki.archlinux.org/index.php/Official_repositories>`_.

.. code-block:: console

    sudo pacman -S coffeebrewer

Using PKGBUILD
--------------

The `source <https://github.com/archlinux/coffeebrewer>`_ contains a binary `PKGBUILD <https://github.com/Project-X-Mods/coffeebrewer/tree/master/PKGBUILD/coffeebrewer>`_ which can be either copied straight off the website or cloned using :code:`git clone https://github.com/Project-X-Mods/coffeebrewer`.

Once you've obtained the `PKGBUILD`, building it is pretty straight forward.

.. code-block:: console

    makepkg -s

Which should produce an `coffeebrewer-X.x.z-1.pkg.tar.zst` which can be installed using:

.. code-block:: console

    sudo pacman -U coffeebrewer-X.x.z-1.pkg.tar.zst

.. note::

    For a complete guide on the build process, please consult the `PKGBUILD on ArchWiki <https://wiki.archlinux.org/index.php/PKGBUILD>`_.

Manual compilation
------------------

You can compile the source manually without using a custom mirror or the `PKGBUILD` that is shipped.
Simply clone or download the source, and while standing in the cloned folder `./coffeebrewer`, execute:

.. code-block:: console

    nuitka3  --standalone --show-progress coffeebrewer

This requires the `nuitka <https://archlinux.org/packages/community/any/nuitka/>`_ package as well as `python3` to be installed locally.
