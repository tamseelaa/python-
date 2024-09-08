
def even(n):
    evens=[]
    for i in n:
       if i%2==0:
          evens.append(i)
    print (f"updated version= {evens}")

List=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(f"original list={List}")
even(List)
