# -*- coding: UTF-8 -*-
# Cada bloco de código, tem 3 linhas de salto, para uma melhor organização!

#ideias : Fazer um comparativo com o resultado atual em relação ao tamanho do dado e retornar uma mensagem de parabens ou tristeza dependendo do valor.
#ideias : Fazer uma função para pular linhas automático com o \n, onde caso não passe nenhum parametro pule apenas uma linha ou pule a quantidade de linhas passadas.
#ideias : Utilizar a biblioteca de tempo para salvar o momento dos sorteios de valores, para depois apresentar os valores e a hora do seu sorteio, dando uma opção para o usuário no starting();

import random;
import sys;
import os;
import time;

Choice = 0;
Sorted = 0;
LastResults = [5,5];




def Starting():
    global Choice;
    global LastResults;

    Apresentation();
    
    print('2 lados      -    (1)');
    print('4 lados      -    (2)');
    print('6 lados      -    (3)');
    print('20 lados     -    (4)');

# Caso o usuário passe uma string, gerará um erro, usei tryexcept para conter isto.

    try:
        Choice = int(input()); 

        if(Choice == 1):
            Dice2();

        elif(Choice == 2):
            Dice4();

        elif(Choice == 3):
            Dice6();

        elif(Choice == 4):
            Dice20();
        
        else:
            Naoentendi()

    except ValueError:
        Naoentendi()



# Sorteia um número, o atribui na váriavel e na lista, limpa a tela.
def Dice2():
    Sorted = random.randint(1,2);
    LastResults.append(Sorted);
    print ("\n" * 100) 

    print("Dice 2");
    Saltos();
    print("Seu resultado foi: " + str(Sorted));
    
    tryagain();


def Dice4():
    Sorted = random.randint(1,4);
    LastResults.append(sorted);
    Saltos(100); 

    print("Dice 4");
    print("\n");
    print("Seu resultado foi: " + str(Sorted) + " de 4...");

    tryagain();


def Dice6():
    Sorted = random.randint(1,6);
    LastResults.append(sorted);
    Saltos(100); 

    print("Dice 6");
    Saltos();
    print("Seu resultado foi: " + str(Sorted) + " de 6...");
    
    tryagain();


def Dice20():
    Sorted = random.randint(1,20);
    LastResults.append(Sorted);
    Saltos(100);

    print("Dice 20");
    Saltos();
    print("Seu resultado foi: " + str(Sorted) + " de 20...");
    
    tryagain();



# Recebe um valor, que caso Y, chama a função Starting() novamente. Caso "n", finaliza. 
def tryagain():
    print('Deseja continuar novamente? Y/n ');
    Choice = input();
    print(Choice);

    if(Choice == '' or Choice == 'y' or Choice == 'Y'):
        Saltos(100);
        Starting();
        
    elif(Choice == 'n' or Choice == 'N'):
        Saltos(100);
        print("Obrigado por me utilizar. Até a proxima! :D")
        sys.exit();

    else: 
        print("Selecione novamente, por favor");
        tryagain();



# É chamada toda vez que o programar for chamado novamente.
def Apresentation():
    Saltos(100);
    print('Olá, eu sou seu dado portatil, escolha uma opção: (1) - Start | (2) - Finish');
    print('Aqui está os tipos de dado: ');



# Função para pular linhas comparando typeof entre um dado int e float com o parâmetro passado, caso sim, pula a quantidade de linhas usando o valor da variavel parâmetro.
#  caso nenhum argumento, pula apenas uma.
def Saltos(saltos = ''):
    Paramint = 1;
    Paramfloat = 1.1;

    if(type(saltos) == type(Paramint) or type(saltos) == type(Paramfloat)):
        print("entrou");
        print("\n" * saltos);

    else:
        print("\n");



def Naoentendi():
    Saltos(100);
    print("Não pude entender, digite novamente em 3 segundos...");
    time.sleep(1);
    print("Não pude entender, digite novamente em 2 segundos...");
    time.sleep(1);
    print("Não pude entender, digite novamente em 1 segundo...");
    time.sleep(1);

    Starting();
        


Starting();