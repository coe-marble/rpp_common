"""ROS-independent lifecycle result values."""

from dataclasses import dataclass
from typing import Generic, TypeVar


State = TypeVar("State")


class LifecycleError(RuntimeError):
    """A plugin lifecycle callback reported failure."""


@dataclass(frozen=True)
class CallbackResult:
    success: bool = True
    message: str = ""

    @classmethod
    def failure(cls, message: str) -> "CallbackResult":
        return cls(success=False, message=message)

    def require_success(self, operation: str) -> None:
        if not self.success:
            raise LifecycleError(f"{operation} failed: {self.message}")


@dataclass(frozen=True)
class DeactivationResult(Generic[State]):
    result: CallbackResult = CallbackResult()
    state: State | None = None
