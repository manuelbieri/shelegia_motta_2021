## Additional Notes

Here you can find some helpful information about the project and the code.

### Project Structure

```
.
+-- .github # includes workflows for the repository
|
+-- docs # includes the API - Documentation
|
+-- resources # includes files for the better understanding of the code
|   +-- dev_notes.md # this file with further information about the code and project structure
|   +-- bargaining_power_beta.pdf # derivation of the additional parameter beta (called the bargaining power of the incumbent)
|
+-- Shelegia_Motta_2021 # package published on PyPI
|   +-- IModel.py # interface used in the models
|   +-- Models.py # models implementing the logic
|
+-- Shelegia_Motta_2021_Test # unittests for the package
|   +-- ModelTest.py # tests the equilibrium path logic (excluded from the PyPI package)
|
+-- demo.ipynb # demonstration of the functionality provided by the package and summary of the paper
|
+-- demo.html # output of demo.ipynb for display in the browser
|
+-- LICENSE # the package is published under the MIT - license
|
+-- README.md # contains an overview over the package and models 
|
+-- requirements.txt # contains all the informations for the necessary packages for this repository
|
+-- setup.py # contains all the informations to build and install the package
|
+-- Shelegia and Motta (2021).pdf # the package is based on this paper
|
+-- slides.ipynb # slides generated from demo.ipynb
```

### Class Hierarchy
![](plots-uml_class.svg)

The implementation of the classes can be found in Models.py.

### Enumeration of the Areas in the Code

The following images will show, which area in the code corresponds to which area in the images in the paper.
The number of the area is denoted in brackets (i.e. (1)).

Additionally, the points used in the testcases are denoted.

#### BaseModel
![](plots-base.svg)

#### BargainingPowerModel
![](plots-bargaining_power.svg)

#### UnobservableModel
![](plots-unobservable.svg)

#### AcquisitionModel
![](plots-acquisition.svg)
