from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from ..logging.LoggerFactory import LoggerFactory

class Log:
    """Log facade."""

    def log(level: str, message: str) -> None:
        """Log a message with the given level."""
        ...
    def debug(message: str) -> None: ...
    def info(message: str) -> None: ...
    def notice(message: str) -> None: ...
    def warning(message: str) -> None: ...
    def error(message: str) -> None: ...
    def critical(message: str) -> None: ...
    def alert(message: str) -> None: ...
    def emergency(message: str) -> None: ...
    def stack(*channels: List[str]) -> "LoggerFactory":
        """On-demand stack channels."""
        ...
    def channel(channel: str) -> "LoggerFactory": ...
    def build(driver: str, options: dict = {}) -> "LoggerFactory": ...
