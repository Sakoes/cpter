from fastapi.testclient import TestClient

from app.core.config import settings

def test_read_item(
    client: TestClient, superuser_token_headers: dict
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/{settings.HEALTH_ENDPOINT}/", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content == {"This is the health endpoint"}
