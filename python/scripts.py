from datetime import date
from browser import document, html # type: ignore

today = date.today()
v = today.strftime("%Y")
element = "Все права защищены © «NFox | ALT STUDIO», 2017-", v

document['text_footer'] <= html.SPAN(element)