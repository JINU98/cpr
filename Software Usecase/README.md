# Flask Backend and React Frontend Application

This repository contains code for CPR implementation in the form of web app.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/JINU98/cpr.git
cd cpr/"Mental Health Usecase"
```

### 2. Setup Flask Backend

#### a. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

#### b. Configure Flask

Re

#### c. Run Flask Server

```bash
python app.py
```

The Flask backend should now be running at `http://localhost:5000`.

### 3. Setup React Frontend

#### a. Install Dependencies

```bash
cd frontend
npm install
```

#### b. Configure Environment Variables

Create a `.env` file in the `frontend` directory and set the appropriate environment variables. For example:

#### c. Run React Development Server

```bash
npm install
npm start
```

The React frontend should now be running at `http://localhost:3000`.

## Usage

You can now access the web application by visiting `http://localhost:3000` in your web browser. The React frontend will communicate with the Flask backend API at `http://localhost:5000/api` by default.


