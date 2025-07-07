from plotly import graph_objs as go
import pandas as pd

def create_temperature_chart(df, unit_name):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['timestamp'], y=df['temperature'],
                             mode='lines+markers', name='Temperature'))
    fig.update_layout(title=f'Temperature Trend for {unit_name}',
                      xaxis_title='Time',
                      yaxis_title='Temperature (°C)',
                      template='plotly_white')
    return fig

def create_vibration_chart(df, unit_name):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['timestamp'], y=df['vibration'],
                             mode='lines+markers', name='Vibration'))
    fig.update_layout(title=f'Vibration Trend for {unit_name}',
                      xaxis_title='Time',
                      yaxis_title='Vibration (m/s²)',
                      template='plotly_white')
    return fig

def create_pressure_chart(df, unit_name):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['timestamp'], y=df['pressure'],
                             mode='lines+markers', name='Pressure'))
    fig.update_layout(title=f'Pressure Trend for {unit_name}',
                      xaxis_title='Time',
                      yaxis_title='Pressure (psi)',
                      template='plotly_white')
    return fig

def create_combined_chart(df, unit_name):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['timestamp'], y=df['temperature'],
                             mode='lines+markers', name='Temperature'))
    fig.add_trace(go.Scatter(x=df['timestamp'], y=df['vibration'],
                             mode='lines+markers', name='Vibration'))
    fig.add_trace(go.Scatter(x=df['timestamp'], y=df['pressure'],
                             mode='lines+markers', name='Pressure'))
    fig.update_layout(title=f'Combined Sensor Data for {unit_name}',
                      xaxis_title='Time',
                      yaxis_title='Values',
                      template='plotly_white')
    return fig

def save_chart(fig, filename):
    fig.write_image(filename)