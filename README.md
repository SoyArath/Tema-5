
# 🎯 Método de Ordenamiento: Selection Sort - Visualización en Python

Este proyecto muestra de forma visual y paso a paso cómo funciona el algoritmo **Selection Sort**, utilizando gráficos de barras con la librería `matplotlib`. Es ideal para aprender o enseñar el proceso de ordenamiento de una manera clara, animada e interactiva.

---

## 👨‍🏫 Información general

- **Materia:** Estructura de Datos  
- **Profesor:** Kevin David Molina Gómez  
- **Fecha de entrega:** 02/08/2025

### 👨‍🎓 Integrantes del equipo:
- Sergio Alexander Antonio Gracida  
- Luis Alberto Figueroa González  
- Carlos Antonio Cortés Torres  
- Arath Yahir López Guzmán  
- Oswaldo Martínez Vidaña  
- Ángel David García Blas

---

## 🧠 ¿Qué hace este proyecto?

Implementa el algoritmo de ordenamiento **por selección (Selection Sort)** con una visualización interactiva de cada paso.  
La interfaz gráfica permite observar cómo el algoritmo va eligiendo el valor mínimo y realizando intercambios hasta que el arreglo queda ordenado.

---

## 🔍 ¿Cómo funciona?

1. Se toma un arreglo de números desordenados.
2. El algoritmo recorre el arreglo y busca el valor más pequeño.
3. Lo intercambia con el primer valor.
4. Repite el proceso desde la siguiente posición.
5. Cada paso se almacena para mostrarse visualmente con colores y mensajes.

El usuario puede navegar paso a paso por el proceso utilizando el teclado:
- **→** o **Espacio**: siguiente paso  
- **←**: paso anterior  
- **R**: reiniciar desde el inicio  
- **Q**: salir del gráfico  

---

## 🧪 ¿Cómo ejecutar el código?

1. Asegúrate de tener Python instalado.
2. Instala `matplotlib` si aún no lo tienes:
   ```bash
   pip install matplotlib
   ```
3. Ejecuta el archivo `.py` que contiene el código:
   ```bash
   python nombre_del_archivo.py
   ```
4. Se abrirá una ventana con la animación del ordenamiento.

---

## 📁 Estructura del código

El código se compone de tres partes:

- **`metodo_seleccion()`**: Implementa el algoritmo y guarda cada paso importante del proceso.
- **`VisualizadorSeleccion`**: Clase que se encarga de mostrar gráficamente cada paso con colores, mensajes y controles de navegación.
- **`probar_metodo_seleccion()`**: Ejecuta todo el proceso con un arreglo de ejemplo.

---

![Visualización del algoritmo](Captura de pantalla 2025-08-02 205416)


