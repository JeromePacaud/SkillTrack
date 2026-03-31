class User:
    """
    Représente un utilisateur du système.

    Attributes:
        name (str) : Le nom de l'utilisateur.
        id (int) : L'identifiant unique de l'utilisateur.
    """

    def __init__(self, name: str, id: int) -> None:
        """
        Initialise un nouvel utilisateur avec un nom et un identifiant.

        Args:
            name (str): Le nom de l'utilisateur.
            id (int): L'identifiant unique de l'utilisateur.
        """
        self.name = name
        self.id = id

    def can_validate(self, skill_id: int) -> bool:
        """
        Indique si l'utilisateur peut valider une compétence spécifique.

        Args:
            skill_id (int) : L'identifiant de la compétence à vérifier.

        Returns:
            bool: Toujours False pour l'instant.
        """
        return False

class Learner(User):
    pass

class Trainer(User):
    pass