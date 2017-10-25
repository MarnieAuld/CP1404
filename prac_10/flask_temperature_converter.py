from flask import Flask

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return "{:.2f}".format(fahrenheit)


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return "{:.2f}".format(celsius)


@app.route('/')
def homepage():
    return "<h1><u>Celsius to Fahrenheit Converter</h1></u>" \
           "Enter <b>.../f/your_temp_in_celsius</b> to return temperature in fahrenheit" \
           "<br> Enter <b>.../c/your_temp_in_fahrenheit</b> to return temperature in celsius</br>"


@app.route('/f/<celsius>')
def f(celsius=0.0):
    celsius = float(celsius)
    return "<h2><u>Celsius to Fahrenheit Conversion</u></h2>" \
           "Celsius: {}" \
           "<br>Fahrenheit : {}</br>".format(celsius, celsius_to_fahrenheit(celsius))


@app.route('/c/<fahrenheit>')
def c(fahrenheit=0.0):
    fahrenheit = float(fahrenheit)
    return "<h2><u>Fahrenheit to Celsius Conversion</u></h2>" \
           "Fahrenheit: {}" \
           "<br>Celsius: {}</br>".format(fahrenheit, fahrenheit_to_celsius(fahrenheit))


if __name__ == '__main__':
    app.run()
