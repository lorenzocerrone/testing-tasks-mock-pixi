from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("mock-pixi-tasks")
except PackageNotFoundError:
    __version__ = "uninstalled"