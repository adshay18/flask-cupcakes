$('.delete-cupcake').click(deleteCupcake);

async function deleteCupcake() {
	const id = $(this).data('id');
	await axios.delete(`/api/cupcakes/${id}`);
	$(this).parent().remove();
}

$('.add-cupcake').click(addCupcake);

async function addCupcake() {
	let flavor = $('#flavor').val();
	let rating = $('#rating').val();
	let size = $('#size').val();
	let image = $('#image').val();

	const cupcakeResponse = await axios.post(
		'/api/cupcakes',
		(params = { flavor: flavor, rating: rating, size: size, image: image })
	);
	let cupcake = $(generateMarkup(cupcakeResponse.data.cupcake));
	$('#cupcakes-list').append(cupcake);
}

function generateMarkup(cupcake) {
	return `<li class="list-group-item d-flex justify-content-between align-items-center">
    <img class="w-50" src="${cupcake.image}" alt="${cupcake.flavor} cupcake">${cupcake.flavor} cupcake <button
    class="delete-cupcake btn-sm btn-danger"
    data-id="${cupcake.id}">X</button>
  </li>`;
}
