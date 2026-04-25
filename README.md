# AI-Study-Planner-API
#  Smart AI Study Planner API

A FastAPI-based backend project that generates optimized study schedules based on user subjects and available time. The system intelligently distributes study hours and stores plans using a database.

---

##  Features

*  Generate personalized study plans
*  Dynamic time allocation based on subjects
*  Store study plans using SQLite database
*  Fast and efficient API using FastAPI
*  Interactive API testing with Swagger UI

---

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

---

##  Project Structure

```
study-planner/
 ├── main.py          # Main API file
 ├── planner.py       # Study plan logic
 ├── models.py        # Database models
 ├── database.py      # Database connection
 └── requirements.txt
```

---

##  Installation & Setup

### 1️ Clone the repository

```
git clone https://github.com/your-username/study-planner.git
cd study-planner
```

### 2️ Create virtual environment

```
python -m venv venv
```

### 3️ Activate virtual environment

* Windows:

```
venv\Scripts\activate
```

### 4️ Install dependencies

```
pip install -r requirements.txt
```

---

##  Run the Application

```
uvicorn main:app --reload
```

---

##  API Documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

##  Example API Request

### POST /plan/

#### Input:

```json
{
  "subjects": ["Math", "AI", "DBMS"],
  "hours_per_day": 6
}
```

#### Output:

```json
{
  "study_plan": {
    "Math": "2 hours",
    "AI": "2 hours",
    "DBMS": "2 hours"
  }
}

---

##  Future Improvements

*  User Authentication (Login/Register)
*  Weekly/Monthly planner
*  AI-based recommendations
*  Deployment on cloud
  
---

##  Contributing

Feel free to fork this repository and contribute!

---

##  License

This project is licensed under the MIT License.

---

##  Author

**Aditi Verma**
