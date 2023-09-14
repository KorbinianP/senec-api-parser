"""All code contacting the senec api"""
import json
import enum
import requests

# Define the base URL
BASE_URL = "https://app-gateway-prod.senecops.com/v1/senec"


class TimePeriod(enum.Enum):
    """The allowed time period values of senec api"""
    HOUR = "STUNDE"
    DAY = "TAG"
    MONTH = "MONAT"
    YEAR = "JAHR"


def login(username, password):
    """Login to senec and return the generated token"""
    # Define the login URL
    login_url = f"{BASE_URL}/login"

    # Define the payload data as a dictionary
    payload_data = {"username": username, "password": password}

    # Convert the payload dictionary to JSON format
    payload_json = json.dumps(payload_data)

    # Define headers
    headers = {"Content-Type": "application/json"}

    try:
        # Send a POST request to the login URL with the JSON payload
        response = requests.post(login_url, data=payload_json, headers=headers, timeout=10)

        # Check if the login request was successful (status code 200)
        if response.status_code == 200:
            # Extract the token from the response JSON
            response_data = response.json()
            access_token = response_data.get("token")
            print("Login successful! " + access_token)
        else:
            print(f"Login failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as error:
        print(f"An error occurred during login: {error}")

    return access_token


def get_devices(access_token):
    """Get the list of senec devices"""
    if access_token is None:
        print("Please login first.")
        return None

    # Define the devices URL
    devices_url = f"{BASE_URL}/anlagen"

    # Define headers with the authorization token
    headers = {"authorization": access_token}

    try:
        # Send a GET request to the devices URL with the authorization header
        response = requests.get(devices_url, headers=headers, timeout=10)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            devices_data = response.json()
            return devices_data
        print(f"Failed to retrieve devices with status code: {response.status_code}")

    except requests.exceptions.RequestException as error:
        print(f"An error occurred while retrieving devices: {error}")
    return None


def get_dashboard(access_token, device_id):
    """get the data from dashboard api endpoint and print it to console"""
    if access_token is None:
        print("Please login first.")
        return

    # Define the dashboard URL
    dashboard_url = f"{BASE_URL}/anlagen/{device_id}/dashboard"

    # Define headers with the authorization token
    headers = {"authorization": access_token}

    try:
        # Send a GET request to the dashboard URL with the authorization header
        response = requests.get(dashboard_url, headers=headers, timeout=10)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            dashboard_data = response.json()
            print("Dashboard Data:")
            print(json.dumps(dashboard_data, indent=4))  # Pretty print the JSON response
        else:
            print(f"Failed to retrieve dashboard with status code: {response.status_code}")

    except requests.exceptions.RequestException as error:
        print(f"An error occurred while retrieving dashboard data: {error}")


def get_zeitverlauf_data(access_token, device_id, period, datetime_obj, timezone):
    """get the data from zeitverlauf api endpoint and print it to a json"""
    # Define the API endpoint
    endpoint = f"anlagen/{device_id}/zeitverlauf"

    # Format the datetime object as a string
    datetime_str = datetime_obj.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Define query parameters
    params = {"periode": period, "timezone": timezone, "before": datetime_str}

    headers = {"authorization": access_token}

    try:
        # Send a GET request to the API endpoint with the query parameters
        response = requests.get(f"{BASE_URL}/{endpoint}", params=params, headers=headers, timeout=20)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            zeitverlauf_data = response.json()
            #print("Zeitverlauf Data:")
            #print(zeitverlauf_data)

            # Write the response data to a JSON file
            with open("senec_time_aggregation_data.json", "w", encoding="utf-8") as json_file:
                json.dump(zeitverlauf_data, json_file, indent=4)

        else:
            print(f"Request failed with status code: {response.status_code}")
            print("Request details:")
            print(f"URL: {response.request.url}")
            print(f"Headers: {response.request.headers}")
            print(f"Body: {response.request.body}")

    except requests.exceptions.RequestException as error:
        print(f"An error occurred during the API call: {error}")


def get_statistik_data(access_token, device_id, datetime_obj, timezone, locale):
    """get the data from statistik api endpoint and print it to a json"""
    # Define the API endpoint
    endpoint = f"anlagen/{device_id}/statistik"

    # Format the datetime object as a string
    datetime_str = datetime_obj.strftime("%Y-%m-%d")

    # Define query parameters
    params = {"periode": TimePeriod.YEAR.value, "timezone": timezone, "datum": datetime_str, "locale": locale}

    headers = {"authorization": access_token}

    try:
        # Send a GET request to the API endpoint with the query parameters
        response = requests.get(f"{BASE_URL}/{endpoint}", params=params, headers=headers, timeout=20)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            zeitverlauf_data = response.json()
            #print("Zeitverlauf Data:")
            #print(zeitverlauf_data)

            # Write the response data to a JSON file
            with open("senec_statistic_data.json", "w", encoding="utf-8") as json_file:
                json.dump(zeitverlauf_data, json_file, indent=4)

        else:
            print(f"Request failed with status code: {response.status_code}")
            print("Request details:")
            print(f"URL: {response.request.url}")
            print(f"Headers: {response.request.headers}")
            print(f"Body: {response.request.body}")

    except requests.exceptions.RequestException as error:
        print(f"An error occurred during the API call: {error}")
