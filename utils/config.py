import yaml


def get_config():
    # Loading the config.yaml file
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f) 