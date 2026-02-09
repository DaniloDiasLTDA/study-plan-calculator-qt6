def clean_preferences(preferences: dict) -> dict:
    return {key: value for key, value in preferences.items() if value is not None}


user_pref_list = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None,
}

print(clean_preferences(user_pref_list))
