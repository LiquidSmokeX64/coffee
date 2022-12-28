import coffeebrewer

# Define the package list in order for lib to source
# which packages will be installed by this profile
__packages__ = ["postgresql"]

coffeebrewer.storage['installation_session'].add_additional_packages(__packages__)

coffeebrewer.storage['installation_session'].arch_chroot("initdb -D /var/lib/postgres/data", run_as='postgres')

coffeebrewer.storage['installation_session'].enable_service('postgresql')
