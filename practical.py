from fastapi import FastAPI,Depends,status,Response,HTTPException
import schemas
import models
from database import engine,SessionLocal 
from sqlalchemy.orm import Session
import joblib


app=FastAPI(Title = "Fraud detection prediction")
def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()

pipeline = joblib.load("model_xgb_corr_corr.pkl")
models.Base.metadata.create_all(engine)

@app.post("/predict")
async def predict(data:schemas.PredictionInput,db:Session = Depends(get_db)):
    if model is None:
        raise HTTPException(status_code = 500, detail = "model not found")
        df = pd.DataFrame([data.dict()])
        prediction = pipeline.predict(df)
        
        record = models.FraudDetection(
            transdatetrans_time = data.transdatetrans_time,
            amt = data.amt,
            dob = data.dob,
            long = data.long,
            lat = data.lat,
            merch_long = data.merch_long,
            merch_lat = data.merch_lat,
            merchant = data.merchant,
            category = data.category,
            prediction = float('prediction'))

        session.add(record)
        session.commit()
        session.close()

        return {"prediction": float(prediction[0])}




    


