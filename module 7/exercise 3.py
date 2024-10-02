airports={
    "EFHK":"helsinki-vantaa airport", "OTBD":"doha international airport" ,"VIDP":"indira gandhi international airport",
    "OPLA":"allama iqbal international airport"
}


entered=input("You want to ENTER new airport, or FETCH the information of existing airport or QUIT : give command through capital word  ").upper()
while entered!="QUIT":
    if entered=="ENTER":
        print("to quit entering name of airports and there icoa ,just press enter on name of airport")
        new_name=input("Enter name of the airport").lower
        new_icao=(input("Enter ICAO code: ")).upper()
        airports[new_icao]=new_name
    elif entered=="FETCH":
        fetch_icao=input("enter icao of the airport").upper()
        print(airports[fetch_icao])
    entered = input("You want to ENTER new airport, or FETCH the information of existing airport or QUIT : give command through capital word  ").upper()
else:
    print("program is ending")




