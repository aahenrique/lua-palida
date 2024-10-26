import os
import sys
import time

def verificar(comando):
    if comando == "usar ouro":
        print("Não aqui.")
        return True
    elif comando == "usar pa":
        print("Agora não.")
        return True
    elif comando == "usar corda":
        print("Você já usou isso.")
        return True
    return False

def caminho_final():
    print("""A LUA PÁLIDA SORRI LARGAMENTE.
Não há caminhos.
A LUA PÁLIDA SORRI LARGAMENTE.
O chão está macio.
A LUA PÁLIDA SORRI LARGAMENTE.
Aqui.\n\n""")
    comando = input("Comando?\n\n>").lower()
    if comando == "cavar buraco":
        print("Você cavou um buraco.")
        comando = input("\n>")
        if comando == "jogar ouro":
            print("Você jogou o ouro no buraco.")
            comando = input("\n>")
            if comando == "tapar buraco":
                print("Você tapou o buraco.")
                count = 20
                time.sleep(3)
                os.system('cls')
                while count >= 0:
                    print("""     PARABÉNS
---- 40.24248 ----
---- 121.4424 ----""")
                    count -= 1
                    time.sleep(0.5)
            else:
                sys.exit()
        else:
            sys.exit()
    else:
        sys.exit()

def floresta():
    while True:
        print("Você está em uma floresta, há caminhos para NORTE, SUL e LESTE.")
        comando = input("Comando?\n\n>").lower()

        if verificar(comando):
            comando = input("Comando?\n\n>").lower()

        if comando == "sul":
            print("Pegue sua recompensa.")
            print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

            print("Você está em uma floresta, há caminhos para NORTE, OESTE e LESTE.")
            comando = input("Comando?\n\n>").lower()

            if verificar(comando):
                comando = input("Comando?\n\n>").lower()

            if comando == "norte":
                print("Pegue sua recompensa.")
                print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                print("Você está em uma floresta, há caminhos para SUL, LESTE e OESTE.")
                comando = input("Comando?\n\n>").lower()

                if verificar(comando):
                    comando = input("Comando?\n\n>").lower()

                if comando == "oeste":
                    print("Pegue sua recompensa.")
                    print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                    print("Você está em uma floresta, há caminhos para NORTE, SUL e LESTE.")
                    comando = input("Comando?\n\n>").lower()

                    if verificar(comando):
                        comando = input("Comando?\n\n>").lower()

                    if comando == "leste":
                        print("Pegue sua recompensa.")
                        print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                        print("Você está em uma floresta, há caminhos para OESTE, NORTE e SUL.")
                        comando = input("Comando?\n\n>").lower()

                        if verificar(comando):
                            comando = input("Comando?\n\n>").lower()

                        if comando == "sul":
                            print("Pegue sua recompensa.")
                            print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                            print("Você está em uma floresta, há caminhos para LESTE, OESTE e NORTE.")
                            comando = input("Comando?\n\n>").lower()

                            if verificar(comando):
                                comando = input("Comando?\n\n>").lower()

                            if comando == "leste":
                                print("Pegue sua recompensa.")
                                print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                print("Você está em uma floresta, há caminhos para SUL, OESTE e NORTE.")
                                comando = input("Comando?\n\n>").lower()

                                if verificar(comando):
                                    comando = input("Comando?\n\n>").lower()

                                if comando == "oeste":
                                    print("Pegue sua recompensa.")
                                    print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                    print("Você está em uma floresta, há caminhos para NORTE, LESTE e SUL.")
                                    comando = input("Comando?\n\n>").lower()

                                    if verificar(comando):
                                        comando = input("Comando?\n\n>").lower()

                                    if comando == "norte":
                                        print("Pegue sua recompensa.")
                                        print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                        print("Você está em uma floresta, há caminhos para SUL, LESTE e OESTE.")
                                        comando = input("Comando?\n\n>").lower()

                                        if verificar(comando):
                                            comando = input("Comando?\n\n>").lower()

                                        if comando == "leste":
                                            print("Pegue sua recompensa.")
                                            print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                            print("Você está em uma floresta, há caminhos para OESTE, NORTE e SUL.")
                                            comando = input("Comando?\n\n>").lower()

                                            if verificar(comando):
                                                comando = input("Comando?\n\n>").lower()

                                            if comando == "sul":
                                                print("Pegue sua recompensa.")
                                                print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                print(
                                                    "Você está em uma floresta, há caminhos para NORTE, OESTE e LESTE.")
                                                comando = input("Comando?\n\n>").lower()

                                                if verificar(comando):
                                                    comando = input("Comando?\n\n>").lower()

                                                if comando == "oeste":
                                                    print("Pegue sua recompensa.")
                                                    print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                    print(
                                                        "Você está em uma floresta, há caminhos para NORTE, LESTE e SUL.")
                                                    comando = input("Comando?\n\n>").lower()

                                                    if verificar(comando):
                                                        comando = input("Comando?\n\n>").lower()

                                                    if comando == "norte":
                                                        print("Pegue sua recompensa.")
                                                        print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                        print(
                                                            "Você está em uma floresta, há caminhos para SUL, LESTE e OESTE.")
                                                        comando = input("Comando?\n\n>").lower()

                                                        if verificar(comando):
                                                            comando = input("Comando?\n\n>").lower()

                                                        if comando == "leste":
                                                            print("Pegue sua recompensa.")
                                                            print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                            print(
                                                                "Você está em uma floresta, há caminhos para OESTE, SUL e NORTE.")
                                                            comando = input("Comando?\n\n>").lower()

                                                            if verificar(comando):
                                                                comando = input("Comando?\n\n>").lower()

                                                            if comando == "sul":
                                                                print("Pegue sua recompensa.")
                                                                print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                print(
                                                                    "Você está em uma floresta, há caminhos para NORTE, OESTE e LESTE.")
                                                                comando = input("Comando?\n\n>").lower()

                                                                if verificar(comando):
                                                                    comando = input("Comando?\n\n>").lower()

                                                                if comando == "oeste":
                                                                    print("Pegue sua recompensa.")
                                                                    print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                    print(
                                                                        "Você está em uma floresta, há caminhos para NORTE, LESTE e SUL.")
                                                                    comando = input("Comando?\n\n>").lower()

                                                                    if verificar(comando):
                                                                        comando = input("Comando?\n\n>").lower()

                                                                    if comando == "norte":
                                                                        print("Pegue sua recompensa.")
                                                                        print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                        print(
                                                                            "Você está em uma floresta, há caminhos para LESTE, OESTE e SUL.")
                                                                        comando = input("Comando?\n\n>").lower()

                                                                        if verificar(comando):
                                                                            comando = input("Comando?\n\n>").lower()

                                                                        if comando == "sul":
                                                                            print("Pegue sua recompensa.")
                                                                            print("A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                            print(
                                                                                "Você está em uma floresta, há caminhos para NORTE, OESTE e LESTE.")
                                                                            comando = input("Comando?\n\n>").lower()

                                                                            if verificar(comando):
                                                                                comando = input("Comando?\n\n>").lower()

                                                                            if comando == "leste":
                                                                                print("Pegue sua recompensa.")
                                                                                print(
                                                                                    "A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                                print(
                                                                                    "Você está em uma floresta, há caminhos para OESTE, SUL e NORTE.")
                                                                                comando = input("Comando?\n\n>").lower()

                                                                                if verificar(comando):
                                                                                    comando = input(
                                                                                        "Comando?\n\n>").lower()

                                                                                if comando == "norte":
                                                                                    print("Pegue sua recompensa.")
                                                                                    print(
                                                                                        "A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                                    print(
                                                                                        "Você está em uma floresta, há caminhos para SUL, LESTE e OESTE.")
                                                                                    comando = input(
                                                                                        "Comando?\n\n>").lower()

                                                                                    if verificar(comando):
                                                                                        comando = input(
                                                                                            "Comando?\n\n>").lower()

                                                                                    if comando == "oeste":
                                                                                        print("Pegue sua recompensa.")
                                                                                        print(
                                                                                            "A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                                        print(
                                                                                            "Você está em uma floresta, há caminhos para NORTE, LESTE e SUL.")
                                                                                        comando = input(
                                                                                            "Comando?\n\n>").lower()

                                                                                        if verificar(comando):
                                                                                            comando = input(
                                                                                                "Comando?\n\n>").lower()

                                                                                        if comando == "leste":
                                                                                            print(
                                                                                                "Pegue sua recompensa.")
                                                                                            print(
                                                                                                "A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                                            print(
                                                                                                "Você está em uma floresta, há caminhos para OESTE, SUL e NORTE.")
                                                                                            comando = input(
                                                                                                "Comando?\n\n>").lower()

                                                                                            if verificar(comando):
                                                                                                comando = input(
                                                                                                    "Comando?\n\n>").lower()

                                                                                            if comando == "sul":
                                                                                                print(
                                                                                                    "Pegue sua recompensa.")
                                                                                                print(
                                                                                                    "A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                                                print(
                                                                                                    "Você está em uma floresta, há caminhos para NORTE, OESTE e LESTE.")
                                                                                                comando = input(
                                                                                                    "Comando?\n\n>").lower()

                                                                                                if verificar(comando):
                                                                                                    comando = input(
                                                                                                        "Comando?\n\n>").lower()

                                                                                                if comando == "oeste":
                                                                                                    print(
                                                                                                        "Pegue sua recompensa.")
                                                                                                    print(
                                                                                                        "A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                                                    print(
                                                                                                        "Você está em uma floresta, há caminhos para SUL, NORTE e LESTE.")
                                                                                                    comando = input(
                                                                                                        "Comando?\n\n>").lower()

                                                                                                    if verificar(
                                                                                                            comando):
                                                                                                        comando = input(
                                                                                                            "Comando?\n\n>").lower()

                                                                                                    if comando == "norte":
                                                                                                        print(
                                                                                                            "Pegue sua recompensa.")
                                                                                                        print(
                                                                                                            "A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                                                        print(
                                                                                                            "Você está em uma floresta, há caminhos para LESTE, OESTE e SUL.")
                                                                                                        comando = input(
                                                                                                            "Comando?\n\n>").lower()

                                                                                                        if verificar(
                                                                                                                comando):
                                                                                                            comando = input(
                                                                                                                "Comando?\n\n>").lower()

                                                                                                        if comando == "sul":
                                                                                                            print(
                                                                                                                "Pegue sua recompensa.")
                                                                                                            print(
                                                                                                                "A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                                                            print(
                                                                                                                "Você está em uma floresta, há caminhos para NORTE, OESTE e LESTE.")
                                                                                                            comando = input(
                                                                                                                "Comando?\n\n>").lower()

                                                                                                            if verificar(
                                                                                                                    comando):
                                                                                                                comando = input(
                                                                                                                    "Comando?\n\n>").lower()

                                                                                                            if comando == "leste":
                                                                                                                print(
                                                                                                                    "Pegue sua recompensa.")
                                                                                                                print(
                                                                                                                    "A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                                                                print(
                                                                                                                    "Você está em uma floresta, há caminhos para OESTE, SUL e NORTE.")
                                                                                                                comando = input(
                                                                                                                    "Comando?\n\n>").lower()

                                                                                                                if verificar(
                                                                                                                        comando):
                                                                                                                    comando = input(
                                                                                                                        "Comando?\n\n>").lower()

                                                                                                                if comando == "norte":
                                                                                                                    print(
                                                                                                                        "Pegue sua recompensa.")
                                                                                                                    print(
                                                                                                                        "A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                                                                    print(
                                                                                                                        "Você está em uma floresta, há caminhos para SUL, LESTE e OESTE.")
                                                                                                                    comando = input(
                                                                                                                        "Comando?\n\n>").lower()

                                                                                                                    if verificar(
                                                                                                                            comando):
                                                                                                                        comando = input(
                                                                                                                            "Comando?\n\n>").lower()

                                                                                                                    if comando == "oeste":
                                                                                                                        print(
                                                                                                                            "Pegue sua recompensa.")
                                                                                                                        print(
                                                                                                                            "A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                                                                        print(
                                                                                                                            "Você está em uma floresta, há caminhos para NORTE, LESTE e SUL.")
                                                                                                                        comando = input(
                                                                                                                            "Comando?\n\n>").lower()

                                                                                                                        if verificar(
                                                                                                                                comando):
                                                                                                                            comando = input(
                                                                                                                                "Comando?\n\n>").lower()

                                                                                                                        if comando == "leste":
                                                                                                                            print(
                                                                                                                                "Pegue sua recompensa.")
                                                                                                                            print(
                                                                                                                                "A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                                                                            print(
                                                                                                                                "Você está em uma floresta, há caminhos para OESTE, SUL e NORTE.")
                                                                                                                            comando = input(
                                                                                                                                "Comando?\n\n>").lower()

                                                                                                                            if verificar(
                                                                                                                                    comando):
                                                                                                                                comando = input(
                                                                                                                                    "Comando?\n\n>").lower()

                                                                                                                            if comando == "sul":
                                                                                                                                print(
                                                                                                                                    "Pegue sua recompensa.")
                                                                                                                                print(
                                                                                                                                    "A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                                                                                print(
                                                                                                                                    "Você está em uma floresta, há caminhos para NORTE, OESTE e LESTE.")
                                                                                                                                comando = input(
                                                                                                                                    "Comando?\n\n>").lower()

                                                                                                                                if verificar(
                                                                                                                                        comando):
                                                                                                                                    comando = input(
                                                                                                                                        "Comando?\n\n>").lower()

                                                                                                                                if comando == "oeste":
                                                                                                                                    print(
                                                                                                                                        "Pegue sua recompensa.")
                                                                                                                                    print(
                                                                                                                                        "A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                                                                                    print(
                                                                                                                                        "Você está em uma floresta, há caminhos para NORTE, LESTE e SUL.")
                                                                                                                                    comando = input(
                                                                                                                                        "Comando?\n\n>").lower()

                                                                                                                                    if verificar(
                                                                                                                                            comando):
                                                                                                                                        comando = input(
                                                                                                                                            "Comando?\n\n>").lower()

                                                                                                                                    if comando == "norte":
                                                                                                                                        print(
                                                                                                                                            "Pegue sua recompensa.")
                                                                                                                                        print(
                                                                                                                                            "A LUA PÁLIDA SORRI PARA VOCÊ.\n\n")

                                                                                                                                        print(
                                                                                                                                            "Você está em uma floresta, há caminhos para LESTE, OESTE e SUL.")
                                                                                                                                        comando = input(
                                                                                                                                            "Comando?\n\n>").lower()

                                                                                                                                        if comando == "sul":
                                                                                                                                            caminho_final()
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
                else:
                    sys.exit()
            else:
                sys.exit()
        else:
            sys.exit()
