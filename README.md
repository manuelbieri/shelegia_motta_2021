This package implements the models of [Shelegia and Motta (2021)](shelegia_motta_2021.pdf).

![GitHub](https://img.shields.io/github/license/manuelbieri/shelegia_motta_2021)
![GitHub language count](https://img.shields.io/github/languages/count/manuelbieri/shelegia_motta_2021)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Shelegia-Motta-2021)
![GitHub top language](https://img.shields.io/github/languages/top/manuelbieri/shelegia_motta_2021)
![GitHub repo size](https://img.shields.io/github/repo-size/manuelbieri/shelegia_motta_2021)
![GitHub last commit](https://img.shields.io/github/last-commit/manuelbieri/shelegia_motta_2021)
![PyPi](https://github.com/manuelbieri/shelegia_motta_2021/actions/workflows/pypi.yml/badge.svg)
![PyPI](https://img.shields.io/pypi/v/Shelegia-Motta-2021)
![PyPI - Status](https://img.shields.io/pypi/status/Shelegia-Motta-2021)
![GitHub Release Date](https://img.shields.io/github/release-date/manuelbieri/shelegia_motta_2021)
![GitHub deployments](https://img.shields.io/github/deployments/manuelbieri/shelegia_motta_2021/github-pages?label=Documentation)

### Installation
Installation over PyPI:
```
pip install Shelegia-Motta-2021
```

### Introduction
Since all models implement the Shelegia_Motta_2021.IModel.IModel - Interface, therefore all models provide the same functionality (public methods), even though the results may change substantially.

For all models add the following import statement:
```
import Shelegia_Motta_2021.Models
```

### Models
#### Base Model
```
base_model = Shelegia_Motta_2021.Models.BaseModel()
```

#### Unobservable Choices Model
```
unobservable_model = Shelegia_Motta_2021.Models.UnobservableModel()
```

#### Acquisition Model
```
acquisition_model = Shelegia_Motta_2021.Models.AcquisitionModel()
```

#### Two-sided Market Model
```
two_sided_market_model = Shelegia_Motta_2021.Models.TwoSidedMarketModel()
```

### Basic usage
```
# every model type can be plugged in
model: Shelegia_Motta_2021.IModel.IModel = Shelegia_Motta_2021.BaseModel()

# print string representation of the model
print(model)

# plot the best answers of the incumbent to the choice of the entrant
model.plot_incumbent_best_answers()

# plot the equilibrium path
model.plot_equilibrium()
```

### Documentation
Install the pdoc package:
```
pip install pdoc
```
Generate api-documentation with the following command:
```
pdoc -o ./docs Shelegia_Motta_2021
```