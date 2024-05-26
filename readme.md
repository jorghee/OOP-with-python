# <samp>Agenda telefónica :green_book:</samp>
## Directrices  generales
1. El programa necesita guardar los datos que el usuario dispone, estos datos deben ser almacenados en algún tipo de archivos. Debido a que se necesitan guardar listas de objetos, se ha decidido hacer uso de archivos JSON, un formato ligero de intercambio de datos, fácil de leer y escribir con la biblioteca json de Python, adecuado para datos estructurado.

2. Leer y escribir en archivos con Python viene de forma nativa y se utiliza a través de las funciones integradas `open`, `read`, `write` entre otras. Sin embargo para manejar ciertos formatos especificos como JSON, Python ofrece el modulo estándar `json`.

## <samp>La clase Contact :hammer:</samp>
Debe contener 4 campos: `name`, `number`, `address` y `relation`. Como métodos debe tener su respectivo constructor y 2  métodos especiales:

- Un método que nos permita parsear el objeto actual como un diccionario. Por ejemplo, que el identificador de referencia al campo `name` sea como clave y su valor sea el correspondiente valor del campo.

- Un método que reciba como argumento un objeto json que se parsea a un diccionario en Python. Este diccionario contiene los campos de una instancia de la clase Contact, por lo tanto con estos datos se debe crear el nuevo objeto. Si analizamos, este método será parte de cargar los datos guardados en un archivo JSON.

- El método `toString()` de java pero que sea análogo en Python, que realice la misma funcionalidad.

## <samp>La clase Agenda :skull:</samp>

## <samp>La clase Main :eyes:</samp>
