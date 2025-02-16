class SocialNetwork:


    def __init__(self, name: str, users: int):
        self.name = name
        self.users = users

    def __str__(self) -> str:
        return f"{self.name} with {self.users} users"

    def __repr__(self) -> str:
        return f"SocialNetwork(name={self.name}, users={self.users})"


class VK(SocialNetwork):


    def __init__(self, name: str, users: int, region: str):

        super().__init__(name, users)
        self.region = region

    def __str__(self) -> str:

        return f"{super().__str__()} in {self.region}"

    def __repr__(self) -> str:
        return f"VK(name={self.name}, users={self.users}, region={self.region})"

    def change_region(self, new_region: str):

        self.region = new_region
