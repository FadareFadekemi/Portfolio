from pydantic import BaseModel, Field

class PredictionInput(BaseModel):
    transdatetrans_time : object = Field(...,description = "This is the date and time the transaction was made")
    amt : float = Field(...,description = "This is the first numerical feature for the model, this is the amount of purchase made")
    dob : object = Field(...,description = "This is the date of birth of the client, it is the first object feature for the model")
    lat:  float = Field(...,description = "This is the second numerical feature for the model, it is the latitude of the client as at the time they made the transaction")
    long: float = Field(...,description = "This is the third numerical feature for the model, it is the longitude of the client as at the time they made the transaction")
    merch_lat: float = Field(...,description = "This is the third numerical feature for the model, it is the latitude of the merchant as at the time they made the transaction")
    merch_long: float = Field(...,description = "This is the fourth numerical feature for the model, it is the longitude of the merchant as at the time they made the transaction")
    merchant: object = Field(...,description = "This is the merchant the financial institution that the client banks with")
    category: object = Field(...,description = "This is the category of the product or services the transaction was made for")
    
