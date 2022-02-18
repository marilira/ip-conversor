base = list(map(lambda x: 2**x, range(7, -1, -1)))

def binario(ip_decimal):
    ip = map(int, ip_decimal.split('.'))
    binario = ['']*4

    index = 0
    for bit in ip:
        for i in range(8):
            flag = False
            if (bit >= base[i]):
                bit -= base[i]
                flag = True
            if flag:
                binario[index] += '1'
            else:
                binario[index] += '0'
        index += 1

    ip_binario = str.join('.', binario)
    return ip_binario

def decimal(ip_binario):
    ip = ip_binario.split('.')
    decimal = []

    for bit in ip:
        num = 0
        for i in range(8):
            if bit[i] == '1':
                num += base[i]
        decimal.append(num)

    ip_decimal = str.join('.', map(str, decimal))    
    return ip_decimal