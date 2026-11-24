# How I teach AI to source candidates

Workshop materials by Daria Ivanova for SPb IT Recruiter Meetup, November 19, 2026. Use a Lead Data Engineer brief to build LinkedIn and Google searches, test them on sample profiles in Codex, and save your checks as a reusable sourcing skill.

[Start with the English workshop guide](en/README.md) or open the slides, handout and exercises below. [Перейти к описанию на русском](#русский)

## Workshop materials / Материалы митапа

| English | Русский |
| --- | --- |
| [Slides (PDF)](en/slides.pdf) | [Веб-презентация на русском (Vercel)](https://ta-meetup-ai-sourcing.vercel.app/) |
| [Two-sided A4 handout (PDF)](en/handout.pdf) · [QR code](en/handout-qr.png) | [Двусторонняя раздатка A4 (PDF)](output/pdf/razdatka.pdf) · [Скачать напрямую](https://raw.githubusercontent.com/Da6ka/ta-meetup-ai-sourcing-2026-11-19/main/output/pdf/razdatka.pdf) · [QR-код](materials/razdatka-qr.png) |
| [Participant guide](en/participant-guide.md) · [Codex prompts](en/participant-guide.md#codex-demo) · [Take-home exercise](en/participant-guide.md#my-first-sourcing-skill) | [Руководство участника](materialy-uchastnikam.md) · [Промпты для Codex](materialy-uchastnikam.md#демо-в-codex) · [Домашняя практика](materialy-uchastnikam.md#мой-первый-скилл-для-сорсинга) |
| [Sample job description](en/lead-data-engineer.md) · [Sample resume](en/sasha.md) | [Учебная вакансия](materials/lead-data-engineer.md) · [Учебное резюме](materials/sasha.md) |
| Talent Intel market map ([PDF](en/talent-intel-lead-data-engineer.pdf), [Markdown](en/talent-intel-lead-data-engineer.md), [JSON](en/talent-intel-lead-data-engineer.json)) | Карта рынка Talent Intel ([PDF](output/pdf/talent-intel-lead-data-engineer.pdf), [Markdown](output/talent-intel-lead-data-engineer.md), [JSON](output/talent-intel-lead-data-engineer.json)) |
| [Presenter guide](en/presenter-guide.md) · [Changelog](en/CHANGELOG.md) | [Сценарий выступления](plan-ta-meetup.md) · [История изменений](CHANGELOG.md) |

The participant guide also includes a hiring brief template, sample search queries and sources. Compensation figures in the market map reflect the research available on the meetup date.

## Русский

**Как я учу ИИ искать кандидатов**

Материалы Дарьи Ивановой для SPb IT Recruiter Meetup «Эффективный поиск», 19 ноября 2026 года. На примере вакансии Lead Data Engineer вы соберёте запросы для LinkedIn и Google, проверите их на учебных профилях в Codex и сохраните свои правила поиска в скилле.

Начните с презентации и раздатки в правой колонке [таблицы материалов](#workshop-materials--материалы-митапа). Затем откройте руководство участника. В нём есть шаблон брифа, примеры запросов, источники и упражнение для вашей вакансии. Данные о ставках в карте рынка относятся к дате митапа.

## Rebuild the Russian handout / Пересборка русской раздатки

Run `python3 scripts/build_handout.py` with Python 3, ReportLab 5.0.0 and the macOS Arial fonts. The script writes the same PDF to `razdatka.pdf` and the legacy download path `ta-meetup-brief-a4.pdf`.

Для сборки запустите `python3 scripts/build_handout.py` с Python 3, ReportLab 5.0.0 и системными шрифтами Arial в macOS. Скрипт сохраняет одинаковый PDF по адресам `razdatka.pdf` и `ta-meetup-brief-a4.pdf`.
