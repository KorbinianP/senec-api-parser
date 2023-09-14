"""Demo code to learn and understand the responses of senec api"""
import datetime
import inquirer
import configparser

from senec_api import (
    login,
    get_devices,
    get_dashboard,
    get_statistik_data,
    get_zeitverlauf_data,
    TimePeriod,
)
from senec_svg import create_interactive_html


def main():
    """Will fetch data from senec api and plot it to a html / svg"""
    config = configparser.ConfigParser()
    config.read('config.ini')
    access_token = config.get("MeinSenec", "token")
    timezone = config.get("MeinSenec", "timezone")
    locale = config.get("MeinSenec", "locale")
    if not access_token:
        access_token = login(config.get("MeinSenec", "username"), config.get("MeinSenec", "password"))
    devices_data = get_devices(access_token)

    if devices_data:
        if len(devices_data) == 1:
            selected_device_id = devices_data[0]["id"]
        else:
            # Extract device names and ids
            device_choices = [{'name': f"{device['gehaeusenummer']} ({device['id']})", 'value': device['id']} for device in devices_data]

            # Ask the user to choose a device
            questions = [
                inquirer.List('device', message="Select a device:", choices=device_choices),
            ]
            answers = inquirer.prompt(questions)
            selected_device_id = answers['device']['value']

        # Get the dashboard data for the selected device
        get_dashboard(access_token, selected_device_id)
        get_zeitverlauf_data(access_token, selected_device_id, TimePeriod.HOUR.value, datetime.datetime.now(), timezone)
        get_statistik_data(access_token, selected_device_id, datetime.datetime.now(), timezone, locale)
        create_interactive_html()


if __name__ == "__main__":
    main()
