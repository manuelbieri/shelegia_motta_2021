This package implements the models of [Shelegia and Motta (2021)](shelegia_motta_2021.pdf).

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