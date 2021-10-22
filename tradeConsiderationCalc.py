#This helps determine the trade consideration for either equity purchase or sale, or discounted money market instrument.
#The login function does not test for authentication just needed to capture the username and the action the user want to carry on. The variable holding the selected option is assigned a global variable and used in the transactionType() function
#The discountedInst() function and equityTransaction() function are both subset transactionType()
 

from datetime import datetime, date

import datetime


def login ():
    global response
    userName=input("Enter Username \n")
    password=input("Enter password \n")

    print(f"You have successfully logged in {userName} \nWhat transaction do you want to do? \nEnter (1) for Equity trade, (2) for Discounted Money Market Instrument and (3) for Bond")
    response=int(input("Enter option \n"))

transCostBuy={
    "brokerageRate":1.35,
    "SECRate":0.00,
    "CSCSRate":0.3,
    "NSERate":0.3,
    "stampDutyRate":0.08
}

transCostSell={
    "brokerageRate":1.35,
    "SECRate":0.0,
    "CSCSRate":0.3,
    "NSERate":0.3,
    "stampDutyRate":0.08
}


def equityTransaction():
    transtype=input("Enter Buy or Sell  \n").upper()
    symbol=input("Enter stock symbol \n")
    units=int(input("Enter Units \n"))
    price=float(input("Enter price \n"))
    #Transaction Type
    if transtype=="BUY":
        typeMultiplier=1
    elif transtype=="SELL":
        typeMultiplier=-1
    
    #Appropriate rate
    if transtype=="BUY":
        brokerage=transCostBuy["brokerageRate"]/100
        SEC=transCostBuy["SECRate"]/100
        CSCS=transCostBuy["CSCSRate"]/100
        NSE=transCostBuy["NSERate"]/100
        stampDuty=transCostBuy["stampDutyRate"]/100
    elif transtype=="SELL":
        brokerage=transCostSell["brokerageRate"]/100
        SEC=transCostSell["SECRate"]/100
        CSCS=transCostSell["CSCSRate"]/100
        NSE=transCostSell["NSERate"]/100
        stampDuty=transCostSell["stampDutyRate"]/100        

    transprice=units*price
    brokerageFee=transprice*brokerage*typeMultiplier
    NSEFee=transprice*NSE*typeMultiplier
    SECFee=transprice*SEC*typeMultiplier
    CSCSFee=transprice*CSCS*typeMultiplier
    stampDutyFee=transprice*stampDuty*typeMultiplier
    totalTransCost=brokerageFee+NSEFee+SECFee+CSCSFee+stampDutyFee
    transConsideration=transprice+totalTransCost

    # To be displayed with "," as separator
    transpriceDisplay="{:,}".format(transprice)
    totalTransCostDisplay="{:,}".format(totalTransCost*typeMultiplier)
    transConsiderationDisplay="{:,}".format(transConsideration)
    
    print(f"Please find details of your trade")
    print(f"Stock: {symbol}")
    print(f"Transaction Type: {transtype}")
    print(f"Units: {units}")
    print(f"price: {price}")
    print(f"Transaction price: {transpriceDisplay}")
    print(f"Transaction costs: {totalTransCostDisplay}")
    print(f"Total Consideration: {transConsiderationDisplay}")

    
def discountedInst ():
    faceValue=float(input("Enter face value you which to sell/purchase  \n"))
    discRate=float(input("Enter appropriate discount rate  \n"))
    print(f"Enter Value date details \n")
    valDateYear=int(input("Enter year \n"))
    valDateMonth=int(input("Enter Month Number \n"))
    valDateDay=int(input("Enter Day \n"))
    print(f"Enter Maturity date details \n")
    matDateYear=int(input("Enter year \n"))
    matDateMonth=int(input("Enter Month Number \n"))
    matDateDay=int(input("Enter Day \n"))

    valDate=date(valDateYear,valDateMonth,valDateDay)
    matDate=date(matDateYear,matDateMonth,matDateDay)
    tenor=int((matDate-valDate).days)

    discount=faceValue*(discRate/100)*(tenor/365)
    discountedValue=round(faceValue-discount,2)
    discountedValueDisplay="{:,}".format(discountedValue)
    print(f"The discounted value of your investment is {discountedValueDisplay}")


def transactionType():
    if response==1:
        equityTransaction()
    elif response==2:
        discountedInst()
    elif response==3:
        print("Coming soon")
    else: 
        print("Wrong selection")

login()
transactionType()