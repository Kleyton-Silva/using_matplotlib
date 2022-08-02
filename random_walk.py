from random import choice

class RandomWlk():
    """Uma classe para gerar caminhos aleatórios"""

    def__init__(self, num_points=5000):
    """Inicializa os atributos de caminho"""
    self.num_points = num_points

    # Todos os caminhos começam em (0, 0)
    self.x_values = [0]
    self.y_values = [0]