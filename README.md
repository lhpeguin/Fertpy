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

Fertpy is designed to:

- Represent agronomic technical bulletins as structured computational models
- Execute deterministic soil correction and nutrient dose calculations
- Separate domain logic from infrastructure and knowledge representation
- Enable transparent and traceable agronomic computations

The project follows a clear separation of concerns:

- `core/` → Domain entities and calculation engine  
- `infra/` → YAML loading and parsing layer  
- `nutrientes/` → Nutrient-specific calculation interfaces  
- `correcao_solo/` → Soil correction models  
- `knowledge/` → Structured agronomic knowledge definitions  

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

Fertpy includes an automated test suite implemented with 'pytest', ensuring the deterministic consistency of the implemented agronomic models.

The test suite covers:

- Soil correction calculation (Liming)
- Nitrogen (N) calculation
- Phosphorus (P) calculation
- Potassium (K) calculation
- Edge cases and validation scenarios
- Stability in the loading and interpretation of YAML knowledge artifacts

The test suite serves as a mechanism for:

- Regression prevention
- Architectural integrity verification
- Ensuring scientific reproducibility of calculations

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

```python
from fertpy import Calagem, Nitrogenio, Fosforo, Potassio


# Soil correction (liming calculation)
c = Calagem("milho")
NC = c.calcular(v_atual=40, ctc=70)


# Nitrogen dose calculation
n = Nitrogenio("milho", "graos")
n_total = n.calcular("alto", 5.9)


# Phosphorus dose calculation
p = Fosforo("milho", "graos")
p_total = p.calcular(16, 5)


# Potassium dose calculation
k = Potassio("milho", "graos")
k_total = k.calcular(3.8, 11)


print(f"Liming requirement: {NC} t/ha")


def print_result(r):
    print(
        f"\nNutrient: {r.nutriente}\n"
        f"Dose: {r.dose} {r.unidade}\n"
        f"Class: {r.classe.nome}\n"
        f"Notes: {r.observacoes or 'None'}\n"
        f"Source: {r.fonte['documento']} "
        f"({r.fonte['instituicao']}, {r.fonte['ano']})\n"
    )


print_result(n_total)
print_result(p_total)
print_result(k_total)
```

---

## Knowledge Representation

Agronomic criteria are defined as structured YAML files located under:

```text
knowledge/
```

Each file encodes technical rules derived from agronomic bulletins.

This architecture enables:

- Clear traceability of calculation parameters
- Separation between data and execution logic
- Deterministic and reproducible outputs
- Simplified extension for new crops and regions

---

## Project Status

**Versão Atual:** v0.2.2 — Documentation Improvements and Distribution Refinement

Fertpy is under active development, with a focus on domain-oriented architectural consolidation, explicit organization of agronomic knowledge, and deterministic validation through automated testing.

### Implemented Scope

- Support for corn (maize)
- Soil correction (liming) calculations
- Nitrogen (N), Phosphorus (P), and Potassium (K) dose calculations
- Single technical reference per nutrient
- Modular structure supporting multiple crop purposes (e.g., grain, silage)
- Technical knowledge organized by domain (fertilization and soil correction)
- Automated test suite covering all core calculation modules

### Architectural Highlights

- Explicit separation between:
  - Agronomic domain
  - Loading infrastructure
  - Calculation engine
- Knowledge base structured by directories (instead of compound file names)
- Specialized loaders for fertilization and soil correction
- Domain-Driven Design (DDD) architecture
- Deterministic and decoupled rule evaluation
- Declarative representation of agronomic knowledge
- Support for N-dimensional criteria
- Regression-safe validation through automated testing

### Improvements Compared to v0.1.0

- Removal of the generic YAML loader
- Elimination of filename-based parsing
- Complete reorganization of the 'knowledge' structure
- Introduction of 'services' and 'utils' layers
- Architectural preparation for multiple technical bulletins and data sources
- Integration of a comprehensive automated test suite ensuring calculation stability

### Current Limitations

- Single supported crop (corn)
- Single technical source per nutrient
- Single analytical method per nutrient
- Brazilian agronomic technical context only
- No multi-source aggregation
- Deterministic logic only (no probabilistic modeling)

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

### Next Phase — v0.3.0 (Agronomic Expansion)

Focus: Expansion of technical scope.

- Explicit input parameterization
- Crop expansion (Soybean, Beans, Wheat, etc.)
- Nutritional expansion (secondary macronutrients and micronutrients)
- Modeling of fertilizer sources
- Improved structured error handling

---

### v0.4.0 — Robustness and Normalization

Focus: Technical and dimensional consistency.

- Automatic unit normalization
- Dimensional validation
- Differentiation between critical errors and technical warnings
- Initial semantic validation layer

---

### v0.5.0 — Explainability and Traceability

Focus: Scientific auditability.

- Complete calculation metadata
- Tracking of activated rules
- Internal trace/debug system
- Explain mode (explain())

---

### v0.6.0 — Structural Expansion

- Support for perennial crops
- Structure for multiple technical bulletins
- Foundation for future internationalization

---

## License

Licensed under the Apache License 2.0.  
See the `LICENSE` file for details.

---

## Authors

See [AUTHORS.md](AUTHORS.md)

---

## Contributions

Contributions are welcome.

Before submitting a pull request:

- Maintain separation between domain and infrastructure layers
- Keep calculation logic deterministic
- Ensure knowledge artifacts are traceable to technical sources
- Use conventional commits

---

## Disclaimer

Fertpy performs deterministic agronomic calculations based on structured technical criteria.

It does not provide agronomic recommendations, professional consultancy, or decision-making services.

Users are responsible for interpreting results within their specific agronomic, regional, and regulatory context.