# Schengen Borders Information Scraper

This Python script scrapes information about temporary reintroduction of border control in the Schengen Area from the [European Commission's website](https://home-affairs.ec.europa.eu/policies/schengen-borders-and-visa/schengen-area/temporary-reintroduction-border-control_en).

## Requirements

* Python 3.x
* `requests` library
* `BeautifulSoup` library

Make sure to install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the following command in bash to install this package with [pip](https://pypi.org/project/pip/)

### Installing the package

```bash
pip install Schengen_Borders_Information_Scraper
```

After installing the library, you can import the scraper module into your Python script and utilize the provided functions.

### Importing the Module

```python
import Schengen_Borders_Information_Scraper.scraper as scraper
```

### Available Functions

`get_countries()`

This function retrieves a list of countries that have temporary border control.

```python
countries = scraper.get_countries()
```

`get_temporary_borders()`

Get information about temporary border controls for all countries. It returns a dictionary with country names as keys and information about the start date, end date, and reason for the border control as values.

```python
borders = scraper.get_temporary_borders()
```

`get_country(country)`

Retrieve information about the temporary border control of a specific country. It returns a dictionary with information about the start date, end date, and reason for the border control.

```python
country_info = scraper.get_country("Austria")
```

### Example Usage

```python
import Schengen_Borders_Information_Scraper.scraper as scraper

# Get a list of countries with temporary border control
countries = scraper.get_countries()
print(countries)

if 'Austria' in countries:
    print("Austria has temporary border control.")
else:
    print("Austria does not have temporary border control.")
```

## Developer Setup Guide

Welcome to the Schengen Borders Information Scraper project! If you're a developer looking to contribute, follow these steps to set up your development environment.

### Prerequisites

Before you begin, make sure you have the following:

* Python installed (recommended version 3.x)
* Git installed
* PyCharm (recommended IDE, but any other IDE works too)

#### Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone git@github.com:Markus-Stuppnig/Schengen_Borders_Information_Scraper.git
cd Schengen_Borders_Information_Scraper
```

#### Create a Virtual Environment

It's a good practice to work in a virtual environment to manage dependencies. Create and activate a virtual environment using the following commands:

```bash
python -m venv venv
source ./bin/activate
```

#### Install Dependencies

Install all the required dependencies for the project using pip:

```bash
pip install -r requirements.txt
```

Now you have your development environment set up and ready to go! You can use your preferred IDE (such as PyCharm) to work on the project. Be sure to add any IDE-specific configuration files to the .gitignore if you choose an alternative IDE.

Happy coding!
