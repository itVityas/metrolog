from django import template

register = template.Library()

@register.filter
def in_month(value):
    if not value:
        return ""

    # Словарь месяцев в предложном падеже
    months_prepositional = {
        1: "январе", 2: "феврале", 3: "марте",
        4: "апреле", 5: "мае", 6: "июне",
        7: "июле", 8: "августе", 9: "сентябре",
        10: "октябре", 11: "ноябре", 12: "декабре"
    }

    month_num = value.month
    month_name = months_prepositional.get(month_num, "")

    return f"{month_name}"
