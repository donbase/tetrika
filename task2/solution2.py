from bs4 import BeautifulSoup
import httpx
import asyncio
from collections import defaultdict
from string import ascii_uppercase
import csv
from time import perf_counter


russian_uppercase = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

animal_counter = defaultdict(int)
base_url = "https://ru.wikipedia.org"
start_page = httpx.get(
    "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
).text
i = 0


async def get_data(page: str, animal_counter: defaultdict) -> str | None:
    soup = BeautifulSoup(page, "html.parser")
    container = soup.find(id="mw-pages")
    next_url = container.find("a", string="Следующая страница")
    next_page = None
    if next_url:
        next_url = base_url + next_url["href"]
        async with httpx.AsyncClient() as session:
            response = await session.get(next_url)
            if response.is_success:
                next_page = response.text

    targets_div = container.find_all("div", class_="mw-category-group")
    for elem in targets_div:
        char = elem.find("h3").text
        ul_element = elem.find("ul")
        animal_counter[char] += len(ul_element.find_all("li"))

    return next_page


async def main(page: str) -> None:
    while page:
        page = await get_data(page, animal_counter)


if __name__ == "__main__":
    #start = perf_counter()
    asyncio.run(main(start_page))

    #print(perf_counter() - start)
    letters = russian_uppercase + ascii_uppercase
    rows = [{"char": char, "val": animal_counter[char]} for char in letters]
    with open("output.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["char", "val"])
        writer.writerows(rows)
    #print(animal_counter)
