![Python](https://img.shields.io/badge/python-3.11-blue)
![Tests](https://img.shields.io/badge/tests-pytest-green)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-Apache%202.0-lightgrey)
[![PyPI version](https://img.shields.io/pypi/v/fertpy.svg)](https://pypi.org/project/fertpy/)

# Fertpy

**Languages:** 🇺🇸 [English](README.md) | 🇧🇷 Português (Brasil)

**Fertpy** é um motor de cálculo agronômico orientado a domínio e baseado em regras para correção de solo e cálculo de doses de nutrientes.

Ele fornece uma estrutura computacional para transformar boletins técnicos agronômicos em modelos determinísticos executáveis, utilizando definições de regras estruturadas em YAML.

O Fertpy não fornece recomendações agronômicas ou consultoria profissional.  
Ele realiza cálculos reprodutíveis com base estrita em critérios técnicos previamente definidos.

---

## Visão Geral

O **Fertpy** é uma biblioteca para modelagem e cálculo agronômico, projetada para transformar boletins técnicos em **modelos computacionais estruturados, reprodutíveis e rastreáveis**.

A biblioteca permite:

- Representar recomendações agronômicas (boletins técnicos) como modelos estruturados
- Executar cálculos determinísticos de:
  - Correção de solo (ex: calagem)
  - Recomendação de nutrientes (N, P₂O₅, K₂O)
  - Formulação de fertilizantes (misturas e fontes comerciais)
- Otimizar formulações com base em:
  - Quantidade mínima de insumos
  - Custo mínimo
- Trabalhar com fontes simples e compostas (ex: NPK comerciais)
- Garantir transparência, rastreabilidade e consistência nos cálculos

---

### Arquitetura

O projeto segue uma arquitetura modular com separação clara de responsabilidades:

#### Núcleo de Domínio

- `core/domain/` → Entidades e regras de negócio (recomendação, fertilizantes, critérios, etc.)
- `core/engine/` → Motor de cálculo agronômico e formulação
- `core/analysis/` → Análises auxiliares (diagnóstico, proporções, nutrientes limitantes)
- `core/factories/` → Criação de objetos de domínio (fertilizantes, corretivos)

---

#### Camada de Aplicação

- `nutrientes/` → Interfaces de cálculo por nutriente (N, P, K)
- `correcao_solo/` → Modelos de correção (ex: calagem)
- `formulacao/` → Interface de formulação de adubação e calagem

---

#### Infraestrutura

- `infra/loaders/` → Carregamento de dados (YAML)
- `infra/parsing/` → Parsing e interpretação de regras agronômicas
- `services/` → Validações e regras auxiliares

---

#### Base de Conhecimento

- `knowledge/` → Definições estruturadas dos boletins agronômicos
  - Regras de recomendação por cultura
  - Fontes de nutrientes e corretivos
  - Parâmetros técnicos versionados

---

#### Interfaces e Ferramentas

- `cli/` → Interface de linha de comando para execução dos cálculos
- `utils/` → Utilitários compartilhados

---

#### Princípios de Projeto

O Fertpy foi construído com base em:

- Separação clara entre domínio, infraestrutura e conhecimento
- Modelagem explícita das regras agronômicas
- Extensibilidade para novas culturas, nutrientes e fontes
- Reprodutibilidade dos cálculos
- Independência de interface (API, CLI, etc.)

---

#### Estrutura do Projeto (resumida)

```text
fertpy/
├── core/           # Domínio e motor de cálculo
├── formulacao/     # Formulação de adubação e calagem
├── nutrientes/     # Cálculo por nutriente
├── correcao_solo/  # Correção do solo
├── infra/          # Carregamento e parsing
├── knowledge/      # Base agronômica (YAML)
├── cli/            # Interface de linha de comando
├── services/       # Validações
└── utils/          # Utilidades
```

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

### Instalação via PyPi  (recomendado)

Para instalar a versão estável publicada:

```bash
pip install fertpy
```

Para verificar a instalação:

```bash
python -c "import fertpy; print(fertpy.__version__)"
```

---

### Instalação para Desenvolvimento

Caso queira contribuir ou modificar o projeto:

#### 1. Clonar o repositório

```bash
git clone https://github.com/lhpeguin/fertpy.git
cd fertpy
```

#### 2. Criar e ativar um ambiente virtual

```bash
python -m venv venv
# Linux / macOS:
source venv/bin/activate  
# Windows: 
venv\Scripts\activate
```

---

#### 3. Instalar as dependências

Instalação padrão (uso da biblioteca)

```bash
pip install -e .
```

Instalação para desenvolvimento (com testes)

```bash
pip install -e .[dev]
```

Instala também as dependências de desenvolvimento, incluindo 'pytest', necessárias para executar a suíte de testes.

---

## Validação e Testes

O Fertpy possui uma suíte de testes automatizados implementada com `pytest`, garantindo a consistência determinística dos modelos agronômicos e dos algoritmos de formulação.

---

### Cobertura dos testes

Os testes contemplam:

- Cálculo de correção do solo (Calagem)
- Cálculo de Nitrogênio (N)
- Cálculo de Fósforo (P)
- Cálculo de Potássio (K)
- Formulação de adubação em múltiplos cenários
- Formulação de calagem com diferentes fontes
- Cálculo de nutrientes fornecidos pelas combinações
- Recomendações baseadas em combinação de fontes
- Tratamento de erros e validações de entrada
- Casos limite e cenários de validação
- Estabilidade na leitura e interpretação dos artefatos YAML

### Objetivos da suíte

A suíte de testes atua como mecanismo de:

- Prevenção de regressões
- Verificação da integridade arquitetural
- Garantia de reprodutibilidade científica dos cálculos
- Validação cruzada entre regras agronômicas e dados declarativos (YAML)

---

### Executando os testes

Após instalar as dependências do projeto:

```bash
pytest
```

Ou alternativamente:

```bash
python -m pytest
```

Todos os testes devem ser executados com sucesso antes da submissão de alterações estruturais ou expansão da base de conhecimento.

---

## Exemplo de Uso

Este exemplo demonstra o fluxo completo de uso do fertpy, incluindo:

- Cálculo agronômico (calagem + macronutrientes)
- Geração da demanda nutricional
- Formulação de adubação com:
  - Fontes simples (mistura na propriedade)
  - Fontes compostas (NPK comerciais)
  - Estratégia de plantio e cobertura

---

### 1. Cálculo Agronômico

```python
from fertpy import Calagem, Nitrogenio, Fosforo, Potassio


# Calagem
calagem = Calagem("milho")
resultado_calagem = calagem.calcular(v_atual=55, ctc=70)

print(f"\nNecessidade de calagem: {resultado_calagem['dose']} t/ha\n")


# Macronutrientes primários
n = Nitrogenio("milho", "graos")
p = Fosforo("milho", "graos")
k = Potassio("milho", "graos")

n_resultado = n.calcular("media_baixa", 12.1)
p_resultado = p.calcular(26, 12.1)
k_resultado = k.calcular(3, 12.1)


def imprimir_calculo_nutrientes(r):
    print(
        f"Nutriente: {r.nutriente}\n"
        f"Dose: {r.dose} {r.unidade}\n"
        f"Classe: {r.classe.nome}\n"
        f"Boletim: {r.fonte['documento']} "
        f"({r.fonte['instituicao']}, {r.fonte['ano']})\n"
    )

    if r.fracionamento:
        print("Fracionamento:")
        print(f"  Plantio: {r.fracionamento['plantio']} {r.unidade}")
        print(f"  Cobertura: {r.fracionamento['cobertura']} {r.unidade}\n")


# Impressão
imprimir_calculo_nutrientes(n_resultado)
imprimir_calculo_nutrientes(p_resultado)
imprimir_calculo_nutrientes(k_resultado)
```

---

### 2. Demanda nutricional

A partir das recomendações calculadas, consolidamos a demanda de nutrientes:

```python
recomendacao_n = n_resultado
fracionamento_n = n_resultado.fracionamento

demanda_total = {
    "N": recomendacao_n.dose,
    "P2O5": p_resultado.dose,
    "K2O": k_resultado.dose
}

demanda_plantio = {
    "N": fracionamento_n["plantio"] if fracionamento_n else recomendacao_n.dose,
    "P2O5": p_resultado.dose,
    "K2O": k_resultado.dose
}

demanda_cobertura = {
    "N": fracionamento_n["cobertura"] if fracionamento_n else 0
}
```

---

### 3. Formulação de Adubação

```python
from fertpy import FormulacaoAdubacao


formulador = FormulacaoAdubacao()


def imprimir_formulacao(resultado, titulo):
    print(f"\n=== {titulo} ===\n")

    for fonte, dose in resultado["doses"].items():
        print(f"- {fonte}: {dose:.2f} {resultado['unidade']}")

    if resultado.get("custo_total") is not None:
        print(f"\nCusto total: R$ {resultado['custo_total']:.2f}")
```

---

### 3.1 Fontes Simples (Mistura na Propriedade)

Combinação otimizada de fertilizantes básicos:

```python
resultado_simples = formulador.calcular(
    demanda=demanda_total,
    fontes=["ureia", "map", "kcl"],
    # Preços das fontes (R$/ton)
    precos={
        "ureia": 2500,
        "map": 3200,
        "kcl": 2800
    },
    solver="custo_minimo"
)

imprimir_formulacao(resultado_simples, "Formulação com fontes simples (mistura)")
```

---

### 3.2 Fontes Compostas (NPK Comerciais)

Seleção da melhor formulação comercial com base na demanda:

```python
# Fontes compostas comerciais (NPK)
# Formato: "nome:N=%,P2O5=%,K2O=%"

fontes_npk = [
    "NPK_04_14_08:N=4,P2O5=14,K2O=8",
    "NPK_08_28_16:N=8,P2O5=28,K2O=16",
    "NPK_20_05_20:N=20,P2O5=5,K2O=20",
    "NPK_12_24_20:N=12,P2O5=24,K2O=20"
]

# Preços das fontes (R$/ton)
precos_npk = {
    "NPK_04_14_08": 2500,
    "NPK_08_28_16": 2600,
    "NPK_20_05_20": 3000,
    "NPK_12_24_20": 3000
}

resultado_npk = formulador.calcular(
    demanda=demanda_plantio,
    entradas_fontes=fontes_npk,
    precos=precos_npk,
    solver="custo_minimo",
    modo="fonte_unica",   # seleciona uma única formulação comercial
    tolerancia=0.1        # tolerância de ajuste na demanda (10%)
)

imprimir_formulacao(resultado_npk, "Fonte composta (NPK comercial)")
```

---

### 3.3 Adubação de Plantio e Cobertura

Separação da adubação conforme o manejo:

- **Plantio**: aplicação de N, P e K na semeadura  
- **Cobertura**: aplicação complementar de Nitrogênio ao longo do ciclo  

```python
# Preços das fontes (R$/ton)
precos = {
    "ureia": 2500,
    "map": 3200,
    "kcl": 2800
}

# Adubação de plantio (NPK completo)
resultado_plantio = formulador.calcular(
    demanda=demanda_plantio,
    entradas_fontes=["ureia", "map", "kcl"],
    precos=precos,
    solver="custo_minimo"
)

# Adubação de cobertura (apenas Nitrogênio)
resultado_cobertura = formulador.calcular(
    demanda=demanda_cobertura,
    entradas_fontes=["ureia"],
    precos={"ureia": 2500},
    solver="custo_minimo"
)

imprimir_formulacao(resultado_plantio, "Adubação de Plantio")
imprimir_formulacao(resultado_cobertura, "Adubação de Cobertura")
```

---

### 4. Formulação de Calagem

Seleção otimizada de corretivos de solo com base no custo e na eficiência de neutralização da acidez.

```python
from fertpy import FormulacaoCalagem

formulador = FormulacaoCalagem()

# Preços dos corretivos (R$/ton)
precos = {
    "calcario_agricola": 150,
    "calcario_calcinado": 180
}

resultado = formulador.calcular(
    cultura="milho",
    v_atual=40,
    ctc=10,
    entradas_fontes=["calcario_agricola", "calcario_calcinado"],
    precos=precos,
    solver="custo_minimo"
)


def imprimir_formulacao_calagem(resultado):
    print("\n=== Formulação de Calagem ===\n")

    for fonte, dose in resultado["doses"].items():
        print(f"- {fonte}")
        print(f"  Dose: {dose:.2f} {resultado['unidade']}")

        if "custo_por_fonte" in resultado:
            custo = resultado["custo_por_fonte"].get(fonte)
            if custo is not None:
                print(f"  Custo: R$ {custo:.2f}")

        print()

    if "custo_total" in resultado:
        print(f"Custo total: R$ {resultado['custo_total']:.2f}\n")


imprimir_formulacao_calagem(resultado)
```

---

### Observações

- O solver `quantidade_minima` (**padrão**) seleciona a combinação que atende a demanda com a menor quantidade total de insumos  
- O solver `custo_minimo` seleciona a combinação mais econômica com base nos preços informados  
- O `modo="mistura"` (**padrão**) permite combinar múltiplas fontes (simples ou compostas) para otimizar o resultado  
- O `modo="fonte_unica"` força a escolha de uma única fonte (ideal para fórmulas comerciais NPK)  
- A separação entre **plantio** e **cobertura** permite maior precisão agronômica no manejo  
- O modelo é extensível para micronutrientes e novas fontes  

#### Tolerância Nutricional

A formulação considera limites de tolerância para evitar excesso ou deficiência de nutrientes:

- `tolerancia` define o percentual máximo de **excesso permitido por nutriente**  
  - Valor padrão: **5%**
- `tol_sup` (tolerância superior) pode ser definido manualmente para controlar excesso de forma mais rigorosa ou flexível  
- `tol_inf` (tolerância inferior) permite déficit controlado na formulação  

**Por padrão:**

- `tol_sup = tolerancia`  
- `tol_inf = 0%` (não permite deficiência de nutrientes)  

#### Impacto do Solver, Modo e Tolerância

Dependendo da configuração, o resultado pode variar significativamente:

- Com `solver="quantidade_minima"`, o foco é reduzir o volume total aplicado  
- Com `solver="custo_minimo"`, o foco é reduzir o custo total  
- Com `modo="mistura"`, o sistema pode combinar múltiplas fontes para otimizar o resultado  
- Com `modo="fonte_unica"`, o sistema seleciona apenas uma formulação  

**Exemplo prático:**

**Mistura otimizada (menor custo):**
```text
npk_08_28_16: 11.76 kg/ha
npk_20_05_20: 25.88 kg/ha
npk_16_12_8: 461.76 kg/ha

Custo total: R$ 1493.53/ha
```

**Fonte única (mais simples operacionalmente):**
```text
npk_16_12_8: 500.00 kg/ha

Custo total: R$ 1500.00/ha
```

Apesar de mais barata, a mistura pode não ser desejável em cenários operacionais (logística, aplicação e padronização).

---

## Representação do Conhecimento

O Fertpy adota uma abordagem baseada em **conhecimento declarativo**, no qual as regras agronômicas são definidas em arquivos no formato YAML.

Esse modelo permite separar completamente:

- Regras agronômicas (dados)
- Lógica de cálculo (código)

---

### Estrutura de conhecimento em produção

As regras utilizadas pelo motor de cálculo estão organizadas em:

```text
src/fertpy/knowledge/
```

Exemplo de organização:

```text
knowledge/
└── boletim_100/
    ├── adubacao/
    │   ├── fontes.yaml
    │   └── milho/
    │       ├── graos/
    │       │   ├── nitrogenio.yaml
    │       │   ├── fosforo.yaml
    │       │   └── potassio.yaml
    │       └── silagem/
    └── calagem/
        ├── fontes.yaml
        └── milho.yaml
```

Características:

- Organização hierárquica por cultura e finalidade
- Dados derivados de boletins agronômicos
- Separação por nutriente e contexto de uso
- Estrutura otimizada para consumo pelo motor de cálcul

### Estrutura de conhecimento para testes

A validação do sistema utiliza uma estrutura complementar em:

```text
tests/knowledge/
```

Exemplo:

```text
knowledge/
├── nitrogenio.yaml
├── fosforo.yaml
├── potassio.yaml
├── calagem.yaml
├── formulacao_cenarios_adubacao.yaml
├── formulacao_cenarios_calagem.yaml
├── nutrientes_fornecidos.yaml
└── recomendacao_combinacao.yaml
```

Características:

- Organização orientada a cenários de teste
- Cada arquivo define:
  - Entradas
  - Saídas esperadas
- Estrutura desacoplada da organização interna da biblioteca
- Foco em validação funcional e reprodutibilidade

---

### Benefícios da abordagem

Essa separação entre conhecimento de produção e conhecimento de validação permite:

- Rastreabilidade clara das regras agronômicas
- Validação independente da implementação
- Facilidade na criação de novos cenários de teste
- Redução de acoplamento entre dados e código
- Maior confiabilidade científica dos resultados

Princípio fundamental

Toda regra agronômica deve ser:

- Declarativa (definida em YAML)
- Rastreável a uma fonte técnica
- Testável via cenários reproduzíveis

---

## Status do Projeto

**Versão Atual:** v0.3.0 — Introdução do Motor de Formulação, CLI inicial e separação de Nitrogênio

O Fertpy agora incorpora um sistema completo de formulação de insumos, mantendo os cálculos agronômicos existentes e adicionando seleção de fontes, otimização por quantidade ou custo, separação de N entre plantio e cobertura e interface de linha de comando (CLI).

O projeto segue em desenvolvimento ativo, com foco na expansão da base de conhecimento, aprimoramento do motor de formulação e consolidação da arquitetura orientada a domínio.

---

### Escopo Implementado

- Suporte à cultura do milho
- Cálculo de correção do solo (calagem)
- Cálculo de doses de Nitrogênio (N), Fósforo (P₂O₅) e Potássio (K₂O)
- Cálculo otimizado de adubação e calagem considerando múltiplas fontes
- Otimização por quantidade mínima ou menor custo
---

### Formulação de Insumos (NOVO)

- Formulação de adubação com múltiplas fontes
- Formulação de calagem com múltiplos corretivos
- Cálculo otimizado da melhor fonte a ser utilizada, considerando:
  - Quantidade mínima aplicada
  - Custo mínimo (incluindo preço e frete)
- Seleção automática da fonte mais adequada para cada cenário
- Cálculo de nutrientes fornecidos por fonte
- Identificação de nutriente limitante na formulação
- Separação do Nitrogênio entre plantio e cobertura, permitindo aplicação fracionada conforme a necessidade da cultura
- Diagnóstico da solução gerada

---

### Interface de Linha de Comando (CLI) (NOVO)

- Execução de formulações via terminal
- Comandos para:
  - Formulação ('formular') 
- Sistema estruturado de argumentos e validação de parâmetros

---

### Base de Conhecimento e Infraestrutura

- Suporte a fontes técnicas (fertilizantes e corretivos) via YAML
- Organização do conhecimento técnico por domínio (adubação e correção)
- Loaders especializados para adubação, correção e fontes
- Estrutura modular para múltiplas finalidades (ex: grãos, silagem)

---

### Qualidade e Validação

- Suíte de testes automatizados baseada em cenários
- Testes orientados a YAML para validação determinística
- Cobertura de:
  - Cálculos de nutrientes
  - Formulação (cenários e erros)
  - Recomendações combinadas

---

### Destaques da Arquitetura

- Separação explícita entre domínio agronômico, infraestrutura de carregamento, motor de cálculo e CLI
- Arquitetura orientada a domínio (DDD)
- Introdução de factories para criação de fertilizantes e corretivos
- Motor de formulação desacoplado com suporte a estratégias de otimização
- Base de conhecimento estruturada por diretórios
- Representação declarativa do conhecimento agronômico
- Avaliação determinística e auditável
- Suporte a critérios N-dimensionais

---

### Avanços em Relação à v0.2.3

- Introdução do motor de formulação de adubação e calagem
- Suporte a múltiplas fontes de insumos
- Otimização por custo mínimo e quantidade mínima
- Implementação de cálculo de nutrientes fornecidos
- Identificação de nutriente limitante
- Separação do Nitrogênio em fracionamento plantio/cobertura
- Criação de sistema de diagnóstico da formulação
- Implementação de CLI completa
- Introdução de factories para objetos de domínio
- Expansão da base de conhecimento com fontes técnicas
- Evolução da suíte de testes com cenários baseados em YAML

---

### Limitações Atuais

- Suporte a uma única cultura (milho)
- Suporte apenas ao método de extração por resina na análise de solo
- Recomendações técnicas baseadas no Boletim 100 (IAC), específico para o estado de São Paulo
- Modelo de otimização limitado a critérios determinísticos (sem heurísticas avançadas)

---

## Roadmap

O desenvolvimento do Fertpy está organizado em ciclos evolutivos com foco em:

- Expansão agronômica
- Robustez técnica
- Explicabilidade
- Escalabilidade estrutural

---

### v0.1.0 — Lançamento Público Inicial (Concluído)

- Engine baseada em regras e fórmulas
- Suporte a milho
- Calagem
- N, P, K
- Estrutura YAML declarativa

---

### v0.2.0 — Consolidação Arquitetural

- Reorganização completa da estrutura knowledge
- Loaders especializados
- Separação domínio/infraestrutura
- Introdução de camadas services e utils
- Base preparada para múltiplos boletins

---

### v0.3.0 — Motor de Formulação e CLI (Concluído)

Foco: transição de cálculo para formulação.

- Introdução do motor de formulação de adubação e calagem
- Suporte a múltiplas fontes de fertilizantes e corretivos
- Otimização baseada em:
  - Quantidade mínima
  - Custo mínimo (preço + frete)
- Cálculo de nutrientes fornecidos por fonte
- Identificação de nutriente limitante
- Sistema de diagnóstico da formulação
- Implementação de interface CLI (`formular` e `nutrientes`)
- Introdução de factories para objetos de domínio
- Expansão da base de conhecimento com fontes técnicas
- Evolução da suíte de testes com cenários baseados em YAML

---

### Próxima Fase — v0.4.0 — Expansão Agronômica e Consolidação de Funcionalidades

Foco: ampliação do escopo técnico

- Parametrização explícita de entradas
- Expansão de culturas (soja, feijão, trigo, etc.)
- Expansão nutricional (macro secundários e micronutrientes)
- Melhor tratamento estruturado de erros
- Consolidação e refinamento das funcionalidades já introduzidas no motor de formulação

---

### v0.5.0 — Explicabilidade e Rastreabilidade

Foco: auditabilidade científica, técnica e transparência.

- Metadados completos de cálculo e formulação
- Rastreamento detalhado das decisões do solver
- Sistema interno de trace/debug
- Modo explicativo ('explain()') para interpretação das recomendações
- Justificativas agronômicas para escolhas de fontes

---

### v0.6.0 — Expansão para Culturas Perenes

Foco: suporte a sistemas produtivos de longo ciclo.

- Suporte a culturas perenes (café, citros, pastagens, etc.)
- Modelagem de recomendações por fase fenológica
- Ajustes de adubação e correção para sistemas contínuos
- Estrutura para manejo nutricional ao longo de múltiplos ciclos
- Adaptação do motor de formulação para demandas específicas de culturas perenes

---

### v0.7.0 — Consolidação da Biblioteca

Foco: estabilidade, padronização e maturidade do projeto.

- Refatoração e padronização da API pública
- Revisão e simplificação de interfaces internas
- Aumento da cobertura e qualidade dos testes
- Padronização de erros e mensagens de validação
- Melhoria da documentação técnica e exemplos de uso
- Garantia de consistência entre módulos (domínio, formulação e CLI)
- Preparação para versionamento estável (semântica e compatibilidade)

---

### Visão de Longo Prazo

- Internacionalização (outros países e sistemas agronômicos)
- Interface gráfica (web ou desktop)
- Integração com dados reais de campo
- Modelos híbridos (determinístico + estatístico)

---

## Licença

Este projeto está licenciado sob a [Apache License 2.0](LICENSE).

---

## Autores

Veja [AUTHORS.md](AUTHORS.md)

---

## Contribuições

Contribuições são bem-vindas e incentivadas. O objetivo do Fertpy é evoluir como uma base confiável e reprodutível de cálculos agronômicos.

### Diretrizes gerais

Antes de submeter um pull request, certifique-se de:

- Manter a separação entre domínio e infraestrutura
- Preservar o caráter determinístico da lógica de cálculo
- Garantir que os artefatos de conhecimento sejam rastreáveis a fontes técnicas
- Utilizar o padrão de commits Conventional Commits

---

### Como contribuir

Você pode contribuir de diferentes formas:

#### 1. Correções e melhorias de código

- Refatorações mantendo compatibilidade
- Otimizações de performance
- Correções de bugs

#### 2. Expansão agronômica

- Inclusão de novas culturas
- Novas recomendações de nutrientes
- Ajustes baseados em boletins técnicos

#### 3. Formulação e otimização

- Novos algoritmos de formulação
- Melhorias nos solvers existentes (`custo_minimo`, `quantidade_minima`)
- Novas estratégias de decisão

#### 4. Base de conhecimento (YAML)

Os arquivos em `tests/knowledge/` representam o conhecimento agronômico validado.

Ao adicionar ou modificar um YAML:

- Utilize dados rastreáveis (boletins, literatura técnica, instituições)
- Mantenha consistência estrutural com os arquivos existentes
- Evite regras implícitas no código — priorize definição declarativa

---

### Adicionando novos cenários de teste

Para garantir consistência científica e evitar regressões:

1. Adicione um novo arquivo YAML em `tests/knowledge/`
2. Crie ou atualize o teste correspondente em `tests/`
3. Garanta que:
   - O cenário seja reprodutível
   - Os valores esperados estejam explícitos
   - Casos limite sejam considerados quando aplicável

---

### Executando os testes

Antes de submeter qualquer contribuição:

```bash
pytest
```

---

## Aviso Legal

O Fertpy é uma biblioteca de software de código aberto que realiza cálculos agronômicos determinísticos com base em critérios técnicos estruturados e em referências agronômicas publicadas.

Os resultados gerados pelo software possuem caráter informativo e técnico e não constituem recomendações agronômicas, consultoria profissional ou serviços de tomada de decisão.

A interpretação e a aplicação dos resultados devem considerar fatores específicos de cada situação, incluindo condições de solo, sistema de cultivo, manejo adotado, método analítico utilizado e recomendações regionais vigentes.

A análise e interpretação dos resultados devem ser realizadas por profissionais legalmente habilitados, conforme as atribuições estabelecidas pelo sistema CONFEA/CREA, como Engenheiros Agrônomos ou Técnicos Agrícolas.

Os usuários são integralmente responsáveis pela interpretação dos resultados e por qualquer decisão ou ação tomada com base nas informações produzidas pelo software.

Os autores e colaboradores do projeto não se responsabilizam por eventuais perdas, danos ou consequências decorrentes do uso direto ou indireto desta ferramenta.

---