let currentPage = 1;
const itemsPerPage = 2;

// Seletores do DOM
const digimonContainer = document.getElementById("digimonContainer");
const searchInput = document.getElementById("searchInput");
const prevPageBtn = document.getElementById("prevPage");
const nextPageBtn = document.getElementById("nextPage");
const pageNumberSpan = document.getElementById("pageNumber");

// Obter todos os Digimons diretamente do HTML
const digimonElements = Array.from(digimonContainer.children);

// Renderizar Digimons
function renderDigimons(filteredList = digimonElements) {
    digimonContainer.innerHTML = "";

    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    const paginatedList = filteredList.slice(startIndex, endIndex);

    if (paginatedList.length === 0) {
        digimonContainer.innerHTML = "<p>Nenhum Digimon encontrado.</p>";
        return;
    }

    paginatedList.forEach(digimon => digimonContainer.appendChild(digimon));
}

// Atualizar paginação
function updatePagination(filteredList = digimonElements) {
    const totalPages = Math.ceil(filteredList.length / itemsPerPage);

    prevPageBtn.disabled = currentPage === 1;
    nextPageBtn.disabled = currentPage === totalPages;

    pageNumberSpan.textContent = `Página ${currentPage}`;
}

// Mudar página
function handlePageChange(increment, filteredList = digimonElements) {
    currentPage += increment;
    renderDigimons(filteredList);
    updatePagination(filteredList);
}

// Busca
function handleSearch() {
    const searchValue = searchInput.value.toLowerCase();
    const filteredDigimons = digimonElements.filter(digimon => {
        const name = digimon.dataset.name.toLowerCase();
        const level = digimon.dataset.level.toLowerCase();
        return name.includes(searchValue) || level.includes(searchValue);
    });

    currentPage = 1; // Reiniciar para a primeira página ao buscar
    renderDigimons(filteredDigimons);
    updatePagination(filteredDigimons);
}

// Eventos
searchInput.addEventListener("input", handleSearch);
prevPageBtn.addEventListener("click", () => handlePageChange(-1));
nextPageBtn.addEventListener("click", () => handlePageChange(1));

// Inicializar
renderDigimons();
updatePagination();
