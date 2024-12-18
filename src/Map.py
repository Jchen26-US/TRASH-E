import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import random
import time

######IMPORTANT, NOT FULLY COMPLETE NEEDS TO BE MODIFIED TO READ FILE AND TAKE LATITUDE AND LONGITUDE########
######SCSc

# Initialize the Dash app
app = dash.Dash(__name__)

# Initial coordinates
latitude = [40.7128, 34.0522, 51.5074]
longitude = [-74.0060, -118.2437, 0.1278]

# Layout of the app
app.layout = html.Div([
    dcc.Graph(id='live-map'),  # Map component
    dcc.Interval(
        id='interval-component',
        interval=2000,  # Update every 2000 ms (2 seconds)
        n_intervals=0   # Starts at zero
    )
])

# Callback to update the map
@app.callback(
    Output('live-map', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_map(n_intervals): #write code in here #can't write gps path in parameters?
    global latitude, longitude

    new_lat = random.uniform(-50,50)
    new_long = random.uniform(-50,50)

    #print("new iteration")#test for seeing how dash iterates

    latitude.append(new_lat)
    longitude.append(new_long)

    #gps_file = open(gps_path, "r")
    #coordinates = gps_file.read() #should be in the form {lat, long} or lat,long
    #latitude = coordinates.split(',', 1)[0]
    #longitude = coordinates.split(',', 2)[0]


    # Simulate updating coordinates

    # Create the figure
    fig = go.Figure()

    # Add scattergeo for live points
    fig.add_trace(go.Scattergeo(
        lat=latitude,
        lon=longitude,
        mode='markers',
        marker=dict(size=10, color='red'),
        text=["Point {}".format(i + 1) for i in range(len(latitude))]
    ))

    # Set map layout
    fig.update_layout(
        geo=dict(
            resolution=50,
            showland=True,
            landcolor="rgb(243, 243, 243)",
            showcountries=True,
            countrycolor="rgb(204, 204, 204)"
        ),
        title="Live Updating Map"
    )

    return fig


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
