# Copyright (c) 2022 Itz-fork

class ResponseStatusError(Exception):
    def __init__(self, status) -> None:
        super().__init__(f"Expected to receive 200 response, got {status}")
