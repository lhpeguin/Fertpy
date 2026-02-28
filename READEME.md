# Fertpy

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
- Strict separation between calculation engine and agronomic criteria
- Extensibility for new crops and technical bulletins
- Traceability of technical sources

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/fertpy.git
cd fertpy
```

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e .
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

```
knowledge/
```

Each file encodes technical rules derived from agronomic bulletins.

This architecture enables:

- Clear traceability of calculation parameters
- Separation between data and execution logic
- Reproducible deterministic outputs
- Simplified extension for new crops and regions

---

## Project Status

This project is under active development.

Current implemented scope:

- Soil correction (calagem)
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)

Planned future directions:

- Micronutrient modeling
- Regional parameter sets
- Versioned bulletin support
- API interface layer

---

## License

Licensed under the Apache License 2.0.  
See the `LICENSE` file for details.

---

## Authors

Luiz Henrique de Lima Peguin  
Pedro Henrique Escaranaro Brasil  

---

## Contributing

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