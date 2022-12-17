function create_charts(rep) {
    const ctx_categorie = document.getElementById('categorieChart');
    const ctx_etat = document.getElementById('finiChart');

    new Chart(ctx_categorie, {
        type: 'doughnut',
        data: {
            labels: rep.categories,
            datasets: [{
                label: 'Utilisation',
                data: rep.nbCategorie,
                borderWidth: 1
            }]
        }

    });

    new Chart(ctx_etat, {
        type: 'doughnut',
        data: {
            labels: rep.etats,
            datasets: [{
                label: 'Utilisation',
                data: rep.nbEtat,
                borderWidth: 1
            }]
        }

    });
}

fetch("/get-stats").then(function (response) {
    response.json().then(function (text) {
        create_charts(text)
    })
})