// C'est quand meme pratique la docu Bootstrap

$(document).on('show.bs.modal','#editCategorieModal', function (event) {
  const button = $(event.relatedTarget) // Button that triggered the modal
  const description = String(button.data('description')) // Extract info from data-* attributes
  console.log(typeof description)
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('.modal-body').html(description.replaceAll("\\r\\n", '<br />'))
})

$(document).on('show.bs.modal','#deletionModal', function (event) {
  const button = $(event.relatedTarget) // Button that triggered the modal
  const tache = button.data('id') // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  console.log("hellloooo", tache)
  var modal = $(this)
  modal.find('.confirm-delete').prop("href", "/supprimer/" + tache)
})

console.log("idajaijadzjiadzij")