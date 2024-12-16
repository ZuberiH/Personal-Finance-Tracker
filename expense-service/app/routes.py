from fastapi import APIRouter, HTTPException
from app.database import get_db
from app.models import Expense
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/expenses/")
def create_expense(amount: float, category: str, description: str = None, db: Session = get_db()):
    expense = Expense(amount=amount, category=category, description=description)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return {"message": "Expense added successfully", "expense": expense}

@router.get("/expenses/")
def read_expenses(db: Session = get_db()):
    expenses = db.query(Expense).all()
    return {"expenses": expenses}

@router.put("/expenses/{expense_id}")
def update_expense(expense_id: int, amount: float, category: str, description: str = None, db: Session = get_db()):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    expense.amount = amount
    expense.category = category
    expense.description = description
    db.commit()
    return {"message": "Expense updated successfully"}

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = get_db()):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted successfully"}
