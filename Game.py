from World import World
from GraphicEngine import GraphicEngine


def main():
    m = input("Enter width : ")
    n = input("Enter height : ")
    mode = int(input("Mode (1 - hex, 0 - normal) : "))
    graphic_engine = GraphicEngine(m, n, mode)
    world = World(m, n, graphic_engine, mode)

    running = True

    while running:
        graphic_engine.reset()

        world.drawScene()

        world.displayMenu()
        graphic_engine.render()

        running = world.handleEvents()

    graphic_engine.quit()


if __name__ == "__main__":
    main()
