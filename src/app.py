from app_ide.ide.ide import IDE
import sys


def main():
    current_document = ""
    ide = IDE(current_document)
    print("Welcome to app_ide.")
    print("""Control Commands:
          :u : undo
          :r : redo
          :e : exit
          :v : view document state
          :wq : write file and quit
          :q : quit
          """)
    print("Please type our code below:")
    while (True):
        text = input()
        try:
            match text:
                case ":u":
                    ide.undo()
                case ":r":
                    ide.redo()
                case ":v":
                    ide.render_document()
                case ":wq":
                    if (len(ide.read()) > 0):
                        file_name = input(
                            "Please supply filename to save the document to: ")
                        with open(file_name, "w") as file:
                            file.write(ide.read())
                        print(f"Document successfully saved to {file_name}")
                    sys.exit(0)
                case ':q':
                    sys.exit(0)
                case _:
                    ide.write(text)
        except Exception as e:
            print(f"Encountered an error. Error: {e}")


if __name__ == "__main__":
    main()
