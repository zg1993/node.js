var fn_hello = async(ctx, next) => {
	var name = ctx.params.name
	console.log(name);
	ctx.response.body = `<h1>Helo, ${name}!</h1>`
}


module.exports = {
	'GET /hello/:name': fn_hello
}


