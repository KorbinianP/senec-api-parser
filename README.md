# senec-api-parser

Demo code to parse the api of senec (senecops.com). The code will fetch the following api endpoints

- login: get token
- devices: in case you have more than one SENEC device you can choose what device to use
- dashboard: current values and values aggregated of today, printed to the console
- zeitverlauf: statisic data before the given date, stored into `senec_time_aggregation_data.json`
- statistik: monthly statistic of the year given, stored into `senec_statistic_data.json`

The statistik data is read from the `senec_statistic_data.json` and then  plottet into `senec_graph.html`

Please modify the datetime objects in main to your needs.

API spec: [documenter.getpostman.com](https://documenter.getpostman.com/view/10329335/UVCB9ihW#50022c18-9f2b-44e5-8ecc-1c7d32c3dcd2)

The code was created by me with the help of ChatGPT.

## Requirements

Required python packages can be installed in a venv with these commands:
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Some more details

- execute with `python main.py` once venv is active

## Configuration

Create a config.ini with this content:

```ini
[MeinSenec]
username=your@login.com
password=your_password
token=optional_you_can_put_token_here
timezone=Europe/Berlin
locale=de_DE
```
