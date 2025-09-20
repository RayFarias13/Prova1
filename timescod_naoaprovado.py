def main():

    lista=[]

    opcao = input("Digite o numero de jogadores e o numero de times separados por espaço ").split()
    N = int(opcao[0])      
    T = int(opcao[1])

    if 2 <= N <= 10000 and 2 <= T <= 1000 and T <= N :
        x = 0
        while x < N:
            opc=input("Digite o nome do jogador e o nivel de habilidade separado por espaço ").split()
            H =int(opc[1])     
            nome = str(opc[0]).lower()

            if nome in [L[1] for L in lista] or H in [L[0] for L in lista] or not 0 <= H <= 1000000:
                print("Nome ou habilidade já existente, digite outro nome ou habilidade")
                continue            
            else:
                print(f"Jogador {nome} - {H}. Registrado")
                lista.append((H,nome))
                x+=1    
        lista.sort(reverse=True)
        times = [[] for i in range(T)]
        for i in range(N):
            H, nome = lista[i]
            separadortimes = i % T
            times[separadortimes].append(nome)        
        for i in range(T):
            print(f"Time {i+1}")
            for nome in sorted(times[i]):
                print(nome)
            print()

    else:
        print ("valores foram de contexto")
if __name__ == "__main__":
    main()