from fertpy.infra.parsing.intervalo import parse_intervalo


def parse_condicao(valor):
    if isinstance(valor, (int, float)):
        return parse_intervalo(str(valor))
    
    if isinstance(valor, str):
        try:
            return parse_intervalo(valor)
        except ValueError:
            return valor.strip()
    
    return valor