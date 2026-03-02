# Fertpy

**Languages:** 🇺🇸 English | 🇧🇷 [Português (Brasil)](README.pt-br.md)

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

### 1. Clone the repository

```bash
git clone https://github.com/lhpeguin/fertpy.git
cd fertpy
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Linux / macOS:
source venv/bin/activate  
# Windows: 
venv\Scripts\activate
```

### 3. Install dependencies

If using editable installation:

```bash
pip install -e .
```

Or, if using requirements file:

```bash
pip install -r requirements.txt
```

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

**Current Version:** v0.1.0 — Initial Public Release

Fertpy is under active development.

### Implemented Scope

- Corn (maize) crop support
- Soil correction (liming) calculation
- Nitrogen (N), Phosphorus (P), and Potassium (K) dose computation
- Single technical source per nutrient
- YAML-based agronomic knowledge modeling

### Engine & Architecture Highlights

- Clear separation between calculation engine and agronomic criteria
- Deterministic rule evaluation (engine executes logic but does not define agronomic rules)
- Domain-driven structure
- Infrastructure-layer parsing for interval and condition normalization
- Explicit interval modeling via a dedicated value object
- N-dimensional rule evaluation (no fixed number of decision variables)
- Fully declarative knowledge representation

### Current Limitations

- Single supported crop (corn)
- Single technical source per nutrient
- Single analytical method per nutrient
- Brazilian agronomic technical context only
- No multi-source aggregation
- Deterministic logic only (no probabilistic modeling)

---

## Roadmap

Fertpy’s development is structured in evolutionary phases, focusing on architectural consolidation, agronomic expansion, and technical robustness.

---

### Phase 1 — Engine Foundation (Completed)

Corresponds to version **v0.1.0 — Initial Public Release**.

This phase established Fertpy’s deterministic agronomic calculation core.

---

#### Implemented

- Deterministic agronomic calculation engine
- Hybrid architecture:
  - N-dimensional rule-based models
  - Algebraic formula-based models (e.g., liming)
- Structured parsing of intervals and conditions
- Clear separation between:
  - Calculation engine
  - Knowledge representation (YAML)
- Soil correction (liming)
- Primary macronutrients:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
- Initial technical source traceability structure

Phase 1 consolidates Fertpy as a declarative and deterministic computational representation of agronomic bulletins.

---

### Phase 2 — Agronomic Scope Expansion

**Focus:** functional expansion and operational consolidation.

---
#### 1. Explicit Input Parameterization

Creation of:

```text
fertpy/utils/parametros.py
```

Objectives:

- Explicit declaration of valid parameters per crop and nutrient
- Improved input validation
- Safer and more self-explanatory public API

---

#### 2. Crop Expansion

Inclusion of cultures such as:

- Soybean
- Common bean
- Cotton
- Wheat
- Sorghum

---

#### 3. Nutritional Scope Expansion

Currently implemented nutrients:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)

Planned:

- Secondary macronutrients
- Micronutrients
Target: 14 modeled nutrients.

---

#### 4. Inorganic Fertilizer Sources

Modeling of different fertilizer sources
Association between calculated doses and available sources

**Important:**

Fertpy will not automatically block incompatible fertilizer combinations.
Chemical compatibility remains the responsibility of the licensed technical professional.

The system may emit informational alerts based on technical bulletins but will not enforce automatic restrictions.

---

#### 5. Improved Error Handling

- Clearer and more structured error messages
- Differentiation between:
  - Structural errors
  - Validation errors
  - Technical warnings

---

### Phase 3 — Technical Consolidation and Structural Expansion

Focus: robustness, explainability, and full traceability.

---

#### 1. Support for Perennial Crops

- Inclusion of perennial crops
- Structural adjustments for multi-year cycles
- Parameterization by phenological stages
- Adaptation of recommendation logic for perennial systems

---

#### 2. Input Normalization

Proposed structure:

```text
fertpy/normalization/base.py
fertpy/normalization/unit.py
```

Objectives:

Automatic unit conversion
Dimensional consistency
Reduction of operational errors
Internal standardization of calculation units

---

#### 3. Dimensional Validation

The system will implement dimensional and agronomic validation of inputs, ensuring physical, mathematical, and technical coherence before rule execution.

This layer aims to prevent operational inconsistencies and misinterpretation of analytical data.

Examples:

- CEC provided in incorrect units → critical error
- pH outside an agronomically plausible range → technical warning
- Base saturation > 100% → critical error
- Negative values for chemical attributes → critical error
- Incompatibility between reported unit and analytical method → error

The system will explicitly differentiate between:

- Critical errors → block calculation execution
- Technical warnings → allow execution but signal potential inconsistency

This distinction preserves the deterministic nature of the engine while maintaining technical rigor and user responsibility.

---

#### 4. Calculation Metadata and Full Traceability

```text
fertpy/core/metadata.py
```

Each result object will carry structured metadata describing not only the computed value, but also the logical path that led to that decision.

This layer turns every output into an auditable artifact, enabling full reconstruction of the technical criteria applied by the engine.

Metadata will include, among other elements:

- crop
- nutrient
- reference technical bulletin
- source YAML file
- activated rule
- evaluated conditions
- assigned interpretative class
- triggered interval or range
- analytical method considered

This enables:

- Full auditability of the decision process
- Verifiable technical reproducibility
- Transparency in rule application
- Comparison between different bulletin versions
- Foundation for future explainability features

The goal is that no recommendation exists as an isolated numeric value, but as a fully traceable outcome derived from explicit technical criteria.

---

#### 5. Activated Rule Tracking

Capability to identify:

- Which rule was triggered
- From which YAML file
- In which section

Ensuring auditability and technical transparency.

---

#### 6. Explainability Mode

Planned usage example:

```text
fertpy/core/explain.py
```
```python
explain(result) -> str
```

Example output:

P = 12 mg/dm³ classified in the <16 category and expected yield of 9, falling within the 8–10 range, according to the information defined in cultura_finalidade_fosforo.yaml. Dose defined as 100 kg/ha.

Objectives:

- Make the engine auditable
- Facilitate academic use
- Increase technical transparency
- Support scientific validation

---

#### 7. Semantic Validation Layer

```text
fertpy/validation/semanticasemantics.py
```

Planned functions:

- Coherence between CEC and recommended dose
- Ca/Mg ratio verification
- Liming consistency validation

Characteristics:

- Warning generation only
- No automatic blocking
- Respect for the user’s technical responsibility

---

#### 8. Internal Debug and Trace System

```text
fertpy/core/trace.py
```

Objective:

- Enable detailed analysis of the decision flow
- Support academic research and validation
- Facilitate structural testing of the engine

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