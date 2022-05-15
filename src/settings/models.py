from dataclasses import dataclass

@dataclass
class DatabaseConfig():
    host: str
    name: str
    port: int
    driver: str
    username: str
    password: str
    
    def build_connection_str(self):
        return f'{self.driver}://{self.username}:{self.password}@{self.host}:{self.port}/{self.name}'