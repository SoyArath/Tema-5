import matplotlib.pyplot as plt
import numpy as np

def metodo_seleccion(arreglo):

    numeros = arreglo.copy()
    pasos = []
    pasos.append((numeros.copy(), -1, -1, None, "Estado inicial"))

    n = len(numeros)
    for i in range(n):
        min_idx = i
        pasos.append((numeros.copy(), i, -1, numeros[min_idx], f"Seleccionando desde posición {i}"))

        for j in range(i + 1, n):
            pasos.append((numeros.copy(), i, j, numeros[min_idx], f"Comparando índice {j} con mínimo actual en índice {min_idx}"))
            if numeros[j] < numeros[min_idx]:
                min_idx = j
                pasos.append((numeros.copy(), i, j, numeros[min_idx], f"Nuevo mínimo encontrado: {numeros[min_idx]} en índice {j}"))

        if i != min_idx:
            numeros[i], numeros[min_idx] = numeros[min_idx], numeros[i]
            pasos.append((numeros.copy(), i, min_idx, numeros[i], f"Intercambiando {numeros[min_idx]} con {numeros[i]}"))

    pasos.append((numeros.copy(), -1, -1, None, "¡Ordenamiento completado!"))
    return pasos


class VisualizadorSeleccion:
    def __init__(self, arreglo_original):
        self.pasos = metodo_seleccion(arreglo_original)
        self.paso_actual = 0
        self.total_pasos = len(self.pasos)

        self.fig, self.axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [4, 1]})
        self.fig.suptitle('Selection Sort', fontsize=14, fontweight='bold')
        self.fig.canvas.mpl_connect('key_press_event', self.navegar)

        self.color_normal = 'lightblue'
        self.color_minimo = 'orange'
        self.color_comparado = 'red'
        self.color_intercambio = 'green'

        self.mostrar_paso()

        print("Controles:")
        print("← Flecha izquierda: Paso anterior")
        print("→ Flecha derecha: Paso siguiente")
        print("Espacio: Siguiente paso")
        print("R: Reiniciar")
        print("Q: Salir\n")

    def mostrar_paso(self):
        for ax in self.axs:
            ax.clear()

        arreglo_actual, i, j, temp, descripcion = self.pasos[self.paso_actual]
        posiciones = range(len(arreglo_actual))
        colores = []

        for idx in range(len(arreglo_actual)):
            if idx == i:
                colores.append(self.color_minimo)
            elif idx == j:
                colores.append(self.color_comparado if "Comparando" in descripcion else self.color_intercambio)
            else:
                colores.append(self.color_normal)

        bars = self.axs[0].bar(posiciones, arreglo_actual, color=colores, alpha=0.8, edgecolor='black')

        for idx, valor in enumerate(arreglo_actual):
            self.axs[0].text(idx, valor + 0.5, str(valor), ha='center', va='bottom', fontweight='bold', fontsize=12)

        extra_info = ""
        if "Seleccionando" in descripcion:
            extra_info = "\nSe comienza una nueva iteración para encontrar el mínimo desde esta posición."
        elif "Comparando" in descripcion:
            extra_info = "\nSe compara el valor actual con el mínimo encontrado hasta ahora."
        elif "Nuevo mínimo" in descripcion:
            extra_info = "\nSe encontró un nuevo valor mínimo más pequeño."
        elif "Intercambiando" in descripcion:
            extra_info = "\nSe intercambian los valores: el menor va a la posición actual."

        self.axs[0].set_title(f'Paso {self.paso_actual + 1}/{self.total_pasos}: {descripcion}{extra_info}', fontsize=12, pad=10)
        self.axs[0].set_ylim(0, max(max(paso[0]) for paso in self.pasos) + 4)
        self.axs[0].set_xticks(posiciones)
        self.axs[0].set_ylabel('Valor', fontsize=11)
        self.axs[0].grid(True, alpha=0.3)

        self.axs[1].axis('off')
        self.axs[1].text(0.5, 0.5, f'mínimo = {temp if temp is not None else ""}',
                         fontsize=18, fontweight='bold', ha='center', va='center',
                         bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='black'))

        plt.tight_layout()
        self.fig.canvas.draw()

    def navegar(self, event):
        if event.key == 'right' or event.key == ' ':
            if self.paso_actual < self.total_pasos - 1:
                self.paso_actual += 1
                self.mostrar_paso()
                print(f"Paso {self.paso_actual + 1}: {self.pasos[self.paso_actual][4]}")

        elif event.key == 'left':
            if self.paso_actual > 0:
                self.paso_actual -= 1
                self.mostrar_paso()
                print(f"Paso {self.paso_actual + 1}: {self.pasos[self.paso_actual][4]}")

        elif event.key == 'r':
            self.paso_actual = 0
            self.mostrar_paso()
            print("Reiniciado al inicio")

        elif event.key == 'q':
            plt.close()
            print("¡Hasta luego!")


def probar_metodo_seleccion():
    print("Selection Sort\n")
    numeros = [1, 6, 7, 4, 2, 9, 8, 5, 3]
    print(f"Arreglo a ordenar: {numeros}\n")
    visualizador = VisualizadorSeleccion(numeros)
    plt.show()


if __name__ == "__main__":
    probar_metodo_seleccion()
