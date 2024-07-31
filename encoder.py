# program enkripsi
# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

flag = 'picoCTF{16_bits_inst34d_of_8_d52c6b93}'
result = ''

for i in range(0, len(flag), 2):
    a = ord(flag[i]) << 8
    b = ord(flag[i+1])
    c = a + b
    result += chr(c)
    print(result)
