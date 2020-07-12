class Window:
    __toolkit = None
    __purpose = None

    def __init__(self, toolkit, purpose):
        self.__toolkit = toolkit
        self.__purpose = purpose

    def get_toolkit(self):
        return self.__toolkit

    def get_purpose(self):
        return self.__purpose


class GtkToolboxWindow(Window):
    def __init__(self):
        Window.__init__(self, "Gtk", "ToolboxWindow")


class GtkLayersWindow(Window):
    def __init__(self):
        Window.__init__(self, "Gtk", "LayersWindow")


class GtkMainWindow(Window):
    def __init__(self):
        Window.__init__(self, "Gtk", "MainWindow")


class QtToolboxWindow(Window):
    def __init__(self):
        Window.__init__(self, "Qt", "ToolboxWindow")


class QtLayersWindow(Window):
    def __init__(self):
        Window.__init__(self, "Qt", "LayersWindow")


class QtMainWindow(Window):
    def __init__(self):
        Window.__init__(self, "Qt", "MainWindow")


# Abstract factory class
class UIFactory:
    def get_toolbox_window(self): pass

    def get_layers_window(self): pass

    def get_main_window(self): pass


class GtkUIFactory(UIFactory):
    def get_toolbox_window(self):
        return GtkToolboxWindow()

    def get_layers_window(self):
        return GtkLayersWindow()

    def get_main_window(self):
        return GtkMainWindow()


class QtUIFactory(UIFactory):
    def get_toolbox_window(self):
        return QtToolboxWindow()

    def get_layers_window(self):
        return QtLayersWindow()

    def get_main_window(self):
        return QtMainWindow()


if __name__ == "__main__":

    for gnome in [0, 1]:
        if gnome:
            ui = GtkUIFactory()
            print("Gtk Factory !!")
        else:
            ui = QtUIFactory()
            print("Qt Factory !!")

        toolbox = ui.get_toolbox_window()
        layers = ui.get_layers_window()
        main = ui.get_main_window()

        print(f"toolbox {toolbox.get_toolkit()}: {toolbox.get_purpose()}")
        print(f"layers {layers.get_toolkit()}: {layers.get_purpose()}")
        print(f"main {main.get_toolkit()}: {main.get_purpose()}")
