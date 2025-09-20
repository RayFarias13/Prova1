def main():
    opcao = input().split()
    N = int(opcao[0])
    T = int(opcao[1])
    lista = []
    for i in range (N):
        opc = input().split()
        nome = str(opc[0])
        habilidade = int(opc[1])
        lista.append((habilidade,nome))
    lista.sort(reverse=True)
    times = [[] for i in range (T)]
    for i in range(N):
        habilidade, nome = lista[i]
        separadortimes = i % T
        times[separadortimes].append(nome)        
    for i in range(T):
        print(f"Time {i+1}")
        for nome in sorted(times[i]):
            print(nome)
        print()
if __name__ == "__main__":
    main()
    