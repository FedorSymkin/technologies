# reactjs hello world
Простейший компонент react, который выводит hello world в браузер
Пример сделан на основе https://github.com/learncodeacademy/react-js-tutorials/tree/master/1-basic-react

## Как запускать
* `cd .../reactjs/hello_world`
* `npm install` - устанавливаем (локально) модули ноды, прописанные в package.json <details><summary>Важный комментарий по безопасности</summary>npm - умная штука, при установке модулей, она проверяет, есть ли известные уязвимости в этих модулях. Когда я ставил модули, она мне написала `found 4 vulnerabilities`  и предложила сделать `npm audit`, в котором написала об этих уязвимостях и даже приложила ссылку на их описание у себя на сайте. Там же она предложила пофиксить - установить более свежие версии. В общем, респект. </details>
* `npm run dev` - запускаем отладочный web-server <details><summary>Немного подробностей</summary>Это алиас на скирпт прописанный в package.json. Фактически там выполняется `webpack-dev-server --content-base src --inline --hot`. Запускается простой http-server отдающий директорию src, и webpack в режиме watch. Флаги --inline --hot делают так, что на странице в браузере появляется вебсокет, который слушает сервер и перезагружает страницу в случае изменений исходных файлов. Удобно, чтобы каждый раз не тыкать F5 в браузере. На диске не будет собранного build.js - он в памяти сервера.</details> 
* `http://127.0.0.1:8080`
* Если всё работает увидим hello world

## Что используется
* reactjs
* webpack
* webpack-dev-server
* babel
* sublime text 3 с плагином babel

## Как работает
* В исходном html есть только общий div container где рендерится приложение react
* Точка входа в js - это получить container средствами обычного js и отдать его в root-вую функцию реакта ReactDOM.render
```js
import React from "react";
import ReactDOM from "react-dom";

import Root from "./components";

const container = document.getElementById('container');
ReactDOM.render(<Root/>, container);
```
* Чтобы сделать компонент реакта надо унаследоваться от React.Component и определить функцию render
```js
import React from "react";

export default class Root extends React.Component {
  render() {
    return (
      <div>
      	Hello world from react!
      </div>
    );
  }
}
```
Возврат псевдо-html из render - это расширенный синтаксис javascript-а - jsx (его потом babel переводит в обычный js).  В этом псевдо-html-е можно делать всякую магию - пробрасывать туда параметры, придумывать свои теги (на основе других компонентов реакта) и проч., подробнее в других разделах.

* Важно - вернуть можно только один элемент html. Если надо больше - оборачивать в div

## А также
* Есть расширение для браузеров, позволяющее смотреть и отлаживать внутренние структуры react: https://fb.me/react-devtools
