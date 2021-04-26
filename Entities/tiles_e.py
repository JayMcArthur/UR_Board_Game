import enum
import Systems.tiles_s as t


class tiles(enum.Enum):
    # Name = Sprite, Function
    Rosette = [[2, 0], t.rosette]
    Eyes = [[1, 1], t.eyes]
    Twenty = [[0, 1], t.twenty]
    Old = [[2, 1], t.old]
    H_Dots = [[1, 0], t.h_dots]
    Big5 = [[0, 0], t.big]
    Start = [[1, 2], t.start]
    End = [[2, 2], t.end]