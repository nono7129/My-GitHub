class Laptop:
    def __init__(self, brand, deal_type, price, year_of_release):
        self.brand = brand
        self.deal_type = deal_type
        self.price = price
        self.year_of_release = year_of_release

    def show_detail(self):
        if self.deal_type == "구매":
            print("{0}에 {1}을(를) {2}에 구매하였습니다.".format(self.year_of_release, self.brand, self.price))
        elif self.deal_type == "대여":
            print("{0}에 {1}을(를) {2}에 대여하였습니다.".format(self.year_of_release, self.brand, self.price))
        else:
            print("올바르지 않은 거래 유형입니다.")


laptops = []
laptop1 = Laptop("LG", "구매", "200만원", "2023년도")
laptop2 = Laptop("삼성", "구매", "240만원", "2023년도")
laptop3 = Laptop("Apple", "구매", "180만원", "2022년도")
laptop4 = Laptop("레노버", "대여", "5만원", "2021년도")

laptops.append(laptop1)
laptops.append(laptop2)
laptops.append(laptop3)
laptops.append(laptop4)

print("총 {0}대의 노트북이 있습니다.".format(len(laptops)))
for laptop in laptops:
    laptop.show_detail()