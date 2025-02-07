import tkinter as tk

# 各セルのサイズ
cellSize = 20  # 各セルの幅と高さ
visibleColumns = 16  # 表示する列数
currentOffset = 0  # 現在の表示開始列
characterX = 3  # キャラクターの初期位置（横の位置）
characterY = 0  # キャラクターのジャンプ高さ
isGameOver = False  # ゲームオーバーフラグ
retryButton = None  # Retryボタン
isJumping = False  # ジャンプ中かどうか

# ステージデータ
stage = [
    ["　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　"],
    ["　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","◉","　"],
    ["　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","◹","亅","　"],
    ["　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","亅","　"],
    ["　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","⍰","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","▨","▨","▨","▨","▨","▨","▨","▨","　","　","　","▨","▨","▨","⍰","　","　","　","　","　","　","　","　","　","　","　","　","　","　","⍰","　","　","　","　","　","　","　","　","　","　","　","▨","▨","▨","　","　","　","　","▨","⍰","⍰","▨","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","亅","　"],
    ["　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","亅","　"],
    ["　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","亅","　"],
    ["　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","↓","↓","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","亅","　"],
    ["　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","⍰","　","　","　","▨","⍰","▨","⍰","▨","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","＝","＝","　","　","　","　","　","　","　","　","　","＝","＝","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","▨","⍰","▨","　","　","　","　","　","　","　","　","　","　","　","　","　","　","▨","　","　","　","　","　","▨","▨","　","　","　","　","⍰","　","　","⍰","　","　","⍰","　","　","　","　","　","▨","　","　","　","　","　","　","　","　","　","　","▨","▨","　","　","　","　","　","■","　","　","■","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","▨","▨","⍰","▨","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","亅","　"],
    ["　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","＝","＝","　","　","　","　","　","　","｜","｜","　","　","　","　","　","　","　","　","　","｜","｜","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","亅","　"],
    ["　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","＝","＝","　","　","　","　","　","　","　","　","｜","｜","　","　","　","　","　","　","｜","｜","　","　","　","　","　","　","　","　","　","｜","｜","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","＝","＝","　","　","　","　","　","　","　","　","　","　","　","　","　","　","＝","＝","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","亅","　"],
    ["　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","▲","　","　","　","　","　","　","｜","｜","　","　","　","　","　","　","　","　","｜","｜","　","　","　","　","　","　","｜","｜","　","　","　","　","　","▲","　","　","　","｜","｜","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","▲","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","▲","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","｜","｜","　","　","　","　","　","　","　","　","　","　","　","　","　","　","｜","｜","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","　","■","　"],
    ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
    ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
]

def getFontSize(character):
    """文字ごとにフォントサイズを設定"""
    if character in {"□", "■",}:
        return 40  # □, ■ はサイズ40
    elif character == "▨":
        return 19  # ▨はサイズ19
    elif character == {"◹","▲"}:
        return 21  # ◹はサイズ21
    elif character == "⍰":
        return 16  # ⍰はサイズ16
    else:
        return 14  # その他の文字はサイズ14

def findFloor(stage, characterX):
    """キャラクターがいる位置での床の高さを見つける"""
    for y in range(len(stage)):
        if stage[y][characterX] == "□":
            return y
    return None  # 床がない場合は None を返す

def showRetryButton():
    """Retry ボタンを1回だけ表示"""
    global retryButton
    if retryButton:
        return
    retryButton = tk.Button(root, text="Retry", command=resetGame, font=("Helvetica", 16))
    retryButton.pack(pady=20)


def resetGame():
    """ゲームをリセット"""
    global characterX, currentOffset, isGameOver, isGameClear, retryButton, isJumping, characterY
    characterX = 3  # キャラクターの初期位置
    currentOffset = 0  # スクロールをリセット
    isGameOver = False  # ゲームオーバーを解除
    isGameClear = False  # **ゲームクリアを解除**
    isJumping = False  # ジャンプ状態リセット
    characterY = 0  # 落下リセット
    
    if retryButton:
        retryButton.destroy()  # Retryボタンを削除
        retryButton = None

    renderStage(canvas, stage, currentOffset, characterX)  # **ステージを再描画**



def isObstacle(stage, x, y):
    """指定された座標が障害物かどうかを判定"""
    if x < 0 or x >= len(stage[0]) or y < 0 or y >= len(stage):
        return True  # 範囲外は障害物とみなす
    return stage[y][x] in {"□", "■", "｜", "＝", "⍰", "▨"}

isGameClear = False  

def checkGameClear():
    """キャラクターがクリア条件を満たしているかチェック"""
    global isGameClear
    clearY = len(stage) - 4  # 下から4マス目のY座標
    if stage[clearY][characterX] == "亅":
        isGameClear = True
        renderStage(canvas, stage, currentOffset, characterX)  # クリア表示


def renderStage(canvas, stage, offset, characterPosition):
    """ステージを描画"""
    global isGameOver, isGameClear
    canvas.delete("all")  # 画面をクリア

    startCol = offset
    endCol = offset + visibleColumns

    for y, row in enumerate(stage):
        for x, cell in enumerate(row[startCol:endCol]):
            xCenter = (x * cellSize) + cellSize / 2
            yCenter = (y * cellSize) + cellSize / 2
            fontSize = getFontSize(cell)
            canvas.create_text(xCenter, yCenter, text=cell, font=("Helvetica", fontSize))

    if isGameOver:
        canvas.create_text(canvasWidth // 2, canvasHeight // 3, text="GAME OVER", font=("DotGothic16", 30), fill="red")
        showRetryButton()
        return

    if isGameClear:
        canvas.create_text(canvasWidth // 2, canvasHeight // 3, text="CLEAR!", font=("DotGothic16", 30), fill="green")
        showRetryButton()
        return

    # **キャラクターを描画**
    charScreenX = characterPosition - offset
    if 0 <= charScreenX < visibleColumns:
        floorY = findFloor(stage, characterPosition)
        if floorY is None:
            isGameOver = True
            renderStage(canvas, stage, offset, characterPosition)
            return
        yCenter = ((floorY - characterY - 1) * cellSize) + cellSize / 2
        xCenter = (charScreenX * cellSize) + cellSize / 2
        canvas.create_text(xCenter, yCenter, text="⬤", font=("Helvetica", 16), fill="red")

def moveCharacterRight(event):
    """キャラクターを右に移動"""
    global characterX, currentOffset, isGameOver
    if isGameOver:
        return

    if characterX < len(stage[0]) - 1:
        targetX = characterX + 1
        floorY = findFloor(stage, targetX)

        if floorY is None or not isObstacle(stage, targetX, floorY - characterY - 1):
            characterX += 1
            if characterX >= currentOffset + visibleColumns // 2:
                currentOffset += 1
            
            checkGameClear()
            fall_step()

    renderStage(canvas, stage, currentOffset, characterX)

def moveCharacterLeft(event):
    """キャラクターを左に移動"""
    global characterX, currentOffset, isGameOver
    if isGameOver:
        return

    if characterX > 0:
        targetX = characterX - 1
        floorY = findFloor(stage, targetX)

        if floorY is None or not isObstacle(stage, targetX, floorY - characterY - 1):
            characterX -= 1
            if characterX < currentOffset:
                currentOffset = max(0, currentOffset - 1)
            
            checkGameClear()
            fall_step()

    renderStage(canvas, stage, currentOffset, characterX)

def jumpCharacter(event):
    """キャラクターをジャンプさせる"""
    global isJumping, characterY, isGameOver
    if isGameOver or isJumping:
        return
    isJumping = True

    floorY = findFloor(stage, characterX)
    if floorY is None:
        isGameOver = True
        renderStage(canvas, stage, currentOffset, characterX)
        return

    jumpOffsets = [1, 2, 3, 4, 5]

    def jump_step(index):
        """ジャンプの1ステップ"""
        global characterY
        if index < len(jumpOffsets):
            targetY = floorY - jumpOffsets[index] - 1
            if isObstacle(stage, characterX, targetY):
                fall_step()
                return
            characterY = jumpOffsets[index]
            renderStage(canvas, stage, currentOffset, characterX)
            root.after(80, lambda: jump_step(index + 1))
        else:
            fall_step()

    jump_step(0)

def fall_step():
    """キャラクターが床に着地するまで下降（穴に落ちたらゲームオーバー）"""
    global characterY, isJumping, isGameOver

    if isGameOver:  # すでにゲームオーバーなら処理を止める
        return

    floorPos = findFloor(stage, characterX)

    if floorPos is None:
        characterY += 1  # 落下を進める
        if characterY > 5:  # 一定距離落下したらゲームオーバー
            isGameOver = True
            renderStage(canvas, stage, currentOffset, characterX)
            return
        else:
            root.after(70, fall_step)  # 次の落下ステップ
    else:
        # **地面がある場合：通常の落下処理**
        if floorPos - characterY - 1 > 0 and not isObstacle(stage, characterX, floorPos - characterY):
            characterY -= 1  # 徐々に落下
            root.after(70, fall_step)  # 次の落下処理をスケジュール
        else:
            characterY = 0  # 地面に着地したら落下終了
            isJumping = False
            renderStage(canvas, stage, currentOffset, characterX)



# Tkinter ウィンドウの作成
root = tk.Tk()
root.title("ステージ表示")

# キャンバスの作成
canvasWidth = visibleColumns * cellSize
canvasHeight = len(stage) * cellSize
canvas = tk.Canvas(root, width=canvasWidth, height=canvasHeight, bg="white")
canvas.pack()

# イベントのバインド
root.bind("<Left>", moveCharacterLeft)  # 左キー
root.bind("<Right>", moveCharacterRight)  # 右キー
root.bind("<Up>", jumpCharacter)  # 上キーでジャンプ

# 初期描画
renderStage(canvas, stage, currentOffset, characterX)

# メインループ開始
root.mainloop()