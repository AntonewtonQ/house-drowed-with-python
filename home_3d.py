from PIL import Image, ImageDraw
import os

largura = 1000
altura = 500

img = Image.new("RGB", (largura, altura), "white")

draw = ImageDraw.Draw(img)

# Desenhar a parte inferior da casa
draw.rectangle([450, 225, 550, 285], fill="blue")  # Parede principal

# Desenhar a parte lateral direita da casa
draw.rectangle([550, 225, 585, 285], fill="yellow")  # Parede lateral direita

# Desenhar o telhado (triângulo acima da parede principal)
draw.polygon([(450, 225), (500, 150), (550, 225)], fill="red")  # Telhado frontal

# Pequeno triângulo superior (lado direito)
draw.polygon([(550, 225), (585, 185), (585, 225)], fill="white")

# Pequeno triângulo inferior (lado direito)
draw.polygon([(550, 285), (585, 255), (585, 285)], fill="white")

# Parte direita do telhado
# draw.polygon([(550, 225), (500, 150), (585, 185)], fill="black")  # Telhado lateral direito


draw.polygon([(550, 225), (500, 150),(550, 150), (585, 205)], fill="gray")  # Quadrilátero de 4 faces



# Ajustar contornos para maior clareza (opcional)
draw.line([(450, 225), (500, 150), (550, 225)], fill="black", width=1)  # Contorno do telhado frontal
# draw.line([(550, 225), (585, 185)], fill="black", width=1)  # Contorno do telhado lateral
draw.line([(585, 205), (585, 225)], fill="black", width=1)  # Contorno lateral superior
draw.line([(550, 285), (585, 255)], fill="black", width=1)  # Contorno lateral inferior

pasta = os.path.expanduser("/home/antonewton/Documents/ann.tech")

# Desenhar régua no lado esquerdo (vertical)
for y in range(0, altura, 10):
    draw.line((0, y, 5, y), fill="black")  # Pequenas marcas de 5px
    draw.text((10, y - 5), str(y), fill="black")  # Adiciona os números

# Desenhar régua na parte inferior (horizontal)
for x in range(0, largura, 25):
    draw.line((x, altura - 5, x, altura), fill="black")  # Pequenas marcas de 5px
    draw.text((x, altura - 20), str(x), fill="black")  # Adiciona os números

# Salvar imagem
img.save(os.path.join(pasta, "home_3d.bmp"))

print("Imagem BMP gerada com sucesso!")

# Mostrar a imagem
img.show()
