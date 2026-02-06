from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Static
from textual.containers import VerticalScroll
import asyncio

class Message(Static):
    pass

class RAGTerminalApp(App):

    CSS = """
    #chat {
        padding: 1;
    }
    Input {
        dock: bottom;
    }
    """

    def __init__(self, qa_chain, retriever):
        super().__init__()
        self.qa_chain = qa_chain
        self.retriever = retriever
        self.history = []  # 👈 conversation memory
        self.show_sources = False

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        self.chat = VerticalScroll(id="chat")
        yield self.chat
        yield Input(
            placeholder="Ask a question (:clear to reset memory, s = sources)"
        )
        yield Footer()

    async def on_input_submitted(self, event: Input.Submitted):
        question = event.value.strip()
        event.input.value = ""

        if not question:
            return

        if question.lower() in {"exit", "quit"}:
            await self.action_quit()
            return

        if question.lower() == ":clear":
            self.history.clear()
            self.chat.mount(Message("[yellow]🧹 Conversation memory cleared[/]"))
            return

        if question.lower() == "s":
            self.show_sources = not self.show_sources
            self.chat.mount(
                Message(
                    f"[yellow]Sources {'ON' if self.show_sources else 'OFF'}[/]"
                )
            )
            return

        # Show user message
        self.chat.mount(Message(f"[bold cyan]You:[/] {question}"))
        thinking = Message("[green]Assistant:[/] Thinking…")
        self.chat.mount(thinking)
        self.chat.scroll_end()

        # Invoke chain with history
        answer = await asyncio.to_thread(
            self.qa_chain.invoke,
            {
                "history": "\n".join(self.history),
                "question": question
            }
        )

        thinking.update(f"[green]Assistant:[/] {answer}")
        self.history.append(f"User: {question}")
        self.history.append(f"Assistant: {answer}")

        # Optional: show sources
        if self.show_sources:
            docs = await asyncio.to_thread(
                self.retriever.get_relevant_documents,
                question
            )
            for i, doc in enumerate(docs, 1):
                snippet = doc.page_content[:200].replace("\n", " ")
                page = doc.metadata.get("page", "?")
                self.chat.mount(
                    Message(
                        f"[dim]Source {i} (page {page}): {snippet}…[/]"
                    )
                )

        self.chat.scroll_end()
