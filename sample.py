#インポート
import sendame

#ゲームを作成
sd = sendame.Sendame()
#プレイヤーを受け取り、名前を設定
player_1 = sd.player_1
player_1.name = "player_1"
player_2 = sd.player_2
player_2.name = "player_2"

#ゲームの処理例
while(1):
    #ターン数を表示
    print(f"ターン : {sd.turn}")
    #一人目の入力
    while(1):
        try:
            select = input("プレイヤー1 : タメ,バリア,ハーのいずれかを入力 : ")
            sd.action(player_1,select)
            break
        except:
            print("無効な入力")
    
    #二人目の入力
    while(1):
        try:
            select = input("プレイヤー2 : タメ,バリア,ハーのいずれかを入力 : ")
            sd.action(player_2,select)
            break
        except:
            print("無効な入力")
    #プレイヤーの選択を表示
    print(f"player_1 : {player_1.action}\nplayer_2 : {player_2.action}")
    #勝敗判定
    result = sd.showdown()
    #None(勝者無し)でなければ勝者を表示して終了
    if result != None:
        input(f"勝者 : {result.name}")
        break