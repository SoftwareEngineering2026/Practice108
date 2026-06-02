# Отчёт по интеграции безопасности в CI/CD

**Проект:** [ManatovIA / Practice105](https://github.com/ManatovIvan/Practice105/actions)

---

## Что было сделано

В исходном воркфлоу только прогонялись тесты — никаких проверок безопасности не было. Рядом с существующим джобом `test` добавлен новый джоб `security` с тремя инструментами: Bandit, Gitleaks и Trivy. Также добавлен `workflow_dispatch` для ручного запуска из вкладки Actions.

---

## Внесённые изменения

### 1. Добавлен `workflow_dispatch`

Позволяет запускать воркфлоу вручную без пуша или PR.

### 2. Новый джоб `security`

| Инструмент | Назначение | Конфигурация |
|---|---|---|
| Bandit | SAST — небезопасные паттерны в Python | `targets: ./ManatovIA` |
| Gitleaks | Утечки секретов и токенов | стандартная |
| Trivy | SCA — CVE в зависимостях | `scan-type: fs` |

---

## Проблемы и решения

**Bandit — нет прав на загрузку SARIF**
Ошибка: `Resource not accessible by integration`. Исправлено добавлением `security-events: write` в `permissions` джоба.

**Gitleaks — недопустимое имя артефакта**
Версия `v2.3.4` падала из-за точки в имени `gitleaks-results.sarif`. Исправлено переходом на `gitleaks/gitleaks-action@v2`.

**Trivy — неверный тип сканирования**
По умолчанию `scan-type: image` — не работает с локальной папкой. Исправлено на `scan-type: fs`, что корректно для Python-проекта с `requirements.txt`.

---

## Итог

Оба джоба запускаются при пуше в `ManatovIA`, при PR в `main` и вручную. Найденные проблемы отображаются во вкладке **Security → Code scanning alerts**.
