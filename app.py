from flask import Flask, render_template
import random  # This is to simulate current readings for testing

app = Flask(__name__)

# Route to display the current value on the web page
@app.route('/')
def index():
    # Simulate a current value (in reality, you'd get this from your Pico or sensor)
    current_value = round(random.uniform(5.0, 15.0), 2)  # Simulate values between 5 and 15 Amps
    threshold = 10.0  # Your set threshold

    # Determine if there's a danger
    danger = current_value >= threshold
    return render_template('index.html', current=current_value, danger=danger)

if __name__ == '__main__':
    app.run(debug=True)
