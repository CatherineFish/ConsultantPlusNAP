# Задание НАП

Консольное приложение, ищущее в текстовом файле пару заданных слов на определённом расстоянии друг от друга.


## Оглавление
1. [Описание элементов приложения и тестирования](#introduction)
2. [Сборка](#paragraph1)
3. [Тестирование](#paragraph2)
	1. [Описание тестов](#subparagraph21)
	2. [Запуск тестов](#subparagraph22)
	3. [Примечание к тестам](#subparagraph23)

## Описание элементов приложения и тестирования <a name="introduction"></a>

В репозитории содержатся следующие файлы:

* main.cpp - основной файл запуска приложения;
* myLibrary.h - библиотека собственных функций;
* myLibrary.cpp - реализация собственных функци;
* Makefile;
* features/findPair.feature - описание сценариев;
* features/steps/findPair.py - обработчики сценариев;
* features/materials - папка с текстовыми документами для тестирования.

## Сборка <a name="paragraph1"></a>

Чтобы собрать приложение: 
```
make
```

Образуются файлы:

* count_pairs.exe - приложение;
* main.o;
* myLibrary.o.

Чтобы очистить папку:
```
make clean
```

## Тестирование <a name="paragraph2"></a>

Реализована возможность запуска тестов на «человеческом языке» с использованием фреймворка Behave

### Описание тестов <a name="subparagraph21"></a>

Тесты представляют собой основные логические развилки в работе приложения и имеют:

* Scenario: - краткое описание тестируемой развилки работы приложения;
* Given - исходное состояние приложения и используемых данных;
* When - непосрественное описание способа запуска приложения;
* Then - получаемый результат.

Реализованы тесты:

* Выдающие ошибку:
	* несуществующий файл во входных параметрах;
	* недостаточно входных параметров;
	* слишком много входных параметров;
	* документ с неправильной кодировкой (ошибка конвертирования произойдёт).
* Отрабатывающие корректно:
	* поиск пары слов на малом расстоянии, пары находятся;
	* поиск пары слов на малом расстоянии, пары не находятся;
	* поиск пары слов на среднем расстоянии, пары находятся;
	* поиск пары слов на среднем расстоянии, пары не находятся;
	* поиск пары слов на большом расстоянии, пары находятся;
	* поиск пары слов на большом расстоянии, пары не находятся;

### Запуск тестов <a name="subparagraph22"></a>

Чтобы запустить тесты, соберите приложение и запустите работу Behave:

```
make
behave
```

### Примечание к тестам <a name="subparagraph23"></a>

В формулировке задания мне остался не до конца ясным один момент - нужно ли считать только ближайшие пары или вообще все. Поясню на примере: пусть заданное расстояние 5, а в тексте содержится фраза:

> firstKeyWord word firstKeyWord secondKeyWord Word secondKeyWord  

Пар тут, конечно, две. Но алгоритм при такой задаче будет весьма сложным, так как нужно хранить информацию о наличии первых ключевых слов ранее на заданном состоянии при обработке каждого слова в документе. В моём приложении реализован вариант, когда ответ на данном примере - 1, считается только внутренняя пара.
