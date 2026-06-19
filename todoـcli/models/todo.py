class Todo:
    def __init__(self, id: int, title: str, completed: bool = False) -> None:
        self.id = id
        self.title = title
        self.completed = completed

    def mark_completed(self) -> None:
        self.completed = True

    def mark_incompleted(self) -> None:
        self.completed = False

    def __str__(self) -> str:
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.id}. {self.title}"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Todo":
        return cls(
            id=data["id"], title=data["title"], completed=data.get("completed", False)
        )
