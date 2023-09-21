# Schengen-Border-Control

## Description

This project provides the functionality to call python functions, which return json data of the current temporary border status of all schengen countries.
This projects scrapes its data from [the official website](https://home-affairs.ec.europa.eu/policies/schengen-borders-and-visa/schengen-area/temporary-reintroduction-border-control_en).

## Dependencies

python modules
* requests
* bs4 (Beautiful Soup webscraper)

## Usage



## For developers only

I recommend [Pycharm](https://www.jetbrains.com/de-de/pycharm/) for the IDE. But it doesn't matter at all. If you decide to use another IDE to contribute to this project, please add the IDE specific config files to the .gitignore.

Clone the repository

```bash
git clone git@github.com:Markus-Stuppnig/Schengen-Border-Control.git
cd Schengen-Border-Control
```

Create and activate a virtual environment

```bash
python -m venv venv
source ./bin/activate
```

Install all required dependencies

```bash
pip install -r requirements.txt
```
