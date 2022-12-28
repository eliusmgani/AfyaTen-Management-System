from django.views.generic.edit import CreateView, UpdateView, DeleteView

from datetime import datetime,timedelta, date


DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S.%f"
DATETIME_FORMAT = f"{DATE_FORMAT} {TIME_FORMAT}"


def get_abbr(string_obj: str, max_len: int = 2) -> str:
    abbr = ""
    for part in str(string_obj).split(" "):
        if len(abbr) < max_len and part:
            abbr += part[0]
    
    return abbr or "?"

def get_date_str(date_obj) -> str:
    new_date_obj = None
    if isinstance(date_obj, str):
        new_date_obj = date(date_obj)
    elif isinstance(date_obj, (datetime, timedelta)):
        new_date_obj = date_obj.date()
    elif isinstance(date_obj, date):
        new_date_obj = date_obj
    
    if not new_date_obj:
        return 

    return new_date_obj.strftime(DATE_FORMAT)

def get_date_str_combined(date_obj: str) -> str:
    today = date.today().strftime("%Y-%m-%d")
    return "".join(
        get_date_str(date_obj).split("-")
    ) if date_obj else "".join(str(today).split("-"))

def count_data(model):
    return model.objects.filter(created_at__date=date.today()).count()

def get_login_user():
    pass