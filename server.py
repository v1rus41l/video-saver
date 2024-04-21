from flask import Flask, render_template, request, jsonify 
import pytube
from urllib.error import HTTPError


app = Flask(__name__)

link = ''
link2 = ''

def main():
    app.run()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', link=link)


@app.route('/process', methods=['POST'])
def process():
    print(1234567)
    global link, link2
    link2 = request.form['link']  # Получаем значение из запроса
    link = str(link2)
    a = link.find('/', 10)
    link = link[:a + 1] + 'embed/' + link[32:] + '?controls=0'
    print(link)
    # Дальнейшая обработка значения my_value
    return render_template('index.html', link=link)


@app.route("/download", methods=["POST"])
def download():
    global link2, link
    # формируем адрес
    # переводим его в нужный формат
    youtubelink=pytube.YouTube(link)
    # получаем ссылку на видео с самым высоким качеством
    video=youtubelink.streams.get_highest_resolution()
    # скачиваем видео
    video.download()
    # выводим результат
    Result="Загрузка завершена"
# если скачать не получилось
    return render_template('index.html', link=link)

    

if __name__ == '__main__':
    main()