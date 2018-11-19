"""Case-study #5 Парсинг web-страниц
Разработчики:
Золотых М.Д., Шерубнева А., Зеленская А.
"""
import urllib.request

with open('input.txt', 'r') as f_in:
    with open('output.txt', 'w') as f_out:
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
            res = res[1:]
            comp_b = res.find(' ')
            comp = res[0:(comp_b)]
            res = res[(comp_b)+1:]
            att_b = res.find(' ')
            att = res[0:(att_b)]
            res = res[(att_b) + 1:]
            yds_b = res.find(' ')
            yds = res[0:(yds_b)]
            res = res[(yds_b) + 1:]
            td_b = res.find(' ')
            td = res[0:(td_b)]
            res = res[(td_b) + 1:]
            int_b = res.find(' ')
            int = res[0:(int_b)]
            res = res[(int_b) + 1:]
            f1 = res.find(' ')
            res = res[(f1)+1:]
            f2 = res.find(' ')
            res = res[(f2) + 1:]
            rate_b = res.find(' ')
            rate = res[0:(rate_b)]
            rate = float(rate)
            print('{:<20s} {:<7s} {:<7s} {:<7s} {:<7s} {:<7s} {:<7.2f}'.format(name, comp, att, yds, td, int, rate), file = f_out)