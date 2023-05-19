from textual.app import App
from textual.widgets import Input, Header, Markdown, Button
from textual.containers import VerticalScroll, Vertical, Horizontal
from src.twitter.search_engine import SearchEngine


class MainApp(App):
    CSS_PATH = "./css/main_screen.css"
    search_engine = SearchEngine()

    def compose(self):
        yield Header(True)
        with Vertical(id="body"):
            with Horizontal(id="search_bar"):
                yield Input(
                    id="query",
                    placeholder="Procure por uma palavra ou frase no Twitter.",
                    classes="box",
                )
                yield Button(
                    id="search_button",
                    label="\U0001f50e",
                )

            with VerticalScroll():
                yield Markdown(id="results")

    def on_button_pressed(self, event: Button.Pressed):
        self._load_tweets()

    def on_input_submitted(self):
        self._load_tweets()

    def _load_tweets(self):
        query: str = self.query_one("#query", Input).value
        if query:
            results = self.search_engine.search(query)
            if results is not None:
                self.query_one("#results", Markdown).update(
                    "\n---\n".join(tweet.text for tweet in results)
                )


if __name__ == "__main__":
    app = MainApp()
    app.run()
