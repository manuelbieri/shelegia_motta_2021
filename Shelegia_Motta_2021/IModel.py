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

        Returns
        -------
        Dict[str, float]
            Includes the thresholds for the fixed costs for copying of the incumbent.
        """
        pass

    @abc.abstractmethod
    def _calculate_asset_values(self) -> Dict[str, float]:
        """
        Calculates the thresholds for the assets of the entrant.

        Number and type of the thresholds will be specific to the model.

        Returns
        -------
        Dict[str, float]
            Includes the thresholds for the assets of the entrant.
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

        Returns
        -------
        Dict[str, float]
            Includes the mentioned utilities for different market configurations.
        """

    @abc.abstractmethod
    def get_asset_values(self) -> Dict[str, float]:
        """
        Returns the asset thresholds of the entrant.

        Number and type of the thresholds will be specific to the model.

        Returns
        -------
        Dict[str, float]
            Includes the thresholds for the assets of the entrant.
        """
        pass

    @abc.abstractmethod
    def get_copying_fixed_costs_values(self) -> Dict[str, float]:
        """
        Returns the fixed costs for copying thresholds of the incumbent.

        Number and type of the thresholds will be specific to the model.

        Returns
        -------
        Dict[str, float]
            Includes the thresholds for the fixed costs for copying of the incumbent.
        """
        pass

    @abc.abstractmethod
    def get_utility_values(self) -> Dict[str, Dict[str, float]]:
        """
        Returns the utility values for different market configurations.

        A market configuration can include:
        - $I_P$ : Primary product sold by the incumbent.
        - $I_C$ : Complementary product to $I_P$ potentially sold by the incumbent, which is copied from $E_C$.
        - $E_P$ : Perfect substitute to $I_P$ potentially sold by the entrant.
        - $E_C$ : Complementary product to $I_P$ currently sold by the entrant
        - $\\tilde{E}_C$ : Complementary product to $I_P$ potentially sold by the entrant.
        <br>

        | Market Config. | $\pi(I)$ | $\pi(E)$ | CS | W |
        |-----------------------|:--------:|:--------:|:--:|:-:|
        | $I_P$ ; $E_C$         | N.A. | N.A. | N.A. | N.A. |
        | $I_P + I_C$ ; $E_C$   | N.A. | N.A. | N.A. | N.A. |
        | $I_P$ ; $E_P + E_C$   | N.A. | N.A. | N.A. | N.A. |
        | $I_P + I_C$ ; $E_P + E_C$ | N.A. | N.A. | N.A. | N.A. |
        | $I_P$ ; $E_C + \\tilde{E}_C$ | N.A. | N.A. | N.A. | N.A. |
        | $I_P + I_C$ ; $E_C + \\tilde{E}_C$ | N.A. | N.A. | N.A. | N.A. |
        <br>
        The utility values are specific to the models.

        Returns
        -------
        Dict[str, Dict[str, float]]
            Contains the mentioned utilities for different market configurations.
        """

    @abc.abstractmethod
    def plot_incumbent_best_answers(self, axis: matplotlib.axes.Axes = None) -> matplotlib.axes.Axes:
        """
        Plots the best answers of the incumbent to all possible actions of the entrant.

        Parameters
        ----------
        axis : matplotlib.axes.Axes
            Axis to draw the plot on. (optional)

        Returns
        -------
        matplotlib.axes.Axes
            Axis containing the plot.
        """
        pass

    @abc.abstractmethod
    def plot_equilibrium(self, axis: matplotlib.axes.Axes = None) -> matplotlib.axes.Axes:
        """
        Plots the equilibrium path based on the choices of the entrant and incumbent.

        Parameters
        ----------
        axis : matplotlib.axes.Axes
            Axis to draw the plot on. (optional)

        Returns
        -------
        matplotlib.axes.Axes
            Axis containing the plot.
        """
        pass

    @abc.abstractmethod
    def plot_utilities(self, axis: matplotlib.axes.Axes = None) -> matplotlib.axes.Axes:
        """
        Plots the utilities for different market configurations.

        Parameters
        ----------
        axis : matplotlib.axes.Axes
            Axis to draw the plot on. (optional)

        Returns
        -------
        matplotlib.axes.Axes
            Axis containing the plot.
        """
        pass

    @abc.abstractmethod
    def get_optimal_choice(self, A: float, F: float):
        """
        Return the optimal choice of the entrant and the incumbent based on a pair of assets of the entrant ann fixed costs for copying of the incumbent.

        Parameters
        ----------
        A : float
            Assets of the entrant.
        F : float
            Fixed costs for copying of the incumbent.

        Returns
        -------
        Optimal choice of the entrant and the incumbent.
        """
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        """
        Returns a string representation of the object.

        Includes:
        - Asset thresholds of the entrant
        - Fixed costs for copying thresholds of the incumbent.
        - Utilities for different market configurations

        Returns
        -------
        String
            String representation of the object.
        """
        pass
