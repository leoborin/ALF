# ALF

https://github.com/user-attachments/assets/239088c9-8b34-4c88-991a-d51fa6bbc6e7


### **Descrição para o Stakeholder:**

O objetivo deste projeto foi **desenvolver uma ferramenta para identificar com precisão o ponto de fratura do trilho** quando um alarme do equipamento detector de trilho quebrado (DTQ) é ativado. Embora a detecção do trilho quebrado já fosse possível, a localização exata da fratura ainda era um desafio. Com o desenvolvimento de um algoritmo matemático avançado, conseguimos estimar com maior precisão o ponto de fratura, permitindo que a equipe de manutenção direcione suas ações de forma mais eficiente e ágil.

### **Descrição Técnica:**

- **Coleta de Dados:**
    - Os dados dos sensores e registros de alarme são extraídos da **API do Elasticsearch** na **AWS**.
- **Processamento na Aplicação Python:**
    - O usuário seleciona um alarme específico.
- **Análise da Curva de Medição:**
    - Um algoritmo processa os dados da curva de medição do equipamento para identificar o **ponto de quebra**.
    - A identificação da fratura é baseada na relação **tempo x espaço**.
- **Critérios para Detecção da Quebra:**
    - O coeficiente de inclinação da reta. Definição dos momentos entre passagens de trem, Quando está linear, não temos trem na secção, quando está ascendente ou descente, sabemos que temos passagem de Trem.
    - Os ângulos formados entre três pontos consecutivos na curva. Quando temos uma angulação no meio da reta de descida ou subida, esse ponto de quebra é o ponto de fratura. Relacionando com tempo e espaço temos o ponto estimado de fratura.
 
      ![image](https://github.com/user-attachments/assets/8429a216-4c35-4e34-ac76-ceeec599decd)

- **Visualização:**
    - A aplicação gera um gráfico destacando o ponto de fratura e sua aproximação.

> Mais informações disponíveis no repositório do Git.
> 

### **Resultados e Ganhos:**

- Redução de 60% no tempo de atuação da equipe em campo.
- A diferença média na identificação do ponto de fratura em relação ao ponto estimado foi de **350 metros**. É importante destacar que, antes da implementação desse método, a distância percorrida para localizar a falha era, em média, **6 km**, demonstrando um avanço significativo na eficiência da detecção.

- 
