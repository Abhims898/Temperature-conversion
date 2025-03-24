from flask import Flask, render_template_string, request

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

@app.route('/')
def home():
    return render_template_string("""
        <h1>Temperature Converter</h1>
        <form action="/convert" method="POST">
            <label for="temperature">Enter temperature:</label>
            <input type="number" name="temperature" required>
            <select name="unit_from" required>
                <option value="celsius">Celsius</option>
                <option value="fahrenheit">Fahrenheit</option>
                <option value="kelvin">Kelvin</option>
            </select>
            <select name="unit_to" required>
                <option value="fahrenheit">Fahrenheit</option>
                <option value="celsius">Celsius</option>
                <option value="kelvin">Kelvin</option>
            </select>
            <button type="submit">Convert</button>
        </form>
    """)

@app.route('/convert', methods=['POST'])
def convert():
    temp = float(request.form['temperature'])
    unit_from = request.form['unit_from']
    unit_to = request.form['unit_to']
    
    if unit_from == "celsius":
        if unit_to == "fahrenheit":
            result = celsius_to_fahrenheit(temp)
            result_unit = "°F"
        elif unit_to == "kelvin":
            result = celsius_to_kelvin(temp)
            result_unit = "K"
        else:
            result = temp
            result_unit = "°C"
    elif unit_from == "fahrenheit":
        if unit_to == "celsius":
            result = fahrenheit_to_celsius(temp)
            result_unit = "°C"
        elif unit_to == "kelvin":
            result = celsius_to_kelvin(fahrenheit_to_celsius(temp))
            result_unit = "K"
        else:
            result = temp
            result_unit = "°F"
    elif unit_from == "kelvin":
        if unit_to == "celsius":
            result = kelvin_to_celsius(temp)
            result_unit = "°C"
        elif unit_to == "fahrenheit":
            result = celsius_to_fahrenheit(kelvin_to_celsius(temp))
            result_unit = "°F"
        else:
            result = temp
            result_unit = "K"
    
    return render_template_string("""
        <h1>Conversion Result</h1>
        <p>{{ result }} {{ result_unit }}</p>
        <a href="/">Go Back</a>
    """, result=result, result_unit=result_unit)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
