print("빵, 속 재료 순으로 선택하세요. 목록에서 숫자만 선택해주세요.\n\n\
      목록: 치아바타: 1, 식빵: 2, 잉글리쉬 머핀: 3 \n\
            쉬림프: 1, 치킨: 2, 포크 바베큐: 3 \n")

sd=[]
price=[]

def bbang():
    b=int(input("빵을 골라주세요. :"))
    if b == 1:
        print("\n빵을 치아바타로 선택하였습니다.")
        b = '치아바타'
        sd.append(b)
        price.append(2000)
    elif b == 2:
        print("\n빵을 식빵을 선택하였습니다.")
        b = '식빵'
        sd.append(b)
        price.append(1500)
    elif b == 3:
        print("\n빵을 잉글리쉬 머핀을 선택하였습니다.")
        b = '잉글리쉬 머핀'
        sd.append(b)
        price.append(2500)
    else:
        print("\n다시 입력해 주십시오.")
        bbang()

def main():
    m=int(input("추가 속 재료를 골라주세요. :"))
    if m == 1:
        print("\n추가 속 재료를 쉬림프로 선택하셨습니다.")
        m = '쉬림프'
        sd.append(m)
        price.append(2000)
    elif m == 2:
        print("\n추가 속 재료를 치킨으로 선택하였습니다.")
        m = '치킨'
        sd.append(m)
        price.append(2500)
    elif m == 3:
        print("\n추가 속 재료를 포크 바베큐로 선택하였습니다.")
        m = '포크 바베큐'
        sd.append(m)
        price.append(3000)
    else :
        print("\n다시 입력해 주십시오.")
        main()

def steave():
    qw=input("\n매장에서 드실건가요? 포장 시 추가금액 200원입니다. Y/N : ")
    if 'Y' in qw or 'Yes' in qw or 'yes' in qw or 'y' in qw :
        print("매장이용 시 마스크를 착용해 주십시오.\n")

    elif 'N' in qw or 'n' in qw or 'No' in 'no' in qw:
        print("포장을 선택하셨습니다.")
        price.append(200)
        result=sum(price)
        print("최종가격은 ",result,"원 입니다.\n")
    else :
        print("\n다시 시도해 주십시오.\n")
        steave()
def ban():
    ase=input("결제방식을 선택해 주십시오.\n 현금/카드 : ")
    if '현금' in ase:
        print("\n현금을 투입구에 올바르게 넣어주십시오.")
    elif '카드' in ase:
        print("\n카드를 리더기에 올바르게 꽂아주십시오.\n")
    else :
        ban()

def dea():
    print("결제중 입니다.\n")
    import time
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)

bbang()
main()
print("\n주문확인", sd)
result=sum(price)
print(result,"원 입니다.")
steave()
ban()
dea()
print("\n결제가 완료되었습니다.\n감사합니다. 또 오세요.")
