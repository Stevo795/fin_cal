
class loan:

    def __init__(self,i=0,t=0,n=0,K=0):
        self.i, self.t,self.n,self.K=float(i),float(t),float(n),float(K)
        self.It_value="-"
        self.Pr_value="-"
        self.OB_value="-"

    def It(self):
        
        v=(1/(1+self.i))

        It=self.K*(1-(v**(self.n-self.t+1)))

        self.It_value=It

    def Pr(self):
        v=(1/(1+self.i))
        Pr=self.K*(v**(self.n-self.t+1))
        ##
        self.Pr_value=Pr

    def OB(self):
        #OB
        v=(1/(1+self.i))
        res=self.K*(1-v**(self.n-self.t))/self.i

        self.OB_value=res 
