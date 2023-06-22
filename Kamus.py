meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "LMAO": " Mirip dengan LOL ",
            "BTW": "Singkatan dari by the way"
            }

for i in range(5):
    word = input("Ketik kata yang tidak kamu mengerti (gunakan huruf kapital semua): ")


    if word in meme_dict.keys():
        print(meme_dict[word])
    
    else:
        print("kata tidak ditemukan")
