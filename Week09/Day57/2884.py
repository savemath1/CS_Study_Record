H, M= input().split()
H = int(H)
M = int(M)
if M >= 45:
   M = M - 45
   print(H, M)
elif M < 45 and H >=1:
   H = H - 1
   M = M + 15
   print(H, M)
else:
   M = M + 15
   print(23, M)