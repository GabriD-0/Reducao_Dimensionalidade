# Conversão de Imagem para PPM e Processamento em Python

## Visão Geral
Este projeto tem como objetivo principal a leitura e conversão de imagens para tons de cinza e posteriormente para uma versão binarizada (preto e branco) sem o uso de libs especializada. O código faz uso da biblioteca **Matplotlib** para a exibição das imagens em diferentes estágios do processamento e do formato **PPM (Portable Pixmap Format)** para as imagens.

## Tecnologias Utilizadas
- **Python 3**
- **Matplotlib** (para visualização das imagens)

## Estrutura do Código
O código é dividido nas seguintes etapas:

1. **Leitura do arquivo PPM**:
   - O formato PPM utilizado é do tipo **P6**, que armazena pixels no formato binário (RGB).
   - O arquivo é lido byte a byte, extraindo os valores de **R (vermelho), G (verde) e B (azul)** para compor a imagem original.

2. **Conversão para tons de cinza**:
   - A conversão é realizada utilizando uma média ponderada dos valores RGB, seguindo a fórmula:
     
     \[ Valor = 0.299R + 0.587G + 0.114B \]
   
   - Essa abordagem reflete a percepção humana de brilho em diferentes cores.

3. **Binarização da imagem**:
   - A imagem em tons de cinza é convertida para uma imagem binária (preto e branco) utilizando um limiar (threshold) de **127**.
   - Se o valor do pixel for maior que 127, ele se torna **branco (255)**, caso contrário, se torna **preto (0)**.

## Exibição dos Resultados
A biblioteca **Matplotlib** é utilizada para exibir as imagens nas três etapas:

1. **Imagem Original (PPM)**
2. **Imagem em Tons de Cinza**
3. **Imagem Binarizada (Preto e Branco)**

As imagens são organizadas em uma figura com três colunas para facilitar a comparação.

## Como Executar
### 1. Instale as dependências (caso necessário):
```sh
pip install matplotlib
```

### 2. Execute o script Python:
```sh
python nome_do_arquivo.py
```

Certifique-se de substituir `imagem_original` pelo caminho correto da imagem **PPM** que deseja processar.

## Conclusão
Este projeto ilustra como manipular imagens no formato PPM, realizando conversões essenciais para processamento de imagens: de colorido para tons de cinza e, posteriormente, para uma versão binarizada. 

