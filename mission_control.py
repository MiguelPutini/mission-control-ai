# mission_control.py

# 1. Nome da missão
NOME_MISSAO = "Orion-experiment-28-05-26"

# 2. Nome da equipe
NOME_EQUIPE = "RocketBoys"

# 5. Lista com as áreas monitoradas
areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# 3. Matriz dados_missao com pelo menos 6 ciclos e 5 informações
dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

# 6. Pelo menos 5 funções (aqui criaremos mais que 5 para organizar melhor)

def analisar_temperatura(temp):
    if temp < 18:
        return ("ATENÇÃO", 1, "Temperatura baixa")
    elif 18 <= temp <= 30:
        return ("NORMAL", 0, "Temperatura estável")
    elif 30 < temp <= 35:
        return ("ATENÇÃO", 1, "Temperatura elevada")
    else:
        return ("CRÍTICO", 2, "Risco de superaquecimento")

def analisar_comunicacao(com):
    if com < 30:
        return ("CRÍTICO", 2, "Comunicação com a base em nível crítico")
    elif 30 <= com <= 59:
        return ("ATENÇÃO", 1, "Comunicação instável")
    else:
        return ("NORMAL", 0, "Comunicação estável")

def analisar_bateria(bat):
    if bat < 20:
        return ("CRÍTICO", 2, "Bateria em nível crítico")
    elif 20 <= bat <= 49:
        return ("ATENÇÃO", 1, "Bateria abaixo do recomendado")
    else:
        return ("NORMAL", 0, "Energia estável")

def analisar_oxigenio(oxi):
    if oxi < 80:
        return ("CRÍTICO", 2, "Oxigênio em nível crítico")
    elif 80 <= oxi <= 89:
        return ("ATENÇÃO", 1, "Oxigênio abaixo do ideal")
    else:
        return ("NORMAL", 0, "Oxigênio adequado")

def analisar_estabilidade(est):
    if est < 40:
        return ("CRÍTICO", 2, "Estabilidade operacional crítica")
    elif 40 <= est <= 69:
        return ("ATENÇÃO", 1, "Estabilidade operacional reduzida")
    else:
        return ("NORMAL", 0, "Estabilidade operacional adequada")

def classificar_ciclo(pontuacao_risco):
    if 0 <= pontuacao_risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif 3 <= pontuacao_risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def gerar_recomendacao(classificacao):
    if classificacao == "MISSÃO ESTÁVEL":
        return "Manter operação normal e continuar monitoramento."
    elif classificacao == "MISSÃO EM ATENÇÃO":
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."

def analisar_tendencia(risco_inicial, risco_final):
    if risco_final > risco_inicial:
        return "A missão apresentou tendência de piora."
    elif risco_final < risco_inicial:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão perman বহুমeceu estável em relação ao início."

def gerar_relatorio_final(medias, ciclo_critico, maior_risco, media_risco, qtde_criticos, tendencia, pontuacoes_areas, area_afetada, classificacao_final):
    print("============================================================")
    print("RELATÓRIO FINAL DA MISSÃO")
    print("============================================================")
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print(f"Média de temperatura: {medias[0]:.2f} °C")
    print(f"Média de comunicação: {medias[1]:.2f}%")
    print(f"Média de bateria: {medias[2]:.2f}%")
    print(f"Média de oxigênio: {medias[3]:.2f}%")
    print(f"Média de estabilidade: {medias[4]:.2f}%")
    print(f"Ciclo mais crítico: Ciclo {ciclo_critico}")
    print(f"Maior pontuação de risco: {maior_risco}")
    print(f"Risco médio da missão: {media_risco:.2f}")
    print(f"Quantidade de ciclos críticos: {qtde_criticos}")
    print("Tendência da missão:")
    print(tendencia)
    print("Pontuação acumulada por área:")
    for i in range(5):
        print(f"{areas_monitoradas[i]}: {pontuacoes_areas[i]} pontos")
    print("Área mais afetada:")
    print(area_afetada)
    print("Classificação final da missão:")
    print(classificacao_final)
    print("Conclusão:")
    if tendencia == "A missão apresentou tendência de piora.":
        print("A missão apresentou instabilidade relevante durante a operação. Apesar da tentativa de recuperação no último ciclo, ainda existem sistemas em atenção e a equipe deve manter o plano de contingência ativo.")
    elif tendencia == "A missão apresentou tendência de melhora.":
        print("A missão iniciou com instabilidades, mas os sistemas foram recuperados com sucesso ao longo dos ciclos.")
    else:
        print("A missão ocorreu conforme as expectativas iniciais. Continue o monitoramento.")

def main():
    print("============================================================")
    print("MISSION CONTROL AI")
    print("============================================================")
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    
    pontuacoes_areas = [0, 0, 0, 0, 0]
    historico_riscos = []
    qtde_criticos = 0
    
    # Acumuladores para médias
    soma_temp = 0
    soma_com = 0
    soma_bat = 0
    soma_oxi = 0
    soma_est = 0

    # 7. Estrutura de repetição para percorrer os ciclos
    for i, ciclo in enumerate(dados_missao):
        print("============================================================")
        print(f"CICLO {i+1}")
        print("------------------------------------------------------------")
        
        temp, com, bat, oxi, est = ciclo
        soma_temp += temp
        soma_com += com
        soma_bat += bat
        soma_oxi += oxi
        soma_est += est
        
        st_temp, pts_temp, msg_temp = analisar_temperatura(temp)
        st_com, pts_com, msg_com = analisar_comunicacao(com)
        st_bat, pts_bat, msg_bat = analisar_bateria(bat)
        st_oxi, pts_oxi, msg_oxi = analisar_oxigenio(oxi)
        st_est, pts_est, msg_est = analisar_estabilidade(est)
        
        pontuacoes_areas[0] += pts_temp
        pontuacoes_areas[1] += pts_com
        pontuacoes_areas[2] += pts_bat
        pontuacoes_areas[3] += pts_oxi
        pontuacoes_areas[4] += pts_est
        
        # 9. Cálculo de risco por ciclo
        risco_ciclo = pts_temp + pts_com + pts_bat + pts_oxi + pts_est
        historico_riscos.append(risco_ciclo)
        
        # 10. Classificação de cada ciclo
        classificacao = classificar_ciclo(risco_ciclo)
        recomendacao = gerar_recomendacao(classificacao)
        
        if classificacao == "MISSÃO CRÍTICA":
            qtde_criticos += 1
            
        print(f"Temperatura: {temp} °C | {st_temp} | {msg_temp}")
        print(f"Comunicação: {com}% | {st_com} | {msg_com}")
        print(f"Bateria: {bat}% | {st_bat} | {msg_bat}")
        print(f"Oxigênio: {oxi}% | {st_oxi} | {msg_oxi}")
        print(f"Estabilidade: {est}% | {st_est} | {msg_est}")
        print(f"Pontuação de risco do ciclo: {risco_ciclo}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {recomendacao}")

    # Cálculos finais
    qtd_ciclos = len(dados_missao)
    medias = [
        soma_temp / qtd_ciclos,
        soma_com / qtd_ciclos,
        soma_bat / qtd_ciclos,
        soma_oxi / qtd_ciclos,
        soma_est / qtd_ciclos
    ]
    
    maior_risco = max(historico_riscos)
    ciclo_critico = historico_riscos.index(maior_risco) + 1
    media_risco = sum(historico_riscos) / qtd_ciclos
    
    # 11. Análise da tendência da missão
    tendencia = analisar_tendencia(historico_riscos[0], historico_riscos[-1])
    
    # 12. Identificação da área mais afetada
    max_pts_area = max(pontuacoes_areas)
    area_afetada_index = pontuacoes_areas.index(max_pts_area)
    area_afetada = areas_monitoradas[area_afetada_index]
    
    classificacao_final = classificar_ciclo(media_risco)
    if historico_riscos[-1] >= 6:
        classificacao_final = "MISSÃO CRÍTICA"
    elif historico_riscos[-1] >= 3:
        classificacao_final = "MISSÃO EM ATENÇÃO"
    
    # 13. Relatório final exibido no terminal
    gerar_relatorio_final(medias, ciclo_critico, maior_risco, media_risco, qtde_criticos, tendencia, pontuacoes_areas, area_afetada, classificacao_final)

if __name__ == "__main__":
    main()
