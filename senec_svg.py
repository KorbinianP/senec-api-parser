import json
import datetime
import matplotlib.pyplot as plt
import mpld3


def create_interactive_html():
    # Load the JSON data from the file
    with open("senec_statistic_data.json", "r") as json_file:
        zeitverlauf_data = json.load(json_file)

    # Extract relevant data from the JSON
    intervalle = zeitverlauf_data.get("intervalle", [])

    # Initialize lists to store data for plotting
    timestamps = []
    netzbezug = []
    netzeinspeisung = []
    speicherbeladung = []
    speicherentnahme = []
    stromerzeugung = []
    stromverbrauch = []

    # Parse and extract data
    for interval in intervalle:
        startzeitpunkt = datetime.datetime.strptime(interval["startzeitpunkt"], "%Y-%m-%dT%H:%M:%SZ")
        timestamps.append(startzeitpunkt)
        netzbezug.append(interval["netzbezug"]["wert"])
        netzeinspeisung.append(interval["netzeinspeisung"]["wert"])
        speicherbeladung.append(interval["speicherbeladung"]["wert"])
        speicherentnahme.append(interval["speicherentnahme"]["wert"])
        stromerzeugung.append(interval["stromerzeugung"]["wert"])
        stromverbrauch.append(interval["stromverbrauch"]["wert"])

    # Create a time series graph
    plt.figure(figsize=(12, 6))
    netzbezug_line, = plt.plot(timestamps, netzbezug, label="Netzbezug")
    netzeinspeisung_line, = plt.plot(timestamps, netzeinspeisung, label="Netzeinspeisung")
    speicherbeladung_line, = plt.plot(timestamps, speicherbeladung, label="Speicherbeladung")
    speicherentnahme_line, = plt.plot(timestamps, speicherentnahme, label="Speicherentnahme")
    stromerzeugung_line, = plt.plot(timestamps, stromerzeugung, label="Stromerzeugung")
    stromverbrauch_line, = plt.plot(timestamps, stromverbrauch, label="Stromverbrauch")

    # Create tooltips with formatted text
    tooltip_netzbezug = mpld3.plugins.LineLabelTooltip(netzbezug_line, label="Netzbezug")
    tooltip_netzeinspeisung = mpld3.plugins.LineLabelTooltip(netzeinspeisung_line, label="Netzeinspeisung")
    tooltip_speicherbeladung = mpld3.plugins.LineLabelTooltip(speicherbeladung_line, label="Speicherbeladung")
    tooltip_speicherentnahme = mpld3.plugins.LineLabelTooltip(speicherentnahme_line, label="Speicherentnahme")
    tooltip_stromerzeugung = mpld3.plugins.LineLabelTooltip(stromerzeugung_line, label="Stromerzeugung")
    tooltip_stromverbrauch = mpld3.plugins.LineLabelTooltip(stromverbrauch_line, label="Stromverbrauch")

    # Add tooltips to the plot
    mpld3.plugins.connect(
        plt.gcf(),
        tooltip_netzbezug,
        tooltip_netzeinspeisung,
        tooltip_speicherbeladung,
        tooltip_speicherentnahme,
        tooltip_stromerzeugung,
        tooltip_stromverbrauch,
    )

    plt.xlabel("Timestamp")
    plt.ylabel("Energy (Wh)")
    plt.title("Energy Data Over Time")
    plt.legend()

    # Make the plot interactive as an HTML file
    interactive_plot = mpld3.fig_to_html(plt.gcf())

    # Save the interactive HTML plot to a file
    with open("senec_graph.html", "w") as html_file:
        html_file.write(interactive_plot)

    # Show the interactive plot (for Jupyter Notebook)
    # mpld3.display()

    # Close the Matplotlib plot
    plt.close()

    print("Interactive SVG graph with tooltips saved to 'interactive_graph.html'")
