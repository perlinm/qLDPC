import pkg_resources

from . import abstract, codes

__version__ = pkg_resources.get_distribution("qldpc").version

__all__ = [
    "__version__",
    "abstract",
    "codes",
]
