from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

CSV_FILE = 'appointments.csv'

def ensure_csv_exists():
    """Create the CSV with headers if it doesn't exist yet."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Serial_Number', 'Date', 'Name', 'Phone'])

def get_total_appointments():
    """Count how many appointments are saved in the CSV."""
    ensure_csv_exists()
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
        # Subtract 1 to ignore the header row
        return len(data) - 1 if len(data) > 0 else 0

@app.route('/')
def index():
    """Load the landing page and pass the total appointment count."""
    total = get_total_appointments()
    return render_template('index.html', total=total)

@app.route('/book', methods=['POST'])
def book_appointment():
    """Handle form submission, save to CSV, and show the success page."""
    date = request.form.get('date')
    name = request.form.get('name')
    phone = request.form.get('phone')

    # Generate the serial number
    total = get_total_appointments()
    serial_number = total + 1

    # Save to CSV
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([serial_number, date, name, phone])

    # Render the new page with the serial and phone number
    return render_template('success.html', serial=serial_number, phone=phone)

if __name__ == '__main__':
    app.run(debug=True)
