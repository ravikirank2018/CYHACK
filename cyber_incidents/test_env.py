import os

def test_env():
    print("DB_HOST:", os.getenv('DB_HOST'))
    print("DB_USER:", os.getenv('DB_USER'))
    print("DB_PASSWORD:", os.getenv('DB_PASSWORD'))
    print("DB_NAME:", os.getenv('DB_NAME'))

if __name__ == "__main__":
    test_env()
