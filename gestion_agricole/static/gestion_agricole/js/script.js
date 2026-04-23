// script.js
document.addEventListener('DOMContentLoaded', function() {
    console.log("Interface de la coopérative chargée !");
    
    // Exemple : Faire disparaître les messages d'alerte après 3 secondes
    setTimeout(function() {
        let alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            alert.style.display = 'none';
        });
    }, 3000);
});