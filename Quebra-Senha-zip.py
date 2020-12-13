from datetime import timedelta
from time import time
import itertools, string
import zipfile, zlib
def forca_bruta(src, min_length=1, max_length=None, chars=string.printable.strip()):
    start = time()
    count = 1
    with zipfile.ZipFile(src, 'r') as zf:
        while True:
            if max_length is not None:
                if min_length == max_length+1:
                    input('A digitalização excedeu o comprimento máximo. Pressione ENTER para sair...')
                    raise SystemExit
            for pwd in itertools.product(chars, repeat=min_length):
                try:
                    zf.extractall(pwd=bytes(''.join(pwd), encoding='utf-8'))
                    fmt = "\n+{}+\n|{:^88}|\n|{:^88}|\n+{}+"
                    return print(fmt.format(f"{'-'*34}_!SENHA_QUEBRADA!_{'-'*34}",
                                            "[+] Senha Encontrada!",
                                            f"Tentativas: {count} | Senha: {''.join(pwd)} | "
                                            f"Tempo Decorrido: {timedelta(seconds=time()-start)}", '-'*88))
                except (RuntimeError, zlib.error, zipfile.BadZipFile):
                    print(f"[{count}] [-] Senha Incorreta: {''.join(pwd)} | "
                          f"Tempo Decorrido: {timedelta(seconds=time()-start)}")
                    count += 1
            min_length += 1
if __name__ == '__main__':
    forca_bruta('facil.zip', min_length=1, max_length=4, chars=string.digits)
    









