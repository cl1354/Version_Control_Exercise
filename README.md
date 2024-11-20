# my-first-app-fall-2024

## Setup

Create a virtual environment (first time only):

```sh
conda create -n reports-env-2024 python=3.10
```

Activate the environment (whenever you come back to this project):

```sh
conda activate reports-env-2024
```

Install packages:

```sh
pip install -r requirements.txt
```

[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.
[Obtain an API Key](https://help.mailgun.com/hc/en-us/articles/203380100-Where-can-I-find-my-API-keys-and-SMTP-credentials) from Mailgun.
Finally, find your sandbox domain from Mailgun and input your own email address as a sender address.

Create a ".env" file and add contents like the following (using your own AlphaVantage API Key):

```sh
# this is the ".env" file:
ALPHAVANTAGE_API_KEY="..."
MAILGUN_API_KEY="..."
MAILGUN_DOMAIN="..."
MAILGUN_SENDER_ADDRESS="..."
```

## Usage

Run the example script:

```sh
python app/example.py
```

Run the unemployment report:

```sh
#ALPHAVANTAGE_API_KEY="..." python app/unemployment.py

python app/unemployment_report.py
```

Run the stocks report:

```sh
python app/stocks_report.py
```
Run the web app (then view in the browser at http://localhost:5000/):
```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

Testing:

```sh
pytest
```