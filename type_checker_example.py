from typing import Dict


avengers = {"Steve Rogers": "Captian America"}
def update_mapping(names: Dict) -> None:
    names.update({"Tony Stark": "The Ironman"})
    return names
