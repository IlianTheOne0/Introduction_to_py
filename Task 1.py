"""
print() - команда для виведення тексту або інших даних у терміналі
\n - використовується, щоб перевести текст на новий рядок


\033[31m - escape-послідовності. У даному випадку код використовується для того, щоб змінити колір тексту на червоний,
    а код \033[0m в свою чергу робить його знову білим.

Escape-послідовності — це ANSI-коди, що використовуються для форматування тексту, управління поведінкою виводу або інших функцій,
    які не є буквами чи цифрами. У Python вони починаються з коду \033 або \x1b.

Далі йдуть символи, які визначають конкретну команду. У нашому випадку код [31m робить текст червоним, а код [0m повертає текст до звичайного кольору.

Всі escape-послідовності можна знайти в різних джерелах. Одне з них: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797


Щоб форматувати текст, також можна використовувати бібліотеки. Одна з них colorama: https://pypi.org/project/colorama/
"""

print('To be\n\033[31mor not\n\033[0mto be')