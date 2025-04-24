import time
from tqdm import tqdm
import random
from colorama import Fore, Style, init

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



# Execução de teste
if __name__ == "__main__":
    tripulantes = ["Alice", "Bruno", "Carla", "Diego"]
    modulo = SuporteDeVida(tripulantes)
    modulo.monitorar(ciclos=10, intervalo=2)  # 3 ciclos, 3 segundos entre cada
