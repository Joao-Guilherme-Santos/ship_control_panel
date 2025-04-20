import time
from tqdm import tqdm
from colorama import Fore, Style

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

despressurizar(4)