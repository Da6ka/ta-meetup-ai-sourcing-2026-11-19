# How I teach AI to source candidates

Workshop materials by Daria Ivanova for [SPb IT Recruiter Meetup](https://proit-fest.timepad.ru/event/4273243/), November 19, 2026. Use a Lead Data Engineer brief to build LinkedIn and Google searches and test them on sample profiles in Codex. Save those checks as a sourcing skill. On your next search, give Codex your new brief and ask it to apply the same rules to your query.

**[Try the exercise on your own role](en/participant-guide.md#my-first-sourcing-skill) · [Попробовать на своей вакансии](materialy-uchastnikam.md#мой-первый-скилл-для-сорсинга)**

[English workshop guide](en/README.md) · [Описание на русском](#русский)

## Workshop materials / Материалы митапа

| English | Русский |
| --- | --- |
| [Slides (PDF)](en/slides.pdf) | [Веб-презентация на русском (Vercel)](https://ta-meetup-ai-sourcing.vercel.app/) |
| [Two-sided A4 handout (PDF)](en/handout.pdf) | [Двусторонняя раздатка A4 (PDF)](output/pdf/razdatka.pdf) |
| [Participant guide](en/participant-guide.md) · [Codex demo prompts](en/participant-guide.md#codex-demo) | [Руководство участника](materialy-uchastnikam.md) · [Промпты для демо в Codex](materialy-uchastnikam.md#демо-в-codex) |
| [Sample job description](en/lead-data-engineer.md) · [Sample resume](en/sasha.md) | [Учебная вакансия](materials/lead-data-engineer.md) · [Учебное резюме](materials/sasha.md) |
| [Talent Intel market map (PDF)](en/talent-intel-lead-data-engineer.pdf) | [Карта рынка Talent Intel (PDF)](output/pdf/talent-intel-lead-data-engineer.pdf) |

The participant guide also includes a hiring brief template, sample search queries and sources. Compensation figures in the market map reflect the research available on the meetup date.

## Русский

**Как я учу ИИ искать кандидатов**

Материалы Дарьи Ивановой для [SPb IT Recruiter Meetup «Эффективный поиск»](https://proit-fest.timepad.ru/event/4273243/), 19 ноября 2026 года. На примере вакансии Lead Data Engineer вы соберёте запросы для LinkedIn и Google и проверите их на учебных профилях в Codex. Сохраните правила проверки в скилле. Когда начнёте поиск по новой вакансии, дайте Codex новый бриф и попросите проверить запрос по тем же правилам.

Начните с презентации и раздатки в правой колонке [таблицы материалов](#workshop-materials--материалы-митапа). Затем откройте руководство участника. В нём есть шаблон брифа, примеры запросов, источники и упражнение для вашей вакансии. Данные о ставках в карте рынка относятся к дате митапа.

## Additional resources / Дополнительные материалы

- [English handout QR code](en/handout-qr.png), market map ([Markdown](en/talent-intel-lead-data-engineer.md), [JSON](en/talent-intel-lead-data-engineer.json)), [presenter guide](en/presenter-guide.md), [changelog](en/CHANGELOG.md).
- [QR-код русской раздатки](materials/razdatka-qr.png), [прямое скачивание раздатки](https://raw.githubusercontent.com/Da6ka/ta-meetup-ai-sourcing-2026-11-19/main/output/pdf/razdatka.pdf), карта рынка ([Markdown](output/talent-intel-lead-data-engineer.md), [JSON](output/talent-intel-lead-data-engineer.json)), [сценарий выступления](plan-ta-meetup.md), [история изменений](CHANGELOG.md).

## Rebuild the Russian handout / Пересборка русской раздатки

Run `python3 scripts/build_handout.py` with Python 3, ReportLab 5.0.0 and the macOS Arial fonts. The script writes the same PDF to `razdatka.pdf` and the legacy download path `ta-meetup-brief-a4.pdf`.

Для сборки запустите `python3 scripts/build_handout.py` с Python 3, ReportLab 5.0.0 и системными шрифтами Arial в macOS. Скрипт сохраняет одинаковый PDF по адресам `razdatka.pdf` и `ta-meetup-brief-a4.pdf`.
