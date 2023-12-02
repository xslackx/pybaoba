from dataclasses import dataclass
from utils import *


@dataclass
class Baoba:
    guestOs: str = osLike(ssh=False, fp=None)
    guestCmd: dict = packMan(guestOs)
    guestPacks: str = packIns(guestCmd, ssh=False)
    guestFmt: dict = packFmt(guestPacks, guestOs)
