class Calculator:
    def add(self, x: int, y: int) -> int:
        return x + y

    def subtract(self, x: int, y: int) -> int:
        return x - y

    def multiply(self, x: int, y: int) -> int:
        return x * y

    def divide(self, x: int, y: int) -> float:
        if y == 0:
            raise ZeroDivisionError("Divide by zero isn't possible")
        return x / y

    def calculate_discount(self, price: float, discount: float) -> float:
        if price < 0:
            raise ValueError("Price cann't be negative")
        if not 0 <= discount <= 100:
            raise ValueError("Discount should be in range[0, 100]")
        return price * (1 - discount / 100)
