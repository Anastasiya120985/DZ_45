from django.http import HttpResponse


writer_info = {'Hemingway': {'1926': 'Информация о книгах, которые написал Хемингуэй в 1926 году',
                             '1940': 'Информация о книгах, которые написал Хемингуэй в 1940 году'
                             }
               }


def main(request):
    res = '''<h1>Главная</h1><br>
    <a href=/writer>Писатели</a><br>
    <a href=/books>Топ лучших книг</a>
    '''
    return HttpResponse(res)


def writer(request):
    if request.GET:
        writers = request.GET.get('writers')
        year = request.GET.get('year')
        return HttpResponse(writer_info[writers][year])
    else:
        return HttpResponse('<h2>Писатели</h2>')


def writer_about(request, write_name):
    writers = {'Hemingway': '<h2>Хемингуэй</h2>',
               'Shakespeare': '<h2>Шекспир</h2>'}
    if write_name in writers:
        return HttpResponse(writers[write_name])
    else:
        return HttpResponse('<h2>Писатели</h2>')


def writer_books(request, write_name, book):
    writer_book = {'Hemingway': {'The_old_man_and_the_sea': '<h2>Старик и море</h2>', 'The_sun_also_rises': '<h2>И восходит солнце</h2>'},
                   'Shakespeare': {'Romeo_and_Juliet': '<h2>Ромео и Джульетта</h2>'}}
    return HttpResponse(writer_book[write_name][book])


def books(request):
    return HttpResponse(f'<h2>Топ лучших книг</h2>')


def book_about(request, books_name):
    book = {'1': '<h2>Старик и море</h2>',
            '2': '<h2>Ромео и Джульетта</h2>',
            '3': '<h2>И восходит солнце</h2>'}
    if books_name in book:
        return HttpResponse(book[books_name])
    else:
        return HttpResponse(f'<h2>Топ лучших книг</h2>')