import re
from pathlib import Path
from urllib.parse import quote
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.barcode.qrencoder import QRCode,QRErrorCorrectLevel

repo = Path(__file__).resolve().parents[1]
src = (repo / 'materialy-uchastnikam.md').read_text(encoding='utf-8')
repo_page = 'https://github.com/Da6ka/ta-meetup-ai-sourcing-2026-11-19/blob/main/'
links = dict(re.findall(r'\[([^]]+)\]\((https?://[^)]+)\)', src))
front, homework = src.split('# Мой первый скилл для сорсинга', 1)
steps = re.findall(r'^\d+\. \*\*(.+?)\*\* (.+)$', src, re.M)
assert len(steps) == 6
root=Path('/System/Library/Fonts/Supplemental')
for name,file in [('Regular','Arial.ttf'),('Bold','Arial Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(root/file)))
out = repo / 'output/pdf/razdatka.pdf'
c = Canvas(str(out), pagesize=A4, invariant=True)
c.setTitle('От брифа к поиску. Примеры и домашняя практика')
c.setAuthor('Дарья Иванова')
c.setViewerPreference('Duplex', 'DuplexFlipLongEdge')
c.setViewerPreference('PrintScaling', 'None')
W,H=A4
L=46
R=W-L
def txt(x,y,s,font='Regular',size=11):
    c.setFont(font,size)
    c.drawString(x,H-y,s)
def section_link(y, label, target, heading, heading_size):
    width = pdfmetrics.stringWidth(label, 'Bold', 10.5)
    x = R - width
    assert x - L - pdfmetrics.stringWidth(heading, 'Bold', heading_size) >= 16
    c.saveState()
    c.setFillColorRGB(0.10, 0.28, 0.49)
    c.setStrokeColorRGB(0.10, 0.28, 0.49)
    txt(x, y, label, 'Bold', 10.5)
    rule(y + 2, x)
    c.restoreState()
    c.linkURL(repo_page + quote(target, safe="/#"), (x - 3, H - y - 4, R + 3, H - y + 12))
def rule(y,x=L,end=R,weight=.42):
    c.setLineWidth(weight)
    c.line(x,H-y,end,H-y)
def lines(s,font,size,width):
    result=['']
    for w in s.split():
        trial=(result[-1]+' '+w).strip()
        if result[-1] and pdfmetrics.stringWidth(trial,font,size)>width:
            result.append(w)
        else: result[-1]=trial
    return result
def wrap(x,y,s,font,size,width,leading):
    for line in lines(s,font,size,width):
        txt(x,y,line,font,size)
        y+=leading
    return y
def header(title, size=32):
    txt(L, 43, 'SPb IT Recruiter Meetup · Эффективный поиск  /  19 ноября 2026', 'Bold', 10)
    c.setFont('Regular', 10)
    c.drawRightString(R, H - 43, 'Дарья Иванова')
    rule(56,weight=1.15)
    assert pdfmetrics.stringWidth(title, 'Bold', size) <= R - L
    txt(L,104,title,'Bold',size)
def qr(x,y,url,side=102):
    code=QRCode(None,QRErrorCorrectLevel.M); code.addData(url); code.make()
    n=code.getModuleCount(); step=side/(n+8)
    for row in range(n):
        ix=0
        while ix<n:
            if not code.isDark(row,ix):
                ix+=1; continue
            end=ix+1
            while end<n and code.isDark(row,end): end+=1
            c.rect(x+(ix+4)*step,H-y-(row+5)*step,(end-ix)*step,step,fill=1,stroke=0)
            ix=end
front_sections = [block.strip().split('\n\n', 1) for block in front.split('\n### ')[1:]]
(brief_title, brief_body), *search_sections = front_sections
brief_fields = re.findall(r'^- \*\*(.+?)\.\*\* (.+)$', brief_body, re.M)
assert len(brief_fields) == 6

header('От брифа к поиску')
txt(L, 135, brief_title, 'Bold', 15)
section_link(135, 'Шаблон брифа', 'materialy-uchastnikam.md#бриф-на-одну-вакансию', brief_title, 15)
gap = 22
col_width = (R - L - gap) / 2
y = 156
for left, right in zip(brief_fields[::2], brief_fields[1::2]):
    row_bottom = y
    for x, (label, value) in ((L, left), (L + col_width + gap, right)):
        txt(x, y, label, 'Bold', 11)
        end = wrap(x, y + 15, value, 'Regular', 10.5, col_width, 13)
        row_bottom = max(row_bottom, end)
    y = row_bottom + 5

rule(y - 5)
y += 14
for index, (title, body) in enumerate(search_sections):
    txt(L, y, title, 'Bold', 13)
    if index == 0:
        section_link(y, 'Отчёт Talent Intel', 'output/pdf/talent-intel-lead-data-engineer.pdf', title, 13)
    y += 19
    for paragraph in body.split('\n\n'):
        is_query = paragraph.startswith('```text\n')
        font = 'Bold' if is_query else 'Regular'
        paragraph_lines = paragraph.splitlines()
        if is_query:
            paragraph_lines = paragraph_lines[1:-1]
        for line in paragraph_lines:
            y = wrap(L, y, line, font, 10.5, R - L, 13)
        y += 3
    y += 8
assert y < 704, f'Front text reaches QR area: {y}'
rule(710)
for i, (label, link) in enumerate([
    ('Скилл Talent Intel', 'Открытый скилл Talent Intel для Claude Code'),
    ('Скилл для брифа', 'Скилл для подготовки брифа'),
    ('Boolean в LinkedIn', 'Boolean в LinkedIn'),
    ('X-ray в Google', 'поиск по сайту в Google'),
]):
    cell_width = (R - L) / 4
    x = L + i * cell_width
    url = links[link]
    qr(x, 721, url, side=73)
    txt(x, 807, label, 'Bold', 10)
    c.linkURL(url, (x, H - 812, x + cell_width - 7, H - 721))
c.showPage()

header('Мой первый скилл для сорсинга', size=30)
txt(L, 137, 'Три карточки из мастер-класса', 'Bold', 15)
cards = re.findall(r'^([АБВ])\. Senior Data Engineer\. (.+)$', src, re.M)
assert len(cards) == 3
for i, (label, value) in enumerate(cards):
    baseline = 158 + 17 * i
    txt(L, baseline, label, 'Bold', 11)
    txt(L + 19, baseline, value, 'Regular', 11)
rule(207)
txt(L, 234, 'Дома: проверьте на своей вакансии', 'Bold', 15)
y = wrap(L, 255, homework.strip().split('\n\n')[0], 'Regular', 11, R - L, 14) + 10
for i, (title, body) in enumerate(steps, 1):
    txt(L, y, str(i), 'Bold', 12)
    txt(L + 19, y, title, 'Bold', 12)
    y = wrap(L + 19, y + 17, body, 'Regular', 11, R - L - 19, 14) + 8
assert y < 710, f'Homework reaches worksheet area: {y}'
rule(715)
txt(L, 738, 'Моя вакансия', 'Bold', 11)
rule(741, L + 95)
txt(L, 769, 'Первый донор', 'Bold', 11)
rule(772, L + 95)
txt(L, 800, 'Что проверю', 'Bold', 11)
rule(803, L + 95)
c.showPage()
c.save()
# Keep the download link already shared with the organiser working.
out.with_name('ta-meetup-brief-a4.pdf').write_bytes(out.read_bytes())
