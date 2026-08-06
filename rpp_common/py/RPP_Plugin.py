from __future__ import annotations

import json
from abc import ABC

import numpy as np


class RPP_Plugin(ABC):
    param_description = []
    log_description = []
    input_description = []
    output_description = []

    def reset(self):
        pass

    def initialize(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def parse_positional_args(self, args):
        if len(args) == 0:
            return {}
        i = 0
        parsed = {}
        while True:
            if i >= len(args):
                break
            if isinstance(args[i], str):
                if i + 1 < len(args):
                    parsed[args[i]] = args[i + 1]
                else:
                    parsed[args[i]] = None
            i += 2
        return parsed

    @classmethod
    def parse_dict(cls, d):
        from types import SimpleNamespace

        if d is None:
            return None
        if isinstance(d, dict):
            return SimpleNamespace(**{k: cls.parse_dict(v) for k, v in d.items()})
        if isinstance(d, list):
            return [cls.parse_dict(item) for item in d]
        if isinstance(d, float):
            if np.isinf(d):
                return d
            if np.isclose(d, np.round(d)):
                return int(d)
            return d
        return d

    @property
    def is_configured(self):
        return self._is_configured

    def data_as_json(self):
        return json.dumps(self.data.__dict__)