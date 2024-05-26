def donut_order_system():
    total_donuts = 30
    order_number = 1
    
    while total_donuts > 0:
        print(f"[남은 도넛 : {total_donuts}]")
        try:
            order = int(input("도넛을 몇 개 구입하시겠습니까? "))
            if order < 1:
                raise ValueError
        except ValueError:
            print("잘못된 값을 입력하였습니다.")
            continue
        
        if order > 6:
            print("한 사람 당 최대 6개의 도넛만 구매할 수 있습니다.")
        elif order > total_donuts:
            print("오늘 준비한 도넛이 매진되었습니다.")
            break
        else:
            total_donuts -= order
            print(f"[대기번호 {order_number}] {order}개 구입이 완료되었습니다.")
            order_number += 1
    
    if total_donuts == 0:
        print("오늘 준비한 도넛이 매진되었습니다.")

donut_order_system()
