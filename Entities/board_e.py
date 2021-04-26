



class Board:
    def __init__(self):
        self.pR = [
            [4, 3,  2,  1,  0, 8, 9, 10, 11, 12, 13, 14, 6, 7, 15, 23, 22, 14, 13, 12, 11, 10, 9, 8, 5],
            [20, 19, 18, 17, 16, 8, 9, 10, 11, 12, 13, 14, 22, 23, 15, 7, 6, 14, 13, 12, 11, 10, 9, 8, 21]
        ]
        self.board = [
            [[0],[0],[0],[0],[7],[0],[0],[0]] +
            [[0],[0],[0],[0],[0],[0],[0],[0]] +
            [[0],[0],[0],[0],[7],[0],[0],[0]]
        ]

        sprites = [
            rosette, eyes, Big5, eyes, start, end, rosette, Set,
            H, Big5, s4of5, rosette, Big5, s4of5, eyes, Big5,
            rosette, eyes, Big5, eyes, start, end, rosette, Set
        ]
