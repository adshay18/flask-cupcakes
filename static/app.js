$('.delete-cupcake').click(deleteCupcake);

async function deleteTodo() {
	const id = $(this).data('id');
	await axios.delete(`/api/cupcake/${id}`);
	$(this).parent().remove();
}
