import math


stations = []
currentstation : str

CardBalance : float
IsSufficient : bool

def paymentprocessing(balance, totalfare):
    if balance  >=  totalfare:
        NewBalance = balance - totalfare
        print(f"Payment Successful. New Balance: Rp {NewBalance:,.0f}")
        return True, NewBalance
    else:
        print("Balance Not Sufficient, Payment Failed")
        return False, CardBalance

def FareCalculation(distance):
    # Is distance <= 25 KM?
    if distance <= 25:
        # Fare = Rp 3,000
        total_fare = 3000
    else:
        # Remaining distance = Total distance - 25 KM
        remaining_distance = distance - 25
        
        # Round remaining distance up to the next multiple of 10 KM
        # and calculate the number of multiples
        num_multiples = math.ceil(remaining_distance / 10)
        
        # Extra fare = Number of multiples x Rp 1,000
        extra_fare = num_multiples * 1000
        
        # Total fare = Rp 3,000 + Extra fare
        total_fare = 3000 + extra_fare
    return total_fare

def turntile_control(HasPaymentSucceeded):
    if HasPaymentSucceeded:
        print("Turntile Opened")
    else:
        print("Turntile Access Denied")

def SaveTransactionRecord(entry_station, exit_station, distance, total_fare, payment_success, balance):
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

def main():
    entry_station = input("Enter entry station: ")
    exit_station = input("Enter exit station: ")
    CardBalance = float(input("Enter digital card balance (Rp): "))
    distance = float(input("Input total trip distancein KM: "))

    total_fare = FareCalculation(distance)
    print(f"Trip Fare: RP {total_fare:,.0f}")
    payment_success, new_balance = paymentprocessing(CardBalance, total_fare)
    turntile_control(payment_success)
    SaveTransactionRecord(entry_station,exit_station,distance,total_fare,payment_success, new_balance)
if __name__ == "__main__":
    main()
