"""Case-study #4 Парсинг web-страниц
Разработчики:
Золотых М.Д., Шерубнева А., Зеленская А.
"""
import urllib.request

with open('input.txt', 'r') as f_in:
    for line in f_in:
        f = urllib.request.urlopen(line)
        s = f.read()
        text = str(s)
        part_name = text.find("player-name")
        name = text[text.find('>', part_name) + 1:text.find('&', part_name)]
        number = text.find("TOTAL")
        res = text[text.find('TOTAL', number) + 5:text.find('</table>', number)]
        res = res.replace("<td>", " ")
        res = res.replace("</td>", " ")
        res = res.replace("t", " ")
        res = res.replace("n", " ")
        res = res.replace("\ ", "")
        res = res.replace("</ r>", "")
        repl1 = res[res.find('.', res.find('.')) - 4:res.find('.', res.find('.')) + 2]
        res = res.replace(repl1, '')
        repl2 = res[res.find('.', res.find('.')) - 3:res.find('.', res.find('.')) + 2]
        res = res.replace(repl2, '')
        res = res.replace("  ", " ")

        print('{:<20s}{:<105s}'.format(name, res))