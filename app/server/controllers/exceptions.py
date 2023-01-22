class UnauthorizedException(Exception):
    "When Enqueue or Dequeue is unauthorized"
    def __init__(self, *args: object) -> None:
        super().__init__(*args)