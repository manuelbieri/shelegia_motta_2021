from typing import Dict, List, Tuple, Literal, Final

import matplotlib.axes
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"

from numpy import arange

import Shelegia_Motta_2021


class BaseModel(Shelegia_Motta_2021.IModel):
    """
    There are two players in our base model: The Incumbent, which sells the primary product, denoted by Ip, and a start-up, called the Entrant, which sells a product Ec complementary to Ip. (One may think of Ip as a platform, and Ec as a service or product which can be accessed through the platform.) We are interested in studying the choice of E between developing a substitute to Ip, denoted by Ep, or another complement to Ip, denoted by Ẽc and the choice of I between copying E’s original complementary product Ec by creating a perfect substitute Ic, or not. Since E may not have enough assets to cover the development cost of its second product, copying its current product will affect the entrant’s ability to obtain funding for the development. We shall show that the incumbent has a strategic incentive to copy when the entrant plans to compete, and to abstain from copying when it plans to create another complement.
    """

    TOLERANCE: Final[float] = 10 ** (-8)
    """Tolerance for the comparison of two floating numbers."""

    def __init__(self, u: float = 1, B: float = 0.5, small_delta: float = 0.5, delta: float = 0.51,
                 K: float = 0.2) -> None:
        """
        Initializes a valid BaseModel object.

        The following preconditions have to be satisfied:
        - (A1b) $\delta$ / 2 < $\Delta$ < 3 * $\delta$ / 2
        - (A2) K < $\delta$ / 2

        Parameters
        ----------
        u : float
            Utility gained from consuming the primary product.
        B : float
            Minimal difference between the return in case of a success and the return in case of failure of E. B is called the private benefit of the entrant in case of failure.
        small_delta : float
            ($\delta$) Additional utility gained from a complement combined with a primary product.
        delta : float
            ($\Delta$) Additional utility gained from the substitute of the entrant compared to the primary product of the incumbent.
        K : float
            Investment costs for the entrant to develop a second product.
        """
        super(BaseModel, self).__init__()
        assert small_delta / 2 < delta < 3 * small_delta / 2, "(A1b) not satisfied."
        assert K < small_delta / 2, "(A2) not satisfied."
        self._u: float = u
        self._B: float = B
        self._small_delta: float = small_delta
        self._delta: float = delta
        self._K: float = K
        self._copying_fixed_costs: Dict[str, float] = self._calculate_copying_fixed_costs_values()
        self._assets: Dict[str, float] = self._calculate_asset_values()
        self._payoffs: Dict[str, Dict[str, float]] = self._calculate_payoffs()

    def _calculate_payoffs(self) -> Dict[str, Dict[str, float]]:
        """
        Calculates the payoffs for different market configurations with the formulas given in the paper.

        The formulas are tabulated in BaseModel.get_payoffs.

        Returns
        -------
        Dict[str, Dict[str, float]]
            Contains the mentioned payoffs for different market configurations.
        """
        return {'basic': {'pi(I)': self._u + self._small_delta / 2,
                          'pi(E)': self._small_delta / 2,
                          'CS': 0,
                          'W': self._u + self._small_delta
                          },
                'I(C)': {'pi(I)': self._u + self._small_delta,
                         'pi(E)': 0,
                         'CS': 0,
                         'W': self._u + self._small_delta
                         },
                'E(P)': {'pi(I)': 0,
                         'pi(E)': self._delta + self._small_delta,
                         'CS': self._u,
                         'W': self._u + self._delta + self._small_delta
                         },
                'I(C)E(P)': {'pi(I)': 0,
                             'pi(E)': self._delta,
                             'CS': self._u + self._small_delta,
                             'W': self._u + self._delta + self._small_delta
                             },
                'E(C)': {'pi(I)': self._u + self._small_delta,
                         'pi(E)': self._small_delta,
                         'CS': 0,
                         'W': self._u + 2 * self._small_delta
                         },
                'I(C)E(C)': {'pi(I)': self._u + 3 / 2 * self._small_delta,
                             'pi(E)': self._small_delta / 2,
                             'CS': 0,
                             'W': self._u + 2 * self._small_delta
                             }
                }

    def _calculate_copying_fixed_costs_values(self) -> Dict[str, float]:
        """
        Calculates the thresholds for the fixed costs of copying for the incumbent.

        The formulas are tabulated in BaseModel.get_copying_fixed_costs_values.

        Returns
        -------
        Dict[str, float]
            Includes the thresholds for the fixed costs for copying of the incumbent.
        """
        return {'F(YY)s': self._small_delta / 2,
                'F(YN)s': self._u + self._small_delta * 3 / 2,
                'F(YY)c': self._small_delta,
                'F(YN)c': self._small_delta / 2}

    def _calculate_asset_values(self) -> Dict[str, float]:
        """
        Calculates the thresholds for the assets of the entrant.

        The formulas are tabulated in BaseModel.get_asset_values.

        Returns
        -------
        Dict[str, float]
            Includes the thresholds for the assets of the entrant.
        """
        return {'A_s': self._B - (self._delta + 3 / 2 * self._small_delta - self._K),
                'A_c': self._B - (3 / 2 * self._small_delta - self._K),
                'A-s': self._B - (self._delta - self._K),
                'A-c': self._B - (1 / 2 * self._small_delta - self._K)}

    def get_asset_values(self) -> Dict[str, float]:
        """
        Returns the asset thresholds of the entrant.

        | Threshold $\:\:\:\:\:$ | Name $\:\:\:\:\:$ | Formula $\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$ |
        |----------------|:----------|:-----------|
        | $A_S$ | A_s | $(2)\: B + K - \Delta - 3\delta/2$ |
        | $A_C$ | A_c | $(3)\: B + K - 3\delta/2$ |
        | $\overline{A}_S$ | A-s | $(4)\: B + K - \Delta$ |
        | $\overline{A}_C$ | A-c | $(5)\: B + K - \delta/2$ |
        <br>
        Returns
        -------
        Dict[str, float]
            Includes the thresholds for the assets of the entrant.
        """
        return self._assets

    def get_copying_fixed_costs_values(self) -> Dict[str, float]:
        """
        Returns the fixed costs for copying thresholds of the incumbent.

        | Threshold $\:\:\:\:\:$ | Name $\:\:\:\:\:$ | Formula $\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$ |
        |----------|:-------|:--------|
        | $F^{YY}_S$ | F(YY)s | $(6)\: \delta/2$ |
        | $F^{YN}_S$ | F(YN)s | $(6)\: u + 3\delta/2$ |
        | $F^{YY}_C$ | F(YY)c | $(6)\: \delta$ |
        | $F^{YN}_C$ | F(YN)c | $(6)\: \delta/2$ |
        <br>
        Returns
        -------
        Dict[str, float]
            Includes the thresholds for the fixed costs for copying of the incumbent.
        """
        return self._copying_fixed_costs

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

        | Market Config. $\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$ | $\pi(I) \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$ | $\pi(E) \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$ | CS $\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$ | W $\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$ |
        |-----------------------|:--------|:--------|:--|:-|
        | $I_P$ ; $E_C$         | $u + \delta/2$ | $\delta/2$ | 0 | $u + \delta$ |
        | $I_P + I_C$ ; $E_C$   | $u + \delta$ | 0 | 0 | $u + \delta$ |
        | $I_P$ ; $E_P + E_C$   | 0 | $\Delta + \delta$ | $u$ | $u + \Delta + \delta$ |
        | $I_P + I_C$ ; $E_P + E_C$ | 0 | $\Delta$ | $u + \delta$ | $u + \Delta + \delta$ |
        | $I_P$ ; $E_C + \\tilde{E}_C$ | $u + \delta$ | $\delta$ | 0 | $u + 2\delta$ |
        | $I_P + I_C$ ; $E_C + \\tilde{E}_C$ | $u + 3\delta/2$ | $\delta/2$ | 0 | $u + 2\delta$ |
        <br>

        Returns
        -------
        Dict[str, Dict[str, float]]
            Contains the mentioned payoffs for different market configurations.
        """
        return self._payoffs

    def get_optimal_choice(self, A: float, F: float) -> Dict[str, str]:
        result: Dict[str, str] = {"entrant": "", "incumbent": "", "development": ""}
        if self._copying_fixed_costs["F(YN)c"] <= F <= self._copying_fixed_costs["F(YN)s"] and A < self._assets["A-s"]:
            result.update({"entrant": self.ENTRANT_CHOICES["complement"]})
            result.update({"incumbent": self.INCUMBENT_CHOICES["refrain"]})
            result.update({"development": self.DEVELOPMENT_OUTCOME["success"]})
        elif F <= self._copying_fixed_costs["F(YN)c"] and A < self._assets["A-s"]:
            result.update({"entrant": self.ENTRANT_CHOICES["indifferent"]})
            result.update({"incumbent": self.INCUMBENT_CHOICES["copy"]})
            result.update({"development": self.DEVELOPMENT_OUTCOME["failure"]})
        else:
            result.update({"entrant": self.ENTRANT_CHOICES["substitute"]})
            result.update({"development": self.DEVELOPMENT_OUTCOME["success"]})
            if F <= self._copying_fixed_costs["F(YY)s"]:
                result.update({"incumbent": self.INCUMBENT_CHOICES["copy"]})
            else:
                result.update({"incumbent": self.INCUMBENT_CHOICES["refrain"]})
        return result

    def _plot(self, coordinates: List[List[Tuple[float, float]]], labels: List[str],
              axis: matplotlib.axes.Axes = None, **kwargs) -> matplotlib.axes.Axes:
        """
        Plots polygons containing the optimal choices and answers into a coordinate system.

        Parameters
        ----------
        coordinates : List[List[Tuple[float, float]]]
            List of all polygons (list of coordinates) to plot.
        labels: List[str]
            List containing all the labels for the polygons.
        axis : matplotlib.axes.Axes
            Axis to draw the plot on. (optional)
        **kwargs
            Optional key word arguments for the plots.<br>
            - title: title of the plot.<br>
            - xlabel: label for the x - axis.<br>
            - ylabel: label for the y - axis.<br>

        Returns
        -------
        Axis containing the plot.
        """
        if axis is None:
            figure, axis = plt.subplots()
        self._draw_thresholds(axis)

        for i, coordinates in enumerate(coordinates):
            poly = plt.Polygon(coordinates, ec="k", color=self._get_color(i), label=labels[i])
            axis.add_patch(poly)

        axis.legend(bbox_to_anchor=(1.3, 1), loc="upper left")
        additional_legend: str = self._create_additional_legend(options_legend=kwargs.get('options_legend', False), thresholds_legend=kwargs.get('thresholds_legend', False))
        if additional_legend != "":
            axis.text(-0.1, -0.6, additional_legend, verticalalignment='top', linespacing=1)
        BaseModel._set_axis_labels(axis, title=kwargs.get('title', ''),
                                   x_label=kwargs.get('xlabel', 'Assets of the entrant'),
                                   y_label=kwargs.get('ylabel', 'Fixed costs of copying for the incumbent'))
        BaseModel._set_axis(axis)
        return axis

    def plot_incumbent_best_answers(self, axis: matplotlib.axes.Axes = None, **kwargs) -> matplotlib.axes.Axes:
        poly_coordinates: List[List[Tuple[float, float]]] = self._get_incumbent_best_answer_coordinates()
        poly_labels: List[str] = self._get_incumbent_best_answer_labels()
        axis: matplotlib.axes.Axes = self._plot(
            title="Best Answers of the incumbent to the choices of the entrant",
            coordinates=poly_coordinates, labels=poly_labels, axis=axis, **kwargs)
        return axis

    def _create_choice_answer_label(self, entrant: Literal["complement", "substitute", "indifferent"],
                                    incumbent: Literal["copy", "refrain"],
                                    development: Literal["success", "failure"],
                                    kill_zone: bool = False) -> str:
        return self.ENTRANT_CHOICES[entrant] + " $\\rightarrow$ " + self.INCUMBENT_CHOICES[
            incumbent] + " $\\rightarrow$ " + self.DEVELOPMENT_OUTCOME[development] + (
                   "\n(Kill Zone)" if kill_zone else "")

    def _get_incumbent_best_answer_labels(self) -> List[str]:
        """
        Returns a list containing the labels for the squares in the plot of the best answers of the incumbent to the choice of the entrant.

        For the order of the labels refer to the file resources/dev_notes.md.

        Returns
        -------
        List containing the labels for the squares in the plot of the best answers of the incumbent to the choice of the entrant.
        """
        return [
            # Square 1
            self._create_choice_answer_label(entrant="substitute", incumbent="copy", development="failure") + " \n" +
            self._create_choice_answer_label(entrant="complement", incumbent="copy", development="failure"),
            # Square 2
            self._create_choice_answer_label(entrant="substitute", incumbent="copy", development="success") + " \n" +
            self._create_choice_answer_label(entrant="complement", incumbent="copy", development="failure"),
            # Square 3
            self._create_choice_answer_label(entrant="substitute", incumbent="copy", development="success") + " \n" +
            self._create_choice_answer_label(entrant="complement", incumbent="copy", development="success"),
            # Square 4
            self._create_choice_answer_label(entrant="substitute", incumbent="copy", development="failure") + " \n" +
            self._create_choice_answer_label(entrant="complement", incumbent="refrain", development="success"),
            # Square 5
            self._create_choice_answer_label(entrant="substitute", incumbent="refrain", development="success") + " \n" +
            self._create_choice_answer_label(entrant="complement", incumbent="copy", development="success"),
            # Square 6
            self._create_choice_answer_label(entrant="substitute", incumbent="refrain", development="success") + " \n" +
            self._create_choice_answer_label(entrant="complement", incumbent="refrain", development="success"),
        ]

    def _get_incumbent_best_answer_coordinates(self) -> List[List[Tuple[float, float]]]:
        """
        Returns a list containing the coordinates for the squares in the plot of the best answers of the incumbent to the choice of the entrant.

        For the order of the squares refer to the file resources/dev_notes.md.

        Returns
        -------
        List containing the coordinates for the squares in the plot of the best answers of the incumbent to the choice of the entrant.
        """
        y_max: float = self._get_y_max()
        x_max: float = self._get_x_max()
        return [
            # Square 1
            [(0, 0), (self._assets['A-s'], 0), (self._assets['A-s'], max(self._copying_fixed_costs['F(YN)c'], 0)),
             (0, max(self._copying_fixed_costs['F(YN)c'], 0))],
            # Square 2
            [(self._assets['A-s'], 0), (self._assets['A-c'], 0),
             (self._assets['A-c'], self._copying_fixed_costs['F(YY)s']),
             (self._assets['A-s'], self._copying_fixed_costs['F(YY)s'])],
            # Square 3
            [(self._assets['A-c'], 0), (x_max, 0), (x_max, self._copying_fixed_costs['F(YY)s']),
             (self._assets['A-c'], self._copying_fixed_costs['F(YY)s'])],
            # Square 4
            [(0, max(self._copying_fixed_costs['F(YN)c'], 0)),
             (self._assets['A-s'], max(self._copying_fixed_costs['F(YN)c'], 0)),
             (self._assets['A-s'], self._copying_fixed_costs['F(YN)s']), (0, self._copying_fixed_costs['F(YN)s'])],
            # Square 5
            [(self._assets['A-c'], self._copying_fixed_costs['F(YY)s']), (x_max, self._copying_fixed_costs['F(YY)s']),
             (x_max, self._copying_fixed_costs['F(YY)c']), (self._assets['A-c'], self._copying_fixed_costs['F(YY)c'])],
            # Square 6
            [(self._assets['A-s'], self._copying_fixed_costs['F(YY)s']),
             (self._assets['A-c'], self._copying_fixed_costs['F(YY)s']),
             (self._assets['A-c'], self._copying_fixed_costs['F(YY)c']), (x_max, self._copying_fixed_costs['F(YY)c']),
             (x_max, y_max), (0, y_max),
             (0, self._copying_fixed_costs['F(YN)s']), (self._assets['A-s'], self._copying_fixed_costs['F(YN)s'])]]

    def plot_equilibrium(self, axis: matplotlib.axes.Axes = None, **kwargs) -> matplotlib.axes.Axes:
        poly_coordinates: List[List[Tuple[float, float]]] = self._get_equilibrium_coordinates()
        poly_labels: List[str] = self._get_equilibrium_labels()
        axis: matplotlib.axes.Axes = self._plot(title="Equilibrium Path", coordinates=poly_coordinates,
                                                labels=poly_labels,
                                                axis=axis, **kwargs)
        return axis

    def _get_equilibrium_labels(self) -> List[str]:
        """
        Returns a list containing the labels for the squares in the plot of the equilibrium path.

        For the order of the squares refer to the file resources/dev_notes.md.

        Returns
        -------
        List containing the labels for the squares in the plot of the best answers of the equilibrium path.
        """
        return [
            # Square 1
            self._create_choice_answer_label(entrant="indifferent", incumbent="copy", development="failure"),
            # Square 2
            self._create_choice_answer_label(entrant="substitute", incumbent="copy", development="success"),
            # Square 3
            self._create_choice_answer_label(entrant="complement", incumbent="refrain", development="success",
                                             kill_zone=True),
            # Square 4
            self._create_choice_answer_label(entrant="substitute", incumbent="refrain", development="success")
        ]

    def _get_equilibrium_coordinates(self) -> List[List[Tuple[float, float]]]:
        """
        Returns a list containing the coordinates for the squares in the plot of the equilibrium path.

        For the order of the squares refer to the file resources/dev_notes.md.

        Returns
        -------
        List containing the coordinates for the squares in the plot of the best answers of the equilibrium path.
        """
        y_max: float = self._get_y_max()
        x_max: float = self._get_x_max()
        return [
            # Square 1
            [(0, 0), (self._assets['A-s'], 0), (self._assets['A-s'], max(self._copying_fixed_costs['F(YN)c'], 0)),
             (0, max(self._copying_fixed_costs['F(YN)c'], 0))],
            # Square 2
            [(self._assets['A-s'], 0), (x_max, 0), (x_max, self._copying_fixed_costs['F(YY)s']),
             (self._assets['A-s'], self._copying_fixed_costs['F(YY)s'])],
            # Square 3
            [(0, max(self._copying_fixed_costs['F(YN)c'], 0)),
             (self._assets['A-s'], max(self._copying_fixed_costs['F(YN)c'], 0)),
             (self._assets['A-s'], self._copying_fixed_costs['F(YN)s']), (0, self._copying_fixed_costs['F(YN)s'])],
            # Square 4
            [(self._assets['A-s'], self._copying_fixed_costs['F(YY)s']), (x_max, self._copying_fixed_costs['F(YY)s']),
             (x_max, y_max), (0, y_max), (0, self._copying_fixed_costs['F(YN)s']),
             (self._assets['A-s'], self._copying_fixed_costs['F(YN)s'])]]

    def plot_payoffs(self, axis: matplotlib.axes.Axes = None) -> matplotlib.axes.Axes:
        if axis is None:
            figure, axis = plt.subplots()
        index = arange(0, len(self._payoffs) * 2, 2)
        bar_width = 0.35
        opacity = 0.8
        spacing = 0.05

        for counter, utility_type in enumerate(self._payoffs[list(self._payoffs.keys())[0]].keys()):
            utility_values: List[float] = []
            for market_configuration in self._payoffs:
                utility_values.append(self._payoffs[market_configuration][utility_type])

            bars = axis.bar(index + counter * (bar_width + spacing), utility_values, bar_width,
                            alpha=opacity,
                            color='w',
                            hatch='///',
                            edgecolor=self._get_color(counter),
                            label=self._convert_payoffs_label(utility_type))
            max_indices: List[int] = list(
                filter(lambda x: utility_values[x] == max(utility_values), range(len(utility_values))))
            for max_index in max_indices:
                bars[max_index].set_color(self._get_color(counter))

        axis.set_xlabel('Market Configuration')
        axis.set_ylabel('Utility')
        axis.set_title('Utility levels for different Market Configurations')
        axis.set_xticks(index + 1.5 * (bar_width + spacing))
        axis.set_xticklabels(tuple([self._convert_market_configuration_label(i) for i in self._payoffs.keys()]))
        axis.legend(bbox_to_anchor=(0, -0.3), loc="lower left", ncol=4)
        axis.text(max(index) + 2 + 1.5 * (bar_width + spacing), self._payoffs["E(P)"]["W"] * 0.5,
                  self._get_market_configuration_annotations())

        # BaseModel._set_axis(axis)
        plt.show()
        return axis

    @staticmethod
    def _get_market_configuration_annotations() -> str:
        """
        Returns a string containing all product options for the entrant and the incumbent.

        Returns
        -------
        str
            Contains all product options for the entrant and the incumbent.
        """
        return "$I_P$: Primary product sold by the incumbent\n" \
               "$I_C$: Complementary product to $I_P$ potentially sold by the incumbent, which is copied from $E_C$\n" \
               "$E_P$: Perfect substitute to $I_P$ potentially sold by the entrant\n" \
               "$E_C$: Complementary product to $I_P$ currently sold by the entrant\n" \
               "$\\tilde{E}_C$: Complementary product to $I_P$ potentially sold by the entrant\n"

    @staticmethod
    def _convert_payoffs_label(raw_label: str) -> str:
        """
        Converts keys of the payoffs dict to latex labels.

        Parameters
        ----------
        raw_label
            As given as key in the payoffs dict.

        Returns
        -------
        str
            Latex compatible pretty label.
        """
        label: str = raw_label.replace("pi", "$\pi$")
        label = label.replace("CS", "Consumer Surplus")
        label = label.replace("W", "Welfare")
        return label

    @staticmethod
    def _convert_market_configuration_label(raw_label: str) -> str:
        """
        Returns the latex string for a specific market configuration.

        Parameters
        ----------
        raw_label
            Of the market configuration as given as key in the payoffs dict.

        Returns
        -------
        str
            Corresponding latex label for the market configuration as given as key in the payoffs dict.
        """
        labels: Dict[str] = {"basic": "$I_P;E_C$",
                             "I(C)": "$I_P+I_C;E_C$",
                             "E(P)": "$I_P;E_C+E_P$",
                             "I(C)E(P)": "$I_P+I_C;E_C+E_P$",
                             "E(C)": "$I_P;E_C+\\tilde{E}_C$",
                             "I(C)E(C)": "$I_P+I_C;E_C+\\tilde{E}_C$"}
        return labels.get(raw_label, 'No valid market configuration')

    def _get_x_max(self) -> float:
        """
        Returns the maximum value to plot on the x - axis.

        Returns
        -------
        float
            Maximum value to plot on the x - axis.
        """
        return round(self._assets['A-c'] * 1.3, 1)

    def _get_y_max(self) -> float:
        """
        Returns the maximum value to plot on the y - axis.

        Returns
        -------
        float
            Maximum value to plot on the y - axis.
        """
        return round(self._copying_fixed_costs['F(YN)s'] * 1.3, 1)

    def _draw_thresholds(self, axis: matplotlib.axes.Axes) -> None:
        """
        Draws the thresholds and the corresponding labels on a given axis.

        Parameters
        ----------
        axis: matplotlib.axes.Axes
            Axis to draw the thresholds on.
        """
        # horizontal lines (fixed cost of copying thresholds)
        self._draw_horizontal_line_with_label(axis, y=self._copying_fixed_costs['F(YN)s'], label="$F^{YN}_S$")
        self._draw_horizontal_line_with_label(axis, y=self._copying_fixed_costs['F(YY)c'], label="$F^{YY}_C$")

        if abs(self._copying_fixed_costs['F(YY)s'] - self._copying_fixed_costs['F(YN)c']) < BaseModel.TOLERANCE:
            self._draw_horizontal_line_with_label(axis, y=self._copying_fixed_costs['F(YY)s'],
                                                  label="$F^{YY}_S=F^{YN}_C$")
        else:
            self._draw_horizontal_line_with_label(axis, y=self._copying_fixed_costs['F(YY)s'], label="$F^{YY}_S$")
            if self._copying_fixed_costs['F(YN)c'] >= 0:
                self._draw_horizontal_line_with_label(axis, y=self._copying_fixed_costs['F(YN)c'], label="$F^{YN}_C$")
        # vertical lines (asset thresholds)
        self._draw_vertical_line_with_label(axis, x=self._assets['A-s'], label=r'$\bar{A}_S$')
        self._draw_vertical_line_with_label(axis, x=self._assets['A-c'], label=r'$\bar{A}_C$')

    def _draw_horizontal_line_with_label(self, axis: matplotlib.axes.Axes, y: float, label: str = None) -> None:
        """
        Draws a horizontal line at a given y - coordinate and writes the corresponding label at the edge.

        Parameters
        ----------
        axis
            To draw the horizontal line and label on.
        y
            Coordinate of the of the line on the y - axis.
        label
            Label for the horizontal line written at the edge.
        """
        label_x: float = self._get_x_max() + 0.05
        axis.axhline(y, linestyle='--', color='k')
        if label is not None:
            axis.text(label_x, y, label)

    def _draw_vertical_line_with_label(self, axis: matplotlib.axes.Axes, x: float, label: str = None) -> None:
        """
        Draws a vertical line at a given x - coordinate and writes the corresponding label at the edge.

        Parameters
        ----------
        axis
            To draw the vertical line and label on.
        x
            Coordinate of the of the line on the x - axis.
        label
            Label for the vertical line written at the edge.
        """
        label_y: float = self._get_y_max() + 0.15
        axis.axvline(x, linestyle='--', color='k')
        if label is not None:
            axis.text(x, label_y, label)

    def _create_additional_legend(self, options_legend: bool, thresholds_legend: bool) -> str:
        legend: str = ""
        if options_legend:
            legend += self._create_options_legend()
        if thresholds_legend:
            legend += self._create_thresholds_legend()
        return legend

    def _create_options_legend(self, latex: bool = True) -> str:
        space: str = "$\quad$" if latex else "\t"
        return "Options of the entrant:\n" + \
               space + self.ENTRANT_CHOICES[
                   'complement'] + ": Develop an additional complementary product to a primary product.\n" + \
               space + self.ENTRANT_CHOICES[
                   'substitute'] + ": Develop an substitute to the primary product of the incumbent.\n" + \
               space + self.ENTRANT_CHOICES['indifferent'] + " : Indifferent between the options mentioned above.\n" + \
               "Options of the incumbent:\n" + \
               space + self.INCUMBENT_CHOICES[
                   'copy'] + " : Copy the original complement of the entrant.\n" + \
               space + self.INCUMBENT_CHOICES[
                   'refrain'] + " : Do not copy the original complement of the entrant.\n" + \
               "Outcomes of the development:\n" + \
               space + self.DEVELOPMENT_OUTCOME[
                   'success'] + " : The entrant has sufficient assets to develop the product.\n" + \
               space + self.DEVELOPMENT_OUTCOME[
                   'failure'] + " : The entrant has not sufficient assets to develop the product."

    @staticmethod
    def _create_thresholds_legend() -> str:
        space: str = "$\quad$"
        return "Thresholds for the assets of the entrant:\n" + \
               space + r'$\bar{A}_S$' + ": Minimum level of assets to ensure a perfect substitute\n" + \
               space + space + space + " gets funded if the incumbent copies.\n" + \
               space + r'$\bar{A}_C$' + ": Minimum level of assets to ensure another complement\n" + \
               space + space + space + " gets funded if the incumbent copies.\n" + \
               "If the incumbent does not copy, the entrant will have sufficient assets.\n\n" + \
               "Thresholds for the fixed costs of copying for the incumbent:\n" + \
               space + r'$F^{YY}_S$' + ": Maximum costs of copying that ensure that the incumbent\n" + \
               space + space + space + space + "copies the entrant if the entrant is guaranteed to invest\n" + \
               space + space + space + space + "in a perfect substitute.\n" + \
               space + r'$F^{YN}_S$' + ": Maximum costs of copying that ensure that the incumbent\n" + \
               space + space + space + space + "copies the entrant if the copying prevents the entrant\n" + \
               space + space + space + space + " from developing a perfect substitute.\n" + \
               space + r'$F^{YY}_C$' + ": Maximum costs of copying that ensure that the incumbent\n" + \
               space + space + space + space + "copies the entrant if the entrant is guaranteed to invest\n" + \
               space + space + space + space + "in another complement.\n" + \
               space + r'$F^{YN}_C$' + ": Maximum costs of copying that ensure that the incumbent\n" + \
               space + space + space + space + "copies the entrant if the copying prevents the entrant\n" + \
               space + space + space + space + "from developing another complement.\n"

    @staticmethod
    def _get_color(i: int) -> str:
        """
        Returns a string corresponding to a matplotlib - color for a given index.

        The index helps to get different colors for different items, when iterating over list/dict/etc..

        Parameters
        ----------
        i: int
            Index of the color.
        Returns
        -------
        str
            A string corresponding to a matplotlib - color for a given index.
        """
        return ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'][i]

    @staticmethod
    def _set_axis(axis: matplotlib.axes.Axes) -> None:
        """
        Adjusts the axis to the given viewport.

        Parameters
        ----------
        axis: matplotlib.axes.Axes
            To adjust to the given viewport.
        """
        axis.autoscale_view()
        axis.figure.tight_layout()

    @staticmethod
    def _set_axis_labels(axis: matplotlib.axes.Axes, title: str, x_label: str, y_label: str) -> None:
        """
        Sets all the labels for a plot, containing the title, x - label and y - label.

        Parameters
        ----------
        axis
            Axis to set the labels for.
        title
            Title of the axis. (not None)
        x_label
            Label of the x - axis. (not None)
        y_label
            Label of the y - axis. (not None)
        """
        assert title is not None
        assert x_label is not None
        assert y_label is not None
        axis.set_title(title, loc='left', y=1.1)
        axis.set_xlabel(x_label)
        axis.set_ylabel(y_label)

    def __str__(self) -> str:
        str_representation: str = 'Assets:'
        for key in self._assets.keys():
            str_representation += '\n\t- ' + key + ':\t' + str(self._assets[key])

        str_representation += '\nCosts for copying:'
        for key in self._copying_fixed_costs.keys():
            str_representation += '\n\t- ' + key + ':\t' + str(self._copying_fixed_costs[key])

        market_configurations: List[str] = list(self._payoffs.keys())
        str_representation += '\nUtility - Levels for different Market Configurations:\n\t' + ''.join(
            ['{0: <14}'.format(item) for item in market_configurations])
        for utility_type in self._payoffs[market_configurations[0]].keys():
            str_representation += '\n\t'
            for market_configuration in market_configurations:
                str_representation += '-' + '{0: <4}'.format(utility_type).replace('pi', 'π') + ': ' + '{0: <5}'.format(
                    str(self._payoffs[market_configuration][utility_type])) + '| '

        return str_representation


class BargainingPowerModel(BaseModel):
    """
    Besides the parameters used in the paper, this class will introduce the parameter $\\beta$ in the models, called
    the bargaining power of the incumbent. In the paper the default value 0.5 is used to derive the results.
    """

    def __init__(self, u: float = 1, B: float = 0.5, small_delta: float = 0.5, delta: float = 0.51,
                 K: float = 0.2, beta: float = 0.5):
        """
        Besides $\\beta$ the parameters in this model do not change compared to Shelegia_Motta_2021.Models.BaseModel.

        Parameters
        ----------
        beta: float
            Bargaining power of the incumbent relative to the entrant ($0 < \\beta < 1$).
        """
        assert 0 < beta < 1, 'Invalid bargaining power beta (has to be between 0 and 1).'
        self._beta: float = beta
        super(BargainingPowerModel, self).__init__(u=u, B=B, small_delta=small_delta, delta=delta, K=K)

    def _calculate_payoffs(self) -> Dict[str, Dict[str, float]]:
        """
        Calculates the payoffs for different market configurations with the formulas given in the paper.

        The formulas are tabulated in BargainingPowerModel.get_payoffs, which are different to the BaseModel.

        Returns
        -------
        Dict[str, Dict[str, float]]
            Contains the mentioned payoffs for different market configurations.
        """
        payoffs: Dict[str, Dict[str, float]] = super()._calculate_payoffs()
        # basic market.
        payoffs['basic']['pi(I)'] = self._u + self._small_delta * self._beta
        payoffs['basic']['pi(E)'] = self._small_delta * (1 - self._beta)

        # additional complement of the entrant
        payoffs['E(C)']['pi(I)'] = self._u + 2 * self._small_delta * self._beta
        payoffs['E(C)']['pi(E)'] = 2 * self._small_delta * (1 - self._beta)

        # additional complement of the incumbent and the entrant
        payoffs['I(C)E(C)']['pi(I)'] = self._u + self._small_delta * (1 + self._beta)
        payoffs['I(C)E(C)']['pi(E)'] = self._small_delta * (1 - self._beta)

        return payoffs

    def _calculate_copying_fixed_costs_values(self) -> Dict[str, float]:
        """
        Calculates the thresholds for the fixed costs of copying for the incumbent.

        The formulas are tabulated in BargainingPowerModel.get_copying_fixed_costs_values, which are different to the BaseModel.

        Returns
        -------
        Dict[str, float]
            Includes the thresholds for the fixed costs for copying of the incumbent.
        """
        return {'F(YY)s': self._small_delta * (1 - self._beta),
                'F(YN)s': self._u + self._small_delta * (2 - self._beta),
                'F(YY)c': 2 * self._small_delta * (1 - self._beta),
                'F(YN)c': self._small_delta * (2 - 3 * self._beta)}

    def _calculate_asset_values(self) -> Dict[str, float]:
        """
        Calculates the thresholds for the assets of the entrant.

        The formulas are tabulated in BargainingPowerModel.get_asset_values, which are different to the BaseModel.

        Returns
        -------
        Dict[str, float]
            Includes the thresholds for the assets of the entrant.
        """
        return {'A_s': self._K + self._B - self._delta - self._small_delta * (2 - self._beta),
                'A_c': self._K + self._B - 3 * self._small_delta * (1 - self._beta),
                'A-s': self._K + self._B - self._delta,
                'A-c': self._K + self._B - self._small_delta * (1 - self._beta)}

    def get_asset_values(self) -> Dict[str, float]:
        """
        Returns the asset thresholds of the entrant.

        | Threshold $\:\:\:\:\:$ | Name $\:\:\:\:\:$ | Formula $\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$ |
        |----------------|:----------|:-----------|
        | $A_S$ | A_s | $B + K - \Delta - \delta(2 - \\beta)$ |
        | $A_C$ | A_c | $B + K - 3\delta(1 - \\beta)$ |
        | $\overline{A}_S$ | A-s | $B + K - \Delta$ |
        | $\overline{A}_C$ | A-c | $B + K - \delta(1 - \\beta)$ |
        <br>
        Returns
        -------
        Dict[str, float]
            Includes the thresholds for the assets of the entrant.
        """
        return self._assets

    def get_copying_fixed_costs_values(self) -> Dict[str, float]:
        """
        Returns the fixed costs for copying thresholds of the incumbent.

        | Threshold $\:\:\:\:\:$ | Name $\:\:\:\:\:$ | Formula $\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$ |
        |----------|:-------|:--------|
        | $F^{YY}_S$ | F(YY)s | $\delta(1 - \\beta)$ |
        | $F^{YN}_S$ | F(YN)s | $u + \delta(2 - \\beta)$ |
        | $F^{YY}_C$ | F(YY)c | $2\delta(1 - \\beta)$ |
        | $F^{YN}_C$ | F(YN)c | $\delta(2 - \\beta)$ |
        <br>
        Returns
        -------
        Dict[str, float]
            Includes the thresholds for the fixed costs for copying of the incumbent.
        """
        return self._copying_fixed_costs

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

        | Market Config. $\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$ | $\pi(I) \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$ | $\pi(E) \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$ | CS $\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$ | W $\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$ |
        |-----------------------|:--------|:--------|:--|:-|
        | $I_P$ ; $E_C$         | $u + \delta\\beta$ | $\delta(1 - \\beta)$ | 0 | $u + \delta$ |
        | $I_P + I_C$ ; $E_C$   | $u + \delta$ | 0 | 0 | $u + \delta$ |
        | $I_P$ ; $E_P + E_C$   | 0 | $\Delta + \delta$ | $u$ | $u + \Delta + \delta$ |
        | $I_P + I_C$ ; $E_P + E_C$ | 0 | $\Delta$ | $u + \delta$ | $u + \Delta + \delta$ |
        | $I_P$ ; $E_C + \\tilde{E}_C$ | $u + 2\delta\\beta$ | $2\delta(1 - \\beta)$ | 0 | $u + 2\delta$ |
        | $I_P + I_C$ ; $E_C + \\tilde{E}_C$ | $u + \delta(1 + \\beta)$ | $\delta(1 - \\beta)$ | 0 | $u + 2\delta$ |
        <br>

        Returns
        -------
        Dict[str, Dict[str, float]]
            Contains the mentioned payoffs for different market configurations.
        """
        return self._payoffs

    def _get_incumbent_best_answer_coordinates(self) -> List[List[Tuple[float, float]]]:
        coordinates: List[List[Tuple[float, float]]] = super(BargainingPowerModel,
                                                             self)._get_incumbent_best_answer_coordinates()
        if self._copying_fixed_costs["F(YY)s"] != self._copying_fixed_costs["F(YN)c"]:
            coordinates.append([(self._assets['A-s'], self._copying_fixed_costs['F(YY)s']),
                                (self._assets['A-c'], self._copying_fixed_costs['F(YY)s']),
                                (self._assets['A-c'], max(self._copying_fixed_costs['F(YN)c'], 0)),
                                (self._assets['A-s'], max(self._copying_fixed_costs['F(YN)c'], 0))])
        return coordinates

    def _get_incumbent_best_answer_labels(self) -> List[str]:
        labels: List[str] = super(BargainingPowerModel, self)._get_incumbent_best_answer_labels()
        if self._copying_fixed_costs["F(YY)s"] != self._copying_fixed_costs["F(YN)c"]:
            if self._copying_fixed_costs["F(YY)s"] > self._copying_fixed_costs["F(YN)c"]:
                labels.append(
                    # Square 7
                    self._create_choice_answer_label(entrant="substitute", incumbent="copy",
                                                     development="success") + " \n" +
                    self._create_choice_answer_label(entrant="complement", incumbent="refrain", development="success"),
                )
            else:
                labels.append(
                    # Square 7
                    self._create_choice_answer_label(entrant="substitute", incumbent="refrain",
                                                     development="success") + " \n" +
                    self._create_choice_answer_label(entrant="complement", incumbent="copy", development="failure"),
                )
        return labels


class UnobservableModel(BargainingPowerModel):
    """
    This model indicates that if the incumbent were not able to observe the entrant at the moment of choosing, the “kill zone” effect whereby the entrant stays away from the substitute in order to avoid being copied) would not take place. Intuitively, in the game as we studied it so far, the only reason why the entrant is choosing a trajectory leading to another complement is that it anticipates that if it chose one leading to a substitute, the incumbent would copy, making it an inefficient strategy for entering the market. However, if the incumbent cannot observe the entrant’s choice of strategy, the entrant could not hope to strategically affect the decision of the incumbent. This would lead to the entrant having a host of new opportunities when entering the market and it makes competing with a large company much more attractive.
    """

    def __init__(self, u: float = 1, B: float = 0.5, small_delta: float = 0.5, delta: float = 0.51,
                 K: float = 0.2, beta: float = 0.5):
        """
        The parameters do not change compared to Shelegia_Motta_2021.Models.BargainingPowerModel.
        """
        super(UnobservableModel, self).__init__(u=u, B=B, small_delta=small_delta, delta=delta, K=K, beta=beta)

    def plot_incumbent_best_answers(self, axis: matplotlib.axes.Axes = None, **kwargs) -> matplotlib.axes.Axes:
        return self.plot_equilibrium(axis=axis, **kwargs)

    def _create_choice_answer_label(self, entrant: Literal["complement", "substitute", "indifferent"],
                                    incumbent: Literal["copy", "refrain"],
                                    development: Literal["success", "failure"],
                                    kill_zone: bool = False) -> str:
        return "{" + self.ENTRANT_CHOICES[entrant] + ", " + self.INCUMBENT_CHOICES[incumbent] + "} $\\rightarrow$ " + \
               self.DEVELOPMENT_OUTCOME[development]

    def _get_equilibrium_labels(self) -> List[str]:
        """
        Returns a list containing the labels for the squares in the plot of the equilibrium path.

        For the order of the squares refer to the file resources/dev_notes.md.

        Returns
        -------
        List containing the labels for the squares in the plot of the best answers of the equilibrium path.
        """
        return [
            # Square 1
            self._create_choice_answer_label(entrant="indifferent", incumbent="copy", development="failure"),
            # Square 2
            self._create_choice_answer_label(entrant="substitute", incumbent="copy", development="success"),
            # Square 3
            self._create_choice_answer_label(entrant="substitute", incumbent="copy", development="failure"),
            # Square 4
            self._create_choice_answer_label(entrant="substitute", incumbent="refrain", development="success")
        ]

    def get_optimal_choice(self, A: float, F: float) -> Dict[str, str]:
        result: Dict = super().get_optimal_choice(A, F)
        # adjust the different choices in area three -> since the kill zone does not exist in this model.
        if result["entrant"] == self.ENTRANT_CHOICES["complement"]:
            result = {"entrant": self.ENTRANT_CHOICES["substitute"], "incumbent": self.INCUMBENT_CHOICES["copy"],
                      "development": self.DEVELOPMENT_OUTCOME["failure"]}
        return result


class AcquisitionModel(BargainingPowerModel):
    """
    In order to explore how acquisitions may modify the entrant’s and the incumbent’s strategic choices, we extend the base model in order to allow an acquisition to take place after the incumbent commits to copying the entrant’s original complementary product (between t=1 and t=2, see table 2). We assume that the incumbent and the entrant share the gains (if any) attained from the acquisition equally.
    """

    def __init__(self, u: float = 1, B: float = 0.5, small_delta: float = 0.5, delta: float = 0.51,
                 K: float = 0.2) -> None:
        """
        An additional constraint is added compared to Shelegia_Motta_2021.Models.BaseModel. Namely, $\Delta$ has to be bigger than $\delta$, meaning the innovation of the entrant is not too drastic.

        Meanwhile, the parameters do not change compared to Shelegia_Motta_2021.Models.BargainingPowerModel.
        """
        assert delta > small_delta, "Delta has to be smaller than small_delta, meaning the innovation of the entrant is not too drastic."
        super(AcquisitionModel, self).__init__(u=u, B=B, small_delta=small_delta, delta=delta, K=K)

    def _calculate_copying_fixed_costs_values(self) -> Dict[str, float]:
        copying_fixed_costs_values: Dict[str, float] = super()._calculate_copying_fixed_costs_values()
        copying_fixed_costs_values.update(
            {'F(ACQ)s': (self._u + self._delta - self._K) / 2 + self._small_delta * (2 - self._beta),
             'F(ACQ)c': self._small_delta * (2.5 - 3 * self._beta) - self._K / 2})
        return copying_fixed_costs_values

    def get_copying_fixed_costs_values(self) -> Dict[str, float]:
        """
        Returns the fixed costs for copying thresholds of the incumbent.

        Additional thresholds for the fixed cost of copying of the incumbent compared to the Shelegia_Motta_2021.Models.BargainingModel:

        | Threshold $\:\:\:\:\:$ | Name $\:\:\:\:\:$ | Formula $\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$ |
        |----------|:-------|:--------|
        | $F^{ACQ}_S$ | F(ACQ)s | $\\frac{(u + \Delta - K)}{2} + \delta(2 - \\beta)$ |
        | $F^{ACQ}_C$ | F(ACQ)c | $\\frac{K}{2} + \delta(2.5 - 3\\beta)$ |
        <br>
        Returns
        -------
        Dict[str, float]
            Includes the thresholds for the fixed costs for copying of the incumbent.
        """
        return self._copying_fixed_costs


if __name__ == '__main__':
    bargaining_power_model = Shelegia_Motta_2021.BargainingPowerModel(beta=0.6)
    fig, (axis_eq, axis_best) = plt.subplots(ncols=2, figsize=(14, 9))
    bargaining_power_model.plot_equilibrium(axis=axis_eq, options_legend=True)
    bargaining_power_model.plot_incumbent_best_answers(axis=axis_best, thresholds_legend=True)
    plt.show()
