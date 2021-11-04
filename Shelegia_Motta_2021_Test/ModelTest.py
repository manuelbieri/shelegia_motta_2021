import unittest
from typing import Dict

from Shelegia_Motta_2021.IModel import IModel
from Shelegia_Motta_2021.Models import BaseModel, BargainingPowerModel, UnobservableModel


class BaseModelTest(unittest.TestCase):
    """
    Tests the constraints and the optimal choice method in the base model.

    See dev_notes.md for the enumeration of the areas used in the testcases.
    """
    @staticmethod
    def setUpModel() -> IModel:
        return BaseModel()

    def setUp(self) -> None:
        self.model: IModel = self.setUpModel()
        self.copying_fixed_costs: Dict[str, float] = self.model.get_copying_fixed_costs_values()
        self.assets: Dict[str, float] = self.model.get_asset_values()
        self.utility: Dict[str, Dict[str, float]] = self.model.get_payoffs()

    def assert_area_one(self, choice: Dict[str, str]):
        self.assertEqual(choice["entrant"], self.model.ENTRANT_CHOICES["indifferent"])
        self.assertEqual(choice["incumbent"], self.model.INCUMBENT_CHOICES["copy"])
        self.assertEqual(choice["development"], self.model.DEVELOPMENT_OUTCOME["failure"])

    def assert_area_two(self, choice: Dict[str, str]):
        self.assertEqual(choice["entrant"], self.model.ENTRANT_CHOICES["substitute"])
        self.assertEqual(choice["incumbent"], self.model.INCUMBENT_CHOICES["copy"])
        self.assertEqual(choice["development"], self.model.DEVELOPMENT_OUTCOME["success"])

    def assert_area_three(self, choice: Dict[str, str]):
        self.assertEqual(choice["entrant"], self.model.ENTRANT_CHOICES["complement"])
        self.assertEqual(choice["incumbent"], self.model.INCUMBENT_CHOICES["refrain"])
        self.assertEqual(choice["development"], self.model.DEVELOPMENT_OUTCOME["success"])

    def assert_area_four(self, choice: Dict[str, str]):
        self.assertEqual(choice["entrant"], self.model.ENTRANT_CHOICES["substitute"])
        self.assertEqual(choice["incumbent"], self.model.INCUMBENT_CHOICES["refrain"])
        self.assertEqual(choice["development"], self.model.DEVELOPMENT_OUTCOME["success"])

    def test_invalid_A1b(self):
        self.assertRaises(AssertionError, BaseModel, small_delta=0.2)
        self.assertRaises(AssertionError, BaseModel, delta=0.2)

    def test_invalid_A2(self):
        self.assertRaises(AssertionError, BaseModel, K=0.3)

    def test_path_indifferent_copy(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"]*0.9, F=self.copying_fixed_costs["F(YN)c"]*0.9)
        self.assert_area_one(choice)

    def test_path_kill_zone(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"]*0.9, F=self.copying_fixed_costs["F(YN)c"]*1.1)
        self.assert_area_three(choice)

    def test_path_substitute_refrain(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"]*1.1, F=self.copying_fixed_costs["F(YY)s"]*1.1)
        self.assert_area_four(choice)

    def test_path_substitute_copy(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"]*1.1, F=self.copying_fixed_costs["F(YY)s"]*0.9)
        self.assert_area_two(choice)

    def test_path_four_areas_corner(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"], F=self.copying_fixed_costs["F(YY)s"])
        self.assert_area_two(choice)

    def test_path_area_three_area_four_corner(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"], F=self.copying_fixed_costs["F(YN)s"])
        self.assert_area_four(choice)

    def test_path_area_three_area_four(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"]*0.9, F=self.copying_fixed_costs["F(YN)s"])
        self.assert_area_three(choice)

    def test_path_area_one_area_two(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"], F=min(self.copying_fixed_costs["F(YY)s"], self.copying_fixed_costs["F(YN)c"])*0.9)
        self.assert_area_two(choice)

    def test_path_area_one_area_three(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"]*0.9, F=self.copying_fixed_costs["F(YN)c"])
        self.assert_area_three(choice)

    def test_path_area_two_area_four(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"]*1.1, F=self.copying_fixed_costs["F(YY)s"])
        self.assert_area_two(choice)


class BargainingPowerModelTestBeta6(BaseModelTest):
    """
    Tests the constraints and the optimal choice method in the BargainingPowerModel with beta=0.6.

    See dev_notes.md for the enumeration of the areas used in the testcases.
    """
    @staticmethod
    def setUpModel() -> IModel:
        return BargainingPowerModel(beta=0.6)

    def test_path_area_two_area_three(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"], F=(self.copying_fixed_costs["F(YY)s"] + self.copying_fixed_costs["F(YN)c"])/2)
        self.assert_area_two(choice)


class BargainingPowerModelTestBeta4(BaseModelTest):
    """
    Tests the constraints and the optimal choice method in the BargainingPowerModel with beta=0.4.

    See dev_notes.md for the enumeration of the areas used in the testcases.
    """
    @staticmethod
    def setUpModel() -> IModel:
        return BargainingPowerModel(beta=0.4)

    def test_path_area_one_area_four(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"], F=(self.copying_fixed_costs["F(YY)s"] + self.copying_fixed_costs["F(YN)c"])/2)
        self.assert_area_four(choice)


class UnobservableModelTestBeta6(BargainingPowerModelTestBeta6):
    """
    Tests the constraints and the optimal choice method in the UnobservableModel with beta=0.6.

    See dev_notes.md for the enumeration of the areas used in the testcases.
    """
    @staticmethod
    def setUpModel() -> IModel:
        return UnobservableModel(beta=0.6)

    def assert_area_three(self, choice: Dict[str, str]):
        self.assertEqual(choice["entrant"], self.model.ENTRANT_CHOICES["substitute"])
        self.assertEqual(choice["incumbent"], self.model.INCUMBENT_CHOICES["copy"])
        self.assertEqual(choice["development"], self.model.DEVELOPMENT_OUTCOME["failure"])


class UnobservableModelTestBeta4(BargainingPowerModelTestBeta4):
    """
    Tests the constraints and the optimal choice method in the UnobservableModel with beta=0.4.

    See dev_notes.md for the enumeration of the areas used in the testcases.
    """
    @staticmethod
    def setUpModel() -> IModel:
        return UnobservableModel(beta=0.4)

    def assert_area_three(self, choice: Dict[str, str]):
        self.assertEqual(choice["entrant"], self.model.ENTRANT_CHOICES["substitute"])
        self.assertEqual(choice["incumbent"], self.model.INCUMBENT_CHOICES["copy"])
        self.assertEqual(choice["development"], self.model.DEVELOPMENT_OUTCOME["failure"])
