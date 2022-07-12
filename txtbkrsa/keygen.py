from pyrsistent import v
import prime,os,random,math
import pandas as pd

class KeyGen:

    refid=0

    def __init__(self,keysize): 
        self.N=0 
        self.d=0 
        self.e=0
        self.keysize = keysize 
        KeyGen.refid+=1
        print("Reference id is"+KeyGen.refid)
    
    def modInverse(self,e,phi):
        '''Returns modular inverse of e%phi, 
        which d where e*d mod phi =1'''
        if math.gcd(e,phi)!=1:
            return None 
        u1,u2,u3=1,0,e 
        v1,v2,v3=0,1,phi
        while v3!=0: 
            q=u3//v3 
            v1,v2,v3,u1,u2,u3 =(u1 - q*v1),(u2 - q*v2),(u3 - q*v3),v1,v2,v3
        return u1%phi

    def storeKeys(self,N,e,d):
        pass

    def generateKey(self,keysize=0): 
        if keysize == 0:
            keysize = self.keysize
        print("Generating p")
        p=prime.generatePrime(keysize) 
        q=prime.generatePrime(keysize) 
        N=p*q 
        phi=(p-1)*(q-1) 
        e=random.randrange(2**(keysize-1),2**keysize) 
        print("Calculating public key e",end="")
        while True:
            if (math.gcd(e,N)==1) and (math.gcd(e,phi)==1) :
                break 
            else:
                print(".",end="")
                e=random.randrange(2**(keysize-1),2**keysize)  
        print("Calculating private key d",end="") 
        d=self.modInverse(e,phi) 
        publickey=(N,e)
        privatekey=(N,d) 
        storeKeys(N,e,d)
        return (publickey,privatekey) 

    

        
