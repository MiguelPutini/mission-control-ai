# Mission Control AI

Este é um projeto desenvolvido para a Global Solution (GS) da FIAP. O Mission Control AI é um sistema em Python que simula o monitoramento inteligente de uma missão espacial experimental, sendo capaz de identificar riscos, emitir alertas e sugerir ações para apoiar a tomada de decisão.

## Equipe Rocketboys
- **Missão:** Orion-experiment-28-05-26
- Integrantes:
   - [Miguel Putini] - RM: [571624]
  - [Alexandre Rizzi] - RM: [569621]


## Estrutura do Projeto
O repositório contém os seguintes arquivos:
- `README.md`: Documentação geral do projeto.
- `mission_control.py`: Código fonte principal do sistema.

## Regras de Alerta e Limites Utilizados
O sistema monitora cinco áreas fundamentais da missão, aplicando regras de pontuação de risco baseadas nas seguintes métricas:

### Temperatura Interna
- Menor que 18 °C: **ATENÇÃO** (1 ponto)
- Entre 18 °C e 30 °C: **NORMAL** (0 ponto)
- Maior que 30 °C até 35 °C: **ATENÇÃO** (1 ponto)
- Maior que 35 °C: **CRÍTICO** (2 pontos)

### Comunicação
- Menor que 30%: **CRÍTICO** (2 pontos)
- Entre 30% e 59%: **ATENÇÃO** (1 ponto)
- 60% ou mais: **NORMAL** (0 ponto)

### Bateria
- Menor que 20%: **CRÍTICO** (2 pontos)
- Entre 20% e 49%: **ATENÇÃO** (1 ponto)
- 50% ou mais: **NORMAL** (0 ponto)

### Oxigênio
- Menor que 80%: **CRÍTICO** (2 pontos)
- Entre 80% e 89%: **ATENÇÃO** (1 ponto)
- 90% ou mais: **NORMAL** (0 ponto)

### Estabilidade
- Menor que 40%: **CRÍTICO** (2 pontos)
- Entre 40% e 69%: **ATENÇÃO** (1 ponto)
- 70% ou mais: **NORMAL** (0 ponto)

## Classificação do Ciclo
Os ciclos são classificados pela soma total de risco:
- **0 a 2 pontos:** MISSÃO ESTÁVEL
- **3 a 5 pontos:** MISSÃO EM ATENÇÃO
- **6 a 10 pontos:** MISSÃO CRÍTICA

## Como Executar
1. Certifique-se de ter o Python instalado na sua máquina (versão 3.x recomendada).
2. Clone o repositório ou baixe os arquivos.
3. Acesse a pasta do projeto via terminal.
4. Execute o comando: `python mission_control.py` ou apenas coloque para rodar
