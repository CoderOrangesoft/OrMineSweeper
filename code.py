import time
import random
import pgzrun
'''
1.时间库
2.随机数库
3.pygame库
'''
with open('startText.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
# 导入库

ver = 'Build22w22a'
# 声明版本

state = 'start'
posX = 0
posY = 0
# 游戏状态

with open('startText2.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
print('版本:', ver)
with open('startText3.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
# 初始界面

allTell = '''更新日志:1.优化内存'''
print('<公告>扫雷', ver, ':', allTell)
blocks = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
buttons = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], ['test', 'test', 'test']]
for i in range(9):
    defaultSweep = random.randint(0, 8)
    blocks[i][defaultSweep] = 9
while True:
    sweep = random.randint(0, 8)
    sweepI = random.randint(0, 8)
    if blocks[sweepI][sweep] == 9:
        continue
    else:
        blocks[sweepI][sweep] = 9
        break
back = Actor('back')
block = Actor('b0')
button = Actor('button')
# 绘制角色

for blocksPainter in range(9):
    for blocksPainter1 in range(9):
        if blocks[blocksPainter][blocksPainter1] != 9:
            aroundSweep = blocks  # ←周围雷数
            # ↓渲染中间的方块
            if blocksPainter > 0 and blocksPainter < 8 and blocksPainter1 > 0 and blocksPainter1 < 8:
                if blocks[blocksPainter][blocksPainter1] == 0:
                    if blocks[blocksPainter][blocksPainter1 - 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter][blocksPainter1 + 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter - 1][blocksPainter1 - 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter - 1][blocksPainter1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter - 1][blocksPainter1 + 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter + 1][blocksPainter1 - 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter + 1][blocksPainter1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter + 1][blocksPainter1 + 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    block.y = blocksPainter * 50 + 25
                    block.x = blocksPainter1 * 50 + 25
                # ↓顶层方块渲染
            if blocksPainter == 0:
                if blocksPainter1 == 0:
                    if blocks[blocksPainter][blocksPainter1 + 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter + 1][blocksPainter1 + 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter + 1][blocksPainter1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    block.y = blocksPainter * 50 + 25
                    block.x = blocksPainter1 * 50 + 25
                if blocksPainter1 > 0 and blocksPainter1 < 8:
                    if blocks[blocksPainter][blocksPainter1 + 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter + 1][blocksPainter1 + 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter + 1][blocksPainter1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter][blocksPainter1 - 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter + 1][blocksPainter1 - 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    block.y = blocksPainter * 50 + 25
                    block.x = blocksPainter1 * 50 + 25
                if blocksPainter1 == 8:
                    if blocks[blocksPainter][blocksPainter1 - 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter + 1][blocksPainter1 - 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter - 1][blocksPainter1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                # ↓底层方块渲染
            if blocksPainter == 8:
                if blocksPainter1 == 0:
                    if blocks[blocksPainter][blocksPainter1 + 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter - 1][blocksPainter1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter - 1][blocksPainter1 + 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                if blocksPainter1 > 0 and blocksPainter1 < 8:
                    if blocks[blocksPainter][blocksPainter1 - 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter - 1][blocksPainter1 - 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter - 1][blocksPainter1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter][blocksPainter1 + 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter - 1][blocksPainter1 + 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                if blocksPainter1 == 8:
                    if blocks[blocksPainter][blocksPainter1 - 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter - 1][blocksPainter1 - 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter - 1][blocksPainter1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                # ↓左侧方块渲染
            if blocksPainter1 == 0:
                if blocksPainter > 0 and blocksPainter < 8:
                    if blocks[blocksPainter][blocksPainter1 + 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter - 1][blocksPainter1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter - 1][blocksPainter1 + 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter + 1][blocksPainter1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter + 1][blocksPainter1 + 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
            # ↓右侧方块渲染
            if blocksPainter1 == 8:
                if blocksPainter > 0 and blocksPainter < 8:
                    if blocks[blocksPainter][blocksPainter1 - 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter - 1][blocksPainter1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter - 1][blocksPainter1 - 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter + 1][blocksPainter1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
                    if blocks[blocksPainter + 1][blocksPainter1 - 1] == 9:
                        aroundSweep[blocksPainter][blocksPainter1] += 1
            # ↑如果不是雷
# blocks[0][0] = 4
# 初始化雷区

HEIGHT = 450
WIDTH = 450
# 窗口绘制


def draw():
    screen.blit('back', [0, 0])
    blocksPainter = 0
    blocksPainter1 = 0
    for blocksPainter in range(9):
        for blocksPainter1 in range(9):
            if buttons[blocksPainter][blocksPainter1] == 0:
                block.y = blocksPainter * 50 + 25
                block.x = blocksPainter1 * 50 + 25
                block.image = 'button'
                block.draw()
            elif buttons[blocksPainter][blocksPainter1] == 'p':
                block.y = blocksPainter * 50 + 25
                block.x = blocksPainter1 * 50 + 25
                block.image = 'buttonp'
                block.draw()
            else:
                if blocks[blocksPainter][blocksPainter1] == 9:
                    block.y = blocksPainter * 50 + 25
                    block.x = blocksPainter1 * 50 + 25
                    block.image = 'boom'
                    block.draw()
                else:
                    block.y = blocksPainter * 50 + 25
                    block.x = blocksPainter1 * 50 + 25
                    block.image = 'b' + \
                        str(blocks[blocksPainter][blocksPainter1])
                    block.draw()
# 绘制角色


def on_mouse_down(button, pos):
    global posX, posY
    posY = pos[1] // 50
    posX = pos[0] // 50
    if buttons[posY][posX] != 1:
        if button == mouse.LEFT:
            if buttons[posY][posX] == 0:
                breakBlock()
        if button == mouse.RIGHT:
            if buttons[posY][posX] == 0:
                buttons[posY][posX] = 'p'
            else:
                breakBlock()


def breakBlock():
    global posX, posY
    buttons[posY][posX] = 1
    if pos[Y] == 0:
        

# 以下用于开发者调试
# 调试驱动
def debug1():
    Debug_sweepCount = 0
    for Debug1_blocksMiner in blocks:
        for Debug1_blocksMiner1 in Debug1_blocksMiner:
            if Debug1_blocksMiner1 == 9:
                Debug_sweepCount += 1
    print('<调试>:blocks:')
    print('<调试>:', blocks)
    print('<调试>:blocks共有', len(blocks),
          '个数据包(81项),其中有', Debug_sweepCount, '项的值是‘9’')


def debug2():
    print('<调试>:buttons:')
    print('<调试>:', buttons)


pgzrun.go()

# 调试
# 选择你想调试的内容，然后删去‘#’,即可启用该内容。
'''↓调试功能1:查看雷分布的位置(blocks列表)'''
# debug1()
# debug2()

# pgzrun.go()
