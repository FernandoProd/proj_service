# proj_service 🏭

**Smart Production Management System** — a Django-based web application for managing manufacturing orders, machines, and schedules, featuring an embedded ML model for processing time prediction.

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.10-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

## ✨ Key Features

*   **Machine Management** – Add, edit, and track machine status.
*   **Orders & Details** – Manage customer orders and part catalog with material specs.
*   **Smart Scheduling** – Automatically assign tasks to machines considering deadlines and priorities.
*   **ML-Powered Prediction** – Neural network predicts actual processing time per part and machine.
*   **Dockerized** – One-command setup with Docker Compose.

## 🚀 Quick Start

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)

### Run the project
1. Clone the repo:
   ```bash
   git clone https://github.com/FernandoProd/proj_service.git
   cd proj_service
   ```
2. (Optional) Place your detail.csv in the project root.

3. Start the container:
    ```bash
    docker-compose up --build
   ```
4. Access the app at http://localhost:8000
   - Admin panel: http://localhost:8000/admin
   - Login: `admin` Password: `admin`

## 📁 Project Structure (Simplified)
```bash
    proj_service/
    ├── manage.py
    ├── add_details.py          # Load parts from detail.csv
    ├── docker-compose.yml
    ├── Dockerfile
    ├── entrypoint.sh           # Auto-migration & superuser creation
    ├── requirements.txt
    ├── proj_service/           # Main Django config
    ├── machines/               # Machine management
    ├── orders/                 # Orders and parts
    ├── schedule/               # Scheduling logic
    └── ml_duration_predictor/  # ML model for time prediction
    ├── predictor.py
    ├── train_model.py
    ├── duration_model.h5
    └── *.pkl               # Encoders and scaler
 ```

 # 🔧 ML Model Usage
  1. Extract historical data – Run extract_data.py to create data.csv from actual schedule data.
  2. Train the model – Execute train_model.py to update duration_model.h5.
  3. Predict – Use predict_duration(detail, machine) from predictor.py in your scheduling logic.

## ⚙️ Manual Setup (without Docker)
```bash
    python -m venv venv
    source venv/bin/activate  # or `venv\Scripts\activate` on Windows
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
```

## 📄 License
MIT © FernandoProd
