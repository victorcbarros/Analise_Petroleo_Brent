texto_introducao = """
<div style="text-align: justify;">

O preço do petróleo é um dos indicadores econômicos mais voláteis e
importantes no cenário global, refletindo não apenas a interação direta
entre oferta e demanda, mas também uma série de fatores complexos que
moldam seu comportamento. Historicamente, a cotação do barril tem
respondido a diversos eventos mundiais significativos. Esses fatores
podem atuar isoladamente ou de forma interconectada, criando momentos
de alta ou baixa abruptas que afetam diretamente a economia mundial, a
inflação, e as estratégias de políticas energéticas.

A seguir, apontaremoscomo acontecimentos marcantes desde o início do século XXI, desempenharam
papéis cruciais nas oscilações de preços. Também serão abordados insights
sobre os principais motivos para essas variações. Compreender essas
influências é essencial para captar as tendências e possíveis desdobramentos
futuros no mercado de petróleo.

"""

texto_extracao = """
<div style="text-align: justify;">

Na etapa de extração dos dados do projeto, utilizamos uma API para obter as informações do preço do petróleo Brent. 
Esse processo foi realizado com o uso de requisições HTTP em Python.
Após a coleta dos dados, aplicamos tratamento e limpeza utilizando a biblioteca Pandas, 
garantindo que as informações estivessem no formato adequado para análise.

Em seguida, construímos um modelo preditivo de séries temporais utilizando TensorFlow/Keras para a modelagem e Scikit-learn para
o processo de pré-processamento e avaliação do modelo. Com os dados tratados e o modelo ajustado, 
geramos gráficos para visualização da evolução do preço do petróleo ao longo dos anos, além de realizar análises de tendências.

Para apresentar os resultados de forma interativa, construímos um dashboard em Power BI, 
integrando os gráficos gerados com o modelo preditivo. Esse dashboard permite uma análise visual e dinâmica das variações
de preços do petróleo ao longo do tempo.

Por fim, fizemos o deploy do MVP (Minimum Viable Product) utilizando GitHub para versionamento de código e Streamlit
para a criação de uma interface interativa. Isso proporcionou uma solução acessível e escalável para visualizar as previsões 
e as análises em tempo real.

"""


texto_analise_parte1_introdutorio = """
<div style="text-align: justify;">

Nesta seção, apresentaremos um dashboard interativo que oferece uma análise abrangente da evolução histórica do preço do petróleo
ao longo dos anos, permitindo uma visualização clara das principais tendências e variações no mercado.
Faremos uma análise detalhada dos períodos de alta e baixa, destacando momentos-chave que moldaram a trajetória dos preços,
como crises econômicas, conflitos geopolíticos e mudanças nas políticas energéticas globais.

Além disso, discutiremos o impacto de fatores externos, como a volatilidade na oferta e demanda,
avanços tecnológicos no setor energético, e a transição para fontes de energia renováveis,
que têm influenciado diretamente o comportamento do mercado petrolífero. Com essa abordagem, 
esperamos proporcionar uma visão estratégica e informada sobre como esses elementos interagem e afetam o setor ao longo do tempo,
auxiliando na compreensão das perspectivas futuras e na tomada de decisões mais assertivas.

"""


texto_analise_parte1 = """
<div style="text-align: justify;">

### 1. Crise Financeira Global (2008-2009)

- **2008: Alta Histórica**: O preço do petróleo atingiu seu pico em julho
  de 2008, ultrapassando US\$ 134 por barril. Essa alta foi alimentada
  pela crescente demanda global, especialmente de economias em desenvolvimento
  como a China, que estava em plena expansão industrial. O aumento também
  foi impulsionado por tensões geopolíticas, como os conflitos no Oriente
  Médio, e pela desvalorização do dólar americano, que tradicionalmente
  torna as commodities cotadas em dólar mais atrativas para compradores
  estrangeiros.

- **2008-2009: Queda Drástica**: Após o auge de 2008, a crise financeira
  global, iniciada com o colapso do mercado de hipotecas subprime nos EUA,
  espalhou-se pelo mundo, causando recessão em diversas economias. A demanda
  por petróleo caiu abruptamente com a desaceleração da atividade econômica,
  resultando em uma queda de preços para cerca de US\$ 40 por barril em dezembro
  de 2008. Os temores de uma recessão profunda e a redução no consumo
  industrial e de transporte foram os principais fatores que puxaram os
  preços para baixo.

### 2. Primavera Árabe e Sanções ao Irã (2011-2014)

- **Impacto da Primavera Árabe**: A onda de protestos e revoltas populares
  que varreu o Oriente Médio e o Norte da África em 2011, conhecida como
  Primavera Árabe, levou à instabilidade política em vários países
  produtores de petróleo, como a Líbia e o Egito. Essa instabilidade
  gerou incertezas no mercado de petróleo, elevando os preços devido ao medo
  de interrupções na oferta.

- **Sanções ao Irã**: Durante esse período, o Irã, um dos maiores produtores
  de petróleo do mundo, enfrentou sanções econômicas impostas por países
  ocidentais devido a seu programa nuclear. As sanções limitaram a capacidade
  do Irã de exportar petróleo, diminuindo a oferta global e contribuindo para
  manter os preços altos, frequentemente acima de US\$ 100 por barril.

### 3. Aumento da Produção dos EUA e Desaceleração Econômica (2014-2016)

- **Revolução do Xisto**: A tecnologia de fraturamento hidráulico (fracking)
  permitiu aos Estados Unidos aumentar drasticamente sua produção de petróleo
  de xisto, tornando-se um dos principais produtores mundiais. Isso criou
  um excesso de oferta global, pressionando os preços para baixo.

- **Desaceleração Econômica Global**: Simultaneamente, a economia global
  começou a mostrar sinais de desaceleração, especialmente em economias
  emergentes como a China. A combinação de oferta abundante e demanda
  em queda levou a uma queda acentuada nos preços do petróleo, de cerca
  de US\$ 100 em meados de 2014 para valores próximos a US\$ 30 por barril
  em janeiro de 2016.

### 4. Pandemia de COVID-19 (2020)

- **Redução de Demanda**: A pandemia de COVID-19, iniciada em 2020,
  resultou em lockdowns globais e uma redução sem precedentes na demanda
  por petróleo, já que o transporte terrestre e aéreo caiu drasticamente.
  Isso, somado a um acordo entre a OPEP e a Rússia que inicialmente falhou
  em cortar a produção, causou um acúmulo de petróleo sem espaço de
  armazenamento.

- **Valor Mínimo Histórico**: Em abril de 2020, o petróleo WTI (West
  Texas Intermediate) chegou a um valor negativo de -US\$ 37,63 por barril
  devido ao excesso de oferta e falta de capacidade de armazenamento nos
  Estados Unidos. O Brent, referência internacional, atingiu US\$ 18,47 por
  barril, o menor valor em duas décadas.

### 5. Invasão da Ucrânia pela Rússia (2022)

- **Impacto das Sanções**: Em fevereiro de 2022, a invasão da Ucrânia
  pela Rússia gerou uma forte reação internacional, resultando em sanções
  econômicas que limitaram a exportação de petróleo russo. Como a Rússia
  é um dos maiores exportadores globais de petróleo e gás, as sanções
  criaram um choque de oferta no mercado.

- **Alta dos Preços**: Em resposta a essa incerteza, o preço do petróleo
  Brent ultrapassou US\$ 110 por barril em março de 2022, chegando a picos
  de mais de US\$ 120 em alguns momentos. As sanções aumentaram a pressão
  sobre a oferta global e fizeram com que os países buscassem alternativas
  para substituir a energia russa.

"""

texto_analise_parte2_introdutorio = """




"""



texto_analise_parte2 = """
<div style="text-align: justify;">

## Fatores que Influenciam a Volatilidade do Preço do Petróleo

O preço do petróleo é amplamente influenciado por uma combinação complexa
de fatores geopolíticos, econômicos, inovações no setor de energia e
eventos mundiais. Cada um desses aspectos desempenha um papel crucial na
dinâmica de oferta e demanda, afetando as cotações no mercado global. Aqui
está uma análise detalhada de como esses fatores contribuem para a
volatilidade nos preços do petróleo:

### 1. Geopolítica

- **Conflitos no Oriente Médio**: O Oriente Médio é responsável por uma
  grande parte da produção global de petróleo. Qualquer instabilidade
  política, como guerras, conflitos civis ou revoluções (e.g., a Guerra
  do Golfo, a invasão do Iraque em 2003, e a Primavera Árabe), pode gerar
  preocupações sobre a continuidade do fornecimento. Essas tensões
  normalmente impulsionam os preços para cima devido ao temor de
  interrupções.

- **Sanções Econômicas**: Países exportadores de petróleo frequentemente
  enfrentam sanções econômicas devido a razões políticas, como no caso
  do Irã e da Rússia. As sanções afetam diretamente a capacidade desses
  países de exportar petróleo, reduzindo a oferta disponível no mercado
  e elevando os preços.

- **Políticas de Grandes Exportadores**: Decisões de grandes produtores
  e alianças como a OPEP e a OPEP+ (que inclui Rússia e outros produtores)
  em ajustar a produção impactam os preços. Aumentos na produção podem
  levar a quedas nos preços, enquanto cortes para estabilizar o mercado
  impulsionam a alta.

### 2. Motivos Econômicos

- **Crises Financeiras e Recessões**: Períodos de recessão econômica,
  como a Crise Financeira Global de 2008-2009 e a desaceleração global
  de 2020 devido à pandemia, causam uma queda acentuada na demanda por
  petróleo. Isso ocorre porque atividades industriais, transporte e
  consumo de energia são reduzidos, levando a uma baixa nos preços.

- **Crescimento Econômico**: Por outro lado, quando as economias globais
  estão em crescimento, a demanda por petróleo aumenta, pois há mais
  produção industrial, uso de transporte e consumo de energia. Isso pode
  elevar os preços, especialmente se a oferta não acompanhar o aumento
  da demanda.

### 3. Inovações e Produção

- **Avanços na Extração de Petróleo de Xisto**: A revolução do xisto
  nos Estados Unidos, possibilitada por tecnologias de fraturamento
  hidráulico e perfuração horizontal, levou a um aumento significativo
  da produção de petróleo. Isso mudou a dinâmica global, pois os EUA
  passaram de importador para um dos principais exportadores. O aumento
  da oferta global pressionou os preços para baixo, como observado entre
  2014 e 2016.

- **Mudanças na Produção da OPEP+**: A OPEP+ tem grande influência
  na oferta de petróleo, ajustando a produção conforme as necessidades
  de estabilização do mercado. Decisões de cortes ou aumentos na produção
  são frequentemente tomadas para impactar os preços globalmente.

### 4. Crises e Eventos Globais

- **Eventos Imprevisíveis**: A pandemia de COVID-19 foi um evento global
  que gerou uma queda abrupta na demanda por petróleo. Além disso, crises
  ambientais, como desastres naturais ou interrupções nas cadeias de
  fornecimento, podem afetar a produção ou o transporte de petróleo,
  causando mudanças inesperadas nos preços.

"""

texto_previsao_introdutorio = """




"""



texto_previsao = """
<div style="text-align: justify;">

O mês de novembro de 2024 mostrou uma tendência de queda gradual no preço do barril de petróleo. 
Iniciando em $82,63, o valor caiu consistentemente, atingindo \$73,52 em seu ponto mais baixo. 
A análise da previsão sugere que essa queda está associada a uma menor demanda, 
especialmente em regiões com expectativa de inverno mais ameno, 
além de incertezas no mercado geradas por cortes de produção da OPEP+.

Os gráficos reforçam essa estabilidade no declínio, mostrando variações diárias mínimas, geralmente em torno de 0,4%, 
sem grandes oscilações. Esses dados indicam que, apesar da queda, o mercado não espera choques significativos, 
mantendo-se dentro de um cenário previsível. No final do mês, sinais de recuperação, com leve alta nos preços, 
apontam para expectativas de aumento da demanda nos próximos períodos e ajustes no equilíbrio entre oferta e demanda global.


"""



texto_conclusao = """
<div style="text-align: justify;">

A volatilidade do preço do petróleo é um reflexo da complexa interação entre fatores políticos, 
econômicos, sociais e tecnológicos. Embora a oferta e a demanda sejam as forças básicas que movem o mercado,
eventos globais, como crises geopolíticas, pandemias e mudanças nas políticas de grandes países produtores, 
frequentemente desempenham um papel ainda mais significativo nas oscilações dos preços.

Essas flutuações impactam diretamente não apenas os investidores e as empresas do setor, 
mas também a economia global, afetando desde o custo de vida até a estabilidade financeira
de nações cuja economia depende fortemente da exportação ou importação de petróleo. 
Além disso, as mudanças climáticas e a pressão por uma transição energética sustentável colocam desafios adicionais ao setor, 
exigindo uma adaptação às novas demandas por fontes de energia mais limpas e menos dependentes de combustíveis fósseis.

Entender esses fatores é fundamental para antecipar tendências e desenvolver estratégias eficazes 
em um cenário cada vez mais dinâmico. O futuro do mercado de petróleo dependerá de como esses elementos
se alinharão nos próximos anos, especialmente diante do crescimento das energias renováveis, 
do avanço tecnológico em energias limpas e da necessidade global de reduzir as emissões de carbono. 
O equilíbrio entre esses fatores definirá não apenas a trajetória dos preços do petróleo,
mas também o papel que ele desempenhará no fornecimento de energia mundial nas próximas décadas.


"""


texto_final = """

Este projeto faz parte do projeto Tech Challenge da Pós Tech Data Analytics FIAP e conta como nota da quarta fase da pós-graduação.
O grupo que desenvolveu esse projeto é composto por:

Aelton Pereira de Lacerda

André Martins Pontes

Arthur do Nascimento Siqueira

Matheus Martins Matias Rodrigues

Victor Campanha Barros


O link do repositorio do github com todos os arquivos pode ser acessado clicando no simbolo do github no menu superior direito
e no link abaixo : 

https://github.com/victorcbarros/Analise_Petroleo_Brent
"""