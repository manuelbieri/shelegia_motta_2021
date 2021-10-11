"""
.. include:: ../README.md
"""
__docformat__ = "restructuredtext"

try:
    from Shelegia_Motta_2021.IModel import IModel
    from Shelegia_Motta_2021.Models import BaseModel, UnobservableModel, AcquisitionModel, TwoSidedMarketModel
except ModuleNotFoundError:
    from IModel import IModel
    from Models import BaseModel, UnobservableModel, AcquisitionModel, TwoSidedMarketModel
