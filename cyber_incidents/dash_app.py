import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
from sqlalchemy import create_engine
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Connect to the MySQL database
engine = create_engine('mysql+mysqlconnector://root:2004@localhost/cyber_incidents_db')  # Update with your credentials
df = pd.read_sql('SELECT * FROM incidents', con=engine)

# Categorize sector
def categorize_sector(details):
    if 'healthcare' in details.lower():
        return 'Healthcare'
    elif 'financial' in details.lower():
        return 'Financial'
    elif 'tech' in details.lower() or 'software' in details.lower():
        return 'Technology'
    elif 'retail' in details.lower():
        return 'Retail'
    else:
        return 'Other'

df['sector'] = df['details'].apply(categorize_sector)

# Generate random latitude and longitude for demonstration (replace with actual data)
df['latitude'] = np.random.uniform(low=-90, high=90, size=len(df))
df['longitude'] = np.random.uniform(low=-180, high=180, size=len(df))

# Simple AI model setup for predicting incidents likelihood
le = LabelEncoder()
df['sector_encoded'] = le.fit_transform(df['sector'])
X = df[['latitude', 'longitude', 'sector_encoded']]
y = np.random.choice([0, 1], size=len(df))  # Simulated target variable
model = RandomForestClassifier()
model.fit(X, y)

def predict_incident(sector, lat, lon):
    sector_encoded = le.transform([sector])[0]
    return model.predict_proba([[lat, lon, sector_encoded]])[0][1]  # Return probability of incident

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

# Create the bar plot figure
def create_bar_plot(df):
    sector_counts = df['sector'].value_counts().reset_index()
    sector_counts.columns = ['sector', 'count']
    fig = px.bar(
        sector_counts,
        x='sector',
        y='count',
        labels={'sector': 'Sector', 'count': 'Number of Incidents'},
        title='Cyber Incidents by Sector',
        color='sector',
        color_discrete_sequence=px.colors.sequential.Blues
    )
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        font=dict(color='#FFFFFF'),
        title=dict(x=0.5, xanchor='center'),
        transition={'duration': 500}  # Animation on updates
    )
    return fig

# Create the map plot with glowing circles and connections
def create_map_plot(df):
    fig = go.Figure()

    # Adding the main scattermapbox trace for markers
    fig.add_trace(go.Scattermapbox(
        lat=df['latitude'],
        lon=df['longitude'],
        mode='markers+text',
        marker=dict(
            size=10,
            color='rgba(255, 0, 0, 0.8)',  # Solid core color
            symbol='circle'
        ),
        text=df['title'],  # Use this to display the title on hover
        hoverinfo='text'
    ))

    # Adding glow effect with additional traces
    for size, opacity in zip([20, 30, 40], [0.3, 0.2, 0.1]):
        fig.add_trace(go.Scattermapbox(
            lat=df['latitude'],
            lon=df['longitude'],
            mode='markers',
            marker=dict(
                size=size,
                color='rgba(255, 0, 0, 0.2)',  # Glow layers with decreasing opacity
                symbol='circle'
            ),
            hoverinfo='skip'  # Skips hover to avoid clutter
        ))

    # Simulating animated connections between random points
    for i in range(10):
        fig.add_trace(go.Scattermapbox(
            lat=[np.random.uniform(-90, 90), np.random.uniform(-90, 90)],
            lon=[np.random.uniform(-180, 180), np.random.uniform(-180, 180)],
            mode='lines',
            line=dict(width=1, color='rgba(0, 255, 0, 0.5)')
        ))

    fig.update_layout(
        mapbox_style="carto-darkmatter",  # Dark map style
        mapbox=dict(
            zoom=1,
        ),
        margin={"r": 0, "t": 50, "l": 0, "b": 0},
        paper_bgcolor='rgba(0, 0, 0, 0)',
        font=dict(color='#FFFFFF'),
        title=dict(text="Live Hacking Incidents Map", x=0.5, xanchor='center')
    )
    return fig

# Layout of the Dash app
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Cyber Incident Dashboard", className="text-center text-primary mb-4 animated bounceIn"), width=12)
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id='sector-bar-plot', figure=create_bar_plot(df), className="floating-card animated fadeIn"), width=6),
        dbc.Col([
            html.H4("Details of All Attacks", className="floating animated fadeIn"),
            dcc.Markdown(id='attack-details', style={'overflowY': 'scroll', 'height': '400px'})
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='live-map', figure=create_map_plot(df), className="animated zoomIn"), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H4("Alerts", className="mt-4 floating animated fadeIn"),
            html.Div(id='alert-box', className="alert-box", style={'height': '50px'}),
            html.Div(id='alert-popup')  # Add the alert-popup here
        ], width=12)
    ]),

    # Detailed view of the selected attack
    dbc.Row([
        dbc.Col(html.H4("Attack Details", className="mt-4 animated fadeIn"), width=12),
        dbc.Col(html.Div(id='selected-attack-details', style={'color': 'white', 'backgroundColor': '#333', 'padding': '10px', 'borderRadius': '5px'}), width=12)
    ]),

    dcc.Interval(
        id='interval-component',
        interval=10 * 1000,  # Refresh every 10 seconds
        n_intervals=0
    ),

    # JavaScript to handle dynamic CSS styling and animations
    html.Script('''
        document.addEventListener('DOMContentLoaded', function() {
            // Adding hover effects to floating cards
            const cards = document.querySelectorAll('.floating-card');
            cards.forEach(card => {
                card.addEventListener('mouseover', () => {
                    card.style.transform = 'translateY(-5px)';
                    card.style.boxShadow = '0 8px 16px rgba(0, 0, 0, 0.3)';
                });
                card.addEventListener('mouseout', () => {
                    card.style.transform = 'translateY(0)';
                    card.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.3)';
                });
            });

            // Adding bounce-in animation to alerts
            const alertBox = document.querySelector('.alert-box');
            if (alertBox) {
                alertBox.style.animation = 'bounceIn 1s ease-in-out';
            }
        });
    ''')
], fluid=True, style={'backgroundColor': '#1e1e1e', 'padding': '20px', 'borderRadius': '15px'})

# Callback to update the details of all attacks
@app.callback(
    Output('attack-details', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_attack_details(n):
    if df.empty:
        return "No attack details available."
    details = []
    for _, row in df.iterrows():
        details.append(f"**Title**: {row['title']}  \n**Date**: {row['date']}  \n**Details**: {row['details']}\n\n")
    return details

# Alert styling with improved animation
alert_style = {
    'height': '50px',
    'animation': 'flash 1s infinite',
    'animationTimingFunction': 'ease-in-out',
    'border': '1px solid #f8d7da',
    'borderRadius': '5px',
    'padding': '10px',
    'backgroundColor': '#721c24',
    'color': '#fff'
}

# Callback to alert when a new attack is detected with enhanced animation
@app.callback(
    [Output('alert-box', 'children'),
     Output('alert-popup', 'children')],
    [Input('interval-component', 'n_intervals')]
)
def show_alerts(n):
    print(f"Interval triggered: {n}")  # Debug statement
    if n % 5 == 0:  # Simulated condition for showing an alert
        probability = predict_incident('Technology', 20.0, 77.0)
        print(f"Predicted probability: {probability}")  # Debug statement
        if probability > 0.5:
            alert_message = dbc.Alert(
                f"Cyber Attack Detected!",
                color="danger",
                dismissable=True,
                className="animate__animated animate__flash",
                style=alert_style
            )
            popup_message = dbc.Alert(
                f"Cyber Attack Detected!",
                color="danger",
                dismissable=True,
                className="animate__animated animate__flash",
                style={
                    'position': 'fixed',
                    'top': '20px',
                    'left': '50%',
                    'transform': 'translateX(-50%)',
                    'width': '90%',
                    'maxWidth': '600px',
                    'zIndex': '9999',
                    'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.3)'
                }
            )
            return alert_message, popup_message
    raise PreventUpdate

# Callback to show details of the clicked attack
@app.callback(
    Output('selected-attack-details', 'children'),
    [Input('live-map', 'clickData')]
)
def display_selected_attack(clickData):
    if clickData is None:
        raise PreventUpdate
    # Get the clicked point's index
    point_index = clickData['points'][0]['pointIndex']
    # Get details from the DataFrame
    selected_attack = df.iloc[point_index]
    details = (
        f"**Title**: {selected_attack['title']}  \n"
        f"**Date**: {selected_attack['date']}  \n"
        f"**Details**: {selected_attack['details']}  \n"
        f"**Sector**: {selected_attack['sector']}  \n"
        f"**Latitude**: {selected_attack['latitude']}  \n"
        f"**Longitude**: {selected_attack['longitude']}"
    )
    return details

if __name__ == '__main__':
    app.run_server(debug=True)
