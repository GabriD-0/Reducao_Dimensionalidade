import matplotlib
import matplotlib.image as img
import matplotlib.pyplot as plt

# Esolhendo a imagem
imagem = r'.\data_set\Cat\7.jpg'

imagem_original = img.imread(imagem)

def coverte_img_cinza(imagem):
    
    # Extraindo canais RGB    
    r = imagem[:, :, 0]
    g = imagem[:, :, 1]
    b = imagem[:, :, 2]

    # imagem_cinza = (r + g + b) / 3 Média Aritmética (igualdade de pesos)
    # formula para imagem cinza
    imagem_cinza = (r * 0.299 + g * 0.587 + b * 0.114) / 3 # Média Ponderada (mais adequada à percepção humana)
    
    return imagem_cinza


imagem_cinza = coverte_img_cinza(imagem_original)



def coverte_img_binarizada(imagem):
  
    return imagem_binarizada


imagem_binarizada = coverte_img_binarizada(imagem_original)



# Exibindo imagens
plt.figure(figsize=(10, 6)) # Criando nova figura 
plt.subplot(1, 3, 1) # 1 linha e 2 colunas
plt.imshow(imagem_original)
plt.title("Imagem Original")

plt.subplot(1, 3, 2)
plt.imshow(imagem_cinza, cmap='gray')
plt.title("Tons de Cinza")

plt.subplot(1, 3, 3)
plt.imshow(imagem_binarizada)
plt.title("Preto e Branco")



plt.show()