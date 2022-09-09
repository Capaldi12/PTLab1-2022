# -*- coding: utf-8 -*-
from operator import itemgetter
from Types import DataType


class Quartile3:
    def __init__(self, data: DataType):
        self.data = data

    @staticmethod
    def get_rating(pair):
        student, scores = pair

        return student, sum(score for _, score in scores)

    def calc(self) -> list[str]:
        students = list(sorted(map(self.get_rating, self.data.items()),
                               key=itemgetter(1), reverse=True))

        fifty = len(students) // 2
        quarter = fifty // 2

        return [name for name, _ in students[fifty:fifty+quarter]]
