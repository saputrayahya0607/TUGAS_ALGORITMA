tasks = []

while True:
    print("\nDaftar menu:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")
    choice = input("\nTambahkan menu baru (tekan 'oke' untuk mengonfirmasi): ")
    if choice.lower() == 'oke':
        break
    else:
        tasks.append(choice)
        
print("\nTerima kasih! Daftar menu Anda:")
for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")