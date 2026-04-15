from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os
import json

app = Flask(__name__)
# Secret key needed for flash messages
app.secret_key = "super_secret_key" 

CSV_FILE = 'appointments.csv'
SETTINGS_FILE = 'settings.json'

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        default_settings = {"blocked_dates": [], "available_time": "10 AM to 3 PM"}
        save_settings(default_settings)
        return default_settings
    with open(SETTINGS_FILE, 'r') as f:
        return json.load(f)

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f)

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
    settings = load_settings()
    return render_template('index.html', total=total, 
                           available_time=settings.get('available_time', '10 AM to 3 PM'),
                           blocked_dates=settings.get('blocked_dates', []))

@app.route('/book', methods=['POST'])
def book_appointment():
    """Handle form submission, save to CSV, and show the success page."""
    date = request.form.get('date')
    name = request.form.get('name')
    phone = request.form.get('phone')

    settings = load_settings()
    if date in settings.get('blocked_dates', []):
        flash("Sorry, the doctor is unavailable on the selected date. Please choose another date.")
        return redirect(url_for('index'))

    # Generate the serial number
    total = get_total_appointments()
    serial_number = total + 1

    # Save to CSV
    ensure_csv_exists()
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([serial_number, date, name, phone])

    # Render the new page with the serial and phone number
    return render_template('success.html', serial=serial_number, phone=phone)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    """Admin portal to view appointments and set availability."""
    settings = load_settings()
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'update_time':
            new_time = request.form.get('available_time')
            if new_time:
                settings['available_time'] = new_time
                save_settings(settings)
                flash("Availability time updated!")
                
        elif action == 'block_date':
            date_to_block = request.form.get('block_date')
            if date_to_block and date_to_block not in settings.get('blocked_dates', []):
                settings.setdefault('blocked_dates', []).append(date_to_block)
                save_settings(settings)
                flash(f"Date {date_to_block} is now marked as an off day.")
                
        elif action == 'unblock_date':
            date_to_unblock = request.form.get('unblock_date')
            if date_to_unblock in settings.get('blocked_dates', []):
                settings['blocked_dates'].remove(date_to_unblock)
                save_settings(settings)
                flash(f"Date {date_to_unblock} has been unblocked.")
        
        return redirect(url_for('admin'))

    # Load all appointments for report
    ensure_csv_exists()
    appointments = []
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        appointments = list(reader)
        
    return render_template('admin.html', 
                           appointments=appointments[1:] if len(appointments)>0 else [], 
                           headers=appointments[0] if len(appointments)>0 else [],
                           available_time=settings.get('available_time', '10 AM to 3 PM'),
                           blocked_dates=settings.get('blocked_dates', []))

if __name__ == '__main__':
    app.run(debug=True)
