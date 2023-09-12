import ui
import config


def main():
    if config.database.connected():
        ui.start()
    else:
        ui.error(404)


if __name__ == '__main__':
    main()
