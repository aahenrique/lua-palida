import sys
import time
import floresta

def texto():
    time.sleep(2)
    print("Você está em uma sala escura. A luz do luar brilha pela janela.")
    print("Há OURO no canto, junto á uma PÁ e uma CORDA.")
    print("Tem uma PORTA no LESTE.\n")
    sala()

def sala():
    comando = input("Comando?\n\nVocê consegue ver uma PORTA\n\n>").lower()
    if comando == "pegar ouro":
        print("PEGOU OURO.")
        comando = input("\n>").lower()
        if comando == "pegar pá" or comando == "pegar pa":
            print("PEGOU PÁ.")
            comando = input("\n>").lower()
            if comando == "pegar corda":
                print("PEGOU CORDA.")
                comando = input("\n>").lower()
                if comando == "abrir porta":
                    print("ABRIU PORTA.")
                    comando = input("\n>").lower()
                    if comando == "leste":
                        print("Pegue sua recompensa.")
                        print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")
                        time.sleep(3)
                        floresta.floresta()
                    else:
                        sys.exit()
                else:
                    sys.exit()
            else:
                sys.exit()
        else:
            sys.exit()
    else:
        sys.exit()