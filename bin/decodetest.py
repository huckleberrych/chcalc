import savedecoder

input = ''
decodedsave = str(savedecoder.decryptSave(input))
f = open('test.txt', 'w')
f.write(decodedsave)
f.close
