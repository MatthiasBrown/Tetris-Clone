#run = True     # Starting the intial window run.
# while run:
#     key_input = pygame.key.get_pressed()
#     pygame.time.delay(100)
#     window.fill((0, 0, 0)) # TODO: Must fix this call
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#              run = False
#         #elif event.type == pygame.KEYDOWN: # If we've intialized the game to 30 fps that means we have to hold for 30 frames which is a second
#         if key_input[pygame.K_q] and pygame.KMOD_CTRL :    # Control_Q is standard app exit on Arch based OS, and other tiling DE
#                 run = False

#     pygame.draw.rect(window, ( 255, 0, 0), (x, y , width, height))
#     pygame.display.update()


#This the gird the game occurs in, 20 rows by 10 coloums
tile_gird= ([], [])
