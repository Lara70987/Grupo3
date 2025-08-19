document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");

    form.addEventListener("submit", (e) => {
        const titulo = document.querySelector("#titulo").value.trim();
        const detalhes = document.querySelector("#detalhes").value.trim();

        if (!titulo || !detalhes) {
            e.preventDefault();
            alert("Preencha título e detalhes antes de salvar 💜");
        }
    });
});
