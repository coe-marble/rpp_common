from __future__ import annotations

from dataclasses import dataclass
from types import SimpleNamespace
from typing import Any, Callable


@dataclass
class ParameterDescription:
    name: str
    default_value: Any = 0
    type: Any = None
    description: str = ""
    is_valid: bool = True
    serialize: bool = True

    def __getitem__(self, key):
        if key == "Name":
            return self.name
        if key == "DefaultValue":
            return self.default_value
        if key == "Type":
            return self.type
        if key == "Description":
            return self.description
        if key == "IsValid":
            return self.is_valid
        if key == "Serialize":
            return self.serialize
        raise KeyError(f"Key {key} not found in ParameterDescription")


ParamDescriptor = ParameterDescription
Parameter = ParameterDescription


def ParamSet(*items: ParameterDescription) -> list[ParameterDescription]:
    return list(items)


@dataclass
class LogEntry:
    name: str
    eval_fn: Callable | str | None = None

    def __post_init__(self):
        if self.eval_fn is None:
            self.eval_fn = f"@(x) x.{self.name}"


@dataclass
class RegistryInfo:
    name: str
    visible: bool


@dataclass
class IOArgument:
    name: str
    dim: Any


class DataModel(SimpleNamespace):
    pass