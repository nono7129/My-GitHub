class Car:
    def __init__(self, manufacturer, model, price, year):
        self.manufacturer = manufacturer
        self.model = model
        self.price = price
        self.year = year

    def __str__(self):
        return f"{self.manufacturer} {self.model} {self.price}만원 {self.year}년"

car1 = Car("현대", "그랜저", 4500, 2020)
car2 = Car("벤츠", "E클래스", 13000, 2023)
car3 = Car("기아", "EV6", 6000, 2024)
car4 = Car("포르쉐", "카이엔", 15000, 2024)

cars = [car1, car2, car3, car4]

print(f"총 {len(cars)}대의 차가 있습니다.\n")

for car in cars:
    print(car)
