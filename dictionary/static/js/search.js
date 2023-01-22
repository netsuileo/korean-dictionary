const debounce = (callback, wait) => {
    let timeoutId = null;
    return (...args) => {
        window.clearTimeout(timeoutId);
        timeoutId = window.setTimeout(() => {
            callback.apply(null, args);
        }, wait);
    };
}

function initializeSearch() {
    const searchInput = document.getElementById("search-input");
    searchInput.addEventListener('input', debounce((event) => {
        const value = event.target.value;
        if (!value) {
            fetchTable('/api/random');
        } else {
            fetchTable(`/api/search/${value}`);
        }
    }, 250));
}

function fetchTable(url) {
    return fetch(url).then(
        (response) => {
            return response.text()
        }).then(html => {
        const resultsTable = document.getElementById("results-table");
        resultsTable.outerHTML = html;
    });
}

document.addEventListener("DOMContentLoaded", function() {
    initializeSearch();
  });