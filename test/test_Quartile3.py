# -*- coding: utf-8 -*-
import pytest

from Quartile3 import Quartile3
from src.Types import DataType


ResultType = list[str]


class TestQuartile3:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, ResultType]:
        data = {
            'Иванов Иван Иванович': [
                ('математика', 67),
                ('литература', 100),
                ('программирование', 91)
            ], 'Петров Петр Петрович': [
                ('математика', 78),
                ('химия', 87),
                ('социология', 61)
            ], 'Денисов Валерий Андреевич': [
                ('математика', 80),
                ('физика', 87),
                ('французский', 90)
            ], 'Кравченя Павел Дмитриевич': [
                ('информатика', 87),
                ('математика', 92),
                ('английский', 100)
            ]
        }

        result = ['Денисов Валерий Андреевич']

        return data, result

    def test_init(self, input_data: tuple[DataType, ResultType]):
        quart = Quartile3(input_data[0])

        assert quart.data == input_data[0]

    def test_calc(self, input_data: tuple[DataType, ResultType]):
        result = Quartile3(input_data[0]).calc()

        assert result == input_data[1]
