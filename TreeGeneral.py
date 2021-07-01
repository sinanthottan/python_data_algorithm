class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        self.children.append(child)
        child.parent = self

    def printer(self):
        space = ' ' * self.get_level() * 3
        prefix = space + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printer()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return(level)

def build_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    mobile = TreeNode("Mobile")
    tv = TreeNode("TV")
    thinkpad = TreeNode("Thinkpad")
    dell = TreeNode("Dell")
    macbook = TreeNode("MacBook")
    nokia = TreeNode("Nokia")
    samsung = TreeNode("Samsung")
    iphone = TreeNode("iPhone")
    ikon = TreeNode("Ikon")
    toshiba = TreeNode("Toshiba")
    lg = TreeNode("LG")
    root.add_child(laptop)
    laptop.add_child(thinkpad)
    laptop.add_child(macbook)
    laptop.add_child(dell)
    root.add_child(mobile)
    mobile.add_child(nokia)
    mobile.add_child(samsung)
    mobile.add_child(iphone)
    root.add_child(tv)
    tv.add_child(lg)
    tv.add_child(toshiba)
    tv.add_child(ikon)
    root.printer()

if __name__ == '__main__':
    build_tree()
