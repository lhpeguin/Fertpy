# Fertpy

**Languages:** 🇺🇸 [English](README.md) | 🇧🇷 Português (Brasil)

**Fertpy** é um motor de cálculo agronômico orientado a domínio e baseado em regras para correção de solo e cálculo de doses de nutrientes.

Ele fornece uma estrutura computacional para transformar boletins técnicos agronômicos em modelos determinísticos executáveis, utilizando definições de regras estruturadas em YAML.

O Fertpy não fornece recomendações agronômicas ou consultoria profissional.  
Ele realiza cálculos reprodutíveis com base estrita em critérios técnicos previamente definidos.

---

## Visão Geral

O Fertpy foi projetado para:

- Representar boletins técnicos agronômicos como modelos computacionais estruturados
- Executar cálculos determinísticos de correção de solo e doses de nutrientes
- Separar lógica de domínio da infraestrutura e da representação do conhecimento
- Permitir cálculos agronômicos transparentes e rastreáveis

O projeto segue uma separação clara de responsabilidades:

- `core/` → Entidades de domínio e motor de cálculo  
- `infra/` → Camada de carregamento e parsing de YAML  
- `nutrientes/` → Interfaces de cálculo específicas por nutriente  
- `correcao_solo/` → Modelos de correção do solo  
- `knowledge/` → Definições estruturadas do conhecimento agronômico  

---

## Escopo

Os modelos de conhecimento atualmente implementados são derivados de boletins técnicos agronômicos brasileiros.

Embora o motor de cálculo seja independente de framework e contexto regional, os artefatos de conhecimento implementados são, neste momento, válidos principalmente para o contexto agronômico brasileiro.

Extensões futuras poderão incluir parametrizações regionais e integração com novas fontes técnicas.

---

## Princípios de Projeto

- Domain-Driven Design (DDD)
- Modelagem determinística baseada em regras
- YAML como camada de representação do conhecimento
- Arquitetura híbrida:
  - Modelos baseados em regras N-dimensionais
  - Modelos baseados em fórmulas algébricas fixas (ex.: calagem)
- Separação rigorosa entre motor de cálculo e critérios agronômicos
- Extensibilidade para novas culturas e boletins técnicos
- Rastreabilidade das fontes técnicas
- Reprodutibilidade determinística dos resultados

---

## Instalação

### Requisitos

- Python >= 3.11
- pip

---

### 1. Clonar o repositório

```bash
git clone https://github.com/lhpeguin/fertpy.git
cd fertpy
```

### 2. Criar e ativar um ambiente virtual

```bash
python -m venv venv
# Linux / macOS:
source venv/bin/activate  
# Windows: 
venv\Scripts\activate
```

---

### 3. Instalar as dependências

Se estiver utilizando instalação editável:

```bash
pip install -e .
```

Ou, utilizando o arquivo requirements:

```bash
pip install -r requirements.txt
```

---

## Exemplo de Uso

```python
from fertpy import Calagem, Nitrogenio, Fosforo, Potassio


# Correção do solo (cálculo de calagem)
c = Calagem("milho")
NC = c.calcular(v_atual=40, ctc=70)


# Cálculo de dose de Nitrogênio
n = Nitrogenio("milho", "graos")
n_total = n.calcular("alto", 5.9)


# Cálculo de dose de Fósforo
p = Fosforo("milho", "graos")
p_total = p.calcular(16, 5)


# Cálculo de dose de Potássio
k = Potassio("milho", "graos")
k_total = k.calcular(3.8, 11)


print(f"Necessidade de calagem: {NC} t/ha")


def print_result(r):
    print(
        f"\nNutriente: {r.nutriente}\n"
        f"Dose: {r.dose} {r.unidade}\n"
        f"Classe: {r.classe.nome}\n"
        f"Observações: {r.observacoes or 'Nenhuma'}\n"
        f"Fonte: {r.fonte['documento']} "
        f"({r.fonte['instituicao']}, {r.fonte['ano']})\n"
    )


print_result(n_total)
print_result(p_total)
print_result(k_total)
```

---

## Representação do Conhecimento

Os critérios agronômicos são definidos como arquivos YAML estruturados localizados em:

```text
knowledge/
```

Cada arquivo codifica regras técnicas derivadas de boletins agronômicos.

Essa arquitetura permite:

- Rastreabilidade clara dos parâmetros de cálculo
- Separação entre dados e lógica de execução
- Saídas determinísticas e reprodutíveis
- Extensão simplificada para novas culturas e regiões

---

## Status do Projeto

**Versão Atual:** v0.1.0 — Lançamento Público Inicial

O Fertpy está em desenvolvimento ativo.

### Escopo Implementado

- Suporte à cultura do milho
- Cálculo de correção do solo (calagem)
- Cálculo de doses de Nitrogênio (N), Fósforo (P) e Potássio (K)
- Fonte técnica única por nutriente
- Modelagem do conhecimento agronômico baseada em YAML

### Destaques da Arquitetura e do Motor

- Separação clara entre motor de cálculo e critérios agronômicos
- Avaliação determinística de regras (o motor executa a lógica, mas não define regras agronômicas)
- Estrutura orientada a domínio (DDD)
- Parsing em camada de infraestrutura para normalização de intervalos e condições
- Modelagem explícita de intervalos via objeto de valor dedicado
- Avaliação de regras N-dimensionais (sem número fixo de variáveis de decisão)
- Representação declarativa do conhecimento

### Limitações Atuais

- Suporte a uma única cultura (milho)
- Fonte técnica única por nutriente
- Um único método analítico por nutriente
- Contexto técnico agronômico brasileiro
- Sem agregação de múltiplas fontes
- Lógica estritamente determinística (sem modelagem probabilística)

---

## Roadmap

O desenvolvimento do Fertpy está estruturado em fases evolutivas, com foco em consolidação arquitetural, expansão agronômica e robustez técnica.

---

### Fase 1 — Fundação do Motor (Concluída)

Corresponde à versão **v0.1.0 — Lançamento Público Inicial**.

Esta fase estabeleceu o núcleo determinístico de cálculo agronômico do Fertpy.

---

#### Implementado

- Motor determinístico de cálculo agronômico
- Arquitetura híbrida:
  - Modelos baseados em regras N-dimensionais
  - Modelos baseados em fórmulas algébricas (ex.: calagem)
- Parsing estruturado de intervalos e condições
- Separação clara entre:
  - Motor de cálculo
  - Representação do conhecimento (YAML)
- Correção de solo (calagem)
- Macronutrientes primários:
  - Nitrogênio (N)
  - Fósforo (P)
  - Potássio (K)
- Estrutura inicial de rastreabilidade de fontes técnicas

A Fase 1 consolida o Fertpy como uma representação computacional declarativa e determinística de boletins agronômicos.

---

### Fase 2 — Expansão do Escopo Agronômico

**Foco:** ampliação funcional e consolidação operacional.

---

#### 1. Parametrização Explícita de Entradas

Criação de:

```text
fertpy/utils/parametros.py
```

Objetivos:

- Declarar explicitamente parâmetros válidos por cultura e nutriente
- Melhorar validação de entradas
- Tornar a API pública mais segura e autoexplicativa

---

#### 2. Expansão de Culturas

Inclusão de culturas como:

- Soja
- Feijão
- Algodão
- Trigo
- Sorgo

---

#### 3. Expansão do Escopo Nutricional

Nutrientes atualmente implementados:

- Nitrogênio (N)
- Fósforo (P)
- Potássio (K)

Expansão planejada:

- Macronutrientes secundários
- Micronutrientes

Meta: 14 nutrientes modelados.

---

#### 4. Fontes de Fertilizantes Inorgânicos

Modelagem de diferentes fontes fertilizantes
Associação entre doses calculadas e fontes disponíveis

**Importante:**

O Fertpy não realizará bloqueio automático de combinações incompatíveis de fertilizantes.
A compatibilidade química permanece sob responsabilidade do profissional técnico habilitado.

O sistema poderá emitir alertas informativos com base em boletins técnicos, mas não aplicará restrições automáticas.

---

#### 5. Melhoria no Tratamento de Erros

- Mensagens de erro mais claras e estruturadas
- Diferenciação entre:
  - Erros estruturais
  - Erros de validação
  - Alertas técnicos

---

### Fase 3 — Consolidação Técnica e Expansão Estrutural

Foco: robustez, explicabilidade e rastreabilidade completa.

---

#### 1. Suporte a Culturas Perenes

- Inclusão de culturas perenes
- Ajustes estruturais para ciclos plurianuais
- Parametrização por estágios fenológicos
- Adequação da lógica de recomendação para sistemas perenes

---

#### 2. Normalização de Entradas

Estrutura proposta:

```text
fertpy/normalizacao/base.py
fertpy/normalizacao/unidade.py
```

Objetivos:

- Conversão automática de unidades
- Consistência dimensional
- Redução de erros operacionais
- Padronização interna das unidades de cálculo

---

#### 3. Validação Dimensional

O sistema implementará validação dimensional e agronômica das entradas, garantindo coerência física, matemática e técnica antes da execução das regras.

Essa camada tem como objetivo prevenir inconsistências operacionais e interpretações incorretas de dados analíticos.

Exemplos:

- CTC informada em unidade incorreta → erro crítico
- pH fora de intervalo agronomicamente plausível → alerta técnico
- Saturação por bases > 100% → erro crítico
- Valores negativos para atributos químicos → erro crítico
- Incompatibilidade entre unidade informada e método analítico → erro

O sistema diferenciará explicitamente:

- Erros críticos → impedem a execução do cálculo
- Alertas técnicos → permitem execução, mas sinalizam possível inconsistência

Essa distinção preserva o caráter determinístico do motor, mantendo ao mesmo tempo rigor técnico e responsabilidade do usuário.

---

#### 4. Metadados de Cálculo e Rastreabilidade Completa

```text
fertpy/core/metadata.py
```

Cada objeto de resultado carregará metadados estruturados que descrevem não apenas o valor calculado, mas também o caminho lógico que levou àquela decisão.

Essa camada transforma o resultado em um artefato auditável, permitindo reconstruir exatamente quais critérios técnicos foram aplicados pelo motor.

Os metadados incluirão, entre outros:

- Cultura
- Nutriente
- Boletim técnico de referência
- Arquivo YAML de origem
- Regra ativada
- Condições avaliadas
- Classe interpretativa atribuída
- Intervalo ou faixa acionada
- Método analítico considerado

Isso permitirá:

- Auditoria completa do processo decisório
- Reprodutibilidade técnica verificável
- Transparência na aplicação das regras
- Comparação entre diferentes versões de boletins
- Base para futuras funcionalidades de explicabilidade

O objetivo é que nenhuma recomendação seja um “valor isolado”, mas sim o resultado rastreável de um conjunto explícito de critérios técnicos..

---

#### 5. Rastreamento da Regra Ativada

Capacidade de identificar:

- Qual regra foi acionada
- De qual arquivo YAML
- Em qual seção

Garantindo auditabilidade e transparência técnica.

---

#### 6. Modo Explicativo

Exemplo planejado de uso:

```text
fertpy/core/explain.py
```
```python
explain(resultado) -> str
```

Exemplo de saída:

P = 12 mg/dm³ enquadrado na classe <16 e produtividade esperada de 9, enquadrando-se no intervalo de 8–10, segundo as informações presentes em cultura_finalidade_fosforo.yaml. Dose definida como 100 kg/ha.

Objetivos:

- Tornar o motor auditável
- Facilitar uso acadêmico
- Aumentar transparência técnica
- Apoiar validação científica

---

#### 7. Camada de Validação Semântica

```text
fertpy/validacao/semantica.py
```

Funções previstas:

- Coerência entre CTC e dose
- Verificação da relação Ca/Mg
- Validação de consistência da calagem

Características:

- Apenas geração de alertas
- Nunca bloqueio automático
- Respeito à responsabilidade técnica do usuário

---

#### 8. Sistema Interno de Debug e Rastreamento

```text
fertpy/core/trace.py
```
Objetivo:

- Permitir análise detalhada do fluxo de decisão
- Apoiar pesquisa e validação acadêmica
- Facilitar testes estruturais do motor

---

## Licença

Licenciado sob a Apache License 2.0.
Consulte o arquivo LICENSE para mais detalhes.

---

## Autores

See [AUTHORS.md](AUTHORS.md)

---

## Contribuições

Contribuições são bem-vindas.
Antes de submeter um pull request:

- Mantenha a separação entre domínio e infraestrutura
- Preserve o caráter determinístico da lógica de cálculo
- Garanta que artefatos de conhecimento sejam rastreáveis a fontes técnicas
- Utilize conventional commits

---

## Aviso Legal

O Fertpy realiza cálculos agronômicos determinísticos com base em critérios técnicos estruturados.
Ele não fornece recomendações agronômicas, consultoria profissional ou serviços de tomada de decisão.
Os usuários são responsáveis por interpretar os resultados dentro de seu contexto agronômico, regional e regulatório específico.

---