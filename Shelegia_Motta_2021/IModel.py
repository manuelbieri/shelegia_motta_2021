import abc
from typing import Dict, Optional

import matplotlib.axes


class IModel:
    @abc.abstractmethod
    def calculate_funding_values(self) -> Dict[str, float]:
        pass

    @abc.abstractmethod
    def calculate_asset_values(self) -> Dict[str, float]:
        pass

    @abc.abstractmethod
    def get_asset_values(self) -> Dict[str, float]:
        pass

    @abc.abstractmethod
    def get_funding_values(self) -> Dict[str, float]:
        pass

    @abc.abstractmethod
    def plot_incumbent_best_answers(self, axis: matplotlib.axes.Axes = None) -> None:
        pass

    @abc.abstractmethod
    def plot_entrant_best_answers(self, axis: matplotlib.axes.Axes = None) -> None:
        pass

    @abc.abstractmethod
    def get_optimal_choice(self, A: float, F: float):
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass
