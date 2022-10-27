def get_current(amount):
    L = []
    i = 0
    amount = int(amount)
    if amount >= 5000:
        kol_nal_per = amount // 5000
        kol_nal_vtor = amount % 5000
        while i < kol_nal_per:
            L.append(5000)
            i += 1
        amount = kol_nal_vtor
    if amount >= 2000:
        i = 0
        kol_nal_per = amount // 2000
        kol_nal_vtor = amount % 2000
        while i < kol_nal_per:
            L.append(2000)
            i += 1
        amount = kol_nal_vtor
    if amount >= 500:
        i = 0
        kol_nal_per = amount // 500
        kol_nal_vtor = amount % 500
        while i < kol_nal_per:
            L.append(500)
            i += 1

        amount = kol_nal_vtor
    if amount >= 200:
        i = 0
        kol_nal_per = amount // 200
        kol_nal_vtor = amount % 200
        while i < kol_nal_per:
            L.append(200)
            i += 1

        amount = kol_nal_vtor
    if amount >= 100:
        i = 0
        kol_nal_per = amount // 100
        kol_nal_vtor = amount % 100
        while i < kol_nal_per:
            L.append(100)
            i += 1

        amount = kol_nal_vtor
    if amount >= 50:
        i = 0
        kol_nal_per = amount // 50
        kol_nal_vtor = amount % 50
        while i < kol_nal_per:
            L.append(50)
            i += 1

        amount = kol_nal_vtor
    if amount >= 20:
        i = 0
        kol_nal_per = amount // 20
        kol_nal_vtor = amount % 20
        while i < kol_nal_per:
            L.append(20)
            i += 1

        amount = kol_nal_vtor
    if amount >= 10:
        i = 0
        kol_nal_per = amount // 10
        kol_nal_vtor = amount % 10
        while i < kol_nal_per:
            L.append(10)
            i += 1

        amount = kol_nal_vtor
    if amount >= 5:
        i = 0
        kol_nal_per = amount // 5
        kol_nal_vtor = amount % 5
        while i < kol_nal_per:
            L.append(5)
            i += 1

        amount = kol_nal_vtor
    if amount >= 3:
        i = 0
        kol_nal_per = amount // 3
        kol_nal_vtor = amount % 3
        while i < kol_nal_per:
            L.append(3)
            i += 1

        amount = kol_nal_vtor
    if amount < 3:
        i = 0
        kol_nal_per = amount // 1
        kol_nal_vtor = amount % 1
        while i < kol_nal_per:
            L.append(1)
            i += 1


    return (L)
S = get_current(7892)
print(S)

