import importlib
import sys
import pathlib

# Load .git version before the builtin version
if pathlib.Path('./coffeebrewer/__init__.py').absolute().exists():
	spec = importlib.util.spec_from_file_location("coffeebrewer", "./coffeebrewer/__init__.py")
	coffeebrewer = importlib.util.module_from_spec(spec)
	sys.modules["coffeebrewer"] = coffeebrewer
	spec.loader.exec_module(sys.modules["coffeebrewer"])
else:
	import coffeebrewer

if __name__ == '__main__':
	coffeebrewer.run_as_a_module()
