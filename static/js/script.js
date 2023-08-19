document.getElementById('englishBtn').addEventListener('click', function () {
    openNewTab('English');
});

document.getElementById('frenchBtn').addEventListener('click', function () {
    openNewTab('French');
});

document.getElementById('hindiBtn').addEventListener('click', function () {
    openNewTab('Hindi');
});

function openNewTab(language) {
    let endpoint = `http://localhost:5000/hello?language=${language}`;
    window.open(endpoint, '_blank');
}