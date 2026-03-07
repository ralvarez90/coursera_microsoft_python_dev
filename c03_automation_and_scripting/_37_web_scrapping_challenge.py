"""
RETO: Escriba un script que utilize BeautifulSoup para extraer el nombre del producto, el precio
y la descripción de este html.
"""
from typing import Any

from bs4 import BeautifulSoup


def get_product_info(html_txt: str) -> dict[str, Any] | None:
    soup = BeautifulSoup(html_txt, "html.parser")
    product = soup.find('div', class_='product')

    return {
        'name': product.select_one('h1').text,
        'price': product.select_one('p.price').text,
        'description': product.select_one('p.description').text,
    } if product else None


html_content: str = """
<div class="product">
  <h1>Awesome Headphones</h1>
  <p class="price">$99.99</p>
  <p class="description">These headphones offer amazing sound quality!</p>
</div>
"""

result: dict[str, Any] | None = get_product_info(html_content)
print(f'Name        : {result.get("name")}')
print(f'Price       : {result.get("price")}')
print(f'Description : {result.get("description")}')
