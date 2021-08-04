# -*- coding: utf-8 -*-
"""
module: chess

rows = ranks
colums = files
"""

# standard imports
from enum import Enum, IntEnum, unique, auto
from collections import OrderedDict

# external imports

# local imports


@unique
class Color(Enum):
    """
    class: Color
    """
    WHITE = auto()
    BLACK = auto()


@unique
class PieceType(Enum):
    """
    class: PieceType
    """
    KING = auto()
    QUEEN = auto()
    BISHOP = auto()
    KNIGHT = auto()
    ROOK = auto()
    PAWN = auto()

INIT = [PieceType.ROOK, PieceType.KNIGHT, PieceType.BISHOP, PieceType.QUEEN,
        PieceType.KING, PieceType.BISHOP, PieceType.KNIGHT, PieceType.ROOK]

@unique
class Rank(IntEnum):
    """
    class: Rank
    """
    _1 = 0
    _2 = 1
    _3 = 2
    _4 = 3
    _5 = 4
    _6 = 5
    _7 = 6
    _8 = 7


@unique
class File(IntEnum):
    """
    class: File
    """
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5
    g = 6
    h = 7


@unique
class Movement(Enum):
    """
    class: Movement
    """
    LEFT = auto()  # file <
    RIGHT = auto()  # file >
    UP = auto()  # rank >
    DOWN = auto()  # rank <
    NE = auto()  # rank > + file >
    SE = auto()  # rank < + file >
    NW = auto()  # rank > + file <
    SW = auto()  # rank < + file <


class ChessPiece:
    """
    class: ChessPiece
    """

    def __init__(self, piece_type, color):
        """
        function: __init__
        """
        self.piece_type = piece_type
        self.color = color

    def __str__(self):
        return ":".join([str(self.piece_type.name), str(self.color.name)])

    def __repr__(self):
        return ":".join([str(self.piece_type.name), str(self.color.name)])


class BoardSquare:
    """
    class: BoardSquare
    """

    def __init__(self, rank, file, color, piece=None):
        """
        function: __init__
        """
        self._rank = rank
        self._file = file
        self._color = color
        self._piece = piece

    def __repr__(self):
        return ",".join([str(self._rank.value+1), str(self._file.name), str(self._color.name),
                         str(self._piece) if self._piece else "Empty"])

    def __str__(self):
        return ",".join([str(self._rank.value+1), str(self._file.name), str(self._color.name),
                         str(self._piece) if self._piece else "Empty"])

class ChessBoard:
    """
    class: ChessBoard
    """

    def __init__(self):
        """
        function: __init__
        """
        # self._files = {_x: None for _x in enumerate(File)}
        # self._ranks = OrderedDict()
        self._board = OrderedDict()
        _color = Color.BLACK
        for _i, _r in enumerate(Rank):
            self._board[_r] = OrderedDict()
            for _file in enumerate(File):
                if (_r.value+1) % 2 == 1:
                    _color = Color.BLACK
                else:
                    _color = Color.WHITE
                for _j, _f in enumerate(File):
                    _sq = BoardSquare(_r, _f, _color)
                    self._board[_r][_f] = _sq
                    if _color == Color.BLACK:
                        _color = Color.WHITE
                    else:
                        _color = Color.BLACK
        # color the squares
        # start on black, rank 1, file a
        # continue, exhausting all files in rank until done w _ranks
        # alternate colors


        # build map of adjacencies
        self._adj_left = []
        for _i, _r in enumerate(Rank):
            left_rank = None
            for _j, _f in enumerate(File):
                if left_rank:
                    self._adj_left.append(
                        (self._board[left_rank][_f], self._board[_r][_f]))
                left_rank = _r

        self._adj_right = []
        for _i, _r in reversed([_x for _x in enumerate(Rank)]):
            right_rank = None
            for _j, _f in enumerate(File):
                if right_rank:
                    self._adj_left.append(
                        (self._board[right_rank][_f], self._board[_r][_f]))
                right_rank = _r

        self._adj_top = []
        self._adj_bottom = []
        self._adj_ne = []
        self._adj_se = []
        self._adj_nw = []
        self._adj_sw = []

        # white pieces
        _r = Rank._1
        for _i, _file in enumerate(File):
            self._board[_r][_file]._piece = ChessPiece(INIT[_file.value], Color.WHITE)
        _r = Rank._2
        for _i, _file in enumerate(File):
            self._board[_r][_file]._piece = ChessPiece(PieceType.PAWN, Color.WHITE)
        _r = Rank._7
        for _i, _file in enumerate(File):
            self._board[_r][_file]._piece = ChessPiece(PieceType.PAWN, Color.BLACK)
        _r = Rank._8
        for _i, _file in enumerate(File):
            self._board[_r][_file]._piece = ChessPiece(INIT[_file.value], Color.BLACK)

    def readout_board(self):
        for _i, _r in enumerate(Rank):
            for _j, _f in enumerate(File):
                print(self._board[_r][_f])

if __name__ == "__main__":
    # for x in enumerate(File):
    #     print(x)
    # for x in enumerate(Rank):
    #     print(x)
    #
    # for x in enumerate(Rank):
    #     for y in enumerate(File):
    #         print(x, y)

    _board = ChessBoard()
    # print(ChessPiece(PieceType.BISHOP, Color.WHITE))
    # print(BoardSquare(Rank._2, File.a, Color.WHITE))
    # print(BoardSquare(Rank._2, File.a, Color.WHITE, piece=ChessPiece(PieceType.BISHOP, Color.WHITE)))
    _board.readout_board()
