from __future__ import annotations

from typing import Any


class ParameterDescription:
    """A named default value exposed by a plugin."""

    def __init__(self, name: str, default_value: Any):
        self.name = name
        self.default_value = default_value


def ParamSet(*items: ParameterDescription) -> list[ParameterDescription]:
    """Create the parameter collection used by plugin declarations."""
    return list(items)
