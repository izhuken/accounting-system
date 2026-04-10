from os import path


def assets(uri: str) -> str:
    return path.join("src/presentation/assets", uri)
