from plotly import graph_objects as go

def create_gauge_chart(value, title, min_value, max_value, thresholds):
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range': [min_value, max_value]},
            'bar': {'color': "blue"},
            'steps': [
                {'range': [min_value, thresholds[0]], 'color': "lightgreen"},
                {'range': [thresholds[0], thresholds[1]], 'color': "yellow"},
                {'range': [thresholds[1], max_value], 'color': "red"}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': thresholds[1]
            }
        }
    ))
    return gauge

def create_multiple_gauges(data):
    figures = []
    for item in data:
        gauge = create_gauge_chart(item['value'], item['title'], item['min'], item['max'], item['thresholds'])
        figures.append(gauge)
    return figures