def char_pol_f(self, M, x): #characteristic polinomyal func 
        if len(M) == 2: 
            self.char_p = pow(x, 2)-self.trace(M)*x+self.det_f(M) 
        elif len(M) == 3: 
            self.char_p = pow(x, 3)-self.trace(M)*pow(x, 2)+self.sum_of_minors_3(M)*x-self.det_f(M) 
        return self.char_p