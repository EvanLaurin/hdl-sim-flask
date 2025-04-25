# HDL Simulation Web App

A simple Flask-based web app that simulates VHDL (HDL) files by parsing entity inputs and allowing users to test values through a friendly interface.

---

## Features

- Upload and parse behavioral VHDL files
- Auto-generate form inputs based on `entity` ports
- Run simple simulations and view outputs instantly
- Styled web interface with persistent forms
- Automatically clears uploaded files on startup

---


## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/hdl-sim-flask.git
cd hdl-sim-flask
```

### 2. Create and Activate Virtual Environment

```bash
py -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Project Structure

```
hdl-sim-flask/
├── app/
│   ├── __init__.py         # App config & upload folder cleanup
│   ├── routes.py           # Flask routes & logic
│   ├── parser.py           # Parses VHDL port definitions
│   ├── simulations.py      # Simulates HDL behavior
│   └── templates/
│       └── upload.html     # Main frontend template
├── uploads/                # Temporary uploaded VHDL files
├── app.py                  # Entry point
├── requirements.txt
└── README.md
```

---

## How It Works

1. User uploads a `.vhdl` or `.vhd` file.
2. The app parses the VHDL entity for input/output ports.
3. Input fields are dynamically generated in the UI.
4. User fills in values and clicks **Simulate**.
5. Simulation logic returns output values which are displayed below.

---

## VHDL Format Supported

This app supports simple **behavioral** VHDL files with a single `entity` and `architecture`. Example:

```vhdl
entity example is
  port (
    A : in std_logic;
    B : in std_logic;
    Y : out std_logic
  );
end example;
```

---

## Notes

- This is a **development tool** — do not use it for secure or critical simulations.
- Current simulation logic is a placeholder — extend it to use real VHDL simulators if needed.
- Uploaded files are wiped each time the app starts.

---

## License

MIT License

---

## Future Improvements

- Real HDL simulation backend (e.g., GHDL integration)
- Support for more complex VHDL constructs
