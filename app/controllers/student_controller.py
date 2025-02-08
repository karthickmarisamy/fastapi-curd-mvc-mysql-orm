from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.student_schema import StudentSchema
from ..db.database import get_db
from ..models.student_model import Personal_detail
from ..utils.response_wrapper import api_response

router = APIRouter()

@router.post('/student')
async def create_student(student: StudentSchema, db: Session = Depends(get_db())):
    if db.query(Personal_detail).filter(Personal_detail.email == student.email).first():
        raise HTTPException(status_code = 400, detail = "Email Id is already registered")
    
    new_student = Personal_detail(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return api_response(data=new_student, message="New Student record is created successfully")