// alert("Hola mundo")

var nombre = "Aldayr Rdz"
var altura= 190

var conta = nombre + " " + altura
// document.write(nombre)
// document.write(altura)
var datos = document.getElementById("datos")
datos.innerHTML = `
        <h1>Hola soy la caja de datos</h1>
        <h1>Hola mi nombre es: ${nombre}</h1>
        <h3>Mido ${altura} cm</h3>
`

if(altura>=190){
    datos.innerHTML += '<h1>Eres una persona alta</h1>'
}else{
    datos.innerHTML += '<h1>Eres una persona bajita</h1>'
}