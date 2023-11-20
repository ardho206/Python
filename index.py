import os

def numInput(inputAvg):
    totalInput = []
    for i in range(inputAvg):
        while True:
            try:
                totalInput.append(int(input(f'Masukkan Angka {i + 1} : ')))
                break
            except ValueError:
                print("Harap Memasukkan Angka!\n")
    return totalInput

def asc(val):
    for i in range(len(val)-1):
        for j in range(len(val)-1-i):
            if val[j] > val[j+1]:
                val[j], val[j+1] = val[j+1], val[j]
    return val

def desc(val):
    for i in range(len(val)-1):
        for j in range(len(val)-1-i):
            if val[j] < val[j+1]:
                val[j], val[j+1] = val[j+1], val[j]
    return val

def display_stats(data):
    max_val = max(data)
    min_val = min(data)
    avg_val = sum(data) / len(data)

    print(f"Max Value: {max_val}")
    print(f"Min Value: {min_val}")
    print(f"Average Value: {avg_val}")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console screen

    print("===================================")
    print("Program Mengurutkan Data\nMenggunakan Bubble Sort")
    print("===================================\n")

    try:
        inputAvg = int(input("Jumlah angka yang ingin di input : "))
    except ValueError:
        print("Harap Masukkan Bilangan Bulat!\n")
        continue

    totalInput = numInput(inputAvg)

    print("===================================\n")
    print("Metode Pengurutan")
    print("1. Ascending")
    print("2. Descending")
    
    try:
        bubbleSortMode = int(input("Pilih Metode Pengurutan (1/2) : "))
    except ValueError:
        print("Masukkan Antara 1 / 2\n")
        continue

    if bubbleSortMode == 1:
        sorted_data = asc(totalInput.copy())
    elif bubbleSortMode == 2:
        sorted_data = desc(totalInput.copy())
    else:
        print("Masukkan Antara 1 / 2\n")
        continue

    print(sorted_data)

    print("===================================\n")
    question = input("Apakah Anda Ingin Menampilkan Max, Min, dan Rata-rata (Y/N) : ")

    if question.lower() == "y":
        display_stats(sorted_data)
        whileBreak = input("\nApakah Ingin mengulangi Program Ini? (Y/N) : ")
        if whileBreak.lower() == "y":
            continue
        elif whileBreak.lower() == "n":
            print("Arigatou😁👍")
            break
        else:
            print("Masukkan dengan format (Y/N)")

    elif question.lower() == "n":
        whileBreak = input("\nApakah Ingin mengulangi Program Ini? (Y/N) : ")
        if whileBreak.lower() == "y":
            continue
        elif whileBreak.lower() == "n":
            print("Arigatou😁👍")
            break
        else:
            print("Masukkan dengan format (Y/N)")