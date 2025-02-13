import matplotlib.pyplot as plt


imagem_original = r'./data_set/Cat/7.ppm'

def read_ppm(filename):
    # Abre um arquivo PPM (formato P6)
    with open(filename, 'rb') as f:
        header = f.readline().decode().strip() # Lê o cabeçalho (primeira linha deve ser 'P6')
        if header != "P6":
            raise ValueError("Arquivo não está no formato P6 PPM")
        
        line = f.readline().decode().strip()
        while line.startswith('#'):
            line = f.readline().decode().strip()
        parts = line.split()
        width, height = int(parts[0]), int(parts[1])
        
        max_val = int(f.readline().decode().strip())
        if max_val > 255:
            raise ValueError("Este exemplo suporta apenas max_val <= 255")
        
        # Lê os dados dos pixels
        pixel_data = f.read()
        image = []
        index = 0
        
        for y in range(height):
            row = []
            for x in range(width):
        
                # Cada pixel é representado por 3 bytes: R, G, B
                r = pixel_data[index]
                g = pixel_data[index+1]
                b = pixel_data[index+2]
                row.append((r, g, b))
                index += 3
        
            image.append(row)
        
        return image, width, height

def image_to_gray(image, width, height):
    gray = []
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = image[y][x]
            # Fórmula ponderada:
            valor = int(0.299 * r + 0.587 * g + 0.114 * b)
            row.append(valor)
        gray.append(row)
    return gray


def binarize_image(gray, width, height, threshold=127): # Ponto médio da escala de cinza
    binary = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(255 if gray[y][x] > threshold else 0)
        binary.append(row)
    return binary



# Leitura da imagem PPM
image, width, height = read_ppm(imagem_original)

# Conversão para tons de cinza
gray = image_to_gray(image, width, height)

# Binarização (preto e branco)
binary = binarize_image(gray, width, height, threshold=127)


# --- Exibição usando matplotlib ---
plt.figure(figsize=(10,5))

plt.subplot(1, 3, 1)# 1 linha e 3 colunas
plt.imshow(image)
plt.title("Imagem Original")

plt.subplot(1, 3, 2)
plt.imshow(gray, cmap='gray')
plt.title("Tons de Cinza")

plt.subplot(1, 3, 3)
plt.imshow(binary, cmap='gray')
plt.title("Preto e Branco")

plt.tight_layout()
plt.show()