from dataclasses import dataclass
from utils import *


@dataclass
class Baoba:
    guestOs: str = osLike()
    guestCmd: dict = packMan(guestOs)
    guestPacks: str = packIns(guestCmd)
    guestFmt: dict = packFmt(guestPacks, guestOs)
