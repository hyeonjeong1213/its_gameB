from turtle import Turtle, Screen
import time
import random

def up():
    if snakes[0].heading() != 270:
        snakes[0].setheading(90)

def down():
    if snakes[0].heading() != 90:
        snakes[0].setheading(270)

def right():
    if snakes[0].heading() != 180:
        snakes[0].setheading(0)

def left():
    if snakes[0].heading() != 0:
        snakes[0].setheading(180)

def create_snake(pos):
    snake_body = Turtle()
    snake_body.shape("square")
    snake_body.color("burlywood")
    snake_body.penup()
    snake_body.goto(pos)
    snakes.append(snake_body)

def rand_pos():
    rand_x = random.randint(-280, 280) 
    rand_y = random.randint(-280, 280)
    return rand_x, rand_y

def score_update():
    global score
    score += 1
    score_pen.clear()
    score_pen.write(f"score: {score}", font=("", 18, "bold"))  
    high_score_pen.clear()
    high_score_pen.write(f"best: {high_score}", font=("", 18, "bold")) 

def show_game_over():
    global high_score, game_on
    game_on = False
    if score > high_score:
        high_score = score
    score_pen.goto(0, 0)
    score_pen.color("black")
    score_pen.write("Game Over", align="center", font=("", 30, "bold"))
    score_pen.goto(0, -40)
    score_pen.color("green")
    score_pen.write("restart: r키", align="center", font=("", 20, "bold"))

def restart_game():
    global game_on, score, start_time # 타이머 파트 추가된 부분

    # 게임 상태 초기화
    score = 0
    start_time = time.time()  # 게임 시작 시간 초기화
    score_pen.clear()
    score_pen.goto(-270, 250)
    score_pen.color("black")
    score_pen.write(f"score: {score}", font=("", 18, "bold"))  
    high_score_pen.clear()
    high_score_pen.write(f"best: {high_score}", font=("", 18, "bold"))  

    # 뱀 초기화
    for segment in snakes:
        segment.goto(1000, 1000) 
    snakes.clear()
    for pos in start_pos:
        create_snake(pos)

    # 먹이 위치 초기화
    food.goto(rand_pos())

    game_on = True

# 타이머 파트
def update_timer():
    global game_on
    elapsed_time = time.time() - start_time # 경과 시간 계산
    remaining_time = max(0, time_limit - int(elapsed_time)) # 남은 시간 계산
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    time_pen.clear()
    time_pen.write(f"Time: {minutes:02}:{seconds:02}", font=("", 18, "bold"))

    if remaining_time <= 0:
        show_game_over() # 남은 시간이 0 이하이면 게임 오버

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("aliceblue")
screen.title("Snake Game")
screen.tracer(0)

# snake 만들기
start_pos = [(0, 0), (-20, 0), (-40, 0)]
snakes = []
score = 0
high_score = 0
time_limit = 2*60  # 플레이 제한 시간 2분(120초)
start_time = time.time() # 게임 시작 시간 기록 

for pos in start_pos:
    create_snake(pos)

# 먹이
food = Turtle()
food.shape("circle")
food.color("firebrick")
food.up()
food.speed(0)
food.goto(rand_pos())

# 현재 점수 표시
score_pen = Turtle()
score_pen.ht()
score_pen.up()
score_pen.goto(-270, 250)
score_pen.color("black")
score_pen.write(f"score: {score}", font=("", 18, "bold")) 

# 최고 점수 표시
high_score_pen = Turtle()
high_score_pen.ht()
high_score_pen.up()
high_score_pen.goto(-270, 220) 
high_score_pen.color("black")

# 남은 시간 표시
time_pen = Turtle() 
time_pen.ht()
time_pen.up()
time_pen.goto(140, 250)  # 상단 오른쪽에 남은 시간을 보여주는 타이머 위치 
time_pen.color("black")

screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(right, "Right")
screen.onkeypress(left, "Left")
screen.onkey(restart_game, "r")  # r키를 눌러 게임 재시작

game_on = True
while True:
    screen.update()
    if game_on:
        time.sleep(0.1)

        # 뱀의 몸통 업데이트
        for i in range(len(snakes) - 1, 0, -1):
            snakes[i].goto(snakes[i-1].pos())
        
        snakes[0].forward(20)

        # 먹이를 먹었을 때 처리
        if snakes[0].distance(food) < 15:
            score_update()
            food.goto(rand_pos())
            create_snake(snakes[-1].pos())

        # 벽 충돌 검사
        x, y = snakes[0].pos()
        if abs(x) > 290 or abs(y) > 290: 
            show_game_over()

        # 몸통 충돌 검사
        for segment in snakes[1:]:
            if snakes[0].distance(segment) < 10:  
                show_game_over()

        update_timer() # 타이머 업데이트
    else:
        time.sleep(0.1)
