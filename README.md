# WAP - Twitch Automation Test

This repository contains an automated test script using Selenium and pytest to navigate the Twitch mobile website, search for "StarCraft II", and take a screenshot of a selected streamer's page.

## Prerequisites

- Python 3.11
- Selenium
- pytest
- ChromeDriver (Make sure it's in your PATH)

## Installation

Clone the repository:
```sh
git clone https://github.com/MaksymMasalov/WAP.git
cd WAP
```

Install requirements.txt
```sh
pip install -r requirements.txt
```

## Usage

```sh
pytest -v test_twitch.py
```