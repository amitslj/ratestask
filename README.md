# Xeneta Rates Application

This is the documentation to create and run Rates API which would fetch and display data from PostgreSQL DB. 

**Pre-requisites :-**

In order to run the Rates application, we need the below tools installed -

1. Python
2. Docker Desktop

**Solution Structure :-**

Below is the folder structure for the provided solution :

**rates_api/src** : This comprises the source code including below files

1. credentials.py - This contains the connection information to connect to Postgres DB
2. main.py - This is the application code which will fetch prices based on parameters passed
3. requirements.txt - This file conatins the python dependencies to be installed before running the application

**rates_api/test** : This comprises the test cases and include the below files

1. api_test_cases.py - This contains the test cases to validate the API using python
2. application_test_cases.py - This file contains test cases to validate the functionality of SQL query and its corresponding method

**rates_db** : This contains the below files 

1. Dockerfile - This file is used to launch the postgres container with base image
2. rates.sql - This contains the regions, ports and prices dataset to be loaded into Postgres DB

**Steps to Run the app :-**

1. Clone the github repository.
2. Start the PostgresDB container by building the image inside rates_db folder
3. Navigate to ratestask/rates_api/src and install the python dependencies using :
```
pip install -r requirements.txt
```
4. Run the python application using command line terminal as :
```
python main.py
```
5. This will load the application which can be validated at localhost:5000 and the below endpoints :

/  *This represnts the Homepage*

/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main *This represents the rates end point*

**Tests**

Navigating to ratestask/rates_api/test will show the below 2 test files :

**api_test_cases** - this file will test the API from Python and perform the below validations -

1. Check if the application running gives a response of 200 when API is called from Python
2. Validate if the API returns a valid response by checking the length of the content in header

**application_test_cases** - this file will validate the application functionality by testing its SQL function -

1. *Test Case 1* : test_custom_prices will run below 2 test cases -

a. Validate if the returned Dataframe is not null

b. Check if 10 rows are returned corresponding to prices queried for 10 days (2016-01-01 to 2016-01-10)


2. *Test Case 2* : test_null_prices

a. Validate if no price is returned for date 2016-01-03

b. Check if 1 row of null price is returned corresponding to the queried date

**NOTE** - In order to run the application_test_cases file, please mark the src folder as - 'Sources Root' when using Python IDE so that src/main file and its methods are reachable in the test file.