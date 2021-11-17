import unittest
from typing import Dict

from Shelegia_Motta_2021.IModel import IModel
from Shelegia_Motta_2021.Models import BaseModel, BargainingPowerModel, UnobservableModel, AcquisitionModel


class BaseModelTest(unittest.TestCase):
    """
    Tests the constraints and the optimal choice method in the base model.

    See dev_notes.md for the enumeration of the areas and testing points used in the testcases.
    """

    class TestPoint:
        """
        Represents a point consisting of assets of the entrant and fixed costs of copying for the incumbent.
        """
        def __init__(self, A: float, F: float):
            self.A: float = A
            self.F: float = F

    @staticmethod
    def setUpModel() -> IModel:
        return BaseModel()

    def setUpTestPoints(self) -> None:
        """
        Sets up points for the testcases.

        For the position of the points on the coordinate system refer to the file resources/dev_notes.md.
        """
        self.costs: Dict[str, float] = self.model.get_copying_fixed_costs_values()
        self.assets: Dict[str, float] = self.model.get_asset_values()
        self.utility: Dict[str, Dict[str, float]] = self.model.get_payoffs()
        self.a = BaseModelTest.TestPoint(self.assets["A-s"]/2, self.costs["F(YN)c"])
        self.b = BaseModelTest.TestPoint(self.assets["A-s"], min(self.costs["F(YN)c"], self.costs["F(YY)s"])*0.9)
        self.c = BaseModelTest.TestPoint(self.assets["A-s"], self.costs["F(YY)s"])
        self.d = BaseModelTest.TestPoint(self.assets["A-c"], self.costs["F(YY)s"])
        self.e = BaseModelTest.TestPoint(self.assets["A-s"]/2, self.costs["F(YN)s"])
        self.f = BaseModelTest.TestPoint(self.assets["A-s"], self.costs["F(YN)s"])
        self.g = BaseModelTest.TestPoint(self.assets["A-s"], (self.costs["F(YN)c"] + self.costs["F(YY)s"])/2)

    def setUp(self) -> None:
        """
        Sets up the model and points (see resources/dev_notes.md) for the tests.
        """
        self.model: IModel = self.setUpModel()
        self.setUpTestPoints()

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

    def test_path_area_one(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.a.A, F=self.a.F * 0.9)
        self.assert_area_one(choice)

    def test_path_area_three(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.e.A, F=self.e.F * 0.9)
        self.assert_area_three(choice)

    def test_path_area_four(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.d.A, F=self.d.F * 1.1)
        self.assert_area_four(choice)

    def test_path_area_two(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.d.A, F=self.d.F * 0.9)
        self.assert_area_two(choice)

    def test_path_four_areas_corner(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.c.A, F=self.c.F)
        self.assert_area_two(choice)

    def test_path_area_three_area_four_corner(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.f.A, F=self.f.F)
        self.assert_area_four(choice)

    def test_path_area_three_area_four(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.e.A, F=self.e.F)
        self.assert_area_three(choice)

    def test_path_area_one_area_two(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.b.A, F=self.b.F)
        self.assert_area_two(choice)

    def test_path_area_one_area_three(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.a.A, F=self.a.F)
        self.assert_area_three(choice)

    def test_path_area_two_area_four(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.d.A, F=self.d.F)
        self.assert_area_two(choice)


class BargainingPowerModelTest(BaseModelTest):
    """
    Tests the constraints and the optimal choice method in the BargainingPowerModel with beta=0.6.

    See dev_notes.md for the enumeration of the areas used in the testcases.
    """
    @staticmethod
    def setUpModel() -> IModel:
        return BargainingPowerModel(beta=0.6)

    @staticmethod
    def setUpModelLowBeta() -> IModel:
        return BargainingPowerModel(beta=0.4)

    def test_path_area_two_area_three(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.g.A, F=self.g.F)
        self.assert_area_two(choice)

    def test_path_area_one_area_four(self):
        self.model = self.setUpModelLowBeta()
        self.setUpTestPoints()
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.g.A, F=self.g.F)
        self.assert_area_four(choice)


class UnobservableModelTest(BargainingPowerModelTest):
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


class AcquisitionModelTest(BaseModelTest):
    @staticmethod
    def setUpModel() -> IModel:
        return AcquisitionModel()

    def assert_area_one(self, choice: Dict[str, str]):
        self.assertEqual(choice["entrant"], self.model.ENTRANT_CHOICES["substitute"])
        self.assertEqual(choice["incumbent"], self.model.INCUMBENT_CHOICES["copy"])
        self.assertEqual(choice["development"], self.model.DEVELOPMENT_OUTCOME["success"])
        self.assertEqual(choice["acquisition"], self.model.ACQUISITION_OUTCOME["merged"])

    def assert_area_two(self, choice: Dict[str, str]):
        super(AcquisitionModelTest, self).assert_area_two(choice)
        self.assertEqual(choice["acquisition"], self.model.ACQUISITION_OUTCOME["merged"])

    def assert_area_three(self, choice: Dict[str, str]):
        super(AcquisitionModelTest, self).assert_area_three(choice)
        self.assertEqual(choice["acquisition"], self.model.ACQUISITION_OUTCOME["apart"])

    def assert_area_four(self, choice: Dict[str, str]):
        super(AcquisitionModelTest, self).assert_area_four(choice)
        self.assertEqual(choice["acquisition"], self.model.ACQUISITION_OUTCOME["merged"])

    def setUpTestPoints(self):
        super(AcquisitionModelTest, self).setUpTestPoints()
        self.a = BaseModelTest.TestPoint(self.assets["A-s"]/2, self.costs["F(ACQ)c"])
        self.b = BaseModelTest.TestPoint(self.assets["A-s"], self.costs["F(ACQ)c"])
        self.c = BaseModelTest.TestPoint(self.assets["A-s"], self.costs["F(YY)c"])
        self.d = BaseModelTest.TestPoint(self.assets["A-c"], self.costs["F(YY)c"])
        self.e = BaseModelTest.TestPoint(self.assets["A-s"]/2, self.costs["F(ACQ)s"])
        self.f = BaseModelTest.TestPoint(self.assets["A-s"], self.costs["F(ACQ)s"])
        self.g = BaseModelTest.TestPoint(self.assets["A-s"], (self.costs["F(ACQ)c"] + self.costs["F(YY)s"])/2)

    def test_setUpInvalidThresholds(self):
        """
        Tests the violation of the following condition: $F^{ACQ}_C <= F^{YY}_C$
        """
        self.assertRaises(AssertionError, AcquisitionModel, beta=0.2)

    def test_area_one_small_delta_bigger_than_delta(self):
        self.model = AcquisitionModel(small_delta=0.52)
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.a.A, F=self.a.F * 0.9)
        self.assertEqual(choice["entrant"], self.model.ENTRANT_CHOICES["complement"])
        self.assertEqual(choice["incumbent"], self.model.INCUMBENT_CHOICES["copy"])
        self.assertEqual(choice["development"], self.model.DEVELOPMENT_OUTCOME["success"])
        self.assertEqual(choice["acquisition"], self.model.ACQUISITION_OUTCOME["merged"])
