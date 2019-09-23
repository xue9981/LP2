# 与えられたファイルにデータを記録する
# データの種類は人名、年齢、出身国、犯罪歴の有無
def save_data(file_name, name, age, country, criminal):
    # 与えられたファイルを開き,、追記モードにする
    f = open('database.txt', 'a')

    # 順番に人名、年齢、出身国、犯罪歴を記入する
    f.write("name: " + name.strip().title() + ", ")
    f.write("age: " + str(age) + ", ")
    f.write("country: " + country.title() + ", ")
    f.write("criminal record: " + criminal.strip() + "\n")
    print(name.title() + "さん、あなたについての記録が完了しました。\n")

    # ファイルを閉じる
    f.close()
    

# 入国調査機の質問(1回のテンプレ）
def survey():
    # 人名、年齢、出身国、犯罪歴について登録する。
    # ふさわしくない回答があった場合では三回までに入力し直すことができ、
    # 一つの質問に三回以上誤答した場合では強制送還する
    answers_count = [1, 1, 1, 1]
    person = {'name': '', 'age': '', 'country': '', 'criminal': ''}
    check_sheet = {'name': False, 'age': False, 'country': False, 'criminal': False}
    forced_repatiration = False
    FORCED=4
    
    while True:
        if FORCED in answers_count:
            forced_repatiration = True
            break
        elif False not in check_sheet.values():
            break
        person['name'] = input("Please enter your name: ")
        check_sheet['name'] = True
        person['age'] = input("Please enter your age: ")
        try:
            if int(person['age']) > 120:
                answers_count[1]+=1
                continue
            else:
                check_sheet['age'] = True
        except ValueError:
            answers_count[1]+=1
            continue
        person['country'] = input("Please enter your origin: ")
        check_sheet['country'] = True
        person['criminal'] = input("Any history of being convicted of a crime? (Not only in the U.S.)"
                     + " (yes/no) ")
        if person['criminal'] == 'yes' or person['criminal'] == 'no':
            check_sheet['criminal'] = True
        else:
            answers_count[3]+=1
            continue

    if forced_repatiration == True:
        forced(person['name'], person['country'])
    else:
        save_data("database.txt", person['name'], person['age'], person['country'], person['criminal'])

# 強制送還を行う
def forced(name, country):
    print("親愛なる " + name.title() + "さん, 残念ながらあなたは私達の国を訪ねるにはふさわしくない" +
          "と判断されましたために、あなたを" + country.title() + "に強制送還することに決まりました.\n")

