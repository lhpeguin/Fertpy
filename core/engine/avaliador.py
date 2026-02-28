from fertpy.core.domain.classe import Classe
from fertpy.core.domain.criterio import Criterio
from fertpy.core.domain.intervalo import Intervalo
from fertpy.core.domain.recomendacao import Recomendacao


class Avaliador:

    @staticmethod
    def avaliar(
        criterios: list[Criterio],
        contexto: dict[str, float],
        nutriente: str,
        unidade: str,
        observacoes: list[str] | None = None,
        fonte: dict | None = None
    ) -> Recomendacao:

        for criterio in criterios:
            for variavel, intervalo in criterio.condicoes.items():
                
                if variavel not in contexto:
                    break

                valor = contexto[variavel]

                if isinstance(intervalo, Intervalo):
                    
                    if not isinstance(valor, (int, float)):
                        break

                    if not intervalo.contem(valor):
                        break
                else:
                    if valor != intervalo:
                        break

            else:
                classe_final = criterio.classe or Classe(nome="dose")

                obs_final = []

                if observacoes:
                    obs_final.extend(observacoes)
                
                if criterio.observacoes:
                    obs_final.append(criterio.observacoes)
                
                obs_final = obs_final or None

                return Recomendacao(
                    nutriente=nutriente,
                    dose=criterio.recomendacao,
                    unidade=unidade,
                    classe=classe_final,
                    observacoes=obs_final,
                    fonte=fonte
                ) 
            
        raise ValueError("Nenhum critério compatível encontrado.")
