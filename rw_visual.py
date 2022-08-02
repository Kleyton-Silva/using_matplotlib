import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Cria passeios aleatórios e plota os pontos
    rw = RandomWalk(50000)
    rw.fill_walk()
    # Define o tamanho da janela de plotagem
    plt.figure(dpi=128, figsize=(15, 7))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Blues, edgecolor='none', s=3)

    # Entafizando o primeiro e o último ponto
    plt.scatter(0, 0, c='green', edgecolors='none', s=35)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
                edgecolors='none', s=35)

    # Remove os eixos para uma melhora visualização
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    plt.axis('off')

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
