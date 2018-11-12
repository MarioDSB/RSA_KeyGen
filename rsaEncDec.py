import genRSAkey
import sys

with open(sys.argv[2],'r') as plain:
  m =plain.read()
l = int(sys.argv[1])

def tobits(s):
  result = []
  for c in s:
      bits = bin(ord(c))[2:]
      bits = '00000000'[len(bits):] + bits
      result.extend([int(b) for b in bits])
  return result

def frombits(bits):
  chars = []
  for b in range(int(len(bits) / 8)):
      byte = bits[b*8:(b+1)*8]
      chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
  return ''.join(chars)

def enc_RSA(m,e,n):

  c = [pow(ord(char),e,n) for char in m]

  return c

def dec_RSA(c,d,n):
  
  m = [chr(pow(char,d,n)) for char in c]

  return ''.join(m)

if __name__ == "__main__":
  
  rsatuple = genRSAkey.genRSAkey(l)

  c = enc_RSA(m,rsatuple[3],rsatuple[0])

  print (c)

  m = dec_RSA(c,rsatuple[4],rsatuple[0])

  print (m)