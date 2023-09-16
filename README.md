# senec-api-parser

Demo code to parse the api of senec (senecops.com). The code will fetch the following api endpoints

- login: get token
- devices: in case you have more than one SENEC device you can choose what device to use
- dashboard: current values and values aggregated of today, printed to the console
- zeitverlauf: statisic data before the given date, stored into `senec_time_aggregation_data.json`
- statistik: yearly statistic of all years where the device exists, stored into `senec_statistic_data.json`

The statistik data is read from the `senec_statistic_data.json` and then 

- aggregated to total values, printed to the console
- plottet into `senec_graph.html`

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

## Configuration

Create a `config.ini` with this content:

```ini
[MeinSenec]
username=your@login.com
password=your_password
token=optional_you_can_put_token_here
timezone=Europe/Berlin
locale=de_DE
```

## Execution

Execute with `python main.py` once venv is active and config.ini is created.
If you want, you can copy the token printed to the console to the config.ini, then the login step will be skipped and the username and password can be removed from config.
