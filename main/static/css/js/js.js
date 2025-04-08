const searchInput = document.getElementById('mapSearch');
const searchResults = document.getElementById('searchResults');

searchInput.addEventListener('input', async function () {
    const searchTerm = this.value.trim();
    searchResults.innerHTML = '';

    if (!searchTerm) {
        searchResults.style.display = 'none';
        return;
    }

    const response = await fetch(`/search_maps/?q=${encodeURIComponent(searchTerm)}`);
    const data = await response.json();

    const results = data.results;

    if (results.length > 0) {
        results.forEach(map => {
            const item = document.createElement('div');
            item.className = 'search-result-item';
            item.textContent = map.name;
            item.addEventListener('click', () => {
                window.location.href = map.url;
            });
            searchResults.appendChild(item);
        });
    } else {
        const noResults = document.createElement('div');
        noResults.className = 'no-results';
        noResults.textContent = 'Ничего не найдено';
        searchResults.appendChild(noResults);
    }

    searchResults.style.display = 'block';
});
