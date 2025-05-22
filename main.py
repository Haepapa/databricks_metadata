from src.utils.config import load_workspace_config
from src.utils.config import WorkspaceConfig
from src.api.catalog import get_catalogs
import json

def main() -> None:
    # load the workspace configuration
    config: WorkspaceConfig = load_workspace_config()

    print("----" * 22)
    for ws in config.workspaces:
        print(f"Workspace Name: {ws.name}")
        print(f"Workspace URL: {ws.url}")
        print("Workspace Token: xxxxxxx")
        print("----" * 22)

        print(json.dumps(get_catalogs(ws.url, ws.token), indent=2))
        print("----" * 22)

if __name__ == "__main__":
    main()
