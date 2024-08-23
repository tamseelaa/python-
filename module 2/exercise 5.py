print("enter a mass in medieval units")
t= int(input("enter talent:"))
p= int(input("enter pound:"))
l= float(input("enter lot:"))
int_lot= 13.3
pound= 32*13.3*p
talent= 20*32*13.3*t
lot= 13.3*l
print(f"The weight in modern units:{int((pound+talent+lot)/1000)}kilogram and {(pound+talent+lot)%1000:.3f}grams")