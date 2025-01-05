from typing import Optional, List
from pydantic import BaseModel, Field


class ShipMount(BaseModel):
    symbol: str
    name: str
    description: Optional[str] = None
    strength: Optional[int] = None
    deposits: Optional[List[str]] = None
    requirements: Optional[dict] = None


class ShipCargo(BaseModel):
    capacity: int
    units: int
    inventory: List[dict]


class ShipNav(BaseModel):
    system_symbol: str = Field(..., alias="systemSymbol")
    waypoint_symbol: str = Field(..., alias="waypointSymbol")
    route: dict
    status: str
    flight_mode: str = Field(..., alias="flightMode")


class Ship(BaseModel):
    symbol: str
    registration: dict
    nav: ShipNav
    cargo: ShipCargo
    fuel: dict
    mounts: List[ShipMount]


class MiningResult(BaseModel):
    extraction: dict
    cooldown: dict
    cargo: ShipCargo
    events: Optional[List[dict]] = None 