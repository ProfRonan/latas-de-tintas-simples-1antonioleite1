print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)

Litro = metros_quadrados/3

if metros_quadrados == 0:
    print("Serão necessários 0 latas totalizando R$ 0")
elif 0 < metros_quadrados <= 54:
    print("Serão necessários 1 lata totalizando R$ 80,00")

elif metros_quadrados > 54:
    qtd_de_latas = Litro/18
    if Litro % 18 > 0:
        qtd_de_latas = int(qtd_de_latas) + 1
    valor_total = qtd_de_latas * 80.00
    print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")



