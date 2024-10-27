class Product:
    def __init__(self,name,sku):
        self.name = name
        self.sku = sku
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value
    @property
    def sku(self):
        return self._sku
    @sku.setter
    def sku(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("SKU must be a non-empty string")
        self._sku = value
    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.sku == other.sku
    def __hash__(self):
        return hash(self.sku)

product1 = Product("Laptop", "12345")
product2 = Product("Notebook", "12345")
product3 = Product("Tablet", "67890")

# Сравнение товаров
print(product1 == product2)  # True
print(product1 == product3)  # False

# Проверка уникальности в множестве
product_set = {product1, product2, product3}
print(len(product_set))  # 2, т.к. product1 и product2 считаются одинаковыми
