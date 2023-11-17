# Documentación de la API

## Rutas

### `/ping`

- Método: `GET`
- Descripción: Esta ruta se utiliza para verificar que el servidor está funcionando correctamente.
- Respuesta: Una cadena de texto 'pong'.

Ejemplo de uso:

#### bash
curl -X GET http://localhost:5000/ping

### `/EmotionClassifer`

-GitHub Copilot: Claro, aquí tienes un ejemplo de cómo podrías documentar el uso de tu API en formato Markdown:

```markdown
# Documentación de la API

## Rutas

### `/ping`

- Método: `GET`
- Descripción: Esta ruta se utiliza para verificar que el servidor está funcionando correctamente.
- Respuesta: Una cadena de texto 'pong'.

Ejemplo de uso:

```bash
curl -X GET http://localhost:5000/ping
```

### `/EmotionClassifer`

- Método: `POST`
- Descripción: Esta ruta se utiliza para clasificar las emociones en un texto dado.
- Cuerpo de la solicitud: Un objeto JSON con una clave 'text' que contiene el texto a analizar.
- Respuesta: Un objeto JSON con la clasificación de las emociones.

Ejemplo de uso:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text":"Estoy muy feliz"}' http://localhost:5000/EmotionClassifer
```

### `/Summary`

- Método: `POST`
- Descripción: Esta ruta se utiliza para obtener un resumen de una pregunta dada.
- Cuerpo de la solicitud: Un objeto JSON con una clave 'question' que contiene la pregunta a resumir y una clave 'context' para tener el contexto del texto y poder responder.
- Respuesta: Un objeto JSON con el resumen de la pregunta.

Ejemplo de uso:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"question":"¿Qué es la inteligencia artificial?"}' http://localhost:5000/Summary
```
```
