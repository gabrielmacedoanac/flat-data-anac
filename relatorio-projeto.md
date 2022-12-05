#  Gestão da criação, armazenamento e acesso a informações sobre objetivos dos normativos de aeronavegabilidade

## 1. Apresentação

Após uma primeira fase de estudos voltada ao diagnóstico dos desafios identificados, registrada por meio de relatório [SEI no. 5547230](https://sei.anac.gov.br/sei/modulos/pesquisa/md_pesq_processo_exibir.php?iI3OtHvPArITY997V09rhsSkbDKbaYSycOHqqF2xsM0IaDkkEyJpus7kCPb435VNEAb16AAxmJKUdrsNWVIqQ3aI01DduSzR6IIGTHBGQQWtjpFraSr02swx5S-uW3QG), o projeto teve iniciada a fase de desenvolvimento, considerando as linhas de ação priorizadas, que incluem:

> **1. Prototipação de bases de dados, busca e interfaces**
>
> Ação foi desenvolvida ao longo dessa fase do projeto e representa o assunto principal deste relatório.

> **2. Levantamento e padronização de fontes de dados como projeto piloto**
>
> As fontes de dados da ANAC e de outras autoridades de aviação civil estrangeiras de interesse normativo foram levantadas, relacionadas e tiveram uma proposta de padronização seguindo: referências para [Boas Práticas para Dados na Web (Recomendação do W3C de 31 de janeiro de 2017)](https://w3c.br/traducoes/DWBP-pt-br/) e um modelo de metadados sugeridos conforme o [SKOS Simple Knowledge Organization System Reference (W3C Rceomendação do W3C de 18 agosto de 2009)](https://www.w3.org/TR/skos-reference/). 

> **3. Implementação de fórum com integração das informações do SEAM e abertura para repositório de discussões técnicas (informais)**
> 
> Ação desenvolvida alo longo dessa fase do projeto envolveu a implementação da ferramenta [Discourse em caráter de homologação](https://homologacao-discourse.anac.gov.br/) (acesso por meio da VPN da ANAC).

>**4. Interface eletrônica para a promoção de busca a material acadêmico**
>
> Essa ação envolveu a descoberta e divulgação de ferramentas para pesquisa de material acadêmico. Parte dessas ferramentas foram apresentadas no relatório da primeira fase [SEI no. 5547230](https://sei.anac.gov.br/sei/modulos/pesquisa/md_pesq_processo_exibir.php?iI3OtHvPArITY997V09rhsSkbDKbaYSycOHqqF2xsM0IaDkkEyJpus7kCPb435VNEAb16AAxmJKUdrsNWVIqQ3aI01DduSzR6IIGTHBGQQWtjpFraSr02swx5S-uW3QG) e são acrescidas de  novas ferramentas e sistematizadas neste relatório com os demais recursos identificados pelo projeto.

>**5. Proposta de evolução do processo de Policy File**
>
> Nessa ação foi feita uma primeira proposta de atualização do processo de publicação de policy files da SAR, com um conjunto de metadados. Com base em tal levantamento a área de normas da SAR, a Gerência Técnica de Normas e Inovação iniciou um processo de estudo da demanda, que tem como uma das alternativas consideradas, a possibilidade de mudar a forma de publicação de policy fiels para o modelo de Instruções Suplementares de processamento expedito. (Adicionar indicação do documento sEI)

### 1.1 Objetivo Geral

Apresentar o resultado dos estudos de soluções no contexto do projeto "Gestão da criação, armazenamento e acesso a informações sobre objetivos dos normativos de aeronavegabilidade.".

### 1.2 Objetivos Específicos

- Apresentar resultado de testes de ferramentas.
- Apresentar ferramentas implementadas e disponíveis para uso.
- Apresentar recomendações para a gestão de dados.
- Promover cultura de gestão e governança de dados.

### 1.3 Definição do problema

O problema central a ser tratado pelo projeto envolveu a produção, organização e recuperação de informações pertinentes ao processo normativo na SAR.

Com base na árvore de problemas produzida na primeira fase deste projeto  foram priorizadas ações junto aos patrocinadores da iniciativa.

### 1.4 Fundamentação

Visando a sustentação das alternativas abordadas nesta fase do projeto, foi necessário aprofundar o entendimento sobre os seguintes assuntos:

- Gestão e governança de dados, considerando uma proposta de mapeamento do processo de gestão de dados.
- Criação e curadoria de metadados de interesse normativo.
- Relacionamento entre dados estruturados e não estruturados.
- Ferramentas e processos de produção de coleta de dados.
- Ferramentas e processos para a automação, integração e versionamento de bases de dados.
- Ferramentas e processos de recuperação da informação.

### 1.5 Estratégia de ação

Conforme representada na figura 1, a fase de aprofundamento do estudo de soluções adotou como estratégia o seguinte fluxo:

1. Análise das causas dos problemas.
1. Identificação de ferramentas e ações necessárias para atacar as causas.
1. Teste de ferramentas e implementação de ações.
1. Avaliação de resultados e produção deste relatório.

![Figura 1 - Estratégia de ação](https://i.imgur.com/pspbFPA.png)
<small>Figura 1 - Estratégia de ação.</small>

### 1.6 Visão temporal do projeto

Colocando, em uma linha do tempo, os passos seguidos pelo projeto e os possíveis desdobramentos, foi traçada uma linha do tempo com o intuito de facilitar uma visualização do esforço empreendido.

> ROADMAP - pegar tabelas de Germano e generalizar as fases.

Período | Ação | Início | Fim |
| :--- | :--- | :---: | :---: |
| **2020-2** | - Planejamento </br> - Diagnóstico </br> - Estruturação de problema </br> - Análise de decisão </br> |08/2020|12/2020
| **2021-1** | - Relatório de diagnóstico e direcionamento do desenvolvimento futuro </br> - Prototipação de base de dados </br> - Prototipação de fórum + SEAM </br> - Análise de processo de police files </br>|01/2021|06/2021
| **2021-2** | - Prototipação de base de dados </br> - Prototipação de fórum + SEAM </br> - Análise de processo de police files </br>|06/2021|03/2022
| **2022-1** | - Avaliação sobre Elastic Search </br> - Avaliação sobre Neo4J e *Knowledge Graphs* </br> - Validação de fórum + SEAM </br> - Levantamento de metadados de normativos </br>|03/2022|06/2022
| **2022-2** | - Captura, criação e avaliação de metadados de normativos </br> - Complemento sobre uso de fórum </br> - Teste de ferramentas de busca </br> - Relatório final de recomendações </br> |06/2022|12/2022

<small>Tabela 1 - Roadmap de etapas desenvolvidas durante o projeto</small>

## 2. Desenvolvimento (Testes e confirmações)

### 2.1 Abordagem do problema

### 2.1.1 Diagnóstico e seleção de causas a serem tratadas

No estudo inicialmente realizado pelo projeto foi identificado como poblema central:

A percepção de dúvidas (internas e externas) recorrentes sobre motivação de requisitos de aeronavegabilidade que são da competência da SAR.

Como possíveis consequências (3 grupos):

1. Casos em que processos normativos não sejam detalhados suficientemente geram dependência de estudo de material de referência (ex. FAA).
1. Ações regulatórias têm sua produtividade prejudicada por falta de acesso rápido à motivação de normativos.
1. Risco de não ser aproveitada experiência anterior com a norma.

E como prováveis Causas (6 grupos):

1. Processo de registro de interpretações não é focado, de maneira efetiva, em facilitar pesquisa interpretativa.
1. As informações estão em bases de dados diversas (ex.: SIGAD, SEI, rgl.faa.gov, federal register etc.).
1. Não se consegue aproveitar metódica e rapidamente o histórico de motivações e interpretações anteriores.
1. Consulta a motivação de requisitos não dá abertura para aproveitamento de conhecimento de público externo.
1. Não há IS para todos os requisitos sob competência da SAR.
1. SAR não tem fácil acesso a teses acadêmicas que poderiam contribuir em análises técnicas.

Diante das causas identificadas o grupo selecionou as que estariam no escopo de atuação do projeto, visto que a intenção seria a de apresentar soluções que facilitassem a conexão e disponibilização de informações já existentes, sem entrar no mérito de exigir melhorias pontuais em processos já em curso.

O critério adotado para tratamento das causas identificadas também ponderou o uso de abordagens que não impusessem a reformulação imediata dos processos em curso ou o retrabalho sobre processos já concluídos. 

No Documento [SEI 5491169](https://sei.anac.gov.br/sei/modulos/pesquisa/md_pesq_processo_exibir.php?iI3OtHvPArITY997V09rhsSkbDKbaYSycOHqqF2xsM0IaDkkEyJpus7kCPb435VNEAb16AAxmJKUdrsNWVIqQ3aI01DduSzR6IIGTHBGQQWtjpFraSr02swx5S-uW3QG), Árvore de Problemas, são apresentados os agrupamentos das causas selecionadas e descartadas durante o projeto.

Destaca-se que a relação de causas tratáveis foi organizada em 5 frentes de trabalho de forma a facilitar a identificação de alternativas.

Com isso, optou-se por reagrupar as causas por:

1.	Mecanismo de busca indexada de informações já explicitadas.
2.	Integração de base de dados.
3.	Registro de discussões feitas fora de formalização processual.
4.	Canal de discussão com público externo.
5.	Mapeamento de conexão de normativos.

Após a constatação inicial de causas tratáveis, partiu-se para a identificação de dados e informações relacionadas com o processo interpretativo na SAR, selecionando os recursos que estariam disponíveis para prototipação de possíveis soluções.

### 2.1.2 Desenvolvimento de um modelo conceitual

Na primeira fase do projeto, o direcionamento para abordar o problema consistiu da identificação de modelos e melhores práticas disponíveis para organizar dados estruturados e não estruturados. Dessa forma foram buscadas as seguintes referências:

1. Fontes de dados da ANAC.
1. Padrões para publicação de dados em ambiente da Web.
1. Trabalhos acadêmicos sobre governança e gestão de dados e metadados.
1. Tipos de bancos de dados para registrar e estabelecer relacionamento entre as informações disponíveis.
1. Ferramentas para prototipar soluções de organização e recuperação das informações (modelos semânticos e ferramentas de busca).

Ainda, se pretendeu que os protótipos desenvolvidos e testados permitissem a inclusão de novas fontes de dados, de modo a servir como uma estrutura confiável para a expansão com outras informações trabalhadas pelas demais áreas da ANAC.

A "Figura 2 - Modelo conceitual da 1ª fase do projeto" apresenta o ponto de partida em forma de síntese para sistematizar a comunicação sobre uma complexa realidade do universo de dados trabalhados no contexto da interpretação e produção de normativos de aeronavegabilidade. A intenção foi internalizar as melhores práticas identificadas nos padrões de publicação para dados na Web e o avanço da produção científica sobre o assunto. 

Dentre as referências trabalhadas, o modelo aponta: 

- banco de conhecimento gerado pelo SEAM.
- fórum de discussões com potencial de abertura para público externo.
- bases de dados de atos normativos da SAR. 
- guias e materiais orientativos da ANAC.
- dados de discussões informais.
- dados de policy files geradas pela ANAC.
- ferramentas ligadas a trabalhos acadêmicos, de assunto de interesse da ANAC.

![](https://i.imgur.com/HdgF4bK.jpg)
<small>Figura 2 - Modelo conceitual da 1ª fase do projeto.</small>

O que se pretendeu foi reunir as diversas fontes de dados que hoje não estão integradas e promover uma ferramenta de recuperação consistente, atravessando essas bases. Então, foram iniciadas ações e testes de ferramentas abordando cada um dos elementos da figura 2, sendo o modelo de organização semântica, por grafos de conhecimento ([*Knowledge Graph*](https://wiki.anac.gov.br/wiki/index.php/Knowledge_graph)), um apesto central para estabelecer o relacionamento, o enriquecimento e ampliação das possibilidades de recuperação dos dados.

> *Knowledege Graph*, Grafo de Conhecimento ou Mapa de Conhecimento representa uma coleção de descrições interligadas de entidades - objetos, eventos ou conceitos. Funcionam como uma abstração para organizar o conhecimento e como uma forma de integrar informações extraídas de diferentes fontes de dados. Os grafos de conhecimento colocam os dados em contexto por meio de links e metadados semânticos e, dessa forma, fornecem uma estrutura para integração, unificação, análise e compartilhamento de dados. É uma base de conhecimento que usa um modelo de dados estruturados em grafos ou topologia para integrar dados. Qualquer conjunto de dados pode ser representado como um grafo.

### 2.2 Criação de um fluxo de trabalho previsível e adaptável

projeto serviu para pensar no processo, tendo partido da ideia inicial de ferramentas

aspecto central é a identificação de metadados

o conteúdo do grafo de conhecimento e a especialização e acurária e relação com os metadados com cada área específica que usa determinados dados

o grafo de conhecimento é o alicerce
metadados são tijolos do sistema

um paráfrafo com um comentário geral sobre metadados, um pra governanca de metadados e um par casos de ngócios

como ir do ideal para o exequível

quais seriam as fases e tarefas

para isso foi feito um mapeamento de processo

o uqe poderia vir a ser um processo de trabalho 

pq que mapeou dessa forma?

como modelar entrada de dado no futuro como um serviço?

gerenciamento de ciclo de vida de dado entrar só como referência

Com base nos recursos disponibilizados para a realização do projeto xx

Dentre o que foi inicialmente idealizado, foi considerado como exequível xxx.

maturidade de governança de dados

o que já existe hoje e o que ainda não existe, parte de integração

corte feito no ponto 4, engenharia de dados

4 para o 5 processo de análise e visualização 

6 é a ferramenta dentro de um contexto

mesma lógica da Web, em que se trabalha com uma tela com várias ferramentas

sendo montada uma tela para o usuário



Na sequência, durante a fase de aprofundamento do estudo de viabilidade do pacote de soluções, procedeu-se xxxxx.

Como resultado, a Figura 2 apresenta xxxx

![](https://i.imgur.com/SwMKkGD.png)

Figura 2 - Novo modelo conceitual xxx

**Gerênciamento de casos de negócio** 

> O gerenciamento de casos é uma extensão do Business Process Management (BPM) que permite gerenciar processos de negócios adaptáveis.[^redhat]

> O gerenciamento de casos (CM) foi introduzido como uma ferramenta para trabalhadores do conhecimento por van der Aalst em 2005. Em maio de 2014, a OMG publicou um padrão para gerenciamento de casos chamado Case Management Model and Notation (CMMN). Seu foco é apoiar processos imprevisíveis, intensivos em conhecimento e fracamente estruturados. O gerenciamento de casos é um tipo de tecnologia de processo de negócios que não usa fluxo de controle para descrever o processo. [^visual]

> BPM é uma prática de gestão utilizada para automatizar tarefas que são repetíveis e possuem um padrão comum, com foco na otimização pelo aperfeiçoamento de um processo. Os processos de negócios geralmente são modelados com caminhos claramente definidos que levam a uma meta de negócios. Isso requer muita previsibilidade, geralmente baseada em princípios de produção em massa. No entanto, muitos aplicativos do mundo real não podem ser descritos completamente do início ao fim (incluindo todos os caminhos, desvios e exceções possíveis). Usar uma abordagem orientada a processos em certos casos pode levar a soluções complexas que são difíceis de manter. [^redhat]
>
> O gerenciamento de casos fornece resolução de problemas para processos imprevisíveis e não repetíveis, em oposição à abordagem orientada para a eficiência do BPM para tarefas rotineiras e previsíveis. Ele gerencia situações pontuais quando o processo não pode ser previsto com antecedência. A definição de caso geralmente consiste em fragmentos de processo fracamente acoplados que podem ser conectados direta ou indiretamente para levar a determinados marcos e, por fim, a um objetivo de negócios, enquanto o processo é gerenciado dinamicamente em resposta a alterações que ocorrem durante o tempo de execução. [^redhat]

**PM x CMMN** [^visual]

Diferenças entre BPMN e CMMN:

|Notações BPMN|	Notação CMMN|
| - | - |
|Imperativo	|Declarativo|
|Centrado no processo|	Centrado em dados|
|Arcos descrevem a sequência	|Nenhuma sequência predefinida|
|Trabalho guiado (trabalhadores de cabeça para baixo)|	Habilita trabalhadores (trabalhadores do conhecimento)|
|Tudo é modelado|	Nem tudo é modelado|

>A **Notação Declarativa** não tenta modelar o fluxo de um problema; eles estabelecem os resultados desejados, ou seja, especificando o que eles querem que aconteça, mas não como isso deve acontecer. A **Notação Imperativa**, por outro lado, tenta modelar o fluxo de um problema.

**Processo Estruturado x Caso x Processo Ad-Hoc** [^visual]

|Processo Estruturado|	Caso|	Processo ad hoc|
|-- | -- | -- |
| Fluxo do processo estruturado. | Fluxo do processo pode ser parcialmente estruturado. | Fluxo do processo não pode ser estruturado - novas tarefas surgindo durante a execução. |
| Atividades conhecidas com antecedência. | Atividades parcialmente conhecidas com antecedência. | Atividades parcialmente conhecidas com antecedência. |
| Muitos elementos repetitivos. | Alguns elementos repetitivos. | Poucos elementos repetitivos. |
| Nenhum grau de liberdade para as pessoas em relação ao fluxo do processo. | Algum grau de liberdade para as pessoas em relação ao fluxo do processo. | Alto grau de liberdade para as pessoas em relação ao fluxo do processo em *t0*. |
| **Pode ser modelado.** | **Pode ser modelado.** | **Não pode ser modelado.** |

**Denifição de um caso de negócio** [^redhat]

> Uma definição de caso é sempre uma definição de processo ad hoc e não requer um nó inicial explícito. A definição de caso é o principal ponto de entrada para o caso de uso de negócios.
>
>Uma definição de processo ainda pode ser introduzida como uma construção de suporte do caso e pode ser chamada conforme definido na definição de caso ou dinamicamente para trazer processamento adicional quando necessário. Uma definição de caso define os seguintes novos objetos:
>
> - Atividades (obrigatório)
> - Arquivo do caso (obrigatório)
> - Conquistas
> - Funções
> - Estágios




### 2.2.1 Desenvolvimento de fontes para descoberta e captura de informações 

(**`Talvez seja interessante sekparar fundamentação teórica de desenvolvimento em dois tópicos ou seções separado(a)s, para que o leitor possa direcionar melhor sua atenção`**).

### 2.2.2 Criação e desenvolvimento de metadados

**Metadados e seus benefícios**

> No gerenciamento de dados, os metadados incluem informações sobre processos técnicos e de negócio, regras e restrições de dados e estruturas de dados lógicas e físicas. Ele descreve os próprios dados (por exemplo, bancos de dados, elementos de dados, modelos de dados),os conceitos que os dados representam (por exemplo, processos de negócios, sistemas de aplicativos, código de software, infraestrutura de tecnologia) e as conexões (relacionamentos) entre os dados e os conceitos.
>
> Os metadados auxiliam uma organização a entender seus dados, sistemas e fluxos de trabalho. Ele permite a avaliação da qualidade dos dados e faz parte do gerenciamento de bancos de dados e outros aplicativos. Contribui para a capacidade de processar, manter, integrar, proteger, auditar e governar outros dados.
> 
> Os dados não podem ser gerenciados sem os metadados. Além disso, os próprios metadados devem ser gerenciados. Atenção, metadados confiáveis e bem gerenciados ajudam a: 
> - Aumentar a confiança nos dados, fornecendo contexto, permitindo a representação consistente dos mesmos conceitos e a medição da qualidade dos dados.
> - Ampliar o valor das informações estratégicas (por exemplo, dados mestre), possibilitando vários usos.
> - Identificar dados e processos redundantes e assim melhorar a eficiência operacional.
> - Impedir o uso de dados desatualizados ou incorretos.
> - Proteger informações confidenciais.
> - Reduzir o tempo de pesquisa orientada a dados.
> - Aperfeiçoar a comunicação entre consumidores de dados e profissionais de TI.
> - Criar análise de impacto precisa, reduzindo assim o risco de falha do projeto.
> - Melhorar o tempo de implementação, reduzindo o tempo do ciclo de vida do desenvolvimento do sistema.
> - Reduzir os custos de treinamento e diminuir o impacto da rotatividade de pessoal por meio de documentação completa do contexto, histórico e origem dos dados.
> - Dar suporte à conformidade regulamentar.
> 
> As organizações obtêm mais valor de seus ativos de dados se os dados forem de alta qualidade. Os dados de qualidade dependem da governança. Como explicam os dados e processos que permitem que as organizações funcionem, os metadados são críticos para a governança de dados. Se os metadados são um guia para os dados em uma organização, eles devem ser bem gerenciados.[^enap]

**Ciclo de vida de gerenciamento da qualidade de dados e metadados**[^enap]
![](https://i.imgur.com/7GapQAc.png) 

> Para um determinado conjunto de dados, um ciclo de melhoria da qualidade começa ientificando os dados que não atendem aos requisitos dos consumidores, que são problemas e geram obstáculos à consecução dos objetivos de negócios. 
> 
> Os dados precisam ser avaliados em relação às principais dimensões da qualidade e aos requisitos de negócio conhecidos. As causas principais dos problemas precisarão ser identificadas para que as partes interessadas possam entender os custos da correção e os riscos de não remediá-los. Esse trabalho geralmente é realizado em conjunto com o Data Stewards e outras partes interessadas. [^enap]

> **Padrão de Registro de Metadados ISO/IEC 11179**[^enap]
> O Padrão de Registro de Metadados da ISO, ISO/IEC 11179 fornece uma estrutura
> para definir um registro de Metadados.
> Este padrão foi projetado para permitir a troca de dados orientada por metadados, com base em definições exatas de dados, começando com elementos de dados. O padrão está estruturado em seis partes:
> Parte 1: Estrutura para geração e padronização de elementos de dados.
> Parte 2: Fornece um modelo conceitual para gerenciar esquemas de classificação.
> Parte 3: Atributos básicos dos elementos de dados.
> Parte 4: Regras e diretrizes para a formulação de definições de dados.
> Parte 5: Princípios de nomeação e identificação para elementos de dados.
> Parte 6: Registro de elementos de dados.
> Mais informações: http://metadata-standards.org/11179/

**Estratégia de Metadados**

> Os passos para a estratégia de metadados incluem:[^enap]
> 
> • Iniciar o planejamento da estratégia de metadados
> O objetivo do início e do planejamento é permitir que a equipe de estratégia de metadados defina suas metas de curto e longo prazo. O planejamento inclui a elaboração de uma carta, escopo e objetivos alinhados aos esforços gerais de governança e o estabelecimento de um plano de comunicação para apoiar o esforço. As principais partes interessadas devem estar envolvidas no planejamento.
> 
> • Realizar entrevistas com as principais partes interessadas
> As entrevistas com as partes interessadas técnicas e de negócios fornecem uma base de conhecimento para a estratégia de Metadados.
> 
> • Avaliar fontes de metadados existentes e arquitetura da informação
> A avaliação determina o grau relativo de dificuldade na solução dos problemas de metadados e sistemas identificados nas entrevistas e na revisão da documentação. Durante esse estágio, realize entrevistas detalhadas da equipe principal de TI e revise a documentação das arquiteturas do sistema, modelos de dados, etc.
> 
> • Desenvolver a arquitetura futura de metadados
> Refine e confirme a visão futura e desenvolva a arquitetura de destino de longo prazo para o ambiente de metadados gerenciados neste estágio. Essa fase deve levar em consideração componentes estratégicos, como estrutura organizacional, alinhamento com administração e administração de dados, arquitetura de metadados gerenciados, arquitetura de entrega de metadados, arquitetura técnica e arquitetura de segurança.
>
> • Desenvolver plano de implementação em fases
> Valide, integre e priorize os resultados das entrevistas e análises de dados. Documente a estratégia de metadados e defina uma abordagem de implementação em fases para passar do ambiente de metadados gerenciado existente para o futuro.
>
> A estratégia evoluirá com o tempo, à medida que os requisitos de metadados, a arquitetura e o ciclo de vida dos metadados forem mais bem compreendidos.


### 2.2.3 Consolidação da base de dados

### 2.2.4 Versionamento

### 2.2.5 Busca e recuperação de informações

### 2.2.6 Criação de contextos e integração de ferramentas (*hubs* de conteúdo)

**Dados adequados para os contextos em que são necessários**

- *Hubs* de conteúdo: contectar silos de dados e dados dispersos, promover o acesso, incentivar ciclo-duplo de conhecimento (consumidor é também produtor e curador de conteúdo).

### 2.3 Ferramentas

#### Ferramentas de busca genéricas

> Comparativo de ferramentas de busca. Busca por termo em texto (FTS - *full text search*): https://supabase.com/blog/postgres-full-text-search-vs-the-rest

- MeiliSearch
- OpenSearch
- SQLite FTS
- Typesense

>  Como testamos o desempenho desses sistemas complexos e díspares em um problema infinitamente redefinido e difícil de resolver? Aderindo aos casos de uso.
> 
> Qualquer mecanismo de pesquisa tem dois empregos:
> 
> 1. Ingerir informações (geralmente chamadas de "documentos")
> 1. Retornar documentos que correspondam às consultas do usuário
>
> A ingestão de informações pode ser importante, mas o "desempenho do mecanismo de pesquisa" geralmente se refere à segunda etapa - fazer consultas e gerar resultados.
> 
> Ou seja, a principal preocupação é assumir que um cluster já possui dados adequados carregados nele, com que rapidez ele pode fornecer os resultados relevantes para uma consulta enviada pelo usuário?
> 
> Vamos nos concentrar no significado de desempenho centrado no usuário final aqui (velocidade de consulta).

RESULTADOS

> **Meilisearch**
>> Concordo que usar o PG em casos de uso simples é uma excelente maneira de ser pragmático. Infelizmente, o PG nunca poderá oferecer uma experiência de pesquisa como a que você poderia ter com o Meilisearch. O Meilisearch possui gerenciamento perfeito de erros de digitação e buscas por prefixo, permitindo uma busca a cada pressionamento de tecla. Relevância aprimorada com regras como o número de palavras presentes, a importância do atributo, a proximidade dos termos pesquisados ​​no documento e parâmetros personalizados. A capacidade de misturar pesquisas textuais, geográficas e de facetas. Meilisearch compreende automaticamente quase todos os idiomas com a possibilidade de ter sinônimos e palavras de parada. Meilisearch tem um desempenho incrível mesmo em grandes volumes de dados, e nenhum proxy de backend é necessário, graças ao gerenciamento completo de API Key.
>>
>> Quentin de Quelen, CEO da Meilisearch

## 3. Conclusão

## 4. Recomendações

Considerando Regimento xxx

Ao SAR itens xx, yy, zz
À ASTEC
À Ouvidoria
À ASCOM
À STI
....

## 5. Sumário Executivo (passar para o final)

### 5.1 Introdução

Após uma primeira rodada de diagnóstico foram identificadas ações a serem desenvolvidas e testadas com o intuito de contribuir para a melhoria da gestão de objetivos de requisitos de normativos na SAR.

### 4.2 Gestão de objetivos de requisitos de normativos

No contexto do projeto em tela, trata-se do conjunto de atividades voltadas a facilitar a recupeeração de histórico de evolução de normativos, assim como de permitir uma verificação célere do relacionamento existente entre normativs.

### 4.3 Problema alvo do projeto

Com base no diagnóstico feito junto ao público interno da SAR, o problema central considerado foiadvindo da percepção da existência de dúvidas (internas e externas) recorrentes sobre motivação de requisitos de aeronavegabilidade que são da competência da SAR.

As consequências do problema foram identificadas em 3 grupos:
i. Casos em que processos normativos não sejam detalhados suficientemente geram dependência de estudo de material de referência (ex. FAA).
ii. Ações regulatórias têm sua produtividade prejudicada por falta de acesso rápido à motivação de normativos.
iii. Risco de não ser aproveitada experiência anterior com a norma.

E as causas em 6 grupos:
i. Processo de registro de interpretações não é focado, de maneira efetiva, em facilitar pesquisa interpretativa.
ii. As informações estão em bases de dados diversas (ex.: SIGAD, SEI, rgl.faa.gov, federal register etc.).
iii. Não se consegue aproveitar metódica e rapidamente o histórico de motivações e interpretações anteriores.
iv. Consulta a motivação de requisitos não dá abertura para aproveitamento de conhecimento de público externo.
v. Não há IS para todos os requisitos sob competência da SAR.
vi. SAR não tem fácil acesso a teses acadêmicas que poderiam contribuir em análises técnicas.

### 4.4 Conjunto de soluções idealizadas

Dentre as ações selecionadas pelo projeto, para serem desenvolvidos testes, te-se a seguir uma listagem:

- xx

 ### 4.5 Achados do projeto
 
Com base nos testes realizados chegou-se em uma relação de recomendações, que são apresentadas neste segundo relatório, as quais são direcionadas em parte à SAR, mas que incluem sugestões que poderiam ser apresentadas a outros setores da ANAC, devido a características de maior abrangência de recursos envolvidos para sua viabilização.

### 4.6 Conclusão do projeto

O presente relatório conclui que já é possível a adoção de soluções isoladas que já contribuiram para a melhoria da gestão de objetivos de normativos na SAR, porém, a adoção completa do que inicialmente foi idealizado, dependerá de avaliação da possibilidade de aproveitamento em esforço em um outro escopo, que alcance uma maior abrangência.


## 5. Síntese do estudo inicial

Com o intuito de aprimorar a atuação da Superintendência de Aeronavegabilidade - SAR foram identificados projetos setoriais entre suas áreas meio e finalísticas. Dentre os projetos escolhidos para o biênio 2020/2021 tem-se o Projeto em epígrafe, iniciado em 13.08.2020.

Este projeto foi idealizado pela Gerência Técnica de Normas e Inovação - GTNI, visando impactar positivamente toda a SAR, principalmente no que concerne à facilitação do processo interpretativo da regulação da aeronavegabilidade, ou seja, as regras sob a competência da superintendência relacionadas a: regulamentação, fiscalização, verificação do cumprimento de requisitos e aplicação de sanções em primeira instância.

Como estratégia de ação o projeto foi iniciado por uma etapa de tomada de subsídios junto a servidores e gestores da SAR, proporcionando ampliar e confirmar a percepção dos problemas existentes e, consequentemente, as possibilidades de melhorias.

O resultado alcançado pelo estudo recomendou a aplicação de um conjunto de soluções, divididas entre: melhorias de processos, criação de novas rotinas de gestão de informações e adoção de ferramentas de Tecnologia de Informação - TI.

A Figura 1 apresenta uma esquematização do resultado inicialmente idealizado com o projeto. A qual indica que o processo de discussão e interpretação dos objetivos dos requisitos de aeronavegabilidade passaria a contar com uma estrutura de dados e informações de maneira organizada e com interfaces com o público interno e externo à SAR.

Figura 1 - Sistema teórico proposto

![](https://i.imgur.com/HdgF4bK.jpg)

Transição de **modelo conceitual** para **fluxo de trabalho**

![](https://i.imgur.com/FpvVdcq.png)



> COMENTÁRIO: 
> Precisamos fazer um avanço nesse modelo, separando: 
>  1) a estrutura para montar uma **base com todos os dados**;
> 2) o **versionamento** das bases disponibilizadas pela ANAC utilizando GIT;
> 2) as **ferramentas de consulta** - as ferramentas prévias em cada sistema de origem já permitiam a consulta em cada base, mas não de forma transversal. 
>
> - Ajustamos as bases da ANAC para simplificar o acesso (104 bases de normas integradas por meio de tags automatizadas). Necessário produzir e divulgar novas bases de dados tendo como referência os processos da SAR. Possibilidade de usar MS-Forms ao final do processo ou algum artefato dentro de cada processo para coletar dados estruturados. Possibilidade de usar IA para marcação de texto automatizado usando vocabulários controlados.
> - Realizamos a implementação do controle de versão utilizando GIT, o que permite acessar diversas versões dos conjuntos de dados (voltar no tempo e comparar as mudanças no conjunto de dados)
> - Testamos e implementamos ferramentas de consultas transversais (ferramentas de diversos tipos: Meilisearch, Datasette-lite SQL e full-text-search, JS-observable, Jupyter-notebook, Flat-data Data Viewer).
>
> Os sistemas que abordamos e estão completamente implementados já fazem as consultas transversais. Essas consultas podem ainda contar com um modelo de GRAFOS, caso a ANAC opte por camihar na adoção dessa boa prática. Destaca-se que os sistemas por tabelas relacionais apresentam complexidades e limitações, dado o esforço de aprendizado das linguagens de consulta, como SQL (Datasette fornece essa interface para todas as bases da ANAC).


> Sistemas de **busca acadêmica** foram pesquisados e disponibilizados conforme relatório 1. Reapresentar as ferramentas com comentários. Essas ferramentas podem aparecer como links ou quadros nas plataformas de integração (MkDocs e WikiANAC)


Fonte: Esquematizada pelo GT

Para acessar a íntegra do estudo inicial, vide Documento SEI no. 5547230.

## 6. 

### 6.1 


## 6. Testes realizados

### 6.1 Busca e relacionamento de bases de dados por grafos

a.	Desenvolvimento de protótipo em Kumu e identificada relação entre capacidades do ElasticSearch contratado pela ANAC frente opções focadas em grafos disponibilizadas no mercado, tendo por base o case do Neo4j.

## 7. Entregas concluídas

### 7.1 Fórum Discourse 

a.	Disponibilizada ferramenta Discourse para uso como ambiente de troca de conhecimento, inicialmente interno à SAR para desenvolvimento de interpretações, compartilhamento de respostas SEAM e registro de discussões técnicas que possam ser reaproveitadas.

b.	Após amadurecimento do uso da ferramenta, a SAR terá oportunidade de avaliar a possiblidade de abertura de seu uso para também aproveitar conhecimento de público externo, com o devido envolvimento da Ouvidoria da ANAC.

### 7.2 Mecanismo de busca, por relacionamento de tabelas de dados – FlatData + Mkdocs (SAR Doc)

a.	Disponibilizado ambiente para busca de dados, com base em listas oriundas de publicações em dados abertos, acrescidas de tabelas incluídas manualmente, tendo por característica essa segunda modalidade, seu uso apenas para controle interno de atualizações de normativos.

### 7.3 Formulário de cadastro de publicação de normativos

### 7.4 Relacionamento de tabelas com FlatData

### 7.5 Atualizaçào de Processo de policy files

a.	Desenvolvida proposta de atualização de procedimento de processamento de interpretações pela SAR com o intuito de dar início a um processo de revisão da prática atual conduzida na SAR.

## 8. Percepção de compatibilidade com soluções já em uso na ANAC

## 9. Desafios

## 10. Recomendações

### 10.1 Laboratório de Gestão de Dados SAR

a.	Recomendação de institucionalização pela SAR de frente de estudo e desenvolvimento de soluções focadas em gestão de dados, de forma a dar continuidade aos achados do projeto setorial.

### 10.2 Padronização de quadros comparativos

a.	Proposta de padronização de templates para facilitar a visualização e localização de quadros comparativos utilizados no desenvolvimento de normativos.

### 10.3 Avaliação de estratégia de gestão de dados sobre pqs e sarps

a.	Feita extração para carregamento em FlatData como exemplo de possibilidade de relacionamento de dados com demais listagens de documentos.
xxx

### 10.4 Recomendação de classificação de dados à ASTEC e Biblioteca da ANAC (SAF)

xxx

### 10.5 Publicação de consultas setorial e pública por meio de dados abertos

a.	Solicitação à ASTEC para publicação de dados abertos das consultas públicas e setoriais, além das demais modalidades de participação social.


## Conclusões

Após dois anos de dedicação ao tema ....


Situação atual:

![](https://i.imgur.com/FfxCiFJ.png)


Recursos: 
- 108 tabelas em JSON fornecidas em dados abertos da ANAC
- 02 regras de correção de dados usando substituição de strings
- 02 estruturas de padrões em Regex
- 02 tabelas de vocabulários controlados
- 01 script em python, descrito e comentado usando Jupyter Notebook para facilitar reutilização

### Ferramentas para produção de dados

- [Data curator](https://frictionlessdata.io/blog/2019/03/01/datacurator/)

### Ferramentas de consulta de dados

Datasette rodando no navegador usando WebAssembly e Pyodide

1. lite.datasette.io
2. ferramenta 2


## Ferramentas entregues

### Ferramentas para produção de dados

- [Data curator](https://frictionlessdata.io/blog/2019/03/01/datacurator/)

### Ferramentas de consulta de dados

Datasette rodando no navegador usando WebAssembly e Pyodide

1. lite.datasette.io
2. ferramenta 2


## Referências para publicação e qualidade de dados

- [theodi.org](https://theodi.org/)



## Exemplo de política de produção e governança de dados

1.3.1. Pesquisa de conjunto de dados
A primeira função principal da Open Energy - Open Energy Search - permite a pesquisa e descoberta de conjuntos de dados. O Open Energy Search capacita os usuários a descobrir quais conjuntos de dados existem e quem os possui/controla. Os resultados da pesquisa também descrevem a classe de confidencialidade , as regras de acesso e as concessões de recursos associado a um determinado conjunto de dados, o que significa que os detalhes de acesso e licenciamento são transparentes. Isso funciona por meio de um mecanismo de pesquisa projetado especificamente para pesquisar conjuntos de dados, com opções de pesquisa por diferentes parâmetros para refinar os resultados. Também pode ser usado para descobrir conjuntos de dados adjacentes a pesquisas; ajudando os usuários a construir uma imagem mais completa do cenário de dados de energia em sua esfera de interesse. A pesquisa Open Energy é gratuita, está disponível para todos e continuará assim. Os caminhos de acesso aos dados abertos e compartilhados são descritos na seção a seguir.

Conjuntos de dados fornecidos por membros da Open Energy ( Data Providers ) e não membros da Open Energy (por exemplo, dados abertos da web) podem ser visíveis no Open Energy Search. Os conjuntos de dados fornecidos por um membro da Open Energy serão demarcados com um visto verde para indicar que a proveniência do conjunto de dados foi verificada, o tempo de atividade é monitorado, o formato da documentação é conhecido e os usuários têm um mecanismo para fornecer feedback sobre o conjunto de dados se forem detectados problemas . (Observe que isso não indica que a Open Energy realizou verificações adicionais e mais extensas sobre a qualidade dos dados nos conjuntos de dados dos membros.)

1.3.2. Serviço de Governança
A segunda função principal da Open Energy - nosso Serviço de Governança ( OEGS ) - oferece suporte aos membros para fornecer, compartilhar e acessar diferentes classes de dados compartilhados (consulte Classes de sensibilidade de dados ) com base no licenciamento preemptivo (consulte Licenciamento de dados ). Os Dados Compartilhados acessados via OEGS serão fornecidos apenas por membros ( Provedores de Dados). O Serviço de Governança visa fornecer um mecanismo seguro e confiável para melhorar o compartilhamento de dados em todo o setor, reduzindo o tempo e os custos financeiros atualmente associados ao acesso a dados compartilhados. Para provedores de dados compartilhados, o Serviço de Governança oferece uma maneira segura e eficaz de listar conjuntos de dados e definir requisitos apropriados de acesso e licenciamento. Para os atores que desejam acessar dados compartilhados, o Serviço de Governança fornece um mecanismo para reduzir o atrito e a negociação bilateral de contratos, mesmo ao solicitar acesso a vários conjuntos de dados de diferentes provedores.

1.4. Quais dados podem ser encontrados e usados ​​por meio da Open Energy?
O Open Energy oferece suporte a conjuntos de dados abertos e compartilhados contendo dados de energia e relacionados a energia. Diferentes classes de dados dentro do ecossistema Open Energy, avaliadas por seus níveis de sensibilidade, são descritas em Classes de sensibilidade de dados .

1.4.1. Dados abertos
Dados abertos são definidos no ecossistema Open Energy como: 'Dados que qualquer pessoa pode usar, para qualquer finalidade, gratuitamente e acessível sob uma licença de dados abertos'. Exemplos de conjuntos de dados abertos incluem (não exaustivos): dados Lower Super Output Layer ID ( LSOA ), Digest of UK Energy Statistics e dados OpenStreetMap.

Os dados abertos são visíveis através do Open Energy Search, que é gratuito e aberto a todos os usuários. Conjuntos de dados abertos fornecidos por membros da Open Energy ( Data Providers ) e não membros da Open Energy estarão visíveis. Não há barreiras para acessar os dados abertos depois de descobertos - os usuários são direcionados para uma URL ou API apropriada para acessar os dados por conta própria. O acesso a dados abertos não é moderado por meio do OEGS , pois não são necessários controles de acesso adicionais.

1.4.2. Dados compartilhados
Dados compartilhados são definidos no ecossistema Open Energy como: 'Dados que não são abertos nem fechados, mas podem ser compartilhados sob termos e condições específicos.' Exemplos de conjuntos de dados atualmente licenciados como dados compartilhados incluem (não exaustivo): capacidade de subestação primária, dados de interrupção de rede, previsões meteorológicas, dados da agência espacial europeia, instalações diárias de medidores inteligentes Electralink, determinadas informações de geolocalização para ativos de energia e tipologias de construção. Conforme ilustrado nesses exemplos, os dados compartilhados são extremamente diversos e podem incluir conjuntos de dados com diversos níveis de sensibilidade comercial, pessoal e de segurança. Para fornecer nuances nessa área, as consultas da Open Energy estabeleceram um conjunto de cinco classes de sensibilidade de dados, nas quais três classes descrevem categorias separadas de dados compartilhados.

Devido à grande diversidade de tipos de dados no setor de energia, a Open Energy teve que limitar o foco para o desenvolvimento da Fase 3. Atualmente, o OEGS pode facilitar o compartilhamento de classes de dados compartilhados não pessoais apenas. Isso significa que, atualmente, o compartilhamento de dados pessoais não agregados (incluindo conjuntos de dados usando formas de anonimização diferentes da agregação em conformidade com as melhores práticas da ICO / ONS ) não é permitido no ecossistema Open Energy. A funcionalidade de compartilhamento de dados pessoais (classe OE-SP ), e dados que foram anonimizados usando outras técnicas que não a agregação, podem ser extensíveis no futuro, sujeitas a consulta adicional.

Os metadados e a classe de sensibilidade dos conjuntos de dados compartilhados são listados no Open Energy Search e são visíveis para qualquer usuário. Os conjuntos de dados compartilhados fornecidos por membros da Open Energy ( Data Providers ) e não membros da Open Energy são visíveis (onde os últimos são conhecidos), conforme descrito mais adiante nesta seção. O acesso a conjuntos de dados compartilhados fornecidos por membros da Open Energy é moderado por meio do Open Energy Governance Service, com base no licenciamento preventivo. O acesso aos dados compartilhados listados na Pesquisa que não são fornecidos por um membro da Open Energy não é suportado - os usuários devem entrar em contato diretamente com a organização não membro para providenciar o acesso.

1.4.3. Dados fechados
Dados fechados são definidos no ecossistema Open Energy como: 'Dados que não podem ser compartilhados ou requerem uma licença personalizada por uso, negociada caso a caso'. Sob nosso modelo atual, os dados fechados nunca são adequados para serem compartilhados no ecossistema Open Energy e não são visíveis por meio do Open Energy Search. Embora reconheçamos o feedback da indústria sinalizando o valor potencial no uso da infraestrutura Open Energy para compartilhar dados fechados de forma privada não listados na Pesquisa ou no diretório OEGS , este não é um foco de desenvolvimento do projeto na fase atual. Qualquer extensibilidade desta função no futuro estará sujeita a consulta.

1.5. Qual o papel da sua organização no ecossistema Open Energy?
Os membros do ecossistema Open Energy têm diferentes funções: Provedores de Dados , Consumidores de Dados ou ambos. Esta seção descreve o significado das diferentes funções e descreve suas responsabilidades básicas.

1.5.1. Provedores de dados
Os Provedores de Dados são organizações que controlam conjuntos de dados que desejam tornar visíveis e/ou acessíveis por meio do ecossistema Open Energy. Os Provedores de Dados podem fornecer conjuntos de dados Abertos e/ou Compartilhados. Os Provedores de Dados são responsáveis ​​por: classificação de sensibilidade de dados, criação de regras de acesso, criação de concessões de capacidade, provisão de dados, integridade e correção de dados, provisão de metadados e disponibilidade de API , estabilidade e gerenciamento de mudanças. A orientação completa sobre as responsabilidades do Provedor de Dados pode ser encontrada em Orientação para Provedores de Dados .

1.5.2. Consumidores de dados
Consumidores de dados são organizações que buscam encontrar e acessar conjuntos de dados por meio do Serviço de Serviço de Governança de Energia Aberta. Os consumidores de dados podem ser estabelecidos para atender às necessidades organizacionais internas, para atender clientes externos ou ambos. Consumidores de dados é um termo genérico que se refere a todas as partes que acessam dados por meio do OEGS . A orientação completa pode ser encontrada em Orientação para consumidores de dados

1.5.2.1. Provedores de serviço
Os Consumidores de Dados que acessam dados para atender clientes externos, incluindo potencialmente clientes fora do ecossistema Open Energy, são categorizados como um tipo específico de Consumidor de Dados chamado Provedor de Serviços . Consulte Consumidor de dados versus provedor de serviços .

1.5.3. Papéis duplos
As organizações que desejam fornecer e acessar dados por meio do ecossistema Open Energy podem fazê-lo, desde que cumpram as responsabilidades de ambas as funções. Os Provedores de Dados que não desejam se registrar como Consumidores de Dados , mas que desejam acessar conjuntos de dados de Energia Aberta, podem fazê-lo usando os serviços de um Provedor de Serviços (um tipo de Consumidor de Dados no ecossistema de Energia Aberta que presta serviços a clientes , potencialmente incluindo não membros da Open Energy).

1.6. Como o acesso e o licenciamento de conjuntos de dados operam em Open Energy?
A Open Energy consultou publicamente e com a indústria sobre políticas relacionadas a: os tipos de condições em que os controles de acesso a dados podem ser baseados, o processo pelo qual os Provedores de Dados estabelecem regras de acesso para um conjunto de dados e o modelo para associar regras de acesso à concessão de capacidades e obrigações particulares (modelo de licenciamento). Essas políticas são resumidas abaixo e detalhadas na Seção 3 das Diretrizes Operacionais.

1.6.1. Tipos de Condições de Acesso
A Open Energy estabeleceu um conjunto de condições que podem ser especificadas para que os Consumidores de Dados atendam para obter acesso a conjuntos de dados em diferentes classes de sensibilidade. Isso inclui, mas não se limita a: pagamento, conformidade de segurança, conformidade regulatória, conformidade com padrões, acesso baseado em grupo e acesso baseado em casos de uso.

1.6.2. Criando Regras de Acesso (Introdução)
Para operacionalizar as condições de Acesso a Dados acima, propomos um sistema pelo qual as concessões de acesso são determinadas, para cada solicitação à API de um Provedor de Dados , com base em um conjunto de regras definidas e publicadas por esse Provedor de Dados nos metadados do conjunto de dados.

1.6.3. Licenciamento de dados (Introdução)
Uma licença de dados é um instrumento legal que define o que um consumidor de dados pode fazer com um artefato específico (por exemplo, conjunto de dados). Isso concede certas 'capacidades' ao consumidor de dados , incluindo uma expressão clara das coisas que eles podem fazer com o artefato. As concessões de capacidade são acompanhadas de quaisquer obrigações que o Consumidor de Dados deve cumprir ao exercer uma capacidade. Os recursos e obrigações associados a cada chamada de API serão convertidos em uma licença por meio do Open Energy Governance Service ( OEGS ).

A Open Energy opera por meio de uma série de concessões e obrigações de capacidade padronizadas. A padronização inclui texto legal, texto 'legível por humanos' e notação de resumo. Os Provedores de Dados devem especificar quais recursos e obrigações estão associados a cada regra de acesso e publicá-los de forma transparente nos metadados do conjunto de dados.

[...]

2.2. Considerações para provedores de dados

Criação de arquivo de metadados (https://docs.openenergy.org.uk/1.0.0/ops_guidelines/before_starting.html)

Aplica-se a todos os conjuntos de dados, dados abertos e dados compartilhados :

[Arquivo de metadados](https://docs.openenergy.org.uk/1.0.0/ops_guidelines/common_policies.html#metadata) criado para cada conjunto de dados

Arquivo de metadados publicado e disponível em um servidor web público (como o [repositório GitHub público](https://github.com/icebreakerone/open-energy-metadata-demo/tree/main/metadata_files) )

Registros do local do arquivo de metadados criado ( [instruções](https://docs.google.com/document/d/1sypYWTeLFSFyfO_zTW6xKCWnao9gKjAo2JHZZIPs2xI/edit?usp=sharing) )

Verificação de que os processos automatizados da Open Energy selecionaram o arquivo e exibiram o conteúdo na Pesquisa

Técnico



Criação de uma regra, ou regras, para cada conjunto de dados e publicação de regra(s) no arquivo de metadados

Conjunto de dados atribuído a uma classe de sensibilidade de energia aberta

Regra ou regras de acesso criadas, para cada uma das quais:

As condições de acesso a dados são especificadas

Uma concessão de Capacidades é articulada

Quaisquer Obrigações que acompanham são articuladas

Operacional, comercial, técnico


METADADOS DO CONJUNTO DE DADOS

https://docs.openenergy.org.uk/1.0.0/metadata.html#data-set-metadata

## Perguntas para teste com usuários

![](https://i.imgur.com/oF1hwhM.png)

- Testes com usuários: Mentimeeter, Slido

## Etapas do processo de inovação

![](https://i.imgur.com/yfgbgT7.png)


## Referências


[^enap]: ENAP. Fundação Escola Nacional de Administração Pública. Módulo 4: Gerenciamento de Metadados e da qualidade de Dados. *In*: **Curso: Governança de Dados**. Conteudistas: BARBOSA, Wellington Luiz; LYRA, Roberto Shayer. Disponível em: https://repositorio.enap.gov.br/bitstream/1/5008/4/M%C3%B3dulo%204%20-%20Gerenciamento%20de%20Metadados%20e%20da%20qualidade%20de%20Dados.pdf. Acesso em: 16/09/2022.


[^redhat]: RED HAT. Red Hat Process Automation Manager. **Designing and building cases for case management. Chapter 1. Case management**. Disponível em: https://access.redhat.com/documentation/en-us/red_hat_process_automation_manager/7.3/html/designing_and_building_cases_for_case_management/case-management-overview-con. Acesso em: 12/09/2022. (Tradução livre)

[^visual]: VISUAL PARADIGM. What is Case Management Model and Notation (CMMN). Disponível em: https://www.visual-paradigm.com/guide/cmmn/what-is-cmmn/. Acesso em: 12/09/2022. (Tradução livre)


## Consultas acadêmicas

![](https://i.imgur.com/BJOnoZP.png)

---
title: Relatório Projeto Setorial
authors: 
tags: projeto, anac, 2022, metadados 
---



- https://hackmd.io/yaml-metadata
- https://hackmd.io/c/tutorials/%2Fs%2Ffeatures
- https://theodi.org/article/introducing-the-smart-data-innovation-guidebook/
- Referência para padronização de infraestrutura de dados: https://open-data-institute.gitbook.io/draft-in-progress-smart-data-innovation-guidebook/data-infrastructure/standards
- https://www.w3.org/ns/csvw - This document describes the CSVW Namespace Vocabulary Terms and Term definitions used for creating Metadata descriptions for Tabular Data. This document provides the RDFS [RDF-SCHEMA] vocabulary definition for terms defined in [tabular-metadata] and a description of the JSON-LD context definition for use with defining metadata documents.
- LEXML

- Referência para publicação de um documento sobre política envolvendo produção e consumo de dados -  https://docs.openenergy.org.uk/1.0.0/ops_guidelines/introduction.html

![Título da imagem](https://i.imgur.com/RJhkJkL.png)

Relatório Projeto Setorial
===


    Citação de código
    
```
Citação de código
```

`Outra citação de código: inline`

> Outra referência de citação


retirado de 2.1
Assim, com base na identificação do problema se priorizou abordar nessa etapa:

1. Prototipação de Base de dados + Busca + interfaces.

3. Levantamento e padronização de fontes de dados - Projeto piloto (GTNI).
4. 
5. Implementação de fórum com integração das informações do SEAM (desejável).
6. 
7. Interface eletrônica para a promoção de busca a material acadêmico.

9. Repositório de discussões técnicas (informais).

11. Proposta de evolução do processo de Policy File.


## Lista de serviços possíveis

*ideia sobre "cardápio de soluções". Vincular com estrutura de segundo modelo, mapeamento do processo*

## Conclusão
Aproveitar essas ideias:

o que foi pensado
o que foi feito
o que deu certo
o que não deu certo e o porque
resgatar parte final do outro relatório