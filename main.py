from src.utils.config import load_workspace_config
from src.utils.config import WorkspaceConfig

def main() -> None:
    config: WorkspaceConfig = load_workspace_config()

    print("----" * 22)
    for ws in config.workspaces:
        print(f"Workspace Name: {ws.name}")
        print(f"Workspace URL: {ws.url}")
        print("Workspace Token: xxxxxxx")
        print("----" * 22)


if __name__ == "__main__":
    main()
