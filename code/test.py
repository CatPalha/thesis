import pygame, math, random, words

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman')


# load images
images = []
for i in range(7):
    image = pygame.image.load(r'C:\Users\hp\Pygame\Hangman\hangman' + str(i) + '.png')
    images.append(image)


# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# game variables
hangman_status = 0
word = random.choice(words.final_words).upper()
guessed = []


# fonts
LETTER_FONT = pygame.font.Font(r'C:\Users\hp\AppData\Local\Microsoft\Windows\Fonts\Azonix.otf', 30)
WORD_FONT = pygame.font.Font(r'C:\Users\hp\AppData\Local\Microsoft\Windows\Fonts\Azonix.otf', 35)
RESULT_FONT = pygame.font.Font(r'C:\Users\hp\AppData\Local\Microsoft\Windows\Fonts\Azonix.otf', 45)

# button variables
RADIUS = 20
GAP = 15
let_pos = []
startx = round((WIDTH - (GAP + RADIUS * 2) * 13) / 2)
starty = 380
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    let_pos.append([x, y, chr(A + i), True])



# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True


# draw
def draw():
    win.fill(WHITE)
    text = RESULT_FONT.render('Hangman', 1, BLACK)
    win.blit(text, (int(WIDTH/2) - int(text.get_width()/2), 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + ' '
        else:
            display_word += '_ '
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (340, 200))

    # draw buttons
    for letter in let_pos:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 2)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - int(text.get_width()/2), y - int(text.get_height()/2)))


    win.blit(images[hangman_status], (100, 80))
    pygame.display.update()

# display  word
def last_word():
    win.fill(BLACK)
    text = RESULT_FONT.render(f'The word was: {word}', 1, WHITE)
    win.blit(text, (int(WIDTH/2 - int(text.get_width()/2)), int(HEIGHT/2) - int(text.get_height()/2)))
    pygame.display.update()

# result
def display_message(message):
    win.fill(BLACK)
    text = RESULT_FONT.render(message, 5, WHITE)
    win.blit(text, (int(WIDTH/2) - int(text.get_width()/2), int(HEIGHT/2) - int(text.get_height()/2)))
    pygame.display.update()
    pygame.time.delay(3000)

# game loop

while run:
    clock.tick(FPS)
    draw()
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in let_pos:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((m_x- x)**2 + (m_y - y)**2)
                    if dis <= RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
    won = True
    for letter in word:
        if letter not in guessed:
            won = False

    # check if the player lost won
    if won:
        last_word()
        pygame.time.delay(2000)
        display_message('You WON!')
        break

    # check if the player lost
    if hangman_status == 6:
        pygame.time.delay(1000)
        last_word()
        pygame.time.delay(4000)
        display_message('You Lost.')
        break

pygame.quit()
print(' '.join(word.split(' ')).title())