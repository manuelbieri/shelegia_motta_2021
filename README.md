This package implements the models of [Shelegia and Motta (2021)](shelegia_motta_2021.pdf).

![GitHub](https://img.shields.io/github/license/manuelbieri/shelegia_motta_2021)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Shelegia-Motta-2021)
![GitHub repo size](https://img.shields.io/github/repo-size/manuelbieri/shelegia_motta_2021)
![GitHub last commit](https://img.shields.io/github/last-commit/manuelbieri/shelegia_motta_2021)
![CI](https://github.com/manuelbieri/shelegia_motta_2021/actions/workflows/ci.yml/badge.svg)
![CodeQL](https://github.com/manuelbieri/shelegia_motta_2021/actions/workflows/codeql-analysis.yml/badge.svg)
![OSSAR](https://github.com/manuelbieri/shelegia_motta_2021/actions/workflows/ossar-analysis.yml/badge.svg)
![GitHub Release Date](https://img.shields.io/github/release-date/manuelbieri/shelegia_motta_2021)
![PyPi](https://github.com/manuelbieri/shelegia_motta_2021/actions/workflows/pypi.yml/badge.svg)
![PyPI](https://img.shields.io/pypi/v/Shelegia-Motta-2021)
![PyPI - Status](https://img.shields.io/pypi/status/Shelegia-Motta-2021)
![GitHub deployments](https://img.shields.io/github/deployments/manuelbieri/shelegia_motta_2021/github-pages?label=Documentation)
[![badge](https://img.shields.io/badge/launch-binder-579ACA.svg?logo=data:image/png;base64,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)](https://hub.gke2.mybinder.org/user/manuelbieri-shelegia_motta_2021-2omkm9cw/doc/tree/demo.ipynb)

### Installation
Installation over [PyPI](https://pypi.org/project/Shelegia-Motta-2021/):
```
pip install Shelegia-Motta-2021
```

Or clone the repository via [GitHub](https://github.com/manuelbieri/shelegia_motta_2021):
```
git clone https://github.com/manuelbieri/shelegia_motta_2021.git
```

### Introduction

The theory of the “kill zone” has become an increasingly prominent cause for concern among economists in recent times, especially with the rise of digital companies that have become monopolists in their sectors internationally. Companies like Facebook are continuously acquiring start-ups that may have a chance of competing with them in some way in the future. The sheer size and dominance of these companies combined with their aggression regarding the acquisition of competitors makes entering these markets as a direct competitor very unattractive at first glance. However, this issue is not as one sided as that. This paper aims to rationalize the well-known “kill zone” argument by providing a simple model that explores how and when an incumbent ﬁrm may induce an entrant to choose a “non-aggressive” innovation path and enter with the goal of being acquired.

The different models revealed that platform-owning incumbents react in diametrically opposing fashion to an entrant’s plans to develop a substitute to their platform and a complement. When a larger firm is dominating a certain sector and new firms are trying to enter this market, these firms may feel a hesitation to produce a direct competitor to the products of the incumbent and they will veer more towards producing a compliment as the prospect of the incumbent copying or acquiring the entrant looms. This is the reason a “kill zone” may emerge. Interestingly, the possibility of an acquisition by the incumbent does not worsen the “kill zone” effect. In fact, it may even induce the entrant to develop a product that rivals the incumbent in the hope of being acquired as this can generate massive profits for the smaller entrant. Meanwhile, a two – sided market will not alter the “kill zone” significantly compared to the basic model. Only simultaneous choices of both parties will avoid the existence of a “kill zone” since the choice of the entrant cannot prevent the incumbent to copy the entrant.


Since all models implement the Shelegia_Motta_2021.IModel.IModel - Interface, therefore all models provide the same functionality (public methods), even though the results may change substantially.

For all models add the following import statement:
```
import Shelegia_Motta_2021.Models
```

### Models
#### Base Model

The base model of the project consists of two players: The incumbent, denoted as Ip, which sells the primary product,
and a start-up otherwise known as the entrant which sells a complementary product to the incumbent (E).
One way to visualize a real-world application of this model would be to think of the entrant as a product or service
that can be accessed through the platform of the incumbent, like a plug in that can be accessed through Google or a game on Facebook.
The aim of this model is to monitor the choice that the entrant has between developing a substitute (Ep) to or
another compliment (Ec) to the incumbent. The second aim is to observe the choice of the incumbent of whether
to copy the original complementary product of the entrant by creating a perfect substitute (Ip) or not.
Seeing as the entrant may not have enough assets to fund a second product, the incumbent copying its first product
would inhibit the entrant’s ability to fund its projects. This report will illustrate how the incumbent has a strategic incentive to copy
the entrant if it is planning to compete and that it would refrain from copying if the entrant plans to develop a compliment.
The subsequent models included in this report will introduce additional factors but will all be based on the basic model.

The equilibrium path arguably supports the “kill zone” argument: due to the risk of an exclusionary strategy by the incumbent,
a potential entrant may prefer to avoid a market trajectory which would lead it to compete with the core product of a dominant incumbent
and would choose to develop another complementary product instead.

```
base_model = Shelegia_Motta_2021.Models.BaseModel()
```

#### Bargaining Power Model



```
bargaining_power_model = Shelegia_Motta_2021.Models.BargainingPowerModel()
```

#### Unobservable Choices Model

This model indicates that if the incumbent were not able to observe the entrant at the moment of choosing,
the “kill zone” effect whereby the entrant stays away from the substitute in order to avoid being copied) would not take place.
Intuitively, in the game as we studied it so far, the only reason why the entrant is choosing a trajectory leading to another complement
is that it anticipates that if it chose one leading to a substitute, the incumbent would copy, making it an inefficient strategy
for entering the market. However, if the incumbent cannot observe the entrant’s choice of strategy, the entrant could not hope to strategically affect the decision
of the incumbent. This would lead to the entrant having a host of new opportunities when entering the market and it makes competing with a large company much more attractive.

Although there may be situations where the entrant could commit to some actions (product design or marketing choices)
which signals that it will not become a rival, and it would have all the incentive to commit to do so,
then the game would be like the sequential moves game analyzed in the basic model.
Otherwise, the entrant will never choose a complement just to avoid copying, and it will enter the “kill zone”.

```
unobservable_model = Shelegia_Motta_2021.Models.UnobservableModel()
```

#### Acquisition Model

In order to explore how acquisitions may modify the entrant’s and the incumbent’s strategic choices, we extend the base model
in order to allow an acquisition to take place after the incumbent commits to copying the entrant’s original complementary product
(between t=1 and t=2, see table 2). We assume that the incumbent and the entrant share the gains (if any) attained from the acquisition equally.

The “kill zone” still appears as a possible equilibrium outcome, however for a more reduced region of the parameter space.
The prospect of getting some of the acquisition gains does tend to increase the proﬁts gained from developing a substitute to the primary product,
and this explains why part of the “kill zone” region where a complement was chosen without the acquisition, the entrant will now choose a substitute instead.

```
acquisition_model = Shelegia_Motta_2021.Models.AcquisitionModel()
```

### Basic usage



```
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

### Dependencies

| Package &emsp;| Version &emsp; | Annotation &emsp;                                     |
|:-----------|:---------|:------------------------------------------------|
| matplotlib | 3.4.3    | Always needed (includes numpy)                  |
| jupyter    | 1.0.0    | Just for the demonstration in demo.ipynb        |
| pdoc       | 8.0.1    | Only to generate the documentation from scratch |
<br>
These packages include all the needed imports for the functionality of this package.

### Documentation
For the latest version of the documentation open [manuelbieri.github.io/shelegia_motta_2021](https://manuelbieri.github.io/shelegia_motta_2021/Shelegia_Motta_2021.html) in your browser or call:
```
import Shelegia_Motta_2021

Shelegia_Motta_2021.docs()
```

#### Build Documentation
Install the pdoc package:
```
pip install pdoc
```
Generate api-documentation with the following command:
```
pdoc -o ./docs Shelegia_Motta_2021 --docformat "numpy" --math
```

#### Additional Notes
For further information about the coordinates used in the code, see resources/dev_notes.md.
