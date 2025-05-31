import pytest
from task2.solution2 import get_data
from unittest.mock import AsyncMock, patch
from collections import defaultdict


res_1 = defaultdict(int, {"А": 200})
res_2 = defaultdict(int, {"А": 98, "Б": 102})
with open("tests/samples/res1.html", "r", encoding="utf-8") as file:
    response_1 = file.read()

with open("tests/samples/res2.html", "r", encoding="utf-8") as file:
    response_2 = file.read()


@pytest.mark.parametrize(
    "path, response, res_cnt",
    [
        ("tests/samples/file_test_1.html", response_1, res_1),
        ("tests/samples/file_test_2.html", response_2, res_2),
    ],
)
@pytest.mark.asyncio
async def test_get_data(path, response, res_cnt):
    with open(path, "r", encoding="utf-8") as file:
        html_content = file.read()

    mock_response = AsyncMock()
    mock_response.text = response

    mock_get = AsyncMock(return_value=mock_response)

    mock_client_instance = AsyncMock()
    mock_client_instance.get = mock_get

    mock_context_manager = AsyncMock()
    mock_context_manager.__aenter__.return_value = mock_client_instance

    with patch("httpx.AsyncClient", return_value=mock_context_manager):
        counter = defaultdict(int)
        next_page_html = await get_data(html_content, counter)
        assert counter == res_cnt
        assert next_page_html == response
