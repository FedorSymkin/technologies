# Webpack, подробности

Webpack умеет очень много всего.

## Немного из того, что он умеет

* Понятие source-map: 
    * Допустим в браузер приезжает монолитный собранный файл build.js
    * Но иногда для отладки хочется в дев-панели браузера видеть отдельные js-файлы из которых он был собран, например чтобы ставить там точки останова. 
    * Браузеры умеют загружать и читать особые файлы .map, в которых указано из каких исходников и как был собран этот build.js
    * Для того, чтобы сказать браузеру загружать .map, ему нужно в js указать особый комментарий вида `//# sourceMappingURL=... `
    * Имея этот .map браузер сможет в дев-панели вывести исходные js файлы как будто они загружены отдельно, хотя физически файл build.js остаётся один
    * Так вот webpack умеет генерить эти .map файлы, причём разными способами, подробнее см. в доках

* Можно сборку своего js файла настроить так, чтобы из него могли импортировать сторонние скрипты снаружи сборки webpack.

* В сборку js, которая поедет на браузер клиента, можно прокинуть переменную среды, указанную при сборке. Это используется например, чтобы разделить development и production сборку
        
* Понятие loader-ов: к каждому исходному файлу в сборке можно применить некоторое преобразование, например перевести какой-то диалект js (коих много) в "обычный" js, который понимают все браузеры. Одним из таких преобразователей является babel - превращение js новых стандартов в js старых стандартов, решая таким образом проблему совместимости с браузерами.

* Сжатие сборки - превращение готового файла в js-однострочник, с устранением всяких недостижимых веток кода и проч.

* Можно писать и подключать плагины

* Умеет брать на вход также CSS и другие статические ресурсы

* watch-режим - webpack умеет работать как демон, который следит за изменениями файлов и сам пересобирает сборку

## Что следует помнить

* <font color=red>Важная штука</font>: при сборке переменные могут переименовываться (в целях сокращения размера текста, чтобы меньше гонять по сети)
* <font color=red>TODO добавить сюда ещё всякие warning-и</font>



## Чуть более сложный пример конфига
[webpack.config.js](webpack.config.js)

## P.S.
Это далеко не всё.

* В итоге webpack это что-то вроде cmake для фронта
* Любые хотелки, связанные с упаковкой/подготовкой/преобразованием исходных файлов для фронта (js, css, html, etc...) стоит гуглить на предмет есть ли они в webpack.
* Если нет  - можно написать свой плагин