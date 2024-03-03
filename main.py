# basic_qrcode.py
import csv
import segno

# qrcode = segno.make_qr("Привет")
# qrcode.save("basic_qrcode.png")

with open('test.csv', 'r', newline='', encoding="cp1251", errors='ignore') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        qrcode = segno.make_qr(row[1])
        qrcode.save(f"{row[0]}.png", scale=5)
        print(row)
