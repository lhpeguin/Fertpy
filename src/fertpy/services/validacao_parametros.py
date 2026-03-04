# Copyright 2026 Luiz Henrique de Lima Peguin
# and Pedro Henrique Escaranaro Brasil
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

import unicodedata

from fertpy.utils.parametros import extrair_parametros
from fertpy.core.domain.exceptions import ParametroInvalidoError


def normalizar(texto: str) -> str:
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    return texto


def validar_parametros(boletim: str, cultura: str, finalidade: str):

    parametros = extrair_parametros()

    boletim_norm = normalizar(boletim)
    cultura_norm = normalizar(cultura)
    finalidade_norm = normalizar(finalidade)

    boletins_validos = {
        normalizar(b): b for b in parametros.keys()
    }

    if boletim_norm not in boletins_validos:
        raise ParametroInvalidoError(
            "Boletim",
            boletim,
            list(parametros.keys())
        )
    
    boletim_real = boletins_validos[boletim_norm]

    culturas_dict = parametros[boletim_real]
    culturas_validas = {
        normalizar(c): c for c in culturas_dict.keys()
    }

    if cultura_norm not in culturas_validas:
        raise ParametroInvalidoError(
            "Cultura",
            cultura,
            list(culturas_dict.keys())
        )
    
    cultura_real = culturas_validas[cultura_norm]

    finalidades_validas = {
        normalizar(f): f for f in culturas_dict[cultura_real]
    }

    if finalidade_norm not in finalidades_validas:
        raise ParametroInvalidoError(
            "Finalidade",
            finalidade,
            list(culturas_dict[cultura_real])
        )
    
    return (
        boletim_real,
        cultura_real,
        finalidades_validas[finalidade_norm]
    )
