# Webpack

Упаковщик разных файлов по веб-разработке в единый файл

## Проблема
* При подготовке кода для фронта возникает множество разрозненных файлов js, css, html, и всяких диалектов js типа typescript, jsx и т.д. (это разные над-языки, на которых проще писать фронт, но потом они так или иначе транслируются в js)
* Доставлять всё это в сыром виде в браузер клиента не всегда здорово (много лишних запросов и путаницы). 
* Хочется упаковать это всё по максимуму в единый файл, и его уже доставить в браузер.

## Что делает webpack
* Готовит единый файл из рассыпухи разных входных файлов
* По пути также умеет преобразовывать всякие над-языки в нативный js
* Делает прочие полезные вещи в этой области (<font color="red">TODO какие</font>)

## Особенности
* Выходной файл webpack-а делается больше для браузера, чем для человека - его неудобно читать и можно воспринимать как "скомпилированный код", хотя это остаётся по-прежнему текст.
* Webpack сам написан на js и работает как консольная утилита в окружении node.js

## Полезные материалы
* https://learn.javascript.ru/screencast/webpack
* https://github.com/iliakan/webpack-screencast
* https://habr.com/ru/post/309306/