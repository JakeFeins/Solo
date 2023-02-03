
class eigenstate:
    def __init__(self, nx, ny, scalar_const=1):
        self.nx = int(nx)
        self.ny = int(ny)
        self.scalar_const = scalar_const
        self.state = (int(nx), int(ny))
    def checkzero(self):
        if self.scalar_const == 0:
            return True
        return False
    def a(self):
        if self.checkzero():
            return eigenstate(0,0,0)
        if self.nx == 0:
            return eigenstate(0,0,0)
        if self.nx == 1:
             return eigenstate(self.nx-1, self.ny, "{}".format(self.scalar_const))
        return eigenstate(self.nx-1, self.ny, "sqrt({})*{}".format(self.nx,self.scalar_const))
    def b(self):
        if self.checkzero():
            return eigenstate(0,0,0)
        if self.ny == 0:
            return eigenstate(0,0,0)
        if self.ny == 1:
             return eigenstate(self.nx, self.ny-1, "{}".format(self.scalar_const))
        return eigenstate(self.nx, self.ny-1, "{}".format(self.scalar_const))
    def at(self):
        if self.checkzero():
            return eigenstate(0,0,0)
        if self.nx == 0:
            return eigenstate(self.nx+1, self.ny, "{}".format(self.scalar_const))
        return eigenstate(self.nx+1, self.ny, "sqrt({})*{}".format(self.nx+1,self.scalar_const))
    def bt(self):
        if self.checkzero():
            return eigenstate(0,0,0)
        if self.ny == 0:
            return eigenstate(self.nx, self.ny+1, "{}".format(self.scalar_const))
        return eigenstate(self.nx, self.ny+1, "sqrt({})*{}".format(self.ny+1,self.scalar_const))
    def info(self):
        return (self.scalar_const,self.nx, self.ny)
    def __str__(self):
        return "{}|{},{}>".format(self.scalar_const,self.nx, self.ny)

def x(eigenlist):
        newlist = []
        for i in eigenlist:
            newlist.append(i.a())
            newlist.append(i.at())
        return newlist
def y(eigenlist):
        newlist = []
        for i in eigenlist:
            newlist.append(i.b())
            newlist.append(i.bt())
        return newlist
def printout(eigenlist):
    for i in eigenlist:
        if i.scalar_const == 0:
            print("0+",end="")
            continue
        if i != eigenlist[-1]:
            print(i.__str__()+"+",end="")
        else:
            print(i.__str__(),end="")
def simplify_eigenlist(eigenlist):
    newlist = []
    for i in eigenlist:
        if i.scalar_const == 0:
            continue
        ## check if i is in newlist
        for j in newlist:
            if i.state == j.state:
                j.scalar_const += "(+){}".format(i.scalar_const)
                break
        else:
            newlist.append(i)
    return newlist
def states(eigenlist):
    newlist = []
    for i in eigenlist:
        if i.scalar_const == 0:
            continue
        if i.state in newlist:
            continue
        newlist.append(i.state)
    return newlist
def innerproduct(eigenstate1, eigenstate2):
    if eigenstate1.nx == eigenstate2.nx and eigenstate1.ny == eigenstate2.ny:
        return eigenstate1.scalar_const*eigenstate2.scalar_const
    return 0
def Hprime(eigenlist):
    xlist = x(eigenlist)
    xylist = y(xlist)
    simplifylist = simplify_eigenlist(xylist)

    xxlist = x(x(simplifylist))
    yylist = y(y(simplifylist))

    return simplify_eigenlist(xxlist+yylist)
def listInnerProduct(eigenlist1, eigenlist2):
    newlist = []
    for i in eigenlist1:
        for j in eigenlist2:
            newlist.append(innerproduct(i,j))
    return newlist
def printoutInnerProduct(eigenlist1, eigenlist2):
    newlist = listInnerProduct(eigenlist1, eigenlist2)
    #if every entry is zero print 0
    if all(i == 0 for i in newlist):
        print("0",end="")
        return
    for i in newlist:
        if i == 0:
                continue
        if i != newlist[-1]:
            print("+({})".format(i),end="")
        else:
            print(i,end="+NaN")
def printnl():
    print("\n")

if __name__ == "__main__":
    onezero = [eigenstate(1,0)]
    zeroone = [eigenstate(0,1)]

    A = Hprime(onezero)
    B = Hprime(zeroone)

    print("<1,0|H'|1,0> =",end=" ")
    printoutInnerProduct(onezero,A)
    printnl()
    print("<0,1|H'|0,1> =",end=" ")
    printoutInnerProduct(zeroone,B)
    printnl()
    print("<1,0|H'|0,1> =",end=" ")
    printoutInnerProduct(zeroone,A)
    printnl()
    print("<0,1|H'|1,0> =",end=" ")
    printoutInnerProduct(onezero,B)
