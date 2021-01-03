
import sympy as sp

class cpeq:


    
    def __init__(self):
        self.res="-"


    def eq(self, input_list):
        F=input_list[0]
        C=input_list[1]
        P=input_list[2]
        r=input_list[3]
        j=input_list[4]
        n=input_list[5]
        
    
        
        #
        try:
            F=float(F)
        except:
            F=sp.symbols(F)
        #
        try:
            C=float(C)
        except:
            C=sp.symbols(C)
        #
        try:
            r=float(r)
        except:
            r=sp.symbols(r)
        #
        try:
            P=float(P)
        except:
            P=sp.symbols(P)
        #
        try:
            n=float(n)
        except:
            n=sp.symbols(n)
        #
        try:
            j=float(j)
        except:
            j=sp.symbols(j)

        return "Solve (" + str(C*(1/(1+j))**n + F*r*((1-(1/(1+j))**n)/j) -P) + ")=0"

    # C*(1/(1+j))**n + F*r*((1-(1/(1+j))**n)/j) -P