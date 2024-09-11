class Task:
    def __init__(self, id, title, description, completed=False) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

# metodo de retorno
    def to_dict(self):
        return{
            "id": self.id,
            "title": self.title,
            "descripition": self.description,
            "completed": self.completed
        }
        