let lista = document.getElementsByClassName('tags');
for (let i = 0; i < lista.length; i++)
	{
		alert(lista[i].id + typeof(lista[i]));
		lista[i].onclick = ativa(self);
	}
let dash = document.getElementById('dash');
let insert = document.getElementById('ins');
let ofs = document.getElementById('ofs');
let logout = document.getElementById('logout');

/*
dash.onclick = function() {
	dash.className += ' active';
	if (insert.className.indexOf('active') != -1) {
		insert.className = insert.className.substring(0, insert.className.indexOf('active'))
	}
}
*/
/*
insert.onclick = function() {insert.className += ' active'}
ofs.onclick = function() {ofs.className += ' active'}
logout.onclick = function() {logout.className += ' active'}
*/
/*
dash.onclick = ativa()
insert.onclick = ativa()
ofs.onclick = ativa(self, lista)
logout.onclick = ativa(self, lista)
*/
function ativa(obj)
{
	for (let i = 0; i <= lista.length; i++)
	{
		if (lista[i].id == obj)
		{
			if (obj.className.indexOf('active') == -1)
			{
				obj.className = obj.className += ' active';
			}
		}
		else
		{
			lista[i].className = lista[i].className.substring(0, lista[i].className.indexOf('active'));
		}
	}
}