import subprocess
import locale

# Задание 1
print('Задание 1')
str1 = 'разработка'
str2 = 'cокет'
str3 = 'декоратор'

print(str1)
print(type(str1))

print(str2)
print(type(str2))

print(str3)
print(type(str3))

str_uni1 =  '\u0440\u0430\u0437\u0440\u0430\u0431\u043E\u0442\u043A\u0430'
print(str_uni1)
print(type(str_uni1))

str_uni2 =  '\u0441\u043E\u043A\u0435\u0442'
print(str_uni2)
print(type(str_uni2))

str_uni3 =  '\u0434\u0435\u043A\u043E\u0440\u0430\u0442\u043E\u0440'
print(str_uni3)
print(type(str_uni3))

# Задание 2
print('Задание 2')
byte_str1 = b'class'
print(byte_str1)
print(type(byte_str1))
print(len(byte_str1))

byte_str2 = b'function'
print(byte_str2)
print(type(byte_str2))
print(len(byte_str2))

byte_str3 = b'method'
print(byte_str3)
print(type(byte_str3))
print(len(byte_str3))

# Задание 3
# В байтовом типе возможно записать только ASCII символы
print('Задание 3')
print('В байтовом типе возможно записать только ASCII символы')
#byte_str_ascii1 = b'класс'
#byte_str_ascii1 = b'функция'

# Задание 4
print('Задание 4')
encode_str1 = 'разработка'
encode_str_bytes1 = encode_str1.encode('utf-8')
print(encode_str_bytes1)
encode_bytes_str1 = encode_str_bytes1.decode('utf-8')
print(encode_bytes_str1)

encode_str2 = 'администрирование'
encode_str_bytes2 = encode_str2.encode('utf-8')
print(encode_str_bytes2)
encode_bytes_str2 = encode_str_bytes2.decode('utf-8')
print(encode_bytes_str2)

encode_str3 = 'protocol'
encode_str_bytes3 = encode_str3.encode('utf-8')
print(encode_str_bytes3)
encode_bytes_str3 = encode_str_bytes3.decode('utf-8')
print(encode_bytes_str3)

encode_str4 = 'standard'
encode_str_bytes4 = encode_str4.encode('utf-8')
print(encode_str_bytes4)
encode_bytes_str4 = encode_str_bytes4.decode('utf-8')
print(encode_bytes_str4)

# Задание 5
print('Задание 5')
arg = [ 'ping', '127.0.0.1' ]
sub_ping = subprocess.Popen(arg,stdout=subprocess.PIPE)
for line in sub_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))

# Задание 6
print('Задание 6')

f_n = open('test_file.txt','w')
f_n.write('сетевое программирование\nсокет\nдекоратор\n')
#f_n.write('сетевое программирование\n сокет\n декоратор\n)
#f_n.write('сетевое программирование\n сокет\n декоратор\n)
f_n.close()
print(f_n)

with open('test_file.txt',encoding='utf-8') as f_n:
    for str in f_n:
        print(str)

# При попытке открыть файл в UTF-8 возвращается ошибка
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 0: invalid continuation byte
