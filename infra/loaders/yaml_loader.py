from importlib import resources
import yaml

def carregar_modelo(boletim: str, cultura: str, nutriente:str):
    pacote_base = f"fertpy.knowledge.{boletim}.{cultura}"
    nome_arquivo = f"{nutriente}.yaml"

    with resources.files(pacote_base).joinpath(nome_arquivo).open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)
