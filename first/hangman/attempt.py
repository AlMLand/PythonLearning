from dataclasses import dataclass


@dataclass
class Attempt:

    def __init__(self, count: int):
        self.count: int = count

    def decrease_attempts(self):
        self.count -= 1

    def is_attempt_available(self) -> bool:
        return self.count != 0

    def display_attempts(self):
        print(f"attempts: {self.count}")
