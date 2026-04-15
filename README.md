# Doctor Appointment Booking System 🩺

A lightweight, minimal web application built with Python and Flask. Patients can easily submit an appointment request, which dynamically generates a unique appointment serial number and logs all records locally to a CSV file. It also includes an **Admin Portal** for the doctor to manage schedules and view patient reports!

## ✨ Features

- **Live Appointment Tracking**: Displays a live count of total appointments recorded on the booking page.
- **Doctor Admin Portal (`/admin`)**: A dedicated dashboard for the doctor to view all requested appointments in a neat data table format.
- **Dynamic Availability & Off-Days**: The doctor can customize working hours or completely block off certain dates. Patients are prevented from submitting appointments natively by JavaScript and backend restrictions on dates the doctor marks.
- **Dynamic Serial Generation**: Automatically produces sequential serial numbers for each incoming appointment based on previous records.
- **Data Persistence**: Ensures that every confirmed appointment is systematically logged into an `appointments.csv` file without the need for a heavy external database. Current configuration settings (like blocked dates) are saved inside `settings.json`.
- **User-Friendly Flow**: A clear, fast 2-step process from selecting a date to immediately receiving a detailed confirmation ticket containing a generated Serial ID.

## 📂 Project Structure

```text
appointment_taking_system-
│
├── app.py                  # The Flask backend Python server handling routes/logic
├── appointments.csv        # Auto-generated CSV file containing logged appointments
├── settings.json           # Auto-generated JSON config for storing off days & hours
├── .gitignore              # Files/folders to be ignored by Git
├── env/                    # Local Python virtual environment
└── templates/              # Directory holding all frontend UI files
    ├── admin.html          # Admin dashboard for the doctor to manage availability
    ├── index.html          # The main booking landing page and submission form
    └── success.html        # The post-submission confirmation ticket UI
```

## 🚀 Getting Started

### Prerequisites

You need [Python 3.7+](https://www.python.org/downloads/) installed on your machine.

### Installation

1. **Clone the repository** (if applicable) or download the files.
2. **Navigate to the project directory** in your terminal:
   ```bash
   cd path/to/appointment_taking_system-
   ```
3. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv env
   # On Windows:
   .\env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate
   ```
4. **Install the required dependencies** (Flask):
   ```bash
   pip install flask
   ```

### Running the App

To start the backend server, run the `app.py` wrapper file via the command line:

```bash
python app.py
```

The application will start locally. Open your web browser and navigate to `http://127.0.0.1:5000`.

## 👨‍💻 Usage Instructions

### For Patients
1. On the landing page (`/`), review the doctor's available times. Fill in the required **Date**, **Patient Name**, and valid **Contact Number**. *(Note: The system will alert and reset the form if you try to book on a pre-established leave/off day!)*
2. Click **Confirm Appointment**.
3. You will immediately be redirected to a `✅ Success!` page, where your **unique Serial Number** and your registered phone number are displayed.
4. Your information is securely logged.

### For the Doctor (Admin)
1. Navigate to the Admin area by clicking **Doctor Login (Admin Portal)** at the bottom of the landing page, or go directly to `http://127.0.0.1:5000/admin`.
2. Use the **Update Working Hours** widget to customize the times displayed to users.
3. Use the **Set Off Days / Leave** inputs to restrict specific dates from future bookings. You can simply hit the **Unblock** button to free it up again!
4. Scroll down to review the **Patient Appointment Report**. It visualizes your CSV file into a straightforward table detailing all requested schedules, ID counts, lengths, and valid contact numbers to manage your day easily.
