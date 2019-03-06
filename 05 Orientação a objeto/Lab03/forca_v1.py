# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random #importaa pacote radom para geral uma palavra aleatoria

# Board (tabuleiro) #uma lista para cada erro do jogo ele ira imprimir uma fase
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman: #criando a super classse

	# Método Construtor
	def __init__(self, word): #metodo contrutor com o parametro word que sera o inicio do jogo quando for instaciada
		self.word = word #função para obter a palavra
		self.missed_letters = [] # lista para letras erradas
		self.guessed_letters = [] #lista para letras certas
		
	# Método para adivinhar a letra
	def guess(self, letter):# metodo que tem como parametro letra
		if letter in self.word and letter not in self.guessed_letters:#condição para se a letra estiver dentro da palavra  e nao estiver dentro da lista de para certa faça
			self.guessed_letters.append(letter) #função para adcionar a letra na lista de palavras certas
		elif letter not in self.word and letter not in self.missed_letters:
			self.missed_letters.append(letter)
		else:
			return False
		return True
		
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		return  self.hangman_won() or (len(self.missed_letters)==6)#retorna se o usuario venceu chamando o metodo de vencedor ou verifica se já foram feito 6 tentativvas.
		
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if '_' not in self.hide_word():#se dentro do objeto hide_word(para esconder as letras) não tiver o caracter underline faça
			return True # se nao tiver undeline ele retornara verdadeiro e assim indicando que o usuario venceu
		return False# caso ainda tenha undeline no objeto ele retornara falso e continuara o jogo caso nao exceda as 6 tentativas
		

	# Método para não mostrar a letra no board
	def hide_word(self):
		rtn = '' # objeto com espaço vazio para receber algum valor
		for letter in self.word: # para cada letra dentro da palavra faça
			if letter not in self.guessed_letters:#se a letra não estiver dentro da lista da letras certas faça
				rtn += '_' #se a letra nao estiver na lista de letras certas vai atribuir um undelainer no objeto etn
			else:
				rtn += letter #caso tenho a letra na lista de palavras certas ele atribui a letra no objeto
		return rtn # metodo vai retorna o objeto com a letra ou com o underlaine
		
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[len(self.missed_letters)])#usamos a função len para ver o tamanho da lista de palavras errada para imprimir o board
		print('\nPalavra: ' + self.hide_word())
		print ('\nLetras erradas: ',)
		for letter in self.missed_letters:#para cada letra dentro da listas letras erradas faça
			print(letter,)
		print ()
		print('Letras corretas: ',)
		for letter in self.guessed_letters:#para cada letra dentro da lista de letras corretas  faça
			print(letter,)# imprimir letra correta
		print()#imprimir um linha em branco
		

# metodo para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f: # abrir o arquivo com as palavras
                bank = f.readlines() # ler uma unica linha cada linha é uma palavra dentro desse arquivo e atribuir no objeto bank
        return bank[random.randint(0,len(bank))].strip()#ussando o random para buscar uma linha aleatoria com o randint dentro do objeto bank


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word()) # instancia um objeto com uma palavra aleatoria

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.hangman_over(): #Enquanto nao for  final do jogo
		game.print_game_status()# vai usar o metodo print para printar o estado do jogo
		user_input = input('\nDigite uma letra')# pedir para usuario digitar uma letra
		game.guess(user_input) #faz a leitura da letra que o usuario digitou e chama o metodo guess

	# Verifica o status do jogo
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
