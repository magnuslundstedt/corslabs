var domain = "http://{{restDomain}}.corslabs.com/echo{{suffix}}"

console.log('Sending POST request to ' + domain);
$.post(domain, JSON.stringify({request: 'post', foo: 'bar', bar: 'foo'}), function(data) {
	console.info('POST Success: ', data);
}, 'json').fail( function(xhr, textStatus, errorThrown) {
	console.error('POST Error, info:', xhr, textStatus, errorThrown)
});

console.log('Sending GET request to ' + domain);
$.get(domain, {request: 'get', foo: 'bar', bar: 'foo'}, function(data) {
	console.info('GET Success: ', data);
}, 'json').fail( function(xhr, textStatus, errorThrown) {
	console.error('GET Error, info:', xhr, textStatus, errorThrown)
});

console.info('Done! If no errors are shown, this test worked fine!');
