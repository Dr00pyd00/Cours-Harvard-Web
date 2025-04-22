# JAVASCRIPT

## Chopper des elements:

```javascript
// choper UN element: 
document.querySelector('h1')

// choper DES elements:
document.querySelectorAll('button')

```

## Attendre que la page charge:

```javascript 
        document.addEventListener('DOMContentLoaded',
            function() {

                  // ici on mets les autres fonctions a faire.
                }
        );

```

## Chercher des data dans les balises par exemple:

```javascript 
  <script>
	// ici on attend bien que la page charge:
        document.addEventListener('DOMContentLoaded' , function()  {   // la on lance une 1er fonction
            

	// Pour chaque 'button' sur la page , on lance une fonction (pour chaque iteration une fonction) :
            document.querySelectorAll('button').forEach(function(button) {
                button.onclick = function() {  // fonction SI y'a un click sur le bouton
                    document.querySelector('#hello').style.color = button.dataset.color    // dataset.color lié a data-color
                }
            })

        }
    );
    </script>

</head>
<body>
    <h1 id="hello">Hello!</h1>
    <button data-color="red">Red</button>
    <button data-color="blue">blue</button>
    <button data-color="green">Green</button>


```
Bien noté que 'data' est un objet qu'on personnalise :
- data-truc dans une balise html 
- dataset.truc


