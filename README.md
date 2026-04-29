# ESPHome PH Sensor Component

Внешний компонент для **ESPHome** для работы с датчиком pH через I2C (на базе библиотеки iArduino).

## Описание

Этот компонент позволяет интегрировать датчик pH в вашу систему умного дома на базе ESPHome. Поддерживает подключение по шине I2C и предоставляет измерения уровня pH с настраиваемой точностью.

## Структура проекта

```
├── components/
│   └── ph_sensor/          # Основной компонент ESPHome
│       ├── __init__.py     # Конфигурация и схема компонента
│       ├── ph_sensor.h     # Заголовочный файл C++
│       ├── ph_sensor.cpp   # Реализация компонента
│       └── *.h, *.cpp      # Библиотека iarduino_I2C_pH
├── lib/                    # Дополнительные библиотеки
│   └── iarduino_I2C_pH*    # Исходные файлы библиотеки iArduino
└── README.md               # Этот файл
```

## Требования

- **ESPHome** версии 2022.10.0 или выше
- Устройство с поддержкой **I2C** (ESP32, ESP8266 и др.)
- Датчик pH с интерфейсом I2C (совместимый с iArduino)

## Установка

### Вариант 1: Локальная установка

1. Скопируйте папку `components/ph_sensor` в корень вашего проекта ESPHome
2. Добавьте внешние компоненты в конфигурацию:

```yaml
external_components:
  - source:
      type: local
      path: components
```

### Вариант 2: Установка из Git-репозитория

```yaml
external_components:
  - source: github://username/repository@main
    components: [ph_sensor]
```

## Конфигурация

Пример полной конфигурации для `esp32`:

```yaml
esphome:
  name: ph-sensor-device
  platform: ESP32
  board: esp32dev

external_components:
  - source:
      type: local
      path: components

i2c:
  sda: GPIO21
  scl: GPIO22
  scan: true

ph_sensor:
  name: "pH Level"
  address: 0x00
  update_interval: 60s
  accuracy_decimals: 3
  icon: "mdi:ph"
  device_class: "ph"
  state_class: "measurement"
```

### Параметры конфигурации

| Параметр | Описание | По умолчанию | Обязательный |
|----------|----------|--------------|--------------|
| `name` | Название сенсора в Home Assistant | — | ✅ Да |
| `address` | I2C адрес устройства | `0x00` | ❌ Нет |
| `update_interval` | Интервал обновления данных | `60s` | ❌ Нет |
| `accuracy_decimals` | Количество знаков после запятой | `3` | ❌ Нет |
| `icon` | Иконка для Home Assistant | `mdi:ph` | ❌ Нет |
| `device_class` | Класс устройства | `ph` | ❌ Нет |
| `state_class` | Класс состояния | `measurement` | ❌ Нет |

## Подключение оборудования

Подключите датчик pH к вашей плате следующим образом:

| Плата | SDA | SCL | VCC | GND |
|-------|-----|-----|-----|-----|
| ESP32 | GPIO21 | GPIO22 | 5V/3.3V | GND |
| ESP8266 | GPIO4 (D2) | GPIO5 (D1) | 5V/3.3V | GND |

> ⚠️ **Внимание:** Убедитесь, что напряжение питания соответствует спецификации вашего датчика.

## Использование в Home Assistant

После прошивки устройства датчик автоматически появится в Home Assistant как сенсор с классом устройства `ph`. Вы можете:

- Отслеживать историю измерений
- Создавать автоматизации на основе значений pH
- Добавлять в панели мониторинга

## Лицензия

Этот проект распространяется под лицензией, совместимой с ESPHome.

## Вклад в проект

Если вы обнаружили ошибку или хотите предложить улучшения, пожалуйста, создайте Issue или Pull Request.

## Ссылки

- [Документация ESPHome](https://esphome.io/)
- [Библиотека iarduino_I2C_pH](https://www.amperka.ru/)
- [Home Assistant](https://www.home-assistant.io/)

