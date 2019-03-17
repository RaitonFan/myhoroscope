from horoscope import times, advices, promises
from horoscope import generate_prophecies
from datetime import datetime as dt


def generate_page(head, body):
    page = "<html>" + head + body + "</html>"
    return page

def generate_head(title):
    head = "<meta charset='utf-8'>" + "<title>" + title + "</title>"
    return "<head>" + head + "</head>"

def generate_body(header, paragraphs):
   body = f"""
   <h1>{header}</h1> 
   <img src=овен.jpg height='100'</img>"""

   t = 0
   a = 0
   p = 0
   body = body + "<ol>"
   body = body + f"<li>Времена</li>"
   while  t < len(times):
   	body = body + f"""<ul><li>{times[t]}</li></ul> """
   	t = t + 1

   body = body + f"<li>Глаголы</li>"
   while a < len(advices):
   	body = body + f"""<ul><li>{advices[a]}</li></ul> """
   	a = a + 1

   body = body + f"<li>Предсказания</li>"
   while p < len(promises):
   	body = body + f"""<ul><li>{promises[p]}</li></ul> """
   	p = p + 1
   body = body + f"<a href=index.html>Вернуться на главную</a>"
   return body +"</ol>"

def save_page(title, header, paragraphs, output="about.html"):
    fp = open(output, "w", encoding="utf-8")
    today = dt.now().date()
    page = generate_page(
        head=generate_head(title),
        body=generate_body(header=header, paragraphs=paragraphs)
    )
    print(page, file=fp)
    fp.close()


today = dt.now().date()
save_page(
   title="О чём всё это",
   header="О чём всё это",
   paragraphs=times,
)
print("Готово")