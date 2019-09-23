from savedata import save_data, survey, forced

# 入国審査を行う
active = True
print("自由と民主の国、アメリカへようこそ！\n" +
          "皆さんが入国する前に、いくつかの質問に答えていただきます。\n" +
          "協力のほど、よろしくお願いいたします。\n")
     
while active == True:
     survey()
     
     while True:
         active = input("次にお待ちの方はいますか？ (yes/no) ")
         if active == 'yes':
             active = True
             break
         elif active == 'no':
             active = False
             break
         else:
             continue

print("定時になりましたために今日の業務を終了します。\n" +
      "調査ご協力のほどありがとうございました。\n")
