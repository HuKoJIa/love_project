from abc import ABC, abstractmethod


class FileStorage(ABC):
    @abstractmethod
    async def save_file(self, file_content: bytes, file_key: str) -> str:
        """Сохраняет файл и возвращает URL или путь к нему."""
        pass