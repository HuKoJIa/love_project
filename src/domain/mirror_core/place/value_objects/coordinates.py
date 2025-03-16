from dataclasses import dataclass
from src.domain.common.exceptions.value_objects_exceptions import ValueObjectError


@dataclass(eq=False)
class InvalidLattitudeError(ValueObjectError):
    @property
    def title(self) -> str:
        return f'Lattitude must be bettwen -90 and 90, got "{self.value}"'

@dataclass(eq=False)
class InvalidLongitudeError(ValueObjectError):
    @property
    def title(self) -> str:
        return f"Longitude must be between -180 and 180, got: {self.value}"





@dataclass(frozen=True)
class Coordinates:
    latitude: float
    longitude: float 

    def __post_init__(self):
        if not (-90 <= self.latitude <= 90):
            raise InvalidLattitudeError(self.latitude, "Latitude")
        if not(-180 <= self.longitude <= 180):
            raise InvalidLongitudeError(self.longitude, "Longitude")