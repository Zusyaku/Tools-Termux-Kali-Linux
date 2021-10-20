from math import *
import json

try:
 B = open("brain.json","r")
 brain = json.loads(B.read())
 B.close()
except:
 brain = {}

def diff(a,b):
  Q =[];X=min([len(a),len(b)])
  for k in range(0,X):
     MX = max([a[k],b[k]])
     MN = min([a[k],b[k]])
     Q.append(MX-MN)
  return Q

def D2A(X):
 return [x for x in X]


def learn(x):
  Q = [ord(z) for z in x]
  D =  {
     'data':Q,'word':x,
     'length':len(Q),
     'max':max(Q),'min':min(Q),
     'datasum':sum(Q)
       }
  brain[sum(Q)]=D
  return D


def think(N):
  E = [ord(x) for x in N]
  Y = [abs(int(S)-sum(E)) for S in brain.keys()]
  C = Y.index(min(Y));
  J=[z for z in brain.keys()]
  return brain[J[C]]


def uthink(N):
  R = [ord(x) for x in N]
  X={};W={}
  for J in brain.keys():
    X[J]=brain[J]['data']
  for K in X.keys():
    W[K]=diff(D2A(X[K]),R)

  ZSUM = [sum(k) for k in D2A(W.values())]
  Y = ZSUM.index(min(ZSUM))
  F = D2A(X.keys())
  return brain[F[Y]]



def bsave():
  E = open("brain.json","w")
  E.write(json.dumps(brain))
  E.close()


while True:
  msg = input("Enter Text : ")
  M = msg.lower().split()
  if M[0] == "l":
     learn(" ".join(M[1:]))
     bsave()
     print(" Learned : {}".format(" ".join(M[1:])))
  elif M[0] == "e":
     C = uthink(" ".join(M[1:]))
     print("Correct : {}".format(C['word']))
  else:
     C = think(msg.lower())
     print("Correct : {}".format(C['word']))
