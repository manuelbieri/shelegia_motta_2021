from typing import Dict, List, Tuple

import matplotlib.axes
import matplotlib.pyplot as plt

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

    def __init__(self, u: float = 1, B: float = 0.5, small_delta: float = 0.5, delta: float = 0.51, K: float = 0.2):
        self.u: float = u
        self.B: float = B
        self.small_delta: float = small_delta
        self.delta: float = delta
        self.K: float = K
        self.funding: Dict[str, float] = self.calculate_funding_values()
        self.assets: Dict[str, float] = self.calculate_asset_values()

    def calculate_funding_values(self) -> Dict[str, float]:
        """
        Calculates the thresholds for the funding of the incumbent.

        Includes:<br>
        - (6) F(YY)s = small_delta / 2
        - (6) F(YN)s = u + 3 * small_delta / 2
        - (6) F(YY)c = small_delta
        - (6) F(YN)c = small_delta / 2

        :return: dict including the thresholds for the funding of the incumbent.
        """
        return {'F(YY)s': self.small_delta / 2,
                'F(YN)s': self.small_delta * 3 / 2,
                'F(YY)c': self.small_delta,
                'F(YN)c': self.small_delta / 2}

    def calculate_asset_values(self) -> Dict[str, float]:
        """
        Calculates the thresholds for the assets of the entrant.

        Includes:
        - (2) A >= A_s = B - (delta + 3 * small_delta / 2 - K)
        - (3) A >= A_c = B - (3 * small_delta / 2 - K)
        - (4) A >= A-s = B - (delta - K)
        - (5) A >= A-c = B - (small_delta / 2 - K)

        :return: dict including the thresholds for the assets of the entrant.
        """
        return {'A_s': self.B - (self.delta + 3 / 2 * self.small_delta - self.K),
                'A_c': self.B - (3 / 2 * self.small_delta - self.K),
                'A-s': self.B - (self.delta - self.K),
                'A-c': self.B - (1 / 2 * self.small_delta - self.K)}

    def get_asset_values(self) -> Dict[str, float]:
        return self.assets

    def get_funding_values(self) -> Dict[str, float]:
        return self.funding

    def get_optimal_choice(self, A: float, F: float):
        pass

    def plot_incumbent_best_answers(self, axis: matplotlib.axes.Axes = None) -> None:
        """
        Plots the best answers of the incumbent to every choice of the entrant, according to figure 1.

        :param axis: to plot the answers to (optional).
        """
        if axis is None:
            fig, axis = plt.subplots()
        y_max: float = self._get_y_max()
        x_max: float = self._get_x_max()

        self._draw_horizontal_lines(axis)

        poly_coordinates: List[List[Tuple[float, float]]] = [
            [(0, 0), (self.assets['A-s'], 0), (self.assets['A-s'], self.funding['F(YY)s']),
             (0, self.funding['F(YY)s'])],
            [(0, self.funding['F(YY)s']), (self.assets['A-s'], self.funding['F(YY)s']),
             (self.assets['A-s'], self.funding['F(YN)s']), (0, self.funding['F(YN)s'])],
            [(self.assets['A-s'], 0), (self.assets['A-c'], 0), (self.assets['A-c'], self.funding['F(YY)s']),
             (self.assets['A-s'], self.funding['F(YY)s'])],
            [(self.assets['A-c'], 0), (x_max, 0), (x_max, self.funding['F(YY)s']),
             (self.assets['A-c'], self.funding['F(YY)s'])],
            [(self.assets['A-c'], self.funding['F(YY)s']), (x_max, self.funding['F(YY)s']),
             (x_max, self.funding['F(YY)c']), (self.assets['A-c'], self.funding['F(YY)c'])],
            [(self.assets['A-s'], self.funding['F(YY)s']), (self.assets['A-c'], self.funding['F(YY)s']),
             (self.assets['A-c'], self.funding['F(YY)c']), (x_max, self.funding['F(YY)c']), (x_max, y_max), (0, y_max),
             (0, self.funding['F(YN)s']), (self.assets['A-s'], self.funding['F(YN)s'])]]

        for i, coordinates in enumerate(poly_coordinates):
            poly = plt.Polygon(coordinates, ec="k", color=self._get_color(i))
            axis.add_patch(poly)

        BaseModel._set_axis(axis)
        plt.show()

    def plot_entrant_best_answers(self, axis: matplotlib.axes.Axes = None) -> None:
        """
        Plots the best answers of the entrant for every combination of assets and funding (figure 2).

        :param axis: to plot the answers to (optional).
        """
        if axis is None:
            fig, axis = plt.subplots()
        y_max: float = self._get_y_max()
        x_max: float = self._get_x_max()

        self._draw_horizontal_lines(axis)

        poly_coordinates: List[List[Tuple[float, float]]] = [
            [(0, 0), (self.assets['A-s'], 0), (self.assets['A-s'], self.funding['F(YY)s']),
             (0, self.funding['F(YY)s'])],
            [(0, self.funding['F(YY)s']), (self.assets['A-s'], self.funding['F(YY)s']),
             (self.assets['A-s'], self.funding['F(YN)s']), (0, self.funding['F(YN)s'])],
            [(self.assets['A-s'], 0), (x_max, 0), (x_max, self.funding['F(YY)s']),
             (self.assets['A-s'], self.funding['F(YY)s'])],
            [(self.assets['A-c'], self.funding['F(YY)s']), (x_max, self.funding['F(YY)s']),
             (x_max, self.funding['F(YY)c']), (self.assets['A-c'], self.funding['F(YY)c'])],
            [(self.assets['A-s'], self.funding['F(YY)s']), (x_max, self.funding['F(YY)s']),
             (x_max, y_max), (0, y_max), (0, self.funding['F(YN)s']), (self.assets['A-s'], self.funding['F(YN)s'])]]

        for i, coordinates in enumerate(poly_coordinates):
            poly = plt.Polygon(coordinates, ec="k", color=self._get_color(i))
            axis.add_patch(poly)

        BaseModel._set_axis(axis)
        plt.show()

    def _get_x_max(self) -> float:
        return round(self.assets['A-c'] * 1.3, 1)

    def _get_y_max(self) -> float:
        return round(self.funding['F(YN)s'] * 1.3, 1)

    def _draw_horizontal_lines(self, axis: matplotlib.axes.Axes) -> None:
        axis.axhline(self.funding['F(YN)s'], linestyle='--', color='k')
        axis.axhline(self.funding['F(YY)s'], linestyle='--', color='k')
        axis.axhline(self.funding['F(YY)c'], linestyle='--', color='k')
        axis.axvline(self.assets['A-s'], linestyle='--', color='k')
        axis.axvline(self.assets['A-c'], linestyle='--', color='k')

    @staticmethod
    def _get_color(i: int) -> str:
        return ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'][i]

    @staticmethod
    def _set_axis(axis: matplotlib.axes.Axes):
        axis.margins(0.1)
        axis.relim()
        axis.autoscale_view()

    def __str__(self) -> str:
        str_representation: str = 'Assets:'
        for key in self.assets.keys():
            str_representation += '\n\t- ' + key + ':\t' + str(self.assets[key])

        str_representation += '\nFunding costs:'
        for key in self.funding.keys():
            str_representation += '\n\t- ' + key + ':\t' + str(self.funding[key])

        return str_representation


class UnobservableModel(BaseModel):
    pass


class AcquisitionModel(BaseModel):
    pass


if __name__ == '__main__':
    base_model = BaseModel()
    print(base_model)
    base_model.plot_incumbent_best_answers()
    base_model.plot_entrant_best_answers()
