rest = 15;

def showRest():
    print("残り%d個です。" % rest)

def finish():
    return rest <= 0

def select():
    if rest == 3: return 2
    if rest == 2: return 1
    if rest == 1: return 1

    v = rest % 4
    if v == 0: return 3
    if v == 1: return 1
    if v == 2: return 1
    if v == 3: return 2

if __name__ == "__main__":
    print("%d個でゲームを開始します。" % rest)

    while True:
        # ユーザーのターン
        count = int(input("何個取りますか？(1〜3)"))
        if (count > 3):
            print("入力値の範囲は 1 〜 3 です。")
            continue
        rest -= count
        showRest()
        if finish():
            print("あなたの負けです。")
            break

        # コンピューターのターン
        count = select()
        print("%d個取りました" % count)
        rest -= count
        showRest()
        if finish():
            print("あなたの勝ちです。")
            break
