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


def docs() -> None:
    """
    Opens the latest published version of the documentation of this package.
    """
    import webbrowser
    webbrowser.open('https://manuelbieri.github.io/shelegia_motta_2021/Shelegia_Motta_2021.html')
