#247CTF - My MAGIC BYTES SABIR Yassine

jpg_header = [0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46, 0x00, 0x01]

encrypted_image = open("/home/ysab/Downloads/my_magic_bytes.jpg.enc","rb")

img_enc = encrypted_image.read()

image_recovered = open("/home/ysab/Downloads/recovered_image.jpg","wb")

xor_key = []

N = len(jpg_header)

for i in range(N):
    xor_key += [jpg_header[i] ^ img_enc[i]]

ind = 0

for i in range(len(img_enc)):
    image_recovered.write((img_enc[i] ^ xor_key[ind]).to_bytes(1,'little'))
    ind += 1
    if ind == N:
        ind = 0
encrypted_image.close()
image_recovered.close()