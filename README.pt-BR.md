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

O Fertpy possui uma suíte de testes automatizados implementada com `pytest`, garantindo a consistência determinística dos modelos agronômicos implementados.

Os testes cobrem:

- Cálculo de correção do solo (Calagem)
- Cálculo de Nitrogênio (N)
- Cálculo de Fósforo (P)
- Cálculo de Potássio (K)
- Casos limite e cenários de validação
- Estabilidade na leitura e interpretação dos artefatos YAML

A suíte de testes atua como mecanismo de:

- Prevenção de regressões
- Verificação da integridade arquitetural
- Garantia de reprodutibilidade científica dos cálculos

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

**Versão Atual:** v0.2.2 — Melhorias na Documentação e Refinamento na Distribuição

O Fertpy está em desenvolvimento ativo, com foco na consolidação da arquitetura orientada a domínio, na organização explícita do conhecimento agronômico e na validação determinística dos modelos por meio de testes automatizados.

### Escopo Implementado

- Suporte à cultura do milho
- Cálculo de correção do solo (calagem)
- Cálculo de doses de Nitrogênio (N), Fósforo (P) e Potássio (K)
- Fonte técnica única por nutriente
- Estrutura modular para múltiplas finalidades (ex: grãos, silagem)
- Organização do conhecimento técnico por domínio (adubação e correção)
- Suíte de testes automatizados cobrindo todos os módulos principais de cálculo

### Destaques da Arquitetura

- Separação explícita entre:
  - Domínio agronômico
  - Infraestrutura de carregamento
  - Motor de cálculo
- Base de conhecimento estruturada por diretórios (não por nomes compostos de arquivos)
- Loaders especializados para adubação e correção
- Arquitetura orientada a domínio (DDD)
- Avaliação determinística e desacoplada de regras
- Representação declarativa do conhecimento agronômico
- Suporte a critérios N-dimensionais
- Validação com segurança contra regressões por meio de testes automatizados

### Avanços em Relação à v0.1.0

- Remoção do loader YAML genérico
- Eliminação de parsing baseado em nome de arquivo
- Reorganização completa da estrutura 'knowledge'
- Introdução de camadas 'services' e 'utils'
- Preparação da arquitetura para múltiplos boletins e fontes técnicas
- Integração de suíte abrangente de testes automatizados garantindo estabilidade dos cálculos

### Limitações Atuais

- Suporte a uma única cultura (milho)
- Fonte técnica única por nutriente
- Um único método analítico por nutriente
- Recomendações técnicas restritas a um único país (Brasil)
- Sem agregação de múltiplas fontes
- Lógica estritamente determinística (sem modelagem probabilística)

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

### Próxima Fase — v0.3.0 (Expansão Agronômica)

Foco: ampliação do escopo técnico.

- Parametrização explícita de entradas
- Expansão de culturas (Soja, Feijão, Trigo, etc.)
- Expansão nutricional (macro secundários e micronutrientes)
- Modelagem de fontes fertilizantes
- Melhor tratamento estruturado de erros

---

### v0.4.0 — Robustez e Normalização

Foco: consistência técnica e dimensional.

- Normalização automática de unidades
- Validação dimensional
- Diferenciação entre erros críticos e alertas
- Primeira camada de validação semântica

---

### v0.5.0 — Explicabilidade e Rastreabilidade

Foco: auditabilidade científica.

- Metadados completos de cálculo
- Rastreamento da regra ativada
- Sistema interno de trace/debug
- Modo explicativo (explain())

---

### v0.6.0 — Expansão Estrutural

- Suporte a culturas perenes
- Estrutura para múltiplos boletins
- Base para internacionalização futura

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