# 被調査者についてのバカンス希望地を登録する辞書
rest_area = {}

# バカンスにて行きたい情報について収集する
poll_active = True
while poll_active == True:
    name = input("Please fill out your name: ")
    area = input("If you could visit one place in the world,\
 where would you go? ")
    # データ登録
    rest_area[name] = area

    # 次の回答者の有無について確認する
    while True:
        repeat = input("Is there anyone waiting for poll? (yes/no) ")
        # (no)いなければpoll_acgiveをFalseにし、一番外のwhile文を抜けられるようにする
        if repeat == 'no':
            poll_active = False
            break
        # (yes)いれば外側のループを継続させる
        elif repeat == 'yes':
            break
        # 入力が上の両パターンのいずれにも当てはめなければ再度確認する

    # 整形のための改行
    print()
    
# 調査結果表示
print("--- Poll result ---")
for name, area in rest_area.items():
    print(name.title() + " would like to go to " + area.title() + ".")

    

