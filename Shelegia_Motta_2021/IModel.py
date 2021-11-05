import abc
from typing import Dict, Final

import matplotlib.axes


class IModel:
    """
    Interface for all models in Shelegia and Motta (2021).
    """
    def __init__(self):
        self.ENTRANT_CHOICES: Final[Dict[str, str]] = {"complement": "C", "substitute": "S", "indifferent": "I"}
        """
        Contains all the possible product choices of the entrant.
        - complement (C)
        - substitute (S)
        - indifferent (I)
        """
        self.INCUMBENT_CHOICES: Final[Dict[str, str]] = {"copy": "©", "refrain": "Ø"}
        """
        Contains all the possible answers of the incumbent to the choice of the entrant.
        - copy (©)
        - refrain (Ø)
        """
        self.DEVELOPMENT_OUTCOME: Final[Dict[str, str]] = {"success": "Y", "failure": "N"}
        """
        Contains all the possible outcomes of the development for the chosen product of the entrant or the merged entity.
        - success (Y)
        - failure (N)
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
    def _calculate_payoffs(self) -> Dict[str, Dict[str, float]]:
        """
        Calculates the payoffs for different market configurations.

        Includes the following payoffs:
        - pi(I):
        - pi(E):
        - CS:
        - W:

        Returns
        -------
        Dict[str, float]
            Includes the mentioned payoffs for different market configurations.
        """
        pass

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
    def get_payoffs(self) -> Dict[str, Dict[str, float]]:
        """
        Returns the payoffs for different market configurations.

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
        The payoffs are specific to the models.

        Returns
        -------
        Dict[str, Dict[str, float]]
            Contains the mentioned payoffs for different market configurations.
        """

    @abc.abstractmethod
    def get_optimal_choice(self, A: float, F: float) -> Dict[str, str]:
        """
        Returns the optimal choice of the entrant and the incumbent based on a pair of assets of the entrant and fixed costs for copying of the incumbent.

        The output dictionary will contain the following details:

        - "entrant": choice of the entrant (possible choices listed in Shelegia_Motta_2021.IModel.IModel.ENTRANT_CHOICES))
        - "incumbent": choice of the incumbent (possible choices listed in Shelegia_Motta_2021.IModel.IModel.INCUMBENT_CHOICES)
        - "development": outcome of the development (possible outcomes listed in Shelegia_Motta_2021.IModel.IModel.DEVELOPMENT_OUTCOME)

        Parameters
        ----------
        A : float
            Assets of the entrant.
        F : float
            Fixed costs for copying of the incumbent.

        Returns
        -------
        Dict[str, str]
            Optimal choice of the entrant, the incumbent and the outcome of the development.
        """
        pass

    @abc.abstractmethod
    def plot_incumbent_best_answers(self, axis: matplotlib.axes.Axes = None, **kwargs) -> matplotlib.axes.Axes:
        """
        Plots the best answers of the incumbent to all possible actions of the entrant.

        Parameters
        ----------
        axis : matplotlib.axes.Axes
            Axis to draw the plot on. (optional)
        **kwargs
            Optional key word arguments for the best answers plot.<br>
            - title: title on top of the plot, instead of the default title.<br>
            - options_legend: If true, an additional legend, explaining the options of the entrant and the incumbent, will be added to the plot.<br>
            - thresholds_legend: If true, an additional legend explaining the thresholds of the entrant and the incumbent will be added to the plot.<br>

        Returns
        -------
        matplotlib.axes.Axes
            Axis containing the plot.
        """
        pass

    @abc.abstractmethod
    def plot_equilibrium(self, axis: matplotlib.axes.Axes = None, **kwargs) -> matplotlib.axes.Axes:
        """
        Plots the equilibrium path based on the choices of the entrant and incumbent.

        Parameters
        ----------
        axis : matplotlib.axes.Axes
            Axis to draw the plot on. (optional)
        **kwargs
            Optional key word arguments for the equilibrium plot.<br>
            - title: title on top of the plot, instead of the default title.<br>
            - options_legend: If true, an additional legend, explaining the options of the entrant and the incumbent, will be added to the plot.<br>
            - thresholds_legend: If true, an additional legend explaining the thresholds of the entrant and the incumbent will be added to the plot.<br>

        Returns
        -------
        matplotlib.axes.Axes
            Axis containing the plot.
        """
        pass

    @abc.abstractmethod
    def plot_payoffs(self, axis: matplotlib.axes.Axes = None) -> matplotlib.axes.Axes:
        """
        Plots the payoffs for different market configurations.

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
