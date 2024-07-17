score=0

def rand_pos():
    rand_x = random.randint(-250,250)
    rand_y = randow.randint(-250,250)
    return rand_x,rand_y

def score_update():
    global score
    score += 1
    score_pen.clear()
    score_pen.write(f"점수 : {score}", font=(" ", 15, "bold"))

#먹이
food = Turtle()
food.shape("circle")
food.color("snow")
food.up()
food.speed(0)
food.goto(rand_pos())

#점수 표시
score_pen = Turtle()
score_pen.ht()
score_pen.up()
score_pen.goto(-270, 250)
score_pen.write(f"점수 : {}", font = (" ", 15, "bold"))

#while gameon밑에 쓰기
if snakes[0].distance(food) < 15:
    score_update()
    food.goto(rand_pos())
    create_snake(snakes[-1].pos())