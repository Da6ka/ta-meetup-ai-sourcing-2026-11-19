import re
from pathlib import Path
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.barcode.qrencoder import QRCode,QRErrorCorrectLevel

src=Path('materialy-uchastnikam.md').read_text()
questions=re.findall(r'^\| ([^|]+?) \| \|$',src,re.M)
links = dict(re.findall(r'\[([^]]+)\]\((https?://[^)]+)\)', src))
assert len(questions) == 6
front, homework = src.split('# Мой первый скилл для сорсинга', 1)
steps = re.findall(r'^\d+\. \*\*(.+?)\*\* (.+)$', src, re.M)
assert len(steps) == 6
root=Path('/System/Library/Fonts/Supplemental')
for name,file in [('Regular','Arial.ttf'),('Bold','Arial Bold.ttf'),('Serif','Georgia.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(root/file)))
out=Path('output/pdf/razdatka.pdf')
c=Canvas(str(out),pagesize=A4)
c.setTitle('Поиск по должности и компании. Бриф и первый скилл')
c.setAuthor('Дарья Иванова')
W,H=A4
L=46
R=W-L
def txt(x,y,s,font='Regular',size=11):
    c.setFont(font,size)
    c.drawString(x,H-y,s)
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
def header(title):
    txt(L, 43, 'SPb IT Recruiter Meetup · Эффективный поиск  /  19 ноября 2026', 'Bold', 10)
    c.setFont('Regular', 10)
    c.drawRightString(R, H - 43, 'Дарья Иванова')
    rule(56,weight=1.15)
    txt(L,104,title,'Bold',32)
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
header('Поиск по должности и компании')
y = 134
for block in front.split('\n### ')[1:]:
    title, body = block.strip().split('\n\n', 1)
    txt(L, y, title, 'Bold', 13)
    y += 19
    for paragraph in body.split('\n\n'):
        if paragraph.startswith('[Metaview Sourcing]'):
            continue
        is_query = paragraph.startswith(('("', 'site:'))
        font = 'Bold' if is_query else 'Regular'
        y = wrap(L, y, paragraph, font, 10.5 if is_query else 11, R - L, 13.5) + 3
    y += 3
assert y < 710, f'Front text reaches QR area: {y}'
rule(712)
for i, (label, link) in enumerate([
    ('Скилл Talent Intel', 'Открытый скилл Talent Intel для Claude Code'),
    ('Boolean в LinkedIn', 'Boolean в LinkedIn'),
    ('X-ray в Google', 'поиск по сайту в Google'),
]):
    x = L + i * (R - L) / 3
    url = links[link]
    qr(x, 725, url, side=76)
    txt(x, 818, label, 'Bold', 11)
    c.linkURL(url, (x, H - 822, x + 130, H - 725))
c.showPage()

header('Бриф на одну вакансию')
txt(L, 128, 'Должность', 'Bold', 11)
rule(129, L + 69, L + 240)
txt(L + 255, 128, 'Компания', 'Bold', 11)
rule(129, L + 315, R)
gap = 18
col_width = (R - L - gap) / 2
for i, question in enumerate(questions):
    x = L + (i % 2) * (col_width + gap)
    top = 153 + (i // 2) * 69
    bottom = wrap(x, top, question, 'Regular', 10.5, col_width, 13)
    assert bottom < top + 52
    rule(top + 52, x, x + col_width)
prep = src.split('### До звонка с нанимающим менеджером\n\n', 1)[1].split('\n## ', 1)[0]
prompt = prep.strip().split('\n\n')[1]
url = links['Скилл для подготовки брифа']
qr(R - 80, 349, url, side=80)
c.linkURL(url, (R - 80, H - 429, R, H - 349))
txt(L, 365, 'До звонка с нанимающим менеджером', 'Bold', 15)
txt(L, 382, 'Откройте скилл по QR. После запроса вставьте описание вакансии.', 'Regular', 10)
end = wrap(L, 399, prompt, 'Regular', 10.5, R - L - 94, 13)
assert end < 455
txt(L, 458, 'Дома: мой первый скилл для сорсинга', 'Bold', 18)
y = wrap(L, 480, homework.strip().split('\n\n')[0], 'Regular', 10.5, R - L, 13) + 5
for i, (title, body) in enumerate(steps, 1):
    txt(L, y, str(i), 'Bold', 11)
    txt(L + 19, y, title, 'Bold', 11)
    y = wrap(L + 19, y + 14, body, 'Regular', 10.5, R - L - 19, 12.5) + 2
assert y < H - 18, f'Homework reaches page bottom: {y}'
c.showPage()
c.save()
# Keep the download link already shared with the organiser working.
out.with_name('ta-meetup-brief-a4.pdf').write_bytes(out.read_bytes())
