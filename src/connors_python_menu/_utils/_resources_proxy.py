from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `connors_python_menu.resources` module.

    This is used so that we can lazily import `connors_python_menu.resources` only when
    needed *and* so that users can just import `connors_python_menu` and reference `connors_python_menu.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("connors_python_menu.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
