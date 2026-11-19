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
urls=re.findall(r'\]\((https?://[^)]+)\)',src)
assert len(questions)==6 and len(urls)==4
steps = re.findall(r'^\d+\. \*\*(.+?)\*\* (.+)$', src, re.M)
assert len(steps) == 6
prompt = re.search(r'^> (.+)$', src, re.M).group(1)
root=Path('/System/Library/Fonts/Supplemental')
for name,file in [('Regular','Arial.ttf'),('Bold','Arial Bold.ttf'),('Serif','Georgia.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(root/file)))
out=Path('output/pdf/ta-meetup-brief-a4.pdf')
c=Canvas(str(out),pagesize=A4)
c.setTitle('Бриф и первый скилл для сорсинга')
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
    txt(L,43,'TA Meetup  /  Дарья Иванова','Bold',10)
    c.setFont('Regular',10)
    c.drawRightString(R,H-43,'19 ноября 2026')
    rule(56,weight=1.15)
    txt(L,104,title,'Bold',32)
header('Бриф на одну вакансию')
txt(L,150,'Кого ищем?','Bold',13)
rule(152,L+85)
for i,q in enumerate(questions):
    top=207+i*102
    txt(L,top,str(i+1).zfill(2),'Regular',10)
    last=wrap(L+32,top,q,'Bold',13,R-L-32,17)
    rule(top+47,L+32)
    rule(top+72,L+32)
c.showPage()
header('Мой первый скилл для сорсинга')
y = wrap(L, 128, 'Дома вы научите Codex расширять поисковый запрос и сохраните эту инструкцию как скилл. Начните с учебной вакансии ниже. Все примеры уже на листе.', 'Regular', 11, R - L, 14) + 9
for i, (title, body) in enumerate(steps, 1):
    txt(L, y, str(i), 'Bold', 11)
    txt(L + 20, y, title, 'Bold', 11.5)
    y = wrap(L + 20, y + 15, body, 'Regular', 10.5, R - L - 20, 13.2) + 6
txt(L, y + 4, 'Сообщение для шага 4', 'Bold', 12)
y = wrap(L, y + 21, prompt, 'Regular', 10.5, R - L, 13.2)
assert y < 614, 'Skill instructions overlap the exercise'
txt(L, 625, 'Мой пример лишнего совпадения для проверки', 'Bold', 11)
rule(651)
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
rule(670)
txt(L, 692, 'Примеры и справка', 'Bold', 13)
labels = ['Карта доноров', 'Пример скилла', 'LinkedIn Boolean', 'Google X-ray']
for i, (url, label) in enumerate(zip(urls, labels)):
    x = L + i * (R - L) / 4
    qr(x, 704, url, side=82)
    txt(x, 802, label, 'Regular', 10)
    c.linkURL(url, (x, H - 807, x + 100, H - 704))
c.showPage()
c.save()
