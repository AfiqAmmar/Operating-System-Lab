from treelib import Node, Tree

tree = Tree()

tree.create_node("User", "User")  # root node
tree.create_node("Document", "Document", parent="User")
tree.create_node("Desktop", "Desktop", parent="User")
tree.create_node("Videos", "Videos", parent="User")
tree.create_node("Music", "Music", parent="User")
tree.create_node("Pictures", "Pictures", parent="User")
tree.create_node("Downloads", "Downloads", parent="User")
tree.create_node("C Drive", "C Drive", parent="User")
tree.show()

def createFolder():
    try:
        folderName = input("Folder name? ")
        directoryName = input("Directory name? ")
        tree.create_node(folderName, folderName, parent=directoryName)
        tree.show()
    except:
        print("Invalid file name or directory name")

def deleteFolder():
    try:
        folderName = input("Folder name? ")   
        tree.remove_node(folderName)
        tree.show()
    except:
        print("No such folder exists")

def moveFolder():
    try:
        folderName = input("Folder name? ")
        newDir = input("New directory? ")
        tree.move_node(folderName, newDir)
        tree.show()
    except:
        print("No such folder or directory exists")    

def showDir():
    try:
        folderName = input("Folder name? ")
        sub_t = tree.subtree(folderName)
        sub_t.show()
    except:
        print("No such folder exists")

check = True

while check == True:

    argument = input("What operation you want to execute?\n 1: Create Folder\n 2: Delete Folder\n 3: Move Folder\n 4: Show Folder\n")

    if argument == "0":
        check = False
    
    elif argument == "1":
        createFolder()
    
    elif argument == "2":
        deleteFolder()
    
    elif argument == "3":
        moveFolder()
    
    elif argument == "4":
        showDir()
    
    else:
        print("Invalid operation")

   
   

