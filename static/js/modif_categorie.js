$(document).on('show.bs.modal','#descriptionModal', function (event) {
  const button = $(event.relatedTarget) // Button that triggered the modal
  const idCategorie = String(button.data('id-categorie')) // Extract info from data-* attributes
  console.log(typeof idCategorie)
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('#change-categorie-form').prop("action", "/modifier-categorie/" + idCategorie)
})