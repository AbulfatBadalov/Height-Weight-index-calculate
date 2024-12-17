boy=int(input("Boyunuzu daxil edin(cm): "))
kilo=float(input("Kilonuzu daxil edin(kq): "))
index=kilo/((boy/100)**2)
print(f"Beden indeksiniz:{index}")
if index<=18.5:
    print("Beden indeksinize gore ariqsiniz.")
elif index<=24.5:
    print("Siz normalsiniz.")
elif index<=30:
    print("Siz koksunuz.")
elif index<=40:
    print("Siz obezsiniz")
else:
    print("Siz cox obezsiniz")
