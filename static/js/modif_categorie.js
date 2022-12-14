$(document).on('show.bs.modal', '#editCategorieModal', function (event) {
    const button = $(event.relatedTarget) // Button that triggered the modal
    const mode = String(button.data('mode'))
    const modal = $(this);
    if (mode === "edit") {
        const idCategorie = String(button.data('id-categorie')) // Extract info from data-* attributes
        const categorie = String(button.data('categorie')) // Extract info from data-* attributes
        console.log(typeof idCategorie)
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.

        modal.find('#change-categorie-form').prop("action", "/modifier-categorie/" + idCategorie)
        modal.find("#categorie-name").prop("value", categorie)
    } else if (mode === "new") {
        modal.find("#change-categorie-form").prop("action", "/nouvelle-categorie")
    }
})

$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})