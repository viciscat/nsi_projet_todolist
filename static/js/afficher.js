// C'est quand meme pratique la documentation Bootstrap

$(document).on('show.bs.modal', '#descriptionModal', function (event) {
    const button = $(event.relatedTarget) // Button that triggered the modal
    const description = String(button.data('description')) // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this)
    modal.find('.modal-body').html(description.replaceAll("\n", '<br>'))
})

$(document).on('show.bs.modal', '#deletionModal', function (event) {
    const button = $(event.relatedTarget) // Button that triggered the modal
    const tache = button.data('id') // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this)
    modal.find('.confirm-delete').prop("href", "/supprimer/" + tache)
})

function change_filtre(element) {
    const val = element.target.getElementsByClassName('option')[0].value
    console.log(val)
    const value = parseInt(val)
    const tasks = $("#taskList")
    if (value === 0) {
        tasks.children().each(function (index, element) {
            if (element.classList.contains("taskList-label")) {return}
            element.style.display = "block";
        })
    } else {
        tasks.children().each(function (index, element) {
            console.log(element)
            if (element.classList.contains("taskList-label")) {return}
            if (element.classList.contains(val)) {
                element.style.display = "block"
            } else {
                element.style.display = "none"
            }
        })
    }
    element.preventDefault()
}