# 7.	Write program to convert prefix/net mask to IP
def mask_to_IP(inp):
  inp = int(inp)
  mask = (0xffffffff >> (32 - inp)) << (32 - inp)
  return (str( (0xff000000 & mask) >> 24)   + '.' +
          str( (0x00ff0000 & mask) >> 16)   + '.' +
          str( (0x0000ff00 & mask) >> 8)    + '.' +
          str( (0x000000ff & mask)))
          
          
print(mask_to_IP(16))
