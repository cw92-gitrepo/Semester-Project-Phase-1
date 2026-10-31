"""
Dataclass that holds information regarding the users temperatures at each temperature interval.
Uses a dictonary to create pairs for each interval and and the temperatures at that interval.

Attributes:
    file_name: The name of the users file
    intervals: The list of time intervals for data in the file
    intervaltemps: Key value pairs of interval: [temperature list]
"""

from dataclasses import dataclass, field

@dataclass
class Dataset:
    file_name: str
    intervals: list[float] = field(default_factory=list)
    intervaltemps: dict[float, list[float]] = field(default_factory=dict)

    """
    Override for string output for this dataclass.
    Changes string to be format as 
        |Temperature dataset: {filename}
        |{interval 1} seconds: [temperature list 1]
        |{interval 2} seconds: [temperature list 2]
        |........
    """

    def __str__(self) -> str:
        lines = [f"Temperature dataset: {self.file_name}"]
        for interval in self.intervals:
            temperatures = self.intervaltemps.get(interval, [])
            lines.append(f"{interval:g} seconds: {temperatures}")
        return "\n".join(lines)