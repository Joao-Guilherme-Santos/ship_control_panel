import time
from tqdm import tqdm
import random
from colorama import Fore, Style, init

def limpar_linha():
        print("\r\033[K", end='')  # Apaga a linha atual inteira


#Função para simular a despressurização de uma porta 
def despressurizar(porta):

    #indica a porta a ser despressurizada
    print(Fore.GREEN + f"Iniciando despressurização da porta {porta}..." + Style.RESET_ALL)

    #simula o tempo de despressurização 
    for psi in tqdm(
        range(14, -1, -1),
        desc=Fore.GREEN + "Despressurizando" + Style.RESET_ALL,
        bar_format="{l_bar}{bar} {n_fmt}/{total_fmt} psi"
    ):
        time.sleep(0.5)

    #simula o tempo de aguardo
    print(Fore.GREEN + "Aguardando estabilização..." + Style.RESET_ALL)
    time.sleep(5)

    #simula o tempo de pressurização 
    print(Fore.GREEN + "Iniciando pressurização..." + Style.RESET_ALL)
    for psi in tqdm(
        range(0, 15),
        desc=Fore.GREEN + "Pressurizando" + Style.RESET_ALL,
        bar_format="{l_bar}{bar} {n_fmt}/{total_fmt} psi"
    ):
        time.sleep(0.8)

    #indica o fim do processo
    print(Fore.GREEN + "Processo concluído!" + Style.RESET_ALL)


class Sistema:
    estados_possiveis = ["OK", "MANUTENÇÃO", "NÃO OK"]

    def __init__(self):
        self.sistemas = []
        self.inicializar_sistemas()

    def verificar_estado(self):
        return random.choices(
            Sistema.estados_possiveis,
            weights=[0.6, 0.25, 0.15]
        )[0]

    def estado_colorido(self, estado):
        if estado == "OK":
            return Fore.GREEN + estado + Style.RESET_ALL
        elif estado == "MANUTENÇÃO":
            return Fore.YELLOW + estado + Style.RESET_ALL
        elif estado == "NÃO OK":
            return Fore.RED + estado + Style.RESET_ALL
        else:
            return estado

    def inicializar_sistemas(self):
        nomes_sistemas = [
            "Turbinas",
            "Corpo Estrutural",
            "Sistema Elétrico",
            "Comunicações",
            "Controle de Navegação",
            "Sensores Externos",
            "Propulsão Auxiliar",
            "Sistemas de Vida",
            "Blindagem Térmica"
        ]

        for nome in nomes_sistemas:
            estado = self.verificar_estado()
            self.sistemas.append((nome, estado))

    def exibir(self):
        print("\n=== PAINEL DE CONTROLE DA ESPAÇONAVE ===")
        for nome, estado in self.sistemas:
            print(f"{nome:<25} --> {self.estado_colorido(estado)}")
        print("========================================\n")

class SuporteDeVida:
    condicoes_possiveis = ["OK", "NÃO OK"]

    def __init__(self, tripulantes):
        self.tripulantes = tripulantes
        self.condicoes = {nome: "OK" for nome in tripulantes}

    def verificar_condicoes(self):
        for nome in self.tripulantes:
            novo_estado = random.choices(
                SuporteDeVida.condicoes_possiveis,
                weights=[0.8, 0.1]
            )[0]
            self.condicoes[nome] = novo_estado

    def estado_colorido(self, estado):
        if estado == "OK":
            return Fore.GREEN + estado + Style.RESET_ALL
        else:
            return Fore.RED + estado + Style.RESET_ALL

    def imprimir_tabela(self):
        print("\033[2K\n=== MONITORAMENTO DAS CONDIÇÕES VITAIS ===")
        for nome in self.tripulantes:
            estado = self.estado_colorido(self.condicoes[nome])
            print(f"\033[2K{nome:<20} --> {estado}")
        print("\033[2K==========================================\n")

    def atualizar_status(self):
        linhas_para_subir = len(self.tripulantes) + 4
        print(f"\033[{linhas_para_subir}F", end='')  # Volta ao topo da tabela
        self.imprimir_tabela()

    def monitorar(self, ciclos=10, intervalo=2):
        self.verificar_condicoes()
        self.imprimir_tabela()
        for _ in range(ciclos):
            time.sleep(intervalo)
            self.verificar_condicoes()
            self.atualizar_status()



class PainelSimulacao:
    def __init__(self):
        self.combustivel = 1000     # litros
        self.distancia = 500        # km até Marte
        self.velocidade = 0         # km/h
        self.linhas_fixas = 6       # Linhas do painel
        self.tempo_intervalo = 5    # segundos (simulando 5 minutos)

    
    def imprimir_tabela(self):
        limpar_linha()
        print("=== PAINEL DE COMANDO - VIAGEM AUTOMÁTICA ===")
        limpar_linha()
        print(f"Velocidade Atual        --> {Fore.CYAN}{self.velocidade} km/h{Style.RESET_ALL}")
        limpar_linha()
        print(f"Combustível Restante    --> {Fore.YELLOW}{self.combustivel} L{Style.RESET_ALL}")
        limpar_linha()
        print(f"Distância até Marte     --> {Fore.GREEN}{self.distancia} km{Style.RESET_ALL}")
        limpar_linha()
        print("===============================================")

    def atualizar_tabela(self):
        print(f"\033[{self.linhas_fixas}F", end='')  # Sobe até o topo da tabela
        self.imprimir_tabela()

    def atualizar_variaveis(self):
        # velocidade aleatória entre 10 e 50 km/h
        self.velocidade = random.randint(10, 50)
        gasto = self.velocidade * 2

        self.combustivel = max(0, self.combustivel - gasto)
        self.distancia = max(0, self.distancia - self.velocidade)

    def iniciar(self):
        self.atualizar_variaveis()
        self.imprimir_tabela()

        while self.combustivel > 0 and self.distancia > 0:
            time.sleep(self.tempo_intervalo)
            self.atualizar_variaveis()
            self.atualizar_tabela()

        print("\n\033[2K" + Fore.MAGENTA + "Missão finalizada! Destino alcançado ou combustível esgotado." + Style.RESET_ALL)


# Execução da simulação
if __name__ == "__main__":
    painel = PainelSimulacao()
    painel.iniciar()