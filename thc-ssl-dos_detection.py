from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *

ip1 = IPAddr('192.168.0.10')
n = 0
class AtaqueUno()
  def comparacion(self, n):
    while ( n < 5 ): 
      fwding =  (match(dstip=ip1) >> fwd(1))
      n = n + 1
    else:
      fwding =  (match(dstip=ip1) >> fwd(2))
