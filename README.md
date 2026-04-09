# Mel-Band Roformer — удобный Colab для разделения аудио

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Y4TSK0V/MelBandRoformer_UserFriendly-Colab/blob/main/MelBandRoformer_UserFriendly_Colab.ipynb)

Colab-ноутбук для разделения музыки на вокал и инструментал с помощью моделей [Mel-Band Roformer](https://github.com/KimberleyJensen/Mel-Band-Roformer-Vocal-Model). Русскоязычный интерфейс, 50+ моделей из коллекции [GaboxR67](https://huggingface.co/GaboxR67/MelBandRoformers), загрузка с компьютера или Google Drive.

## Что умеет

- Извлечение вокала из песни (акапелла)
- Создание минусовки (инструментал без голоса)
- Караоке-версии (убирает ведущий вокал, оставляет бэки)
- Шумоподавление и удаление реверберации

## Как пользоваться

1. Откройте ноутбук по кнопке выше
2. Включите GPU: *Среда выполнения → Сменить среду → T4 GPU*
3. Выполняйте ячейки по порядку: выбор модели → установка → загрузка файлов → обработка → прослушивание и скачивание

На выходе получите два WAV-файла: `*_vocals.wav` и `*_instrumental.wav`.

## Модели

Ноутбук автоматически генерирует подходящий конфиг под выбранную модель. Модели делятся на три архитектуры:

| Архитектура | dim | depth | Размер | Примеры |
|-------------|-----|-------|--------|---------|
| Стандартная | 384 | 6 | ~913 MB | Inst GaboxF v9, Vocal Fv6, Karaoke GaBox V1 |
| Компактная | 256 | 12 | ~490 MB | Vocal Fv7, Inst Flowers V10 |
| Малая | 384 | 6 (mlp=1) | ~203 MB | Small Karaoke |

**Если не знаете, что выбрать:**
- Для минусовки — *Inst GaboxF v9*
- Для вокала — *Vocal Fv6* (стабильная) или *Vocal GaboxFv2*
- Для караоке — *Karaoke GaBox V1*

Полный список — в интерфейсе ноутбука, там же описания.

## Форматы

Загружать можно MP3, WAV, FLAC, M4A, OGG, WMA, AIFF, OPUS. Всё автоматически конвертируется в WAV перед обработкой. Результаты — WAV 44100 Hz стерео.

## Отличия от оригинала

Оригинальный ноутбук [KimberleyJensen](https://github.com/KimberleyJensen/Mel-Band-Roformer-Vocal-Model) поддерживает одну модель и только WAV-файлы. Здесь:

- Каталог из 50+ моделей с разбивкой по категориям
- Программная генерация YAML-конфигов (не скачивание чужих файлов с возможными ошибками)
- Загрузка файлов с компьютера или Google Drive
- Конвертация любых аудиоформатов через ffmpeg
- MP3-превью результатов прямо в браузере (не грузит гигабайтные WAV в DOM)
- ZIP-архив по кнопке, а не автоматически
- Проверки: GPU, размер модели, совпадение архитектуры с профилем, целостность скачанного файла

## Известные ограничения

- Модели с профилем `small` (203 MB) могут не работать — параметр `mlp_expansion_factor` поддерживается не всеми версиями inference-кода
- Для инструментальных моделей выходные файлы `_vocals` и `_instrumental` иногда перепутаны — просто послушайте оба
- Бесплатный Colab даёт ~12 GB RAM и T4 GPU; на длинных треках (>10 мин) может не хватить памяти — попробуйте компактную модель (490 MB)

## Источники

- Код inference: [KimberleyJensen/Mel-Band-Roformer-Vocal-Model](https://github.com/KimberleyJensen/Mel-Band-Roformer-Vocal-Model)
- Модели: [GaboxR67/MelBandRoformers](https://huggingface.co/GaboxR67/MelBandRoformers)
- Оригинальный Colab: [ссылка](https://colab.research.google.com/drive/1tyP3ZgcD443d4Q3ly7LcS3toJroLO5o1)

## Лицензия

Следует лицензии [оригинального репозитория](https://github.com/KimberleyJensen/Mel-Band-Roformer-Vocal-Model).

---

# Mel-Band Roformer — User-Friendly Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Y4TSK0V/MelBandRoformer_UserFriendly-Colab/blob/main/MelBandRoformer_UserFriendly_Colab.ipynb)

A Colab notebook for separating music into vocals and instrumentals using [Mel-Band Roformer](https://github.com/KimberleyJensen/Mel-Band-Roformer-Vocal-Model) models. Russian-language interface, 50+ models from [GaboxR67](https://huggingface.co/GaboxR67/MelBandRoformers), upload from local machine or Google Drive.

## What it does

- Vocal extraction (acapella)
- Instrumental creation (music without voice)
- Karaoke versions (removes lead vocals, keeps backing)
- Denoising and dereverb

## How to use

1. Open the notebook via the button above
2. Enable GPU: *Runtime → Change runtime type → T4 GPU*
3. Run cells in order: model selection → setup → upload files → process → listen & download

Output: two WAV files per track — `*_vocals.wav` and `*_instrumental.wav`.

## Models

The notebook generates compatible YAML configs automatically. Three architecture tiers:

| Architecture | dim | depth | Size | Examples |
|-------------|-----|-------|------|----------|
| Standard | 384 | 6 | ~913 MB | Inst GaboxF v9, Vocal Fv6, Karaoke GaBox V1 |
| Compact | 256 | 12 | ~490 MB | Vocal Fv7, Inst Flowers V10 |
| Small | 384 | 6 (mlp=1) | ~203 MB | Small Karaoke |

**Quick picks:**
- Instrumentals — *Inst GaboxF v9*
- Vocals — *Vocal Fv6* (stable) or *Vocal Fv7* (compact, newer)
- Karaoke — *Karaoke GaBox V1*

## Differences from original

The original notebook supports one model and WAV-only input. This version adds 50+ models with category browsing, programmatic config generation, multi-format support via ffmpeg, MP3 previews in browser, optional ZIP download, and validation checks throughout.

## Sources

- Inference code: [KimberleyJensen/Mel-Band-Roformer-Vocal-Model](https://github.com/KimberleyJensen/Mel-Band-Roformer-Vocal-Model)
- Models: [GaboxR67/MelBandRoformers](https://huggingface.co/GaboxR67/MelBandRoformers)

## License

Follows the license of the [original repository](https://github.com/KimberleyJensen/Mel-Band-Roformer-Vocal-Model).
