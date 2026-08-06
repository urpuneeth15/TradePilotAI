import json
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parents[2]

TOKEN_FILE = BASE_DIR / "storage" / "token.json"


class TokenManager:

    def save(self, access_token: str):

        TOKEN_FILE.parent.mkdir(
            exist_ok=True
        )

        data = {

            "access_token": access_token,

            "created_at": datetime.now().isoformat()

        }

        with open(
            TOKEN_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    def load(self):

        if not TOKEN_FILE.exists():

            return None

        with open(
            TOKEN_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return data.get(
            "access_token"
        )

    def exists(self):

        return TOKEN_FILE.exists()

    def delete(self):

        if TOKEN_FILE.exists():

            TOKEN_FILE.unlink()

    def info(self):

        if not TOKEN_FILE.exists():

            return None

        with open(
            TOKEN_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


token_manager = TokenManager()