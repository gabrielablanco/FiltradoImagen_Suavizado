from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

def añadir_filtro(mascara):
    fila = matriz.shape[0]-mascara.shape[0]+1
    columnas = matriz.shape[1]-mascara.shape[1]+1
    m_aux = np.zeros((fila, columnas))
    #mascara_f = np.rot90(np.rot90(mascara))

    for i in range (0, m_aux.shape[0]):
        for j in range (0, m_aux.shape[1]):
            imagen2 = matriz[i:i+len(mascara), j:j+len(mascara)]
            m_aux[i][j] = ((mascara*imagen2).sum())//9
    print('\n\nMatriz suavizada\n')
    imprimir_imagenes(m_aux)
    print(m_aux)
    desenfocar_funcion = ndimage.gaussian_filter(matriz, sigma=5) #Funcion desenfocar
    imprimir_imagenes(desenfocar_funcion)
    #aux = 0
    #for a in range(0,3):
     #   for b in range (0,3):
     #       aux += (m_aux[a][b]*mascara[a][b])
            #print(aux)
    #aux = aux//9
    #print(aux)
    #imagen2[i+1][j+1] = aux
    #print(imagen2)

def imprimir_imagenes(m_aux):
    plt.subplot(121), plt.imshow(imagen_o), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(m_aux, cmap='gray'), plt.title('Difuminada')
    plt.xticks([]), plt.yticks([])
    plt.show()


imagen_o = Image.open('img_prueba.jpg')
imagen = imagen_o.convert("L")
matriz = np.asarray(imagen) #Guarda la imagen en un arreglo de numpy
mascara = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
#imagen2 = np.zeros((915,915))
añadir_filtro(mascara)

#print(matriz.shape)
#for i in range(0,915):
 #   for j in range(0, 915):
  #      m_aux = matriz[i:i + 3][j:j + 3]
   #     añadir_filtro(m_aux, mascara, i, j)
    #    m_aux = np.zeros((3,3))

#imprimir_imagenes()
print('\n\nMatriz original\n')
print(matriz)
