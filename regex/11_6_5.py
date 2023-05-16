from re import match, IGNORECASE

message = input()
print(
    bool(
    match(
    r"Здравствуйте|Доброе утро|Добрый день|Добрый вечер", message, flags=IGNORECASE
    )
    )
)
