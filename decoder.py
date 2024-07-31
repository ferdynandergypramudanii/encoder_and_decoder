flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽'
result = ''

for i in range(0, len(flag), 1):
    a = (ord(flag[i]) >> 8)
    result += chr(a)
    b = (ord(flag[i]) - ((ord(flag[i]) >> 8) << 8))    
    result += chr(b)
    print(result)
    print('-----')