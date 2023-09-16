import json


def aggregate_statistic():
    # Read the JSON file
    with open('senec_statistic_data.json', 'r') as file:
        data = json.load(file)

    # Initialize variables for aggregation
    total_netzbezug = 0
    total_netzeinspeisung = 0
    total_speicherbeladung = 0
    total_speicherentnahme = 0
    total_stromerzeugung = 0
    total_stromverbrauch = 0

    # Iterate through the intervals and aggregate the values
    for interval in data:
        total_netzbezug += interval["netzbezug"]["wert"]
        total_netzeinspeisung += interval["netzeinspeisung"]["wert"]
        total_speicherbeladung += interval["speicherbeladung"]["wert"]
        total_speicherentnahme += interval["speicherentnahme"]["wert"]
        total_stromerzeugung += interval["stromerzeugung"]["wert"]
        total_stromverbrauch += interval["stromverbrauch"]["wert"]

    # Print the aggregated values
    print("Total netzbezug:", total_netzbezug, "Wh")
    print("Total netzeinspeisung:", total_netzeinspeisung, "Wh")
    print("Total speicherbeladung:", total_speicherbeladung, "Wh")
    print("Total speicherentnahme:", total_speicherentnahme, "Wh")
    print("Total stromerzeugung:", total_stromerzeugung, "Wh")
    print("Total stromverbrauch:", total_stromverbrauch, "Wh")
