# Как я учу ИИ искать кандидатов

Материалы Дарьи Ивановой для SPb IT Recruiter Meetup «Эффективный поиск», 19 ноября 2026 года. На примере Lead Data Engineer вы соберёте запрос для LinkedIn и Google, проверите его на учебных профилях в Codex и попробуете сохранить свои правила поиска в скилле.

## Для участников

1. Откройте [двустороннюю раздатку A4](output/pdf/razdatka.pdf). Её также можно [скачать на телефон](https://raw.githubusercontent.com/Da6ka/ta-meetup-ai-sourcing-2026-11-19/main/output/pdf/razdatka.pdf).
2. Возьмите [учебную вакансию](materials/lead-data-engineer.md), [карту рынка Talent Intel](output/pdf/talent-intel-lead-data-engineer.pdf) и [пример резюме](materials/sasha.md).
3. Скопируйте [запросы для демо](materialy-uchastnikam.md#демо-в-codex) и пройдите [домашнюю практику на своей вакансии](materialy-uchastnikam.md#мой-первый-скилл-для-сорсинга).

В [материалах для участников](materialy-uchastnikam.md) также есть шаблон брифа, примеры поисковых запросов и источники. Данные о ставках в отчёте относятся к дате митапа.

## Для ведущей

- [PowerPoint с заметками](materials/spb-it-recruiter-meetup.pptx) и [сценарий по слайдам](plan-ta-meetup.md). QR-код на слайде 4 совпадает с [отдельным PNG](materials/razdatka-qr.png).
- [Исходник отчёта Talent Intel](output/talent-intel-lead-data-engineer.md) и [данные отчёта в JSON](output/talent-intel-lead-data-engineer.json).
- Для пересборки раздатки нужны Python 3, ReportLab 5.0.0 и системные шрифты Arial в macOS. Команда `python3 scripts/build_handout.py` пересобирает `razdatka.pdf` и записывает те же байты по прежнему адресу `ta-meetup-brief-a4.pdf`.
