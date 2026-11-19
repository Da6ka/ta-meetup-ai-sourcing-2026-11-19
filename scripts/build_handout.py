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
assert len(questions)==6 and len(urls)==3
demo = re.findall(r'^### (Слайд [^\n]+)\n\n```text\n(.*?)\n```', src, re.M | re.S)
assert len(demo) == 2
steps = re.findall(r'^\d+\. \*\*(.+?)\*\* (.+)$', src, re.M)
assert len(steps) == 6
root=Path('/System/Library/Fonts/Supplemental')
for name,file in [('Regular','Arial.ttf'),('Bold','Arial Bold.ttf'),('Serif','Georgia.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(root/file)))
out=Path('output/pdf/razdatka.pdf')
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
    txt(L, 43, 'SPb IT Recruiter Meetup · Эффективный поиск  /  19 ноября 2026', 'Bold', 10)
    c.setFont('Regular', 10)
    c.drawRightString(R, H - 43, 'Дарья Иванова')
    rule(56,weight=1.15)
    txt(L,104,title,'Bold',32)
header('Бриф на одну вакансию')
txt(L,137,'Кого ищем?','Bold',13)
rule(139,L+85)
top = 168
for i,q in enumerate(questions):
    txt(L,top,str(i+1).zfill(2),'Regular',10)
    last=wrap(L+32,top,q,'Bold',11,R-L-32,14)
    rule(last+9,L+32)
    top = last + 32
rule(top, weight=1)
txt(L,top+23,'Демо в Codex','Bold',18)
txt(L,top+41,'Отправьте сообщения по очереди в один чат.','Regular',11)
y = top + 64
for title,prompt in demo:
    txt(L,y,title,'Bold',12)
    y += 16
    for paragraph in prompt.split('\n\n'):
        y = wrap(L, y, paragraph, 'Regular', 10.5, R-L, 13.1) + 3
    y += 7
assert y - 10 < H - 28, f'Demo reaches page bottom at {y:.1f} pt'
c.showPage()
header('Мой первый скилл для сорсинга')
y = wrap(L, 128, src.split('\n\n')[1], 'Regular', 11, R - L, 14) + 9
for i, (title, body) in enumerate(steps, 1):
    txt(L, y, str(i), 'Bold', 11)
    txt(L + 20, y, title, 'Bold', 11.5)
    y = wrap(L + 20, y + 15, body, 'Regular', 10.5, R - L - 20, 13.2) + 6
assert y < 667, f'Instructions reach QR area at {y:.1f} pt'
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
labels = ['Пример скилла', 'LinkedIn Boolean', 'Google X-ray']
for i, (url, label) in enumerate(zip(urls, labels)):
    x = L + i * (R - L) / len(labels)
    qr(x, 704, url, side=82)
    txt(x, 802, label, 'Regular', 10)
    c.linkURL(url, (x, H - 807, x + 100, H - 704))
c.showPage()
c.save()
# Keep the download link already shared with the organiser working.
out.with_name('ta-meetup-brief-a4.pdf').write_bytes(out.read_bytes())
