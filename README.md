# Quebrador-de-Senhas-Arquivos-Zip

Ataque de Força Bruta – Desafio de Programação
Nesse desafio o programa gera todas as possíveis senhas para abrir um arquivo! Um clássico ataque de força bruta.
Aqui vamos imaginar que não há limite no número de tentativas, então a única restrição é a de conseguir gerar todas as senhas

O desafio está dividido em 3 níveis

Fácil - Gere todas as combinações de números até 4 dígitos [0, 9999];
A linha 28 deverá ficar dessa maneira: 
forca_bruta('facil.zip', min_length=1, max_length=4, chars=string.digits)
onde 'facil.zip' é o arquivo que contem uma senha numerica de até 4 digitos

Médio - Gere todas as combinações de números e letras, maiúsculas e minúsculas, até tamanho 8;
A linha 28 deverá ficar dessa maneira: 
forca_bruta('medio.zip', min_length=1, max_length=8, chars=string.printable)
onde 'medio.zip' é o arquivo que contem uma senha alfanumerica de até 8 digitos

Avançado O programa recebe uma lista de caracteres ASCII e um parâmetro k indicando o tamanho máximo da senha, gerando todas as possíveis combinações;
A linha 28 deverá ficar dessa maneira: 
forca_bruta('hard.zip', min_length=1, max_length=30, chars=string.printable)
onde 'hard.zip' é o arquivo que contem uma senha alfanumerica de até 30 digitos

Aqui estão algumas variações do string.:

min_length = Quantidade de Caracteres
chars = tipo que pode ser letras com a string.
#ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
hexdigits = '0123456789abcdefABCDEF'
octdigits = '01234567'
printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
whitespace = ' \t\n\r\x0b\x0c'
