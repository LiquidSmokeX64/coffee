import coffeebrewer

# Define the package list in order for lib to source
# which packages will be installed by this profile
__packages__ = ["lighttpd"]

coffeebrewer.storage['installation_session'].add_additional_packages(__packages__)

coffeebrewer.storage['installation_session'].enable_service('lighttpd')
