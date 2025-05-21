from pathlib import Path
import json
from dataclasses import dataclass

@dataclass
class Workspace:
    name: str
    url: str
    token: str
@dataclass
class WorkspaceConfig:
    workspaces: list[Workspace]

def load_workspace_config(config_file: Path = Path("config/workspaces.json")) -> WorkspaceConfig:
    if not config_file.exists():
        raise FileNotFoundError(f"Configuration file {config_file} not found.")
    with config_file.open("r", encoding="utf-8") as f:
        try:
            config_data: dict[str,list[dict[str,str]]] = json.load(f)
            workspaces: list[Workspace] = [Workspace(**ws) for ws in config_data["workspaces"]]
            return WorkspaceConfig(workspaces=workspaces)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing JSON configuration file: {e}")