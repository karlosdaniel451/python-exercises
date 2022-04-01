def somar_imposto(taxa_imposto_em_porcentagem: int, custo_em_centavos: int):
    return custo_em_centavos * (1 - taxa_imposto_em_porcentagem / 100) 


print(somar_imposto(taxa_imposto_em_porcentagem=1, custo_em_centavos=10000) / 100)
