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
prompt=re.search('Первое задание для ИИ: «(.*?)»',src).group(1)
root=Path('/System/Library/Fonts/Supplemental')
for name,file in [('Regular','Arial.ttf'),('Bold','Arial Bold.ttf'),('Serif','Georgia.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(root/file)))
out=Path('output/pdf/ta-meetup-brief-a4.pdf')
c=Canvas(str(out),pagesize=A4)
c.setTitle('Бриф на одну вакансию')
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
header('От брифа к первому поиску')
txt(L,150,'Запрос для ИИ','Bold',14)
wrap(L,178,'«'+prompt+'»','Serif',13,R-L,20)
rule(285)
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
def item(y,idx,title,description):
    side=102
    url=urls[idx]
    qr(R-side,y-15,url,side)
    txt(L,y+7,title,'Bold',17)
    wrap(L,y+32,description,'Regular',12,R-L-side-19,17)
    c.linkURL(url,(L,H-y-11,L+pdfmetrics.stringWidth(title,'Bold',17),H-y+9))
    c.linkURL(url,(R-side,H-y+15-side,R,H-y+15))
item(311,0,'Карта компаний-доноров','Выберите компанию и команду. Найдите публикацию или вакансию, по которой видно, что команда решает похожую задачу.')
item(432,1,'Как расширить запрос','Добавьте смежное название должности и сравните выдачу. Какой подходящий профиль появился только со второй попытки?')
rule(546)
txt(L,580,'Справка по поиску','Bold',14)
for x,idx,title in [(L,2,'Boolean в LinkedIn'),(L+(R-L)/2,3,'Поиск по сайту в Google')]:
    qr(x,606,urls[idx])
    txt(x,736,title,'Bold',12)
    c.linkURL(urls[idx],(x,H-742,x+pdfmetrics.stringWidth(title,'Bold',12),H-722))
    c.linkURL(urls[idx],(x,H-708,x+102,H-606))
c.showPage()
c.save()
