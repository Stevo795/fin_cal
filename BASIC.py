
import sympy as sp

class basic:

    def __init__(self):
        self.an_value=""
        self.sn_value=""
        self.an_due_value=""
        self.an_due_value=""
        self.Ia_value=""



    def an(self, n,j):
        """ annuity immeidiate- present value

        Args:
            n ([int]): number of terms
            j ([int]): interest rate

        Returns:
            [double]: annuity immediate value
        """
        v=(1/(1+j))
        res=(1-v**n)/j
        # print(f"the result of n {n} j{j}: {res}")
        return res

    def sn(self,n,j):
        """accumulated annuity immediate - accumulated value

        Args:
            n ([int]): number of terms
            j ([int]): interest rate
        Returns:
            [double]: accumulated annuity immediate value
        """
        t1=(1+j)**n
        res=(t1-1)/j
        return res

    def an_due(self,n,j):
        v=(1/(1+j))
        d=(j/(1+j))
        res=(1-v**n)/d
        return res

    def sn_due(self,n,j):

        d=(j/(1+j))
        t1=(1+j)**n
        res=(t1-1)/d
        return res

    def IS(self,n,j):
        
        d=(j/(1+j))
        t1=(1+j)**n
        s_res=(t1-1)/d
        res=(s_res-n)/j

        return res