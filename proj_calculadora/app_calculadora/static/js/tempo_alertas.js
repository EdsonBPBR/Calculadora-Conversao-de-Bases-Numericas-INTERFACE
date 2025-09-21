document.addEventListener("DOMContentLoaded", () => {
    const alerts = document.querySelectorAll("#alertas .alert");

    alerts.forEach(alert => {
        // Aplica animação de entrada (fade-in)
        alert.classList.add("fade-in");

        // Depois de 3 segundos, inicia o fade-out
        setTimeout(() => {
            alert.classList.remove("fade-in");
            alert.classList.add("fade-out");

            // Remove do DOM após a animação de saída
            alert.addEventListener("animationend", () => {
                alert.remove();
            });
        }, 3000);
    });
});
