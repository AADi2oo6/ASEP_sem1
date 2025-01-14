
// Sample data for suggestions
const suggestionsData = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Phoenix",
    "Philadelphia",
    "San Antonio",
    "San Diego",
    "Dallas",
    "San Jose"
];

let selectedIndex = -1; // Track the selected suggestion index

function showSuggestions(value) {
    const suggestionsBox = document.getElementById('suggestions');
    suggestionsBox.innerHTML = ''; // Clear previous suggestions
    selectedIndex = -1; // Reset selected index

    if (value.length === 0) {
        suggestionsBox.style.display = 'none'; // Hide if no input
        return;
    }

    const filteredSuggestions = suggestionsData.filter(item =>
        item.toLowerCase().includes(value.toLowerCase())
    );

    if (filteredSuggestions.length > 0) {
        suggestionsBox.style.display = 'block'; // Show suggestions
        filteredSuggestions.forEach((suggestion, index) => {
            const suggestionItem = document.createElement('div');
            suggestionItem.classList.add('suggestion-item');
            suggestionItem.textContent = suggestion;
            suggestionItem.onclick = () => selectSuggestion(suggestion);
            suggestionItem.onmouseover = () => highlightSuggestion(index);
            suggestionsBox.appendChild(suggestionItem);
        });
    } else {
        suggestionsBox.style.display = 'none'; // Hide if no matches
    }
}

function selectSuggestion(suggestion) {
    document.getElementById('search-bar').value = suggestion; // Set input value
    hideSuggestions(); // Hide suggestions
}

function hideSuggestions() {
    document.getElementById('suggestions').style.display = 'none'; // Hide suggestions
}

function highlightSuggestion(index) {
    const items = document.querySelectorAll('.suggestion-item');
    items.forEach((item, i) => {
        item.classList.remove('selected'); // Remove highlight from all
        if (i === index) {
            item.classList.add('selected'); // Highlight the current item
        }
    });
    selectedIndex = index; // Update selected index
}

document.getElementById('search-bar').addEventListener('input', function (event) {
    showSuggestions(event.target.value);
});

document.getElementById('search-bar').addEventListener('keydown', function (event) {
    const items = document.querySelectorAll('.suggestion-item');
    if (event.key === 'ArrowDown') {
        selectedIndex = (selectedIndex + 1) % items.length; // Move down
        highlightSuggestion(selectedIndex);
    } else if (event.key === 'ArrowUp') {
        selectedIndex = (selectedIndex - 1 + items.length) % items.length; // Move up
        highlightSuggestion(selectedIndex);
    } else if (event.key === 'Enter') {
        if (selectedIndex > -1) {
            selectSuggestion(items[selectedIndex].textContent); // Select highlighted suggestion
        }
    }
});

//        function performSearch() {
//            const searchValue = document.getElementById('search-bar').value;
//            if (searchValue) {
//                const url = `https://example.com/search/${encodeURIComponent(searchValue)}`;
//                window.location.href = url;
//            }
//        }
