
import requests
from typing import Any

def get_catalogs(workspace_url: str, token: str) -> list[dict[str, Any]]:
    url: str = f"{workspace_url}/api/2.1/unity-catalog/catalogs"
    headers: dict[str, str] = {
        "Authorization": f"Bearer {token}"
    }
    resp: requests.Response = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json().get("catalogs", [])
