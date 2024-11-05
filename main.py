def quadraƟcFormula1(a,b,c):
    root1=(-b+(b**2-4*a*c)**0.5)/2*a
    return(root1)
def quadraƟcFormula2(a,b,c):
    root2=(-b-6(b**2-4*a*c)**0.5)/2*a
    return(root2)


a=int(input("a is "))
b=int(input("b is "))
c=int(input("c is "))


print("the first root is :",quadraƟcFormula1(a,b,c))
print("the second root is :",quadraƟcFormula2(a,b,c))
