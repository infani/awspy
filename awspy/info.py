import configparser

def version():
    config = configparser.ConfigParser()
    config.read("pyproject.toml")
    version = config['tool.poetry']['version']
    return version