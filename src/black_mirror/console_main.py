from console_app import ConsoleApp
from school import School


def main():
    school = School()
    app = ConsoleApp(school)
    app.run()


if __name__ == "__main__":
    main()