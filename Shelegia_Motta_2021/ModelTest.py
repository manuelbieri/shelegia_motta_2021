import unittest
from typing import Dict

from Shelegia_Motta_2021.IModel import IModel
from Shelegia_Motta_2021.Models import BaseModel


class BaseModelTest(unittest.TestCase):
    @staticmethod
    def setUpModel() -> IModel:
        return BaseModel()

    def setUp(self) -> None:
        self.model: IModel = self.setUpModel()
        self.copying_fixed_costs: Dict[str, float] = self.model.get_copying_fixed_costs_values()
        self.assets: Dict[str, float] = self.model.get_asset_values()
        self.utility: Dict[str, Dict[str, float]] = self.model.get_utility_values()

    def test_invalid_A1b(self):
        self.assertRaises(AssertionError, BaseModel, small_delta=0.2)
        self.assertRaises(AssertionError, BaseModel, delta=0.2)

    def test_invalid_A2(self):
        self.assertRaises(AssertionError, BaseModel, K=0.3)

    def test_path_indifferent_copy(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"]*0.9, F=self.copying_fixed_costs["F(YN)c"]*0.9)
        self.assertEqual(choice["entrant"], self.model.ENTRANT_CHOICES["indifferent"])
        self.assertEqual(choice["incumbent"], self.model.INCUMBENT_CHOICES["copy"])
        self.assertEqual(choice["development"], self.model.DEVELOPMENT_OUTCOME["failure"])

    def test_path_kill_zone(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"]*0.9, F=self.copying_fixed_costs["F(YN)c"]*1.1)
        self.assertEqual(choice["entrant"], self.model.ENTRANT_CHOICES["complement"])
        self.assertEqual(choice["incumbent"], self.model.INCUMBENT_CHOICES["refrain"])
        self.assertEqual(choice["development"], self.model.DEVELOPMENT_OUTCOME["success"])

    def test_path_substitute_refrain(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"]*1.1, F=self.copying_fixed_costs["F(YN)c"]*1.1)
        self.assertEqual(choice["entrant"], self.model.ENTRANT_CHOICES["substitute"])
        self.assertEqual(choice["incumbent"], self.model.INCUMBENT_CHOICES["refrain"])
        self.assertEqual(choice["development"], self.model.DEVELOPMENT_OUTCOME["success"])

    def test_path_substitute_copy(self):
        choice: Dict[str, str] = self.model.get_optimal_choice(A=self.assets["A-s"]*1.1, F=self.copying_fixed_costs["F(YN)c"]*0.9)
        self.assertEqual(choice["entrant"], self.model.ENTRANT_CHOICES["substitute"])
        self.assertEqual(choice["incumbent"], self.model.INCUMBENT_CHOICES["copy"])
        self.assertEqual(choice["development"], self.model.DEVELOPMENT_OUTCOME["success"])
