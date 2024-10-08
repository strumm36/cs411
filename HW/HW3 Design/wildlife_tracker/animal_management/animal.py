from typing import Any, Optional

class Animal:
    
    def __init__(self,
                 age: Optional[int],
                 animal_id: int,
                 species: str,
                 health_status: Optional[str] = None) -> None:
        self.age = age
        self.animal_id = animal_id

    def get_animal_details(animal_id) -> dict[str, Any]:
        pass

    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass

    pass
