class ShoppingCart:
    def __init__(self, emp_discount=None):
        self.total = 0
        self.item_count = 0
        self.items = []
        self.emp_discount = emp_discount

    def add_item(self, name, price, quantity=1):
        for _ in range(quantity):
            self.items.append((name, price))
            self.total += price
            self.item_count += 1

    def remove_item(self, name):
        removed_items = []
        updated_items = []
        for item in self.items:
            if item[0] == name:
                self.total -= item[1]
                self.item_count -= 1
                removed_items.append(item)
            else:
                updated_items.append(item)
        self.items = updated_items
        return removed_items

    def mean_item_price(self):
        return self.total / self.item_count

    def median_item_price(self):
        if self.item_count == 0:
            return 0
        sorted_prices = sorted([item[1] for item in self.items])
        mid_index = self.item_count // 2
        if self.item_count % 2 == 0:
            mid_index -= 1
            return (sorted_prices[mid_index] + sorted_prices[mid_index + 1]) / 2
        else:
            return sorted_prices[mid_index]

    def apply_discount(self):
        if self.emp_discount:
            self.base = self.total
            self.total = self.total - ((self.total * self.emp_discount) / 100)
        return self.total

    def void_last_item(self):
        if self.item_count > 0:
            last_item = self.items.pop()
            self.base -= last_item[1]
            self.item_count -= 1
        return self.base

    def get_item_count(self):
        return self.item_count

    def get_total(self):
        return self.total

    def display_items(self):
        for item in self.items:
            print(f"{item[0]} - ${item[1]}")

    def empty_cart(self):
        self.total = 0
        self.item_count = 0
        self.items = []
