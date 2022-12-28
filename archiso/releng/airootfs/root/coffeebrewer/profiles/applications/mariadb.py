import coffeebrewer

# Define the package list in order for lib to source
# which packages will be installed by this profile
__packages__ = ["mariadb"]

coffeebrewer.storage['installation_session'].add_additional_packages(__packages__)

coffeebrewer.storage['installation_session'].arch_chroot("mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql")

coffeebrewer.storage['installation_session'].enable_service('mariadb')
