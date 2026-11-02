import math

route = [
        ("Jakarta Kota", 0.0),
        ("Manggarai", 9.8),
        ("Depok", 32.1),
        ("Bogor", 54.8)
    ]

def paymentprocessing(balance, totalfare): # check if balance covers total fare
    if balance  >=  totalfare:
        NewBalance = balance - totalfare
        print(f"Payment Successful. New Balance: Rp {NewBalance:,.0f}")
        return True, NewBalance
    else:
        print("Balance Not Sufficient, Payment Failed")
        return False, balance

def FareCalculation(distance): # Calculates the total fare
    if distance <= 25:
        total_fare = 3000
    else:
        remaining_distance = distance - 25
        
        num_multiples = math.ceil(remaining_distance / 10)
        
        extra_fare = num_multiples * 1000
        
        total_fare = 3000 + extra_fare
    return total_fare

def turntile_control(HasPaymentSucceeded): #check if payment has succeeded if so open the turntile
    if HasPaymentSucceeded:
        print("Turntile Opened")
    else:
        print("Turntile Access Denied")

def SaveTransactionRecord(entry_station, exit_station, distance, total_fare, payment_success, balance): #Save the transaction record 
    if payment_success:
        status = "Successful"
    else:
        status = "Failed (Insufficient Balance)"
    TransactionRecord = {
        "entry_station": entry_station,
        "exit_station": exit_station,
        "distance_km": distance,
        "fare_paid": total_fare,
        "payment_status": status,
        "remaining_balance": balance
    }
    for key, value in TransactionRecord.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

def printavailablestations():
    for station, distance in route:
       print("Available Stations")
       print(f" Stasiun: {station} - Distance: {distance} KM")

def checkifisinlist(StationChecked):
    returnvalue = False, 0
    for station, distance in route:
        if station == StationChecked:
            returnvalue = True, distance
        else:
            pass
    return returnvalue

        

def main(): #takes inputs and uses the functions in tandem to create a final output
    entrycorrect : bool
    exitcorrect : bool
    entrydistance : float
    exitdistance : float
    entry_station = input("Enter entry station name: ")
    exit_station = input("Enter exit station name: ")
    CardBalance = float(input("Enter digital card balance (Rp): "))
    entrycorrect, entrydistance = checkifisinlist(entry_station)
    exitcorrect, exitdistance = checkifisinlist(exit_station)
    print(entrycorrect, exitcorrect)
    if entrycorrect and exitcorrect:
        distance = abs(entrydistance - exitdistance)
        total_fare = FareCalculation(distance)
        print(f"Trip Fare: RP {total_fare:,.0f}")
        payment_success, new_balance = paymentprocessing(CardBalance, total_fare)
        turntile_control(payment_success)
        SaveTransactionRecord(entry_station,exit_station,distance,total_fare,payment_success, new_balance)
    else:
        print("Station Invalid!, Please Enter a valid Station")


if __name__ == "__main__":
    printavailablestations()
    main()

