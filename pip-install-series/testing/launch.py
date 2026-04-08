def can_launch(
        is_armed: bool,
        safety_key_inserted: bool
    ) -> bool:
    if is_armed and safety_key_inserted:
        return True
    return False
