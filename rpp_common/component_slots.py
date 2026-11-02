"""Shared helpers for describing component slots."""


def parse_component_slot_type(slot_type: str) -> tuple[str, bool]:
    """Return the plugin type and whether a slot accepts multiple values."""
    if slot_type.startswith("List[") and slot_type.endswith("]"):
        return slot_type[5:-1], True
    if slot_type.startswith("Options[") and slot_type.endswith("]"):
        return slot_type[8:-1], True
    return slot_type, False
