import re 
import sys

f=open('izlaz.txt','w')
f.close()

class Ulaz:
    def __init__ (self,grad,pov,sprat,soba,cena):
        self.grad=grad
        self.pov=pov
        self.sprat=sprat
        self.soba=soba
        self.cena=cena
    
    def __str__ (self):
        return('{}|{}|{}|{}|{}'.format(self.grad
                                       ,self.pov,self.sprat,self.soba,self.cena))
    
class Ucitulaz:
    def __init__(self):
        self.sve=[]

    def unos(self):
        l=[line.strip() for line in open ('ulaz.txt','r')]
        l.pop(0)
        for x in l:
            grad=x.split(',')[0]
            pov=x.split(',')[1]
            sprat=x.split(',')[2]
            soba=x.split(',')[3]
            cena=x.split(',')[4]
            ln=Ulaz(grad,pov,sprat,soba,cena)
            self.sve.append(ln)

    def sgradovi (self):
        self.gradovi=[]
        for x in self.sve:
            self.gradovi.append(x.grad)
        self.gradovi.sort()
        self.gradovi = list(dict.fromkeys(self.gradovi))

    def kriterijum(self):
        self.krit1=''
        self.krit2=''
        x=input('Unesite dva broja u formatiu a,b: ')
        a=x.split(',')[0]
        b=x.split(',')[1]
        if a.isdigit()==False and b.isdigit()==False:
            print ('Pogresno uneti podaci')
            quit()
            return
        if a.isdigit()==True and b.isdigit()==False and b!='':
            print ('Pogresno uneti podaci')
            quit()
            return
        if a.isdigit()==False and b.isdigit()==True and a!='':
            print ('Pogresno uneti podaci')
            quit()
            return
        if a.isdigit()==True and b.isdigit()==True:
            self.krit1=a
            self.krit2=b
            return
        if a.isdigit()==True and b.isdigit()==False and b=='':
            self.krit1=a
            self.krit2=''
            return
        if a.isdigit()==False and b.isdigit()==True and a=='':
            self.krit1=''
            self.krit2=b
            return

    def proverakriterijuma(self):
        self.izlaz=[]
        if self.krit1.isdigit()==True and self.krit2.isdigit()==True:
            for x in self.gradovi:
                for y in self.sve:
                    if x==y.grad:
                        if self.krit1==y.sprat and self.krit2==y.soba:
                            self.izlaz.append(y.grad)
        if self.krit1.isdigit()==False and self.krit2.isdigit()==True and self.krit1=='':
            for x in self.gradovi:
                for y in self.sve:
                    if x==y.grad:
                        if self.krit2==y.soba:
                            self.izlaz.append(y.grad)
        if self.krit1.isdigit()==True and self.krit2.isdigit()==False and self.krit2=='':
            for x in self.gradovi:
                for y in self.sve:
                    if x==y.grad:
                        if self.krit1==y.sprat:
                            self.izlaz.append(y.grad)

    def izdatoteka(self):
        self.out=[]
        for x in self.izlaz:
            a=[x,0,100000000000,0,0,0]
            for y in self.sve:
                if x==y.grad:
                    b=float(y.pov)
                    c=float(y.cena)     
                    a[3]=a[3]+c
                    a[4]=a[4]+b
                    d=a[3]/a[4]
                    if a[1]<c:
                        a[1]=c
                    if a[2]>c:
                        a[2]=c
                    a[5]=d
            self.out.append(a)

    def stampa(self):
        self.stampa=[]
        for x in self.out:
            l=[x[0],x[1],x[2],x[5]]
            self.stampa.append(l)

    def enstampa(self):
        f=open('izlaz.txt','w')
        f.close()
        f = open('izlaz.txt', 'a')
        for x in K.stampa:
            aa=('{} {} {} {}'.format(x[0],x[1],x[2],x[3]))
            print(aa, file=f)
        f.close()        


K=Ucitulaz()
K.unos()
K.sgradovi()
K.kriterijum()

K.proverakriterijuma()
K.izdatoteka()
K.stampa()
K.enstampa()

for x in K.izlaz:
    print (x)

print('==============================================')

for x in K.stampa:
    print (x)




   

