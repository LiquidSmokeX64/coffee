import time

import coffeebrewer

coffeebrewer.storage['UPSTREAM_URL'] = 'https://archlinux.life/profiles'
coffeebrewer.storage['PROFILE_DB'] = 'index.json'

for name, info in coffeebrewer.list_profiles().items():
	# Tailored means it's a match for this machine
	# based on it's MAC address (or some other criteria
	# that fits the requirements for this machine specifically).
	if info['tailored']:
		print(f'Found a tailored profile for this machine called: "{name}".')
		print('Starting install in:')
		for i in range(10, 0, -1):
			print(f'{i}...')
			time.sleep(1)

		profile = coffeebrewer.Profile(None, info['path'])
		profile.install()
		break
