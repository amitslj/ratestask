import requests


def api_test_cases():
    """
    description:
        This method runs 2 test cases :
        1. Asserts if the application is up and running by checking API response code
        2. Asserts if the data is fetched by checking length of content in response
    """
    url = "http://127.0.0.1:5000/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"
    try:
        response = requests.get(url)
        assert response.status_code == 200, f"API response code 200 expected , got : {response.status_code}"

        assert int(response.headers.get(
            'Content-Length')) > 0, f"content length > 0 expected from API response, got : {response.headers.get('Content-Length')}"

    except Exception as err:
        print(err)


if __name__ == '__main__':
    api_test_cases()
