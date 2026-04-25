from fastapi import FastAPI
from pydantic import BaseModel
from planner import generate_plan
from database import engine, SessionLocal
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class StudyInput(BaseModel):
    subjects: list[str]
    hours_per_day: int

@app.post("/plan/")
def create_plan(data: StudyInput):
    db = SessionLocal()

    plan = generate_plan(data.subjects, data.hours_per_day)

    new_plan = models.StudyPlan(
        subjects=",".join(data.subjects),
        hours=data.hours_per_day,
        plan=str(plan)
    )

    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)

    return {"message": "Plan saved!", "plan": plan}