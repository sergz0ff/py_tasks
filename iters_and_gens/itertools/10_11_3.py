from itertools import groupby

tasks = [('Отдых', 'поспать днем', 3),
        ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
        ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
        ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
        ('Отдых', 'погулять вечером', 4),
        ('Курс по ооп', 'обсудить темы', 1),
        ('Урок по groupby', 'добавить задачи на программирование', 3),
        ('Урок по groupby', 'написать конспект', 1),
        ('Отдых', 'погулять днем', 2),
        ('Урок по groupby', 'добавить тестовые задачи', 2),
        ('Уборка', 'убраться в ванной', 2),
        ('Уборка', 'убраться в комнате', 1),
        ('Уборка', 'убраться на кухне', 3),
        ('Отдых', 'погулять утром', 1),
        ('Курс по ооп', 'обсудить задачи', 2)]

groups = groupby(
    sorted(tasks, key=lambda tpl: (tpl[0], tpl[2])),
    key=lambda tpl: tpl[0]
)

for task, actions in groups:
    print(
        f'{task}:'
    )
    for action in actions:
        print(
            f'    {action[2]}. {action[1]}'
        )
    print()