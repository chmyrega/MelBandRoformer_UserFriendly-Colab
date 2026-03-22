# 🎵 Mel-Band-Roformer - Расширенная версия с русским интерфейсом

[![Open In Colab](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/chmyrega/MelBandRoformer_UserFriendly-Colab/blob/main/MelBandRoformer_UserFriendly_Colab.ipynb)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Models-blue)](https://huggingface.co/GaboxR67/MelBandRoformers)

[English version](#english-version) (planned, not yet available)

## 📖 О проекте

Это расширенная версия [Mel-Band-Roformer-Vocal-Model](https://github.com/KimberleyJensen/Mel-Band-Roformer-Vocal-Model) с русскоязычным интерфейсом и дополнительными моделями для профессионального разделения аудио на компоненты.

### 🔗 Источники
- **Оригинальный репозиторий**: [KimberleyJensen/Mel-Band-Roformer-Vocal-Model](https://github.com/KimberleyJensen/Mel-Band-Roformer-Vocal-Model)
- **Базовый Colab notebook**: [Original Colab](https://colab.research.google.com/drive/1tyP3ZgcD443d4Q3ly7LcS3toJroLO5o1)
- **Дополнительные модели**: [GaboxR67/MelBandRoformers](https://huggingface.co/GaboxR67/MelBandRoformers/tree/main/melbandroformers)

## ✨ Особенности

- 🇷🇺 **Полностью русифицированный интерфейс**
- 🎯 **7 специализированных моделей** для различных задач
- 📁 **Поддержка популярных форматов**: MP3, WAV, FLAC, M4A, OGG
- 🎨 **Интерактивный выбор модели** с описанием каждой
- ⚡ **Упрощенная установка** - всего несколько кликов
- 📦 **Автоматическая упаковка результатов** в ZIP-архив

## 🤖 Доступные модели

### Вокальные модели
- **🎤 Стандартная модель** - оригинальная модель для извлечения вокала
- **🎙️ Вокальная (улучшенная)** - специализирована на извлечении вокала с сохранением деталей

### Инструментальные модели  
- **🎸 Инструментальная (последняя версия V7z)** - создание качественных минусовок
- **🎹 Инструментальная V8** - стабильная версия с хорошим балансом

### Специальные модели
- **🎤 Караоке модель** - оптимизирована для создания караоке-треков
- **🧪 Экспериментальная V10** - новейшие разработки
- **🎵 Шумоподавление** - удаление шумов и артефактов из старых записей

## 🚀 Быстрый старт

1. Откройте notebook в Google Colab
2. Убедитесь, что включен GPU (Среда выполнения → Сменить среду выполнения → GPU)
3. Запустите ячейки по порядку:
   - **Шаг 1**: Выберите модель
   - **Шаг 2**: Установка (автоматическая)
   - **Шаг 3**: Загрузите аудиофайлы
   - **Шаг 4**: Обработка
   - **Шаг 5**: Скачайте результаты

## 📊 Результаты

После обработки вы получите:
- `[имя_файла]_vocals.wav` - извлеченный вокал
- `[имя_файла]_instrumental.wav` - музыка без вокала

## 💡 Советы по использованию

- Для современной музыки используйте стандартные модели
- Для старых записей попробуйте модель с шумоподавлением  
- Экспериментальные модели могут дать неожиданные результаты
- Качество зависит от исходного файла, не рекомендуется закидывать сэмплы плохого качества

## 🛠️ Технические детали

- Основан на архитектуре Mel-Band Roformer
- Использует PyTorch для обработки
- Поддерживает CUDA для ускорения на GPU
- Автоматическая конвертация различных аудиоформатов

## 📝 Лицензия

Этот проект следует лицензии оригинального репозитория [Mel-Band-Roformer-Vocal-Model](https://github.com/KimberleyJensen/Mel-Band-Roformer-Vocal-Model).

## 🤝 Благодарности

- [KimberleyJensen](https://github.com/KimberleyJensen) за оригинальную реализацию
- [GaboxR67](https://huggingface.co/GaboxR67) за дополнительные модели

---

<a name="english-version"></a>

# 🎵 Mel-Band-Roformer - Extended Version with Russian Interface

[![Open In Colab](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/chmyrega/MelBandRoformer_UserFriendly-Colab/blob/main/MelBandRoformer_UserFriendly_Colab.ipynb)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Models-blue)](https://huggingface.co/GaboxR67/MelBandRoformers)

**Note**: English version of the interface is planned but not yet implemented. The current version features a fully Russian interface.

## 📖 About

This is an extended version of [Mel-Band-Roformer-Vocal-Model](https://github.com/KimberleyJensen/Mel-Band-Roformer-Vocal-Model) with Russian interface and additional models for professional audio source separation.

### 🔗 Sources
- **Original repository**: [KimberleyJensen/Mel-Band-Roformer-Vocal-Model](https://github.com/KimberleyJensen/Mel-Band-Roformer-Vocal-Model)
- **Base Colab notebook**: [Original Colab](https://colab.research.google.com/drive/1tyP3ZgcD443d4Q3ly7LcS3toJroLO5o1)
- **Additional models**: [GaboxR67/MelBandRoformers](https://huggingface.co/GaboxR67/MelBandRoformers/tree/main/melbandroformers)

## ✨ Features

- 🇷🇺 **Fully Russian interface** (English version planned)
- 🎯 **7 specialized models** for different tasks
- 📁 **Support for popular formats**: MP3, WAV, FLAC, M4A, OGG
- 🎨 **Interactive model selection** with descriptions
- ⚡ **Simplified installation** - just a few clicks
- 📦 **Automatic result packaging** in ZIP archive

## 🤖 Available Models

### Vocal Models
- **🎤 Standard Model** - original model for vocal extraction
- **🎙️ Vocal (Enhanced)** - specialized in vocal extraction with detail preservation

### Instrumental Models
- **🎸 Instrumental (Latest V7z)** - quality instrumental creation
- **🎹 Instrumental V8** - stable version with good balance

### Special Models
- **🎤 Karaoke Model** - optimized for karaoke track creation
- **🧪 Experimental V10** - latest developments
- **🎵 Denoise** - noise and artifact removal from old recordings

## 🚀 Quick Start

1. Open notebook in Google Colab
2. Ensure GPU is enabled (Runtime → Change runtime type → GPU)
3. Run cells in order:
   - **Step 1**: Select model
   - **Step 2**: Installation (automatic)
   - **Step 3**: Upload audio files
   - **Step 4**: Processing
   - **Step 5**: Download results

## 📊 Results

After processing you'll get:
- `[filename]_vocals.wav` - extracted vocals
- `[filename]_instrumental.wav` - music without vocals

## 🛠️ Technical Details

- Based on Mel-Band Roformer architecture
- Uses PyTorch for processing
- Supports CUDA for GPU acceleration
- Automatic conversion of various audio formats

## 📝 License

This project follows the license of the original [Mel-Band-Roformer-Vocal-Model](https://github.com/KimberleyJensen/Mel-Band-Roformer-Vocal-Model) repository.

## 🤝 Acknowledgments

- [KimberleyJensen](https://github.com/KimberleyJensen) for the original implementation
- [GaboxR67](https://huggingface.co/GaboxR67) for additional models

---
