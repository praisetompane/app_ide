from app_ide.ide.ide import IDE


def test_ide():
    current_document = ""
    ide = IDE(current_document)

    ide.write("public void add(int index, int element){")
    ide.write("typo")
    ide.undo()
    ide.write(
        """
                if(numberOfElements < _size)
                    array[index] = element;
    """
    )
    ide.write(
        """
                else {
                    resize();
                    array[index] = element;
                }
    """
    )
    ide.write(
        """
            numberOfElements++;
        }
    """
    )
