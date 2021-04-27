function validarTextoEntrada(input, patron) {
    var texto = input.value

    var letras = texto.split("")

    for (var x in letras) {
        var letra = letras[x]

        if (!(new RegExp(patron, "i")).test(letra)) {
            letras[x] = ""
        }
    }

    input.value = letras.join("")
}


// Solo Letras Asuntos
var asunto = document.getElementById("asunto")
asunto.addEventListener("input", function (event) {
    validarTextoEntrada(this, "[a-z ]")
})

// Solo Letras Nombre y Apellido

var nombre = document.getElementById("nombre")
nombre.addEventListener("input", function (event) {
    validarTextoEntrada(this, "[a-z ]")
})


// Solo numeros
var telefono = document.getElementById("telefono")
telefono.addEventListener("input", function (event) {
    validarTextoEntrada(this, "[0-9]")
})