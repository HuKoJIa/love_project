import aiofiles
from pathlib import Path
from src.application.photo.interfaces.persistence import FileStorage

class LocalFileStorage(FileStorage):
    def __init__(self, base_dir: str = "storage/photos"):
        self._base_dir = Path(base_dir)
        self._base_dir.mkdir(parents=True, exist_ok=True)
    
    async def save_file(self, file_content: bytes, file_key: str) -> str:
        file_path = self._base_dir / file_key
        file_path.parent.mkdir(parents=True, exist_ok=True)

        async with aiofiles.open(file_path, "wb") as f:
            await f.write(file_content)
        
        return str(file_path.absolute())
        #base_dir вынести в .env убрать захардкоженность!!!
        