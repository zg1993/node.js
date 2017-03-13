"use strict"

const Koa = require('koa')
const router = require('koa-router')()
const bodyParser = require('koa-bodyparser')
const controller = require('./controllers')

const app = new Koa()

app.use(async (ctx, next) => {
    console.log(`Process ${ctx.request.method} ${ctx.request.url}`);
    await next();
});

app.use(bodyParser());

app.use(controller())

app.listen(8000)
console.log('app start at port 8000')






