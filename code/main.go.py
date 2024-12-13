import pygame
import sys


from const import *
import Game

# Опции меню
MENU_OPTIONS = ["Новая игра", "Инструкция", "Выход"]
OPTION_NEW_GAME = 0
OPTION_INSTRUCTIONS = 1
OPTION_EXIT = 2

selected_option = OPTION_NEW_GAME  # Индекс выбранного пункта

# Проверка пользователя
is_user_authenticated = False

# Загрузка фона
pygame.init()
background_image = pygame.image.load("image/background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

def draw_menu(screen, font):
    global selected_option
    """Функция для отрисовки меню."""
    screen.blit(background_image, (0, 0))
    # Заголовок меню
    title = font.render("Меню", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 80))

    for i, option in enumerate(MENU_OPTIONS):
        color = BLUE if i == selected_option else BLACK
        text_surface = font.render(option, True, color)
        x = (WIDTH - text_surface.get_width()) // 2
        y = HEIGHT // 2 + i * 60
        screen.blit(text_surface, (x, y))

def get_option_at_pos(pos, font):
    """Определяет, на какую опцию в меню нажали."""
    x, y = pos
    for i, option in enumerate(MENU_OPTIONS):
        text_surface = font.render(option, True, BLACK)
        option_x = (WIDTH - text_surface.get_width()) // 2
        option_y = HEIGHT // 2 + i * 60
        if option_x <= x <= option_x + text_surface.get_width() and option_y <= y <= option_y + text_surface.get_height():
            return i
    return None

def instructions_screen():
    """Функция отображения инструкции."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Инструкция")

    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    instructions_text = [
        "Основные правила игры в Шашки Вигмана:",
        "В игре действуют почти те же правила, что и в Русские Шашки.",
        "Различия заключаются в следующем:",
        "",
        "1. У каждого игрока по 24 фигуры обоих цветов на доске.",
        "2. Игроки одновременно играют в две партии.",
        "3. Каждый игрок делает по два хода за ход.",
        "4. Если игрок не может сделать второй ход, он проигрывает",
        "",
        "Нажмите любую клавишу для возврата в меню."
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        # Отображение фона
        screen.blit(background_image, (0, 0))

        # Отображение текста инструкции
        y_offset = 50
        for line in instructions_text:
            line_surface = font.render(line, True, BLACK)
            screen.blit(line_surface, (WIDTH // 2 - line_surface.get_width() // 2, y_offset))
            y_offset += 40

        pygame.display.flip()
        clock.tick(30)

def login_registration_screen():
    global is_user_authenticated

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 1000 на 600
    pygame.display.set_caption("Вход / Регистрация")

    font = pygame.font.Font(None, 36)
    input_box_login = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 60, 200, 40)
    input_box_password = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 20, 200, 40)
    login_text = ''
    password_text = ''
    active_input = None
    error_message = ""

    clock = pygame.time.Clock()

    running = True
    while running:
        screen.blit(background_image, (0, 0))

        # Заголовок
        title_surface = font.render("Вход / Регистрация", True, BLACK)
        screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, HEIGHT // 2 - 140))

        # Поля ввода и текст над ними
        login_label = font.render("Логин:", True, BLACK)
        screen.blit(login_label, (WIDTH // 2 - 120 - login_label.get_width(), HEIGHT // 2 - 60))
        pygame.draw.rect(screen, WHITE, input_box_login)
        pygame.draw.rect(screen, BLACK, input_box_login, 2)

        login_display = login_text + ("|" if active_input == 'login' and pygame.time.get_ticks() % 1000 < 500 else "")
        login_surface = font.render(login_display, True, BLACK)
        screen.blit(login_surface, (input_box_login.x + 5, input_box_login.y + 5))

        password_label = font.render("Пароль:", True, BLACK)
        screen.blit(password_label, (WIDTH // 2 - 120 - password_label.get_width(), HEIGHT // 2 + 20))
        pygame.draw.rect(screen, WHITE, input_box_password)
        pygame.draw.rect(screen, BLACK, input_box_password, 2)

        password_display = '*' * len(password_text) + ("|" if active_input == 'password' and pygame.time.get_ticks() % 1000 < 500 else "")
        password_surface = font.render(password_display, True, BLACK)
        screen.blit(password_surface, (input_box_password.x + 5, input_box_password.y + 5))

        login_button_text = font.render("Вход", True, BLACK)
        login_button_pos = (WIDTH // 2 - 140, HEIGHT // 2 + 100)
        screen.blit(login_button_text, login_button_pos)

        register_button_text = font.render("Регистрация", True, BLACK)
        register_button_pos = (WIDTH // 2 - 40, HEIGHT // 2 + 100)
        screen.blit(register_button_text, register_button_pos)

        if error_message:
            error_surface = font.render(error_message, True, (0, 0, 0))
            screen.blit(error_surface, (WIDTH // 2 - error_surface.get_width() // 2, HEIGHT // 2 + 180))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box_login.collidepoint(event.pos):
                    active_input = 'login'
                elif input_box_password.collidepoint(event.pos):
                    active_input = 'password'
                elif login_button_pos[0] <= event.pos[0] <= login_button_pos[0] + login_button_text.get_width() and \
                        login_button_pos[1] <= event.pos[1] <= login_button_pos[1] + login_button_text.get_height():
                    if authenticate_user(login_text, password_text):
                        is_user_authenticated = True
                        running = False
                    else:
                        error_message = "Такого пользователя не существует!"
                elif register_button_pos[0] <= event.pos[0] <= register_button_pos[
                    0] + register_button_text.get_width() and \
                        register_button_pos[1] <= event.pos[1] <= register_button_pos[
                    1] + register_button_text.get_height():
                    if login_text.strip() == "" or password_text.strip() == "":
                        error_message = "Логин и пароль не могут быть пустыми!"
                    else:
                        register_user(login_text, password_text)
                        is_user_authenticated = True
                        running = False

            if event.type == pygame.KEYDOWN:
                if active_input == 'login':
                    if event.key == pygame.K_BACKSPACE:
                        login_text = login_text[:-1]
                    else:
                        login_text += event.unicode
                elif active_input == 'password':
                    if event.key == pygame.K_BACKSPACE:
                        password_text = password_text[:-1]
                    else:
                        password_text += event.unicode

        clock.tick(30)

def authenticate_user(login, password):
    try:
        with open("users.txt", "r") as file:
            for line in file:
                stored_login, stored_password = line.strip().split(',')
                if login == stored_login and password == stored_password:
                    return True
    except FileNotFoundError:
        pass
    return False

def register_user(login, password):
    if login and password:
        with open("users.txt", "a") as file:
            file.write(f"{login},{password}\n")

def main():
    global selected_option, is_user_authenticated

    while not is_user_authenticated:
        login_registration_screen()

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Шашки Вигмана")

    font = pygame.font.Font(None, 50)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_option = get_option_at_pos(event.pos, font)
                if clicked_option is not None:
                    selected_option = clicked_option
                    if selected_option == OPTION_NEW_GAME:
                        game = Game.Class_Game()
                        game.run_game()
                    elif selected_option == OPTION_INSTRUCTIONS:
                        instructions_screen()
                    elif selected_option == OPTION_EXIT:
                        running = False

        draw_menu(screen, font)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
