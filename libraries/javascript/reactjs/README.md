# reactjs

Библиотека на стороне клиента для разработки сложных пользовательских интерфейсов.

## Когда стоит использовать
* Когда нужен полноценный интерфейс с блекджеком и контролами, т.е. нечто большее чем просто пара страничек, связанных ссылками
* Когда фронт на jquery становится мешаниной из вложенных функций, кусков html, callback-ов в callback-ах и т.д.
* Когда фронт на jquery тормозит

## Основные принципы:
* Большинство элементов DOM приезжают не в html, а генерируются средствами javascript внутри react
* Изоляция от реального DOM - в случае изменений, принцип не "найти элемент в DOM и поменять", как в jquery, а все изменения идут в объектах react-a, а дальше react уже сам подумает как отрендерить в DOM
* У React внутри есть свой виртуальный DOM, в котором отслеживаются изменения, и только реально изменившиеся элементы рендерятся в настоящий DOM. Это делает react на порядок быстрее чем jquery, так как основное время занимает не интерпретатор javascript, а изменение DOM.
* Все разделено на компоненты - небольшие смысловые куски страницы
* Каждому компоненту соответствует класс js, у которого явно прописано, как он будет рендериться в DOM (здесь имеется ввиду виртуальный DOM)
* Компоненты могут иерархически вкладываться друг в друга
* TODO написать про события, параметры и роутинг

## Полезные материалы
* https://www.youtube.com/watch?v=MhkGQAoc7bc&list=PLoYCgNOIyGABj2GQSlDRjgvXtqfDxKm5b
* https://github.com/learncodeacademy/react-js-tutorials/blob/master/1-basic-react
