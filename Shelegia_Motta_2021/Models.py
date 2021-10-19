from typing import Dict, List, Tuple, Literal

import matplotlib.axes
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "monospace"
from numpy import arange

import Shelegia_Motta_2021


class BaseModel(Shelegia_Motta_2021.IModel):
    """
    There are two players in our base model: the Incumbent, which sells the primary product, denoted
by Ip, and a start-up, that we call Entrant, which sells a product Ec complementary to Ip. (One may
think of Ip as a platform, and Ec as a service or product which can be accessed through the platform.)
We are interested in studying the choice of E between developing a substitute to Ip, denoted by
Ep, or another complement to Ip, denoted by E˜c;23 and the choice of I between copying E’s original
complementary product Ec by creating a perfect substitute Ic, or not.24 Since E may not have enough
assets to cover the development cost of its second product, copying its current product will a↵ect E’s
ability to obtain funding
"""

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
            Utility gained from consuming the primary product
        B : float
            Minimal difference between the return in case of a success and the return in case of failure of E. B is called the private benefit of E in case of failure.
        small_delta : float
            ($\delta$) Additional utility gained from from a complement combined with a primary product.
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
        self._utility: Dict[str, Dict[str, float]] = self._calculate_welfare()

    def _calculate_welfare(self) -> Dict[str, Dict[str, float]]:
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

        Includes:
        - (6) F(YY)s = $\delta$ / 2
        - (6) F(YN)s = u + 3 * $\delta$ / 2
        - (6) F(YY)c = $\delta$
        - (6) F(YN)c = $\delta$ / 2

        Returns
        -------
        Dict including the thresholds fixed costs of copying for the incumbent.
        """
        return {'F(YY)s': self._small_delta / 2,
                'F(YN)s': self._u + self._small_delta * 3 / 2,
                'F(YY)c': self._small_delta,
                'F(YN)c': self._small_delta / 2}

    def _calculate_asset_values(self) -> Dict[str, float]:
        """
        Calculates the thresholds for the assets of the entrant.

        Includes:
        - (2) A >= A_s = B - ($\Delta$ + 3 * $\delta$ / 2 - K)
        - (3) A >= A_c = B - (3 * $\delta$ / 2 - K)
        - (4) A >= A-s = B - ($\Delta$ - K)
        - (5) A >= A-c = B - ($\delta$ / 2 - K)

        Returns
        -------
        Dict including the thresholds for the assets of the entrant.
        """
        return {'A_s': self._B - (self._delta + 3 / 2 * self._small_delta - self._K),
                'A_c': self._B - (3 / 2 * self._small_delta - self._K),
                'A-s': self._B - (self._delta - self._K),
                'A-c': self._B - (1 / 2 * self._small_delta - self._K)}

    def get_asset_values(self) -> Dict[str, float]:
        return self._assets

    def get_copying_fixed_costs_values(self) -> Dict[str, float]:
        return self._copying_fixed_costs

    def get_utility_values(self) -> Dict[str, Dict[str, float]]:
        return self._utility

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
              axis: matplotlib.axes.Axes = None) -> matplotlib.axes.Axes:
        """
        Plots polygons containing the optimal choices and answers into a coordinate system.

        Parameters
        ----------
        coordinates : List[List[Tuple[float, float]]]
            List of all polygons (list of coordinates) to plot.
        axis : matplotlib.axes.Axes
            Axis to draw the plot on. (optional)

        Returns
        -------
        Axis containing the plot.
        """
        if axis is None:
            fig, axis = plt.subplots()
        self._draw_thresholds(axis)

        for i, coordinates in enumerate(coordinates):
            poly = plt.Polygon(coordinates, ec="k", color=self._get_color(i), label=labels[i])
            axis.add_patch(poly)

        axis.legend(bbox_to_anchor=(1.15, 1), loc="upper left")
        BaseModel._set_axis(axis)
        plt.show()
        return axis

    def plot_incumbent_best_answers(self, axis: matplotlib.axes.Axes = None) -> matplotlib.axes.Axes:
        poly_coordinates: List[List[Tuple[float, float]]] = self._get_incumbent_best_answer_coordinates()
        poly_labels: List[str] = self._get_incumbent_best_answer_labels()
        axis: matplotlib.axes.Axes = self._plot(coordinates=poly_coordinates, labels=poly_labels, axis=axis)
        return axis

    def _create_choice_answer_label(self, entrant: Literal["complement", "substitute", "indifferent"],
                                    incumbent: Literal["copy", "refrain"],
                                    development: Literal["success", "failure"]) -> str:
        return self.ENTRANT_CHOICES[entrant] + " $\\rightarrow$ " + self.INCUMBENT_CHOICES[
            incumbent] + " $\\rightarrow$ " + self.DEVELOPMENT_OUTCOME[development]

    def _get_incumbent_best_answer_labels(self) -> List[str]:
        return [
            # Square 1
            self._create_choice_answer_label(entrant="substitute", incumbent="copy", development="failure") + " \n" +
            self._create_choice_answer_label(entrant="complement", incumbent="copy", development="failure"),
            # Square 2
            self._create_choice_answer_label(entrant="substitute", incumbent="copy", development="failure") + " \n" +
            self._create_choice_answer_label(entrant="complement", incumbent="refrain", development="success"),
            # Square 3
            self._create_choice_answer_label(entrant="substitute", incumbent="copy", development="success") + " \n" +
            self._create_choice_answer_label(entrant="complement", incumbent="copy", development="failure"),
            # Square 4
            self._create_choice_answer_label(entrant="substitute", incumbent="copy", development="success") + " \n" +
            self._create_choice_answer_label(entrant="complement", incumbent="copy", development="success"),
            # Square 5
            self._create_choice_answer_label(entrant="substitute", incumbent="refrain", development="success") + " \n" +
            self._create_choice_answer_label(entrant="complement", incumbent="copy", development="success"),
            # Square 6
            self._create_choice_answer_label(entrant="substitute", incumbent="refrain", development="success") + " \n" +
            self._create_choice_answer_label(entrant="complement", incumbent="refrain", development="success"),
        ]

    def _get_incumbent_best_answer_coordinates(self) -> List[List[Tuple[float, float]]]:
        y_max: float = self._get_y_max()
        x_max: float = self._get_x_max()
        return [
            # Square 1
            [(0, 0), (self._assets['A-s'], 0), (self._assets['A-s'], self._copying_fixed_costs['F(YY)s']),
             (0, self._copying_fixed_costs['F(YY)s'])],
            # Square 2
            [(0, self._copying_fixed_costs['F(YY)s']), (self._assets['A-s'], self._copying_fixed_costs['F(YY)s']),
             (self._assets['A-s'], self._copying_fixed_costs['F(YN)s']), (0, self._copying_fixed_costs['F(YN)s'])],
            # Square 3
            [(self._assets['A-s'], 0), (self._assets['A-c'], 0),
             (self._assets['A-c'], self._copying_fixed_costs['F(YY)s']),
             (self._assets['A-s'], self._copying_fixed_costs['F(YY)s'])],
            # Square 4
            [(self._assets['A-c'], 0), (x_max, 0), (x_max, self._copying_fixed_costs['F(YY)s']),
             (self._assets['A-c'], self._copying_fixed_costs['F(YY)s'])],
            # Square 5
            [(self._assets['A-c'], self._copying_fixed_costs['F(YY)s']), (x_max, self._copying_fixed_costs['F(YY)s']),
             (x_max, self._copying_fixed_costs['F(YY)c']), (self._assets['A-c'], self._copying_fixed_costs['F(YY)c'])],
            # Square 6
            [(self._assets['A-s'], self._copying_fixed_costs['F(YY)s']),
             (self._assets['A-c'], self._copying_fixed_costs['F(YY)s']),
             (self._assets['A-c'], self._copying_fixed_costs['F(YY)c']), (x_max, self._copying_fixed_costs['F(YY)c']),
             (x_max, y_max), (0, y_max),
             (0, self._copying_fixed_costs['F(YN)s']), (self._assets['A-s'], self._copying_fixed_costs['F(YN)s'])]]

    def plot_equilibrium(self, axis: matplotlib.axes.Axes = None) -> matplotlib.axes.Axes:
        poly_coordinates: List[List[Tuple[float, float]]] = self._get_equilibrium_coordinates()
        poly_labels: List[str] = self._get_equilibrium_labels()
        axis: matplotlib.axes.Axes = self._plot(coordinates=poly_coordinates, labels=poly_labels, axis=axis)
        return axis

    def _get_equilibrium_labels(self) -> List[str]:
        return [
            # Square 1
            self._create_choice_answer_label(entrant="indifferent", incumbent="copy", development="failure"),
            # Square 2
            self._create_choice_answer_label(entrant="complement", incumbent="refrain", development="success"),
            # Square 3
            self._create_choice_answer_label(entrant="substitute", incumbent="copy", development="success"),
            # Square 4
            self._create_choice_answer_label(entrant="substitute", incumbent="refrain", development="success")
        ]

    def _get_equilibrium_coordinates(self) -> List[List[Tuple[float, float]]]:
        y_max: float = self._get_y_max()
        x_max: float = self._get_x_max()
        return [
            # Square 1
            [(0, 0), (self._assets['A-s'], 0), (self._assets['A-s'], self._copying_fixed_costs['F(YY)s']),
             (0, self._copying_fixed_costs['F(YY)s'])],
            # Square 2
            [(0, self._copying_fixed_costs['F(YY)s']), (self._assets['A-s'], self._copying_fixed_costs['F(YY)s']),
             (self._assets['A-s'], self._copying_fixed_costs['F(YN)s']), (0, self._copying_fixed_costs['F(YN)s'])],
            # Square 3
            [(self._assets['A-s'], 0), (x_max, 0), (x_max, self._copying_fixed_costs['F(YY)s']),
             (self._assets['A-s'], self._copying_fixed_costs['F(YY)s'])],
            # Square 4
            [(self._assets['A-s'], self._copying_fixed_costs['F(YY)s']), (x_max, self._copying_fixed_costs['F(YY)s']),
             (x_max, y_max), (0, y_max), (0, self._copying_fixed_costs['F(YN)s']),
             (self._assets['A-s'], self._copying_fixed_costs['F(YN)s'])]]

    def plot_utilities(self, axis: matplotlib.axes.Axes = None) -> matplotlib.axes.Axes:
        if axis is None:
            fig, axis = plt.subplots()
        index = arange(0, len(self._utility) * 2, 2)
        bar_width = 0.35
        opacity = 0.8
        spacing = 0.05

        for counter, utility_type in enumerate(self._utility[list(self._utility.keys())[0]].keys()):
            utility_values: List[float] = []
            for market_configuration in self._utility:
                utility_values.append(self._utility[market_configuration][utility_type])

            bars = axis.bar(index + counter * (bar_width + spacing), utility_values, bar_width,
                            alpha=opacity,
                            color='w',
                            hatch='///',
                            edgecolor=self._get_color(counter),
                            label=self._convert_utility_label(utility_type))
            max_indices: List[int] = list(
                filter(lambda x: utility_values[x] == max(utility_values), range(len(utility_values))))
            for max_index in max_indices:
                bars[max_index].set_color(self._get_color(counter))

        axis.set_xlabel('Market Configuration')
        axis.set_ylabel('Utility')
        axis.set_title('Utility levels for different Market Configurations')
        axis.set_xticks(index + 1.5 * (bar_width + spacing))
        axis.set_xticklabels(tuple([self._convert_market_configuration_label(i) for i in self._utility.keys()]))
        axis.legend(bbox_to_anchor=(0, -0.3), loc="lower left", ncol=4)
        axis.text(max(index) + 2 + 1.5 * (bar_width + spacing), self._utility["E(P)"]["W"]*0.5, self._get_market_configuration_annotations())

        # BaseModel._set_axis(axis)
        plt.show()
        return axis

    @staticmethod
    def _get_market_configuration_annotations() -> str:
        return "$I_P$: Primary product sold by the incumbent\n" \
               "$I_C$: Complementary product to $I_P$ potentially sold by the incumbent, which is copied from $E_C$\n" \
               "$E_P$: Perfect substitute to $I_P$ potentially sold by the entrant\n" \
               "$E_C$: Complementary product to $I_P$ currently sold by the entrant\n" \
               "$\\tilde{E}_C$: Complementary product to $I_P$ potentially sold by the entrant\n"

    @staticmethod
    def _convert_utility_label(raw_label: str) -> str:
        label: str = raw_label.replace("pi", "$\pi$")
        label = label.replace("CS", "Consumer Surplus")
        label = label.replace("W", "Welfare")
        return label

    @staticmethod
    def _convert_market_configuration_label(raw_label: str) -> str:
        labels: Dict[str] = {"basic": "$I_P;E_C$",
                             "I(C)": "$I_P+I_C;E_C$",
                             "E(P)": "$I_P;E_C+E_P$",
                             "I(C)E(P)": "$I_P+I_C;E_C+E_P$",
                             "E(C)": "$I_P;E_C+\\tilde{E}_C$",
                             "I(C)E(C)": "$I_P+I_C;E_C+\\tilde{E}_C$"}
        return labels.get(raw_label, 'No valid market configuration')

    def _get_x_max(self) -> float:
        return round(self._assets['A-c'] * 1.3, 1)

    def _get_y_max(self) -> float:
        return round(self._copying_fixed_costs['F(YN)s'] * 1.3, 1)

    def _draw_thresholds(self, axis: matplotlib.axes.Axes) -> None:
        horizontal_line_x: float = self._get_x_max() + 0.05
        vertical_line_y: float = self._get_y_max() + 0.15
        axis.axhline(self._copying_fixed_costs['F(YN)s'], linestyle='--', color='k')
        axis.text(horizontal_line_x, self._copying_fixed_costs['F(YN)s'], r'$F^{YN}_S$')
        axis.axhline(self._copying_fixed_costs['F(YY)s'], linestyle='--', color='k')
        axis.text(horizontal_line_x, self._copying_fixed_costs['F(YY)s'], r'$F^{YY}_S=F^{YN}_C$')
        axis.axhline(self._copying_fixed_costs['F(YY)c'], linestyle='--', color='k')
        axis.text(horizontal_line_x, self._copying_fixed_costs['F(YY)c'], r'$F^{YY}_C$')
        axis.axvline(self._assets['A-s'], linestyle='--', color='k')
        axis.text(self._assets['A-s'], vertical_line_y, r'$\bar{A}_S$')
        axis.axvline(self._assets['A-c'], linestyle='--', color='k')
        axis.text(self._assets['A-c'], vertical_line_y, r'$\bar{A}_C$')

    @staticmethod
    def _get_color(i: int) -> str:
        return ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'][i]

    @staticmethod
    def _set_axis(axis: matplotlib.axes.Axes):
        axis.autoscale_view()
        axis.figure.tight_layout()

    def __str__(self) -> str:
        str_representation: str = 'Assets:'
        for key in self._assets.keys():
            str_representation += '\n\t- ' + key + ':\t' + str(self._assets[key])

        str_representation += '\nCosts for copying:'
        for key in self._copying_fixed_costs.keys():
            str_representation += '\n\t- ' + key + ':\t' + str(self._copying_fixed_costs[key])

        market_configurations: List[str] = list(self._utility.keys())
        str_representation += '\nUtility - Levels for different Market Configurations:\n\t' + ''.join(
            ['{0: <14}'.format(item) for item in market_configurations])
        for utility_type in self._utility[market_configurations[0]].keys():
            str_representation += '\n\t'
            for market_configuration in market_configurations:
                str_representation += '-' + '{0: <4}'.format(utility_type).replace('pi', 'π') + ': ' + '{0: <5}'.format(
                    str(self._utility[market_configuration][utility_type])) + '| '

        return str_representation


class UnobservableModel(BaseModel):
    pass


class AcquisitionModel(BaseModel):
    def __init__(self, u: float = 1, B: float = 0.5, small_delta: float = 0.5, delta: float = 0.51,
                 K: float = 0.2) -> None:
        assert delta > small_delta, "Delta has to be smaller than small_delta, meaning the innovation of the entrant is not too drastic."
        super(AcquisitionModel, self).__init__(u=u, B=B, small_delta=small_delta, delta=delta, K=K)

    def _calculate_copying_fixed_costs_values(self) -> Dict[str, float]:
        copying_fixed_costs_values: Dict[str, float] = super()._calculate_copying_fixed_costs_values()
        copying_fixed_costs_values.update({'F(ACQ)s': (self._u + (3 * self._small_delta) + self._delta - self._K) / 2,
                                           'F(ACQ)c': self._small_delta - self._K / 2})
        return copying_fixed_costs_values


class TwoSidedMarketModel(BaseModel):
    def __init__(self, u: float = 1, B: float = 0.5, small_delta: float = 0.5, delta: float = 0.51,
                 K: float = 0.2, gamma: float = 0.5) -> None:
        assert 0 < gamma < 1, "Gamma has to be between 0 and 1."
        assert K < small_delta < gamma * small_delta + delta, "(A4) not satisfied."
        assert small_delta * (1 - small_delta) < u + delta, "(A5) not satisfied."
        super(TwoSidedMarketModel, self).__init__(u=u, B=B, small_delta=small_delta, delta=delta, K=K)


if __name__ == '__main__':
    base_model = BaseModel()
    base_model.plot_equilibrium()
    base_model.plot_incumbent_best_answers()
    base_model.plot_utilities()
    print(base_model)
