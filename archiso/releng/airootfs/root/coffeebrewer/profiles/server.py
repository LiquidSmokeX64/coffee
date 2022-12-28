# Used to select various server application profiles on top of a minimal installation.

import logging
from typing import Any, TYPE_CHECKING

import coffeebrewer
from coffeebrewer import Menu
from coffeebrewer.lib.menu.menu import MenuSelectionType

if TYPE_CHECKING:
	_: Any

is_top_level_profile = True

__description__ = str(_('Provides a selection of various server packages to install and enable, e.g. httpd, nginx, mariadb'))

available_servers = [
	"cockpit",
	"docker",
	"httpd",
	"lighttpd",
	"mariadb",
	"nginx",
	"postgresql",
	"sshd",
	"tomcat",
]


def _prep_function(*args, **kwargs):
	"""
	Magic function called by the importing installer
	before continuing any further.
	"""
	choice = Menu(str(_(
		'Choose which servers to install, if none then a minimal installation will be done')),
		available_servers,
		preset_values=kwargs['servers'],
		multi=True
	).run()

	if choice.type_ != MenuSelectionType.Selection:
		return False

	if choice.value:
		coffeebrewer.storage['_selected_servers'] = choice.value
		return True

	return False


if __name__ == 'server':
	"""
	This "profile" is a meta-profile.
	"""
	coffeebrewer.log('Now installing the selected servers.', level=logging.INFO)
	coffeebrewer.log(coffeebrewer.storage['_selected_servers'], level=logging.DEBUG)
	for server in coffeebrewer.storage['_selected_servers']:
		coffeebrewer.log(f'Installing {server} ...', level=logging.INFO)
		app = coffeebrewer.Application(coffeebrewer.storage['installation_session'], server)
		app.install()

	coffeebrewer.log('If your selections included multiple servers with the same port, you may have to reconfigure them.', fg="yellow", level=logging.INFO)
