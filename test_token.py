from app.auth.token_manager import token_manager

token_manager.save("TEST_TOKEN_123")

print(token_manager.load())

print(token_manager.info())