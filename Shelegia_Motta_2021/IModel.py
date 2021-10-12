import abc
from typing import Dict

import matplotlib.axes


class IModel:
    """
    Interface for all models in Shelegia and Motta (2021).
    """
    @abc.abstractmethod
    def _calculate_copying_fixed_costs_values(self) -> Dict[str, float]:
        """
        Calculates the thresholds for the fixed costs for copying of the incumbent.

        Number and type of the thresholds will be specific to the model.

        :return: dict including the thresholds for the fixed costs for copying of the incumbent.
        """
        pass

    @abc.abstractmethod
    def _calculate_asset_values(self) -> Dict[str, float]:
        """
        Calculates the thresholds for the assets of the entrant.

        Number and type of the thresholds will be specific to the model.

        :return: dict including the thresholds for the assets of the entrant.
        """
        pass

    @abc.abstractmethod
    def _calculate_welfare(self) -> Dict[str, Dict[str, float]]:
        """
        Calculates the utility values for different market configurations.

        Includes the following utilities:
        - pi(I):
        - pi(E):
        - CS:
        - W:

        :return: dict containing the mentioned utilities for different market configurations.
        """

    @abc.abstractmethod
    def get_asset_values(self) -> Dict[str, float]:
        """
        Returns the asset thresholds of the entrant.

        Number and type of the thresholds will be specific to the model.

        :return: dict including the thresholds for the assets of the entrant.
        """
        pass

    @abc.abstractmethod
    def get_copying_fixed_costs_values(self) -> Dict[str, float]:
        """
        Returns the fixed costs for copying thresholds of the incumbent.

        Number and type of the thresholds will be specific to the model.

        :return: dict including the thresholds for the fixed costs for copying of the incumbent.
        """
        pass

    @abc.abstractmethod
    def get_utility_values(self) -> Dict[str, Dict[str, float]]:
        """
        Returns the utility values for different market configurations.

        Includes the following utilities:
        TODO Add explanations for the different types
        - pi(I):
        - pi(E):
        - CS:
        - W:

        :return: dict containing the mentioned utilities for different market configurations.
        """

    @abc.abstractmethod
    def plot_incumbent_best_answers(self, axis: matplotlib.axes.Axes = None) -> None:
        """
        Plots the best answers of the incumbent to all possible actions of the entrant.

        :param axis: to plot the figure to (optional)
        :return:
        """
        pass

    @abc.abstractmethod
    def plot_equilibrium(self, axis: matplotlib.axes.Axes = None) -> None:
        """
        Plots the equilibrium path based on the choices of the entrant and incumbent.

        :param axis: to plot the figure to (optional)
        :return:
        """
        pass

    @abc.abstractmethod
    def plot_utilities(self, axis: matplotlib.axes.Axes = None) -> None:
        """
        Plots the utilities for different market configurations.

        :param axis: to plot the figure to (optional)
        :return:
        """
        pass

    @abc.abstractmethod
    def get_optimal_choice(self, A: float, F: float):
        """
        Return the optimal choice of the entrant and the incumbent based on a pair of assets of the entrant ann fixed costs for copying of the incumbent.

        :param A: assets of the entrant.
        :param F: fixed costs for copying of the incumbent.
        :return: optimal choice of the entrant and the incumbent.
        """
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        """
        Returns a string representation of the object.

        Includes:
        - Asset thresholds of the entrant
        - fixed costs for copying thresholds of the incumbent.
        - Utilities for different market configurations

        :return: string representation of the object.
        """
        pass
