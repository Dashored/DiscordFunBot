from dataclasses import dataclass
import tomllib


@dataclass
class Settings:
    prefix:str
    rps:dict

    @classmethod
    def load_from_config(cls):
        with open("config/cfg.toml","rb") as config_file:
            toml_data = tomllib.load(config_file).get("settings")
            return cls(**toml_data)
        

if __name__ == "__main__":
    settings = Settings.load_from_config()

    print(settings.prefix)