print("Hello World")

class HelloPrinter:
    def __init__(self, message: str = "Hello World"):
        self.message = message

    def say(self) -> None:
        print(self.message)

if __name__ == "__main__":
    output_var = HelloPrinter("Go away")
    output_var.say()

# new comment