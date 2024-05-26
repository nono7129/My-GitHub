def std_bmr(s, weight, height, age):
    if s == 'male':
        return 66.47 + (13.75 * weight) + (5 * height) - (6.76 * age)
    else:
        return 665.1 + (9.56 * weight) + (1.85 * height) - (4.68 * age)
    

s = 'male'      
weight = 62       
height = 178      
age = 20         

bmr = std_bmr(s, weight, height, age)
print(f"당신의 기초대사량은 {bmr} 입니다.")