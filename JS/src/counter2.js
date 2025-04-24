// je check si mon storage contient un key 'counter':   ! = NOT 
if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);


}



// la fonction:
function count() {
        // on prend le valeur stocker:
    let counter = localStorage.getItem('counter');

    counter++;
    document.querySelector('h1').innerHTML = counter;
        // on met a jout la valeur sotcker:
    localStorage.setItem('counter', counter);

    if (counter % 10 === 0) {
        alert(`Count is now ${counter}`);
    }
}

// je vais mettre un ecouteur d'evennements (listner) en place:
// on atttend l'event: toute la page est chargée .
document.addEventListener('DOMContentLoaded', function() {

    // je dois setupe le count par rapport au storage au rechargement de la page:
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');

    document.querySelector('button').onclick = count;
});



// on créé un truc qui va se lancer toute les 1000 milliseconde , et ça lancera la fonction count:
// setInterval(count, 1000);