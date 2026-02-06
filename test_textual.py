from textual.app import App
from textual.widgets import Header, Footer, Static

class TestApp(App):
    def compose(self):
        yield Header()
        yield Static("🚀 Textual is WORKING!", style="bold green")
        yield Footer()

if __name__ == "__main__":
    TestApp().run()
