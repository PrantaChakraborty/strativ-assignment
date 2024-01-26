# Assignment for strativ AB

## Getting Started

These instructions will guide you through setting up the project on your local machine.

### Prerequisites

- Python 3.10
- pip (Python package installer)
- Install [virtual environment ](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

## Setup

#### 1. Clone the Repository
- Using ssh
```bash 
git clone git@github.com:PrantaChakraborty/strativ-assignment.git
```
- Using https
```bash
git clone https://github.com/PrantaChakraborty/strativ-assignment.git
```
#### 2. cd to project directory & create virtual environment & activate the virtual environment
``` bash
cd strativ-assignment
python3 -m venv venv  # create virtual environment
source venv/bin/activate # activate the virtual environment
```

### 3. Install the dependencies by running the following command.
```bash
pip install -r rerquirements.txt
```
### 4. Create a .env file and copy everything from example.env to .env
```bash
cp example.env .env
```
### 5. Run the migrations command
```bash
python manage.py migrate
```

### 6. Run the Test(Optional)
```bash
python manage.py test
```
### 7. Run the project
```bash
python manage.py runserver
```

## About the API's
- Visit ``http://127.0.0.1:8000/`` and click the swagger **documentation link**  or,
- Visit ``http://127.0.0.1:8000/swagger/`` to view the api documentation

### CURL command 
- For coolest districts
```bash
curl --location --request GET 'http://127.0.0.1:8000/api/v1/weather/coolest_districts/'
```
- For travel suggestions
```bash
curl --location --request POST 'http://127.0.0.1:8000/api/v1/weather/suggestions/' \
--header 'Content-Type: application/json' \
--data-raw '{
  "location": {
    "lat": 23.75,
    "long": 90.375
  },
  "destination": {
    "lat":23.172534,
    "long": 89.512672
  },
  "date": "2024-01-27"
}'
```

### Some optimization Ideas
- When hit the API for the first time it took some time to return the response.
- Though the weather rarely changed daily, or hourly we can run a cron job every night at 12:01 AM and save the data and then return the data from db.