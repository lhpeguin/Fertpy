![Python](https://img.shields.io/badge/python-3.11-blue)
![Tests](https://img.shields.io/badge/tests-pytest-green)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-Apache%202.0-lightgrey)
[![PyPI version](https://img.shields.io/pypi/v/fertpy.svg)](https://pypi.org/project/fertpy/)

# Fertpy

**Languages:** 🇺🇸 English | 🇧🇷 [Português (Brasil)](README.pt-BR.md)

**Fertpy** is a domain-driven, rule-based agronomic calculation engine for soil correction and nutrient dose computation.

It provides a structured computational framework to transform agronomic technical bulletins into executable, deterministic calculation models using YAML-based rule definitions.

Fertpy does not provide agronomic recommendations or consultancy.  
It performs reproducible calculations based strictly on predefined technical criteria.

---

## Overview

**Fertpy** is a library for agronomic modeling and calculation, designed to transform technical bulletins into **structured, reproducible, and traceable computational models**.

The library enables:

- Representing agronomic recommendations (technical bulletins) as structured models
- Performing deterministic calculations for:
  - Soil correction (e.g., liming)
  - Nutrient recommendations (N, P₂O₅, K₂O)
  - Fertilizer formulation (blends and commercial sources)
- Optimizing formulations based on:
  - Minimum input usage
  - Minimum cost
- Working with both simple and compound sources (e.g., commercial NPK)
- Ensuring transparency, traceability, and consistency in calculations

---

### Architecture

The project follows a modular architecture with a clear separation of responsibilities:

#### Domain Core

- `core/domain/` → Entities and business rules (recommendations, fertilizers, criteria, etc.)
- `core/engine/` → Agronomic calculation and formulation engine
- `core/analysis/` → Auxiliary analyses (diagnostics, proportions, limiting nutrients)
- `core/factories/` → Creation of domain objects (fertilizers, soil amendments)

---

#### Application Layer

- `nutrientes/` → Calculation interfaces by nutrient (N, P, K)
- `correcao_solo/` → Soil correction models (e.g., liming)
- `formulacao/` → Fertilization and liming formulation interface

---

#### Infrastructure

- `infra/loaders/` → Data loading (YAML)
- `infra/parsing/` → Parsing and interpretation of agronomic rules
- `services/` → Validations and auxiliary rules

---

#### Knowledge Base

- `knowledge/` → Structured definitions of agronomic bulletins
  - Recommendation rules by crop
  - Nutrient and amendment sources
  - Versioned technical parameters

---

#### Interfaces and Tools

- `cli/` → Command-line interface for running calculations
- `utils/` → Shared utilities

---

#### Design Principles

Fertpy was built based on:

- Clear separation between domain, infrastructure, and knowledge
- Explicit modeling of agronomic rules
- Extensibility for new crops, nutrients, and sources
- Reproducibility of calculations
- Interface independence (API, CLI, etc.)

---

#### Project Structure (summary)

```text
fertpy/
├── core/           # Domain and calculation engine
├── formulacao/     # Fertilization and liming formulation
├── nutrientes/     # Nutrient-based calculations
├── correcao_solo/  # Soil correction
├── infra/          # Loading and parsing
├── knowledge/      # Agronomic knowledge base (YAML)
├── cli/            # Command-line interface
├── services/       # Validations
└── utils/          # Utilities
```

---

## Scope

Current knowledge models are derived from Brazilian agronomic technical bulletins.

While the calculation engine itself is framework-agnostic, the implemented knowledge artifacts are primarily valid within Brazilian agronomic contexts.

Future extensions may include regional parameterization and additional technical sources.

---

## Design Principles

- Domain-Driven Design (DDD)
- Deterministic rule-based modeling
- YAML as knowledge representation layer
- Hybrid architecture:
  - N-dimensional rule-based models
  - Fixed algebraic formula-based models (e.g., liming)
- Strict separation between the calculation engine and agronomic criteria
- Extensibility for new crops and technical bulletins
- Traceability of technical sources
- Deterministic reproducibility of results

---

## Installation

### Requirements

- Python >= 3.11
- pip

---

### Installation via PyPI (recommended)

To install the latest stable release:

```bash
pip install fertpy
```

To verify the installation:

```bash
python -c "import fertpy; print(fertpy.__version__)"
```

---

### Development Installation

If you intend to contribute or modify the project:

#### 1. Clone the repository

```bash
git clone https://github.com/lhpeguin/fertpy.git
cd fertpy
```

#### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Linux / macOS:
source venv/bin/activate  
# Windows: 
venv\Scripts\activate
```

#### 3. Install dependencies

Standard installation (library usage)

```bash
pip install -e .
```

Development installation (with tests)

```bash
pip install -e .[dev]
```

This also installs the development dependencies, including 'pytest', required to run the test suite.

---

## Validation and Testing

Fertpy includes an automated test suite implemented with `pytest`, ensuring the deterministic consistency of agronomic models and formulation algorithms.

---

### Test Coverage

The tests cover:

- Soil correction calculation (Liming)
- Nitrogen (N) calculation
- Phosphorus (P) calculation
- Potassium (K) calculation
- Fertilizer formulation across multiple scenarios
- Liming formulation with different sources
- Calculation of nutrients supplied by combinations
- Recommendations based on source combinations
- Error handling and input validation
- Edge cases and validation scenarios
- Stability in reading and interpreting YAML artifacts

### Suite Objectives

The test suite acts as a mechanism for:

- Regression prevention
- Verification of architectural integrity
- Ensuring scientific reproducibility of calculations
- Cross-validation between agronomic rules and declarative data (YAML)

---

### Running the Tests

After installing the project dependencies:

```bash
pytest
```

Alternatively:

```bash
python -m pytest
```

All tests must pass successfully before submitting structural changes or expanding the knowledge base.

---

## Usage Example

This example demonstrates the complete workflow of using fertpy, including:

- Agronomic calculation (liming + macronutrients)
- Nutritional demand generation
- Fertilizer formulation with:
  - Simple sources (on-farm blending)
  - Compound sources (commercial NPK)
  - Planting and topdressing strategy

---

### 1. Agronomic Calculation

```python
from fertpy import Calagem, Nitrogenio, Fosforo, Potassio


# Liming
calagem = Calagem("milho")
resultado_calagem = calagem.calcular(v_atual=55, ctc=70)

print(f"\nLime requirement: {resultado_calagem['dose']} t/ha\n")


# Primary macronutrients
n = Nitrogenio("milho", "graos")
p = Fosforo("milho", "graos")
k = Potassio("milho", "graos")

n_resultado = n.calcular("media_baixa", 12.1)
p_resultado = p.calcular(26, 12.1)
k_resultado = k.calcular(3, 12.1)


def print_nutrient_calculation(r):
    print(
        f"Nutrient: {r.nutriente}\n"
        f"Dose: {r.dose} {r.unidade}\n"
        f"Class: {r.classe.nome}\n"
        f"Bulletin: {r.fonte['documento']} "
        f"({r.fonte['instituicao']}, {r.fonte['ano']})\n"
    )

    if r.fracionamento:
        print("Split application:")
        print(f"  At planting: {r.fracionamento['plantio']} {r.unidade}")
        print(f"  Topdressing: {r.fracionamento['cobertura']} {r.unidade}\n")


# Output
print_nutrient_calculation(n_resultado)
print_nutrient_calculation(p_resultado)
print_nutrient_calculation(k_resultado)
```

---

### 2. Nutritional Demand

From the calculated recommendations, we consolidate the nutrient demand:

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

### 3. Fertilizer Formulation

```python
from fertpy import FormulacaoAdubacao


formulador = FormulacaoAdubacao()


def print_formulation(resultado, titulo):
    print(f"\n=== {titulo} ===\n")

    for fonte, dose in resultado["doses"].items():
        print(f"- {fonte}: {dose:.2f} {resultado['unidade']}")

    if resultado.get("custo_total") is not None:
        print(f"\nTotal cost: R$ {resultado['custo_total']:.2f}")
```

---

#### 3.1 Simple Sources (On-farm Blending)

Optimized combination of basic fertilizers:

```python
resultado_simples = formulador.calcular(
    demanda=demanda_total,
    fontes=["ureia", "map", "kcl"],
    # Source prices (R$/ton)
    precos={
        "ureia": 2500,
        "map": 3200,
        "kcl": 2800
    },
    solver="custo_minimo"
)

print_formulation(resultado_simples, "Formulation with simple sources (blend)")
```

---

#### 3.2 Compound Sources (Commercial NPK)

Selection of the best commercial formulation based on demand:

```python
# Commercial compound fertilizers (NPK)
# Format: "name:N=%,P2O5=%,K2O=%"

fontes_npk = [
    "NPK_04_14_08:N=4,P2O5=14,K2O=8",
    "NPK_08_28_16:N=8,P2O5=28,K2O=16",
    "NPK_20_05_20:N=20,P2O5=5,K2O=20",
    "NPK_12_24_20:N=12,P2O5=24,K2O=20"
]

# Source prices (R$/ton)
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
    modo="fonte_unica",   # selects a single commercial formulation
    tolerancia=0.1        # demand tolerance (10%)
)

print_formulation(resultado_npk, "Compound source (commercial NPK)")
```

---

#### 3.3 Planting and Topdressing Fertilization

Fertilization split according to management strategy:

- Planting: application of N, P, and K at sowing
- Topdressing: supplemental Nitrogen application during the crop cycle

```python
# Source prices (R$/ton)
precos = {
    "ureia": 2500,
    "map": 3200,
    "kcl": 2800
}

# Planting fertilization (full NPK)
resultado_plantio = formulador.calcular(
    demanda=demanda_plantio,
    entradas_fontes=["ureia", "map", "kcl"],
    precos=precos,
    solver="custo_minimo"
)

# Topdressing fertilization (Nitrogen only)
resultado_cobertura = formulador.calcular(
    demanda=demanda_cobertura,
    entradas_fontes=["ureia"],
    precos={"ureia": 2500},
    solver="custo_minimo"
)

print_formulation(resultado_plantio, "Planting fertilization")
print_formulation(resultado_cobertura, "Topdressing fertilization")
```

---

#### 4. Liming Formulation

Optimized selection of soil amendments based on cost and acidity neutralization efficiency.

```python
from fertpy import FormulacaoCalagem

formulador = FormulacaoCalagem()

# Amendment prices (R$/ton)
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


def print_limimg_formulation(resultado):
    print("\n=== Liming Formulation ===\n")

    for fonte, dose in resultado["doses"].items():
        print(f"- {fonte}")
        print(f"  Dose: {dose:.2f} {resultado['unidade']}")

        if "custo_por_fonte" in resultado:
            custo = resultado["custo_por_fonte"].get(fonte)
            if custo is not None:
                print(f"  Cost: R$ {custo:.2f}")

        print()

    if "custo_total" in resultado:
        print(f"Total cost: R$ {resultado['custo_total']:.2f}\n")


print_limimg_formulation(resultado)
```

---

### Notes

- The `quantidade_minima` solver (**default**) selects the combination that meets the demand with the lowest total amount of inputs  
- The `custo_minimo` solver selects the most economical combination based on the provided prices  
- The `modo="mistura"` (**default**) allows combining multiple sources (simple or compound) to optimize the result  
- The `modo="fonte_unica"` forces the selection of a single source (ideal for commercial NPK formulas)  
- The separation between **planting** and **topdressing** enables greater agronomic precision in management  
- The model is extensible to micronutrients and new sources  

#### Nutritional Tolerance

The formulation considers tolerance limits to avoid excess or deficiency of nutrients:

- `tolerancia` defines the maximum percentage of **allowed excess per nutrient**  
  - Default value: **5%**
- `tol_sup` (upper tolerance) can be manually defined to control excess more strictly or flexibly  
- `tol_inf` (lower tolerance) allows controlled deficit in the formulation  

**By default:**

- `tol_sup = tolerancia`  
- `tol_inf = 0%` (does not allow nutrient deficiency)  

#### Impact of Solver, Mode, and Tolerance

Depending on the configuration, the result may vary significantly:

- With `solver="quantidade_minima"`, the focus is on reducing the total applied volume  
- With `solver="custo_minimo"`, the focus is on reducing total cost  
- With `modo="mistura"`, the system can combine multiple sources to optimize the result  
- With `modo="fonte_unica"`, the system selects only a single formulation  

**Practical example:**

**Optimized blend (lowest cost):**
```text
npk_08_28_16: 11.76 kg/ha
npk_20_05_20: 25.88 kg/ha
npk_16_12_8: 461.76 kg/ha

Total cost: R$ 1493.53/ha
```

**Single source (operationally simpler):**
```text
npk_16_12_8: 500.00 kg/ha

Total cost: R$ 1500.00/ha
```

---

## Knowledge Representation

Fertpy adopts a **declarative knowledge-based** approach, in which agronomic rules are defined in YAML files.

This model allows a complete separation between:

- Agronomic rules (data)
- Calculation logic (code)

---

### Knowledge Structure in Production

The rules used by the calculation engine are organized in:

```text
src/fertpy/knowledge/
```

Example structure:

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

Characteristics:

- Hierarchical organization by crop and purpose
- Data derived from agronomic bulletins
- Separation by nutrient and usage context
- Structure optimized for consumption by the calculation engine

### Knowledge Structure for Testing

System validation uses a complementary structure in:

```text
tests/knowledge/
```

Example:

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

Characteristics:

- Scenario-oriented organization for testing
- Each file defines:
  - Inputs
  - Expected outputs
- Structure decoupled from the internal organization of the library
- Focus on functional validation and reproducibility

---

### Benefits of the Approach

This separation between production knowledge and validation knowledge enables:

- Clear traceability of agronomic rules
- Independent validation of the implementation
- Ease of creating new test scenarios
- Reduced coupling between data and code
- Greater scientific reliability of results

Fundamental principle

Every agronomic rule must be:

- Declarative (defined in YAML)
- Traceable to a technical source
- Testable through reproducible scenarios

---

## Project Status

**Current Version:** v0.3.0 — Introduction of the Formulation Engine, initial CLI, and Nitrogen splitting

Fertpy now incorporates a complete input formulation system, maintaining existing agronomic calculations while adding source selection, optimization by quantity or cost, nitrogen splitting between planting and topdressing, and a command-line interface (CLI).

The project is under active development, with a focus on expanding the knowledge base, improving the formulation engine, and consolidating the domain-oriented architecture.

---

### Implemented Scope

- Support for maize (corn) crop
- Soil correction calculation (liming)
- Calculation of Nitrogen (N), Phosphorus (P₂O₅), and Potassium (K₂O) doses
- Optimized fertilization and liming calculations considering multiple sources
- Optimization by minimum quantity or lowest cost

---

### Input Formulation (NEW)

- Fertilizer formulation with multiple sources
- Liming formulation with multiple soil amendments
- Optimized calculation of the best source to be used, considering:
  - Minimum applied quantity
  - Minimum cost (including price and freight)
- Automatic selection of the most suitable source for each scenario
- Calculation of nutrients supplied by each source
- Identification of limiting nutrient in the formulation
- Nitrogen splitting between planting and topdressing, allowing staged application according to crop needs
- Diagnosis of the generated solution

---

### Command-Line Interface (CLI) (NEW)

- Execution of formulations via terminal
- Commands for:
  - Formulation (`formular`)
- Structured system for arguments and parameter validation

---

### Knowledge Base and Infrastructure

- Support for technical sources (fertilizers and soil amendments) via YAML
- Organization of technical knowledge by domain (fertilization and soil correction)
- Specialized loaders for fertilization, soil correction, and sources
- Modular structure for multiple purposes (e.g., grain, silage)

---

### Quality and Validation

- Scenario-based automated test suite
- YAML-driven tests for deterministic validation
- Coverage of:
  - Nutrient calculations
  - Formulation (scenarios and errors)
  - Combined recommendations

---

### Architecture Highlights

- Explicit separation between agronomic domain, loading infrastructure, calculation engine, and CLI
- Domain-Driven Design (DDD) architecture
- Introduction of factories for creating fertilizers and soil amendments
- Decoupled formulation engine with support for optimization strategies
- Directory-structured knowledge base
- Declarative representation of agronomic knowledge
- Deterministic and auditable evaluation
- Support for N-dimensional criteria

---

### Improvements Compared to v0.2.3

- Introduction of fertilization and liming formulation engine
- Support for multiple input sources
- Optimization by minimum cost and minimum quantity
- Implementation of nutrient supply calculations
- Identification of limiting nutrient
- Nitrogen splitting into planting/topdressing
- Creation of formulation diagnostic system
- Implementation of a complete CLI
- Introduction of factories for domain objects
- Expansion of the knowledge base with technical sources
- Evolution of the test suite with YAML-based scenarios

---

### Current Limitations

- Support for a single crop (maize/corn)
- Support only for resin extraction method in soil analysis
- Technical recommendations based on Boletim 100 (IAC), specific to the state of São Paulo
- Optimization model limited to deterministic criteria (no advanced heuristics)

---

## Roadmap

Fertpy’s development is organized into evolutionary cycles focused on:

- Agronomic expansion
- Technical robustness
- Explainability
- Structural scalability

---

### v0.1.0 — Initial Public Release (Completed)

- Rule- and formula-based engine
- Support for corn (maize)
- Liming calculations
- Nitrogen (N), Phosphorus (P), and Potassium (K)
- Declarative YAML-based knowledge structure

---

### v0.2.0 — Architectural Consolidation

- Complete reorganization of the knowledge structure
- Specialized loaders
- Clear separation between domain and infrastructure
- Introduction of services and utils layers
- Foundation prepared for multiple technical bulletins

---

### v0.3.0 — Formulation Engine and CLI (Completed)

Focus: transition from calculation to formulation.

- Introduction of fertilization and liming formulation engine
- Support for multiple fertilizer and soil amendment sources
- Optimization based on:
  - Minimum quantity
  - Minimum cost (price + freight)
- Calculation of nutrients supplied by each source
- Identification of limiting nutrient
- Formulation diagnostic system
- Implementation of CLI interface (`formular` and `nutrientes`)
- Introduction of factories for domain objects
- Expansion of the knowledge base with technical sources
- Evolution of the test suite with YAML-based scenarios

---

### Next Phase — v0.4.0 — Agronomic Expansion and Feature Consolidation

Focus: expansion of technical scope

- Explicit parameterization of inputs
- Expansion to new crops (soybean, beans, wheat, etc.)
- Nutritional expansion (secondary macronutrients and micronutrients)
- Improved structured error handling
- Consolidation and refinement of features introduced in the formulation engine

---

### v0.5.0 — Explainability and Traceability

Focus: scientific auditability, technical transparency.

- Complete metadata for calculation and formulation
- Detailed tracking of solver decisions
- Internal trace/debug system
- Explain mode (`explain()`) for interpreting recommendations
- Agronomic justification for source selection

---

### v0.6.0 — Expansion to Perennial Crops

Focus: support for long-cycle production systems.

- Support for perennial crops (coffee, citrus, pastures, etc.)
- Modeling recommendations by phenological stage
- Fertilization and soil correction adjustments for continuous systems
- Structure for nutrient management across multiple cycles
- Adaptation of the formulation engine for perennial crop demands

---

### v0.7.0 — Library Consolidation

Focus: stability, standardization, and project maturity.

- Refactoring and standardization of the public API
- Review and simplification of internal interfaces
- Increased test coverage and quality
- Standardization of errors and validation messages
- Improved technical documentation and usage examples
- Ensuring consistency across modules (domain, formulation, and CLI)
- Preparation for stable versioning (semantics and compatibility)

---

### Long-Term Vision

- Internationalization (other countries and agronomic systems)
- Graphical interface (web or desktop)
- Integration with real field data
- Hybrid models (deterministic + statistical)

---


## License

This project is licensed under the [Apache License 2.0](LICENSE).

---

## Authors

See [AUTHORS.md](AUTHORS.md)

---

## Contributions

Contributions are welcome and encouraged. The goal of Fertpy is to evolve as a reliable and reproducible foundation for agronomic calculations.

### General Guidelines

Before submitting a pull request, make sure to:

- Maintain the separation between domain and infrastructure
- Preserve the deterministic nature of the calculation logic
- Ensure that knowledge artifacts are traceable to technical sources
- Use the Conventional Commits standard

---

### How to Contribute

You can contribute in different ways:

#### 1. Code fixes and improvements

- Refactoring while maintaining compatibility
- Performance optimizations
- Bug fixes

#### 2. Agronomic expansion

- Adding new crops
- New nutrient recommendations
- Adjustments based on technical bulletins

#### 3. Formulation and optimization

- New formulation algorithms
- Improvements to existing solvers (`custo_minimo`, `quantidade_minima`)
- New decision strategies

#### 4. Knowledge Base (YAML)

Files in `tests/knowledge/` represent validated agronomic knowledge.

When adding or modifying a YAML:

- Use traceable data (bulletins, technical literature, institutions)
- Maintain structural consistency with existing files
- Avoid implicit rules in code — prioritize declarative definitions

---

### Adding New Test Scenarios

To ensure scientific consistency and avoid regressions:

1. Add a new YAML file in `tests/knowledge/`
2. Create or update the corresponding test in `tests/`
3. Ensure that:
   - The scenario is reproducible
   - Expected values are explicit
   - Edge cases are considered when applicable

---

### Running Tests

Before submitting any contribution:

```bash
pytest
```

## Legal Disclaimer

Fertpy is an open-source software library that performs deterministic agronomic calculations based on structured technical criteria and published agronomic references.

The results generated by the software are intended for informational and technical purposes only and do not constitute agronomic recommendations, professional consulting, or decision-making services.

The interpretation and application of the results should consider factors specific to each situation, including soil conditions, cropping systems, management practices, analytical methods used, and applicable regional recommendations.

The analysis and interpretation of the results should be carried out by legally qualified professionals, in accordance with the professional responsibilities established by regulatory bodies (such as licensed agronomists or agricultural technicians).

Users are fully responsible for the interpretation of the results and for any decisions or actions taken based on the information produced by the software.

The authors and contributors of the project shall not be held responsible for any losses, damages, or consequences resulting from the direct or indirect use of this tool.