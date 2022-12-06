from game import Game, GameView

game = Game()
gameView = GameView(game)

for entity in game.entities:
    print(f"{entity.x} {entity.y}")


