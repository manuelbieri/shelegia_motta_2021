This package implements the models of [Shelegia and Motta (2021)](https://github.com/manuelbieri/shelegia_motta_2021/blob/f48f46ad2a37e3686189f17650d0923a88c1ae0d/Shelegia%20and%20Motta%20(2021).pdf).

![GitHub](https://img.shields.io/github/license/manuelbieri/shelegia_motta_2021)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Shelegia-Motta-2021)
![GitHub repo size](https://img.shields.io/github/repo-size/manuelbieri/shelegia_motta_2021)
![GitHub last commit](https://img.shields.io/github/last-commit/manuelbieri/shelegia_motta_2021)
![CI](https://github.com/manuelbieri/shelegia_motta_2021/actions/workflows/ci.yml/badge.svg)
![CodeQL](https://github.com/manuelbieri/shelegia_motta_2021/actions/workflows/codeql.yml/badge.svg)
![GitHub Release Date](https://img.shields.io/github/release-date/manuelbieri/shelegia_motta_2021)
![PyPi](https://github.com/manuelbieri/shelegia_motta_2021/actions/workflows/python-publish.yml/badge.svg)
![PyPI](https://img.shields.io/pypi/v/Shelegia-Motta-2021)
![PyPI - Status](https://img.shields.io/pypi/status/Shelegia-Motta-2021)
![GitHub deployments](https://img.shields.io/github/deployments/manuelbieri/shelegia_motta_2021/github-pages?label=Documentation)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/manuelbieri/shelegia_motta_2021/HEAD)

### Installation
Installation over [PyPI](https://pypi.org/project/Shelegia-Motta-2021/):
```
pip install Shelegia-Motta-2021
```

Or installation over [GitHub](https://github.com/manuelbieri/shelegia_motta_2021):
```
pip install git+https://github.com/manuelbieri/shelegia_motta_2021.git
```

### Introduction

The theory of the “kill zone” has become an increasingly prominent cause for concern among economists in recent times, especially with the rise of digital companies that have become monopolists in their sectors internationally. Companies like Facebook are continuously acquiring start-ups that may have a chance of competing with them in some way in the future. The sheer size and dominance of these companies combined with their aggression regarding the acquisition of competitors makes entering these markets as a direct competitor very unattractive at first glance. However, this issue is not as one-sided as that. This paper aims to rationalize the well-known “kill zone” argument by providing a simple model that explores how and when an incumbent firm may induce an entrant to choose a “non-aggressive” innovation path and enter with the goal of being acquired.

The different models revealed that platform-owning incumbents react in diametrically opposing fashion to an entrant’s plans to develop a substitute to their platform and a complement. When a larger firm is dominating a certain sector and new firms are trying to enter this market, these firms may feel a hesitation to produce a direct competitor to the products of the incumbent, and they will veer more towards producing a compliment as the prospect of the incumbent copying or acquiring the entrant looms. This is the reason a “kill zone” may emerge. Interestingly, the possibility of an acquisition by the incumbent does not worsen the “kill zone” effect. In fact, it may even induce the entrant to develop a product that rivals the incumbent in the hope of being acquired as this can generate massive profits for the smaller entrant. Meanwhile, a two – sided market will not alter the “kill zone” significantly compared to the basic model. Only simultaneous choices of both parties will avoid the existence of a “kill zone” since the choice of the entrant cannot prevent the incumbent to copy the entrant.


Since all models implement the Shelegia_Motta_2021.IModel.IModel - Interface, therefore all models provide the same functionality (public methods), even though the results may change substantially.

For all models add the following import statement:
```python
import Shelegia_Motta_2021.Models
```

### Models
#### Base Model

The base model of the project consists of two players: The incumbent, which sells the primary product,
and a start-up otherwise known as the entrant which sells a complementary product to the incumbent.
One way to visualize a real-world application of this model would be to think of the entrant as a product or service
that can be accessed through the platform of the incumbent, like a plug in that can be accessed through Google or a game on Facebook.
The aim of this model is to monitor the choice that the entrant has between developing a substitute to or
another compliment to the incumbent. The second aim is to observe the choice of the incumbent of whether
to copy the original complementary product of the entrant by creating a perfect substitute or not.
Seeing as the entrant may not have enough assets to fund a second product, the incumbent copying its first product
would inhibit the entrant’s ability to fund its projects. This report will illustrate how the incumbent has a strategic incentive to copy
the entrant if it is planning to compete and that it would refrain from copying if the entrant plans to develop a compliment.
The subsequent models included in this report will introduce additional factors but will all be based on the basic model.

The equilibrium path arguably supports the “kill zone” argument: due to the risk of an exclusionary strategy by the incumbent,
a potential entrant may prefer to avoid a market trajectory which would lead it to compete with the core product of a dominant incumbent
and would choose to develop another complementary product instead.

```python
base_model = Shelegia_Motta_2021.Models.BaseModel()
```

#### Bargaining Power Model

Besides the parameters used in the paper (and in the BaseModel), this class will introduce the parameter $\beta$ in the models, called
the bargaining power of the incumbent. $\beta$ describes how much of the profits from the complementary product of the entrant will go to the incumbent
In the paper the default value $\beta=0.5$ is used to derive the results, which indicate an equal share of the profits.

```python
bargaining_power_model = Shelegia_Motta_2021.Models.BargainingPowerModel()
```

#### Unobservable Choices Model

This model indicates that if the incumbent were not able to observe the entrant at the moment of choosing,
the “kill zone” effect whereby the entrant stays away from the substitute in order to avoid being copied would not take place.
Intuitively, in the game as we studied it so far, the only reason why the entrant is choosing a trajectory leading to another complement
is that it anticipates that if it chose one leading to a substitute, the incumbent would copy, making it an inefficient strategy
for entering the market. However, if the incumbent cannot observe the entrant’s choice of strategy, the entrant could not hope to strategically affect the decision
of the incumbent. This would lead to the entrant having a host of new opportunities when entering the market makes the entrant competing with a large company much more attractive.

Although there may be situations where the entrant could commit to some actions (product design or marketing choices)
which signals that it will not become a rival, and it would have all the incentive to commit to do so,
then the game would be like the sequential moves game analyzed in the basic model.
Otherwise, the entrant will never choose a complement just to avoid copying, and it will enter the “kill zone”.

```python
unobservable_model = Shelegia_Motta_2021.Models.UnobservableModel()
```

#### Acquisition Model

In order to explore how acquisitions may modify the entrant’s and the incumbent’s strategic choices, we extend the base model
in order to allow an acquisition to take place after the incumbent commits to copying the entrant’s original complementary product
(between t=1 and t=2, see demo.ipynb "Timing of the game"). We assume that the incumbent and the entrant share the gains (if any) attained from the acquisition equally.

The “kill zone” still appears as a possible equilibrium outcome, however for a more reduced region of the parameter space.
The prospect of getting some acquisition gains does tend to increase the profits gained from developing a substitute to the primary product,
and this explains why part of the “kill zone” region where a complement was chosen without the acquisition, the entrant will now choose a substitute instead.

```python
acquisition_model = Shelegia_Motta_2021.Models.AcquisitionModel()
```

##### Alternative formulations of the acquisition game
An alternative formulation could be introduced in order to allow acquisitions to take place before the copying decision by the incumbent. The results are qualitatively like the results of the model which had the acquisition after the copying decision. In this alternative formulation of the game, copying would never occur along the equilibrium path. Indeed, there would be an additional source of gains from acquisition consisting of avoiding the fixed cost of copying.


### Basic usage

```python
# import package
import Shelegia_Motta_2021.Models

# every model type can be plugged in without changing the following code.
# initialize model with custom parameters
model: Shelegia_Motta_2021.IModel.IModel = Shelegia_Motta_2021.Models.BaseModel()

# print string representation of the model
print(model)

# plot the payoffs for different market configurations for all stakeholders
model.plot_payoffs()

# plot the best answers of the incumbent to the choice of the entrant
model.plot_incumbent_best_answers()

# plot the equilibrium path
model.plot_equilibrium()

# not necessary when working with jupyter notebooks
plt.show()
```

A demonstration of the code can be found in [demo.html](demo.html) (output of [demo.ipynb](demo.ipynb), on small screens it may not be displayed correctly).

### Dependencies

| Package &emsp; | Version &emsp; | Annotation &emsp;                               |
|:---------------|:--------------:|:------------------------------------------------|
| matplotlib     |     3.9.2      | Always needed (includes numpy)                  |
| jupyter        |     1.1.1      | Just for the demonstration in demo.ipynb        |
| IPython        |     8.27.0     | Just for the demonstration in demo.ipynb        |
| pdoc           |     14.7.0     | Only to generate the documentation from scratch |
<br>
Install the dependencies with the following command:

```bash
pip install -r requirements.txt
```
(Note: Make sure you are operating in the same directory as the `requirements.txt` is located.)

These packages include all the needed imports for the functionality of this package.

#### Additional Notes
For further information about the project (structure) and the code, see [resources/dev_notes.md](https://github.com/manuelbieri/shelegia_motta_2021/blob/master/resources/dev_notes.md).

#### Tests

Run the testsuite with the following command:

```bash
python -m unittest Shelegia_Motta_2021_Test/*Test.py
```

### Documentation
For the latest version of the documentation open [manuelbieri.github.io/shelegia_motta_2021](https://manuelbieri.github.io/shelegia_motta_2021/Shelegia_Motta_2021.html) in your browser or call:
```python
import Shelegia_Motta_2021

Shelegia_Motta_2021.docs()
```

#### Build Documentation

Generate api-documentation with the following command (note the use of `pdoc`):
```bash
pdoc -o ./docs Shelegia_Motta_2021 --docformat "numpy" --math
```
