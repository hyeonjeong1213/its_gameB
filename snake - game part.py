def game_loop():
    """게임 루프를 실행합니다."""
    global game_on
    while game_on:
        screen.update()
        time.sleep(0.1)

        # 뱀의 몸통 업데이트
        for i in range(len(snakes) - 1, 0, -1):
            snakes[i].goto(snakes[i - 1].pos())
        snakes[0].forward(10)

        # 먹이를 먹었을 때 처리
        if snakes[0].distance(food) < 15:
            food.goto(rand_pos())
            create_snake(snakes[-1].pos())
            score_update()

        # 충돌 검사
        check_collision()

def check_collision():
    """뱀의 충돌을 검사합니다."""
    global game_on
    # 벽 충돌 검사
    x, y = snakes[0].pos()
    if abs(x) > 290 or abs(y) > 290:
        game_on = False
        show_game_over()
    # 몸통 충돌 검사
    for segment in snakes[1:]:
        if snakes[0].distance(segment) < 10:
            game_on = False
            show_game_over()

def show_game_over():
    """게임 오버 메시지를 표시합니다."""
    score_pen.goto(0, 0)
    score_pen.write("Game Over", align="center", font=("", 30, "bold"))
    screen.update()

def score_update():
    """점수를 업데이트합니다."""
    global score
    score += 1
    score_pen.clear()
    score_pen.write(f"점수 : {score}", font=("", 15, "bold"))


