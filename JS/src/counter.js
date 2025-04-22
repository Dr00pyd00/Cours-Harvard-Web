// mes variables :
let counter = 0;

// la fonction:
function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;

    if (counter % 10 === 0) {
        alert(`Count is now ${counter}`);
    }
}

// je vais mettre un ecouteur d'evennements (listner) en place:
// on atttend l'event: toute la page est chargée .
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;
});