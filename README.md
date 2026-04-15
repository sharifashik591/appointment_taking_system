# Doctor Appointment Booking System 🩺

A lightweight, minimal web application built with Python and Flask. Patients can easily submit an appointment request, which dynamically generates a unique appointment serial number and logs all records locally to a CSV file.

## ✨ Features

- **Live Appointment Tracking**: Displays a live count of total appointments recorded on the booking page.
- **Dynamic Serial Generation**: Automatically produces sequential serial numbers for each incoming appointment based on previous records.
- **Data Persistence**: Ensures that every confirmed appointment is systematically logged into an `appointments.csv` file without the need for a heavy external database. 
- **User-Friendly Flow**: A clear, fast 2-step process from selecting a date to immediately receiving detailed confirmation containing a generated Serial ID.

## 📂 Project Structure

```text
appointment_taking_system-
│
├── app.py                  # The Flask backend Python server handling routes/logic
├── appointments.csv        # Auto-generated CSV file containing logged appointments
├── .gitignore              # Files/folders to be ignored by Git
├── env/                    # Local Python virtual environment
└── templates/              # Directory holding all frontend UI files
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

## 👨‍💻 Usage Instruction

1. On the landing page (`/`), fill in the required **Date**, **Patient Name**, and valid **Contact Number**.
2. Click **Confirm Appointment**.
3. You will immediately be redirected to a `✅ Success!` page, where your **unique Serial Number** and your registered phone number are displayed.
4. Your information is now securely stored inside `appointments.csv` at the root of the project.
5. If you decide to `Go back to Homepage`, the total recorded appointments counter will dynamically update to reflect your recent submission.
