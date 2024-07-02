# Esquema de Base de Datos

![Esquema de Base de Datos](file:///mnt/data/image.png)

# Esquema de Base de Datos

```mermaid
erDiagram
    Artista {
        INT ID_Artista PK "Identificador único del artista"
        NVARCHAR(25) nombre NN "Nombre del artista"
        NVARCHAR(25) apellido NN "Apellido del artista"
        NVARCHAR(25) seudonimo NN "Seudónimo del artista"
        NVARCHAR(25) genero NN "Género musical del artista"
    }
    
    Asiento {
        INT ID_Asiento PK "Identificador único del asiento"
        NVARCHAR(10) localizacion NN "Localización del asiento"
        NVARCHAR(10) bloque NN "Bloque del asiento"
        TINYINT fila NN "Fila del asiento"
        TINYINT numero NN "Número del asiento"
        DECIMAL(10,2) costo NN "Costo del asiento"
    }

    Lugar {
        INT ID_Lugar PK "Identificador único del lugar"
        NVARCHAR(25) nombre NN "Nombre del lugar"
        TINYINT capacidad NN "Capacidad del lugar"
        NVARCHAR(25) direccion NN "Dirección del lugar"
    }

    Evento {
        INT ID_Evento PK "Identificador único del evento"
        INT ID_Lugar NN FK "Identificador del lugar donde se realiza"
        NVARCHAR(25) nombreGira NN "Nombre de la gira del evento"
        DATE fechaEvento NN "Fecha del evento"
        TIMESTAMP horaInicio NN "Hora de inicio del evento"
        TIMESTAMP horaFin NN "Hora de fin del evento"
    }

    ArtistaXEvento {
        INT ID_Artista NN FK PK "Identificador del artista"
        INT ID_Evento NN FK PK "Identificador del evento"
    }

    AsientoXEvento {
        INT ID_Asiento NN FK PK "Identificador del asiento"
        INT ID_Evento NN FK PK "Identificador del evento"
    }

    Ticket {
        INT ID_Ticket PK "Identificador único del ticket"
        INT ID_Evento NN FK "Identificador del evento"
        NVARCHAR(25) codigoTicket NN "Código del ticket"
    }

    Compra {
        INT ID_Compra PK "Identificador único de la compra"
        INT ID_Usuario NN FK "Identificador del usuario que realiza la compra"
        INT ID_Ticket NN FK "Identificador del ticket comprado"
        INT ID_MetodoPago NN FK "Identificador del método de pago utilizado"
        NUMERIC(3,1) iva NN "IVA aplicado a la compra"
        NVARCHAR(25) codigoCompra NN "Código de la compra"
        DATE fechaCompra NN "Fecha de la compra"
    }

    Usuario {
        INT ID_Usuario PK "Identificador único del usuario"
        NVARCHAR(25) nombre NN "Nombre del usuario"
        NVARCHAR(25) apellido NN "Apellido del usuario"
        NVARCHAR(25) email NN UNIQUE "Correo electrónico del usuario"
        VARCHAR(10) telefono UNIQUE "Teléfono del usuario"
        VARCHAR(10) cedula UNIQUE "Cédula del usuario"
        DATE fechaNac NN "Fecha de nacimiento del usuario"
    }

    MetodoPago {
        INT ID_MetodoPago PK "Identificador único del método de pago"
        NVARCHAR(25) metodo NN "Método de pago (e.g., tarjeta de crédito, PayPal)"
    }

    Artista ||--o{ ArtistaXEvento : "asiste a"
    Evento ||--o{ ArtistaXEvento : "tiene"
    Evento ||--|{ AsientoXEvento : "contiene"
    Asiento ||--o{ AsientoXEvento : "asigna"
    Lugar ||--o{ Evento : "se lleva a cabo en"
    Evento ||--o{ Ticket : "emite"
    Ticket ||--o{ Compra : "se incluye en"
    Usuario ||--o{ Compra : "realiza"
    MetodoPago ||--o{ Compra : "usa"


## Descripción de Tablas y Campos

### Artista
| Campo         | Tipo                | Descripción                                  |
|---------------|---------------------|----------------------------------------------|
| ID_Artista    | INT, Identity, PK   | Identificador único del artista.             |
| nombre        | NVARCHAR(25), NN    | Nombre del artista.                          |
| apellido      | NVARCHAR(25), NN    | Apellido del artista.                        |
| seudonimo     | NVARCHAR(25), NN    | Seudónimo del artista.                       |
| genero        | NVARCHAR(25), NN    | Género musical del artista.                  |

### Asiento
| Campo         | Tipo                | Descripción                                  |
|---------------|---------------------|----------------------------------------------|
| ID_Asiento    | INT, Identity, PK   | Identificador único del asiento.             |
| localizacion  | NVARCHAR(10), NN    | Localización del asiento.                    |
| bloque        | NVARCHAR(10), NN    | Bloque del asiento.                          |
| fila          | TINYINT, NN         | Fila del asiento.                            |
| numero        | TINYINT, NN         | Número del asiento.                          |
| costo         | DECIMAL(10,2), NN   | Costo del asiento.                           |

### Lugar
| Campo         | Tipo                | Descripción                                  |
|---------------|---------------------|----------------------------------------------|
| ID_Lugar      | INT, Identity, PK   | Identificador único del lugar.               |
| nombre        | NVARCHAR(25), NN    | Nombre del lugar.                            |
| capacidad     | TINYINT, NN         | Capacidad del lugar.                         |
| direccion     | NVARCHAR(25), NN    | Dirección del lugar.                         |

### Evento
| Campo         | Tipo                | Descripción                                  |
|---------------|---------------------|----------------------------------------------|
| ID_Evento     | INT, Identity, PK   | Identificador único del evento.              |
| ID_Lugar      | INT, NN, FK         | Identificador del lugar donde se realiza.    |
| nombreGira    | NVARCHAR(25), NN    | Nombre de la gira del evento.                |
| fechaEvento   | DATE, NN            | Fecha del evento.                            |
| horaInicio    | TIMESTAMP, NN       | Hora de inicio del evento.                   |
| horaFin       | TIMESTAMP, NN       | Hora de fin del evento.                      |

### ArtistaXEvento
| Campo         | Tipo                | Descripción                                  |
|---------------|---------------------|----------------------------------------------|
| ID_Artista    | INT, NN, FK, PK     | Identificador del artista.                   |
| ID_Evento     | INT, NN, FK, PK     | Identificador del evento.                    |

### AsientoXEvento
| Campo         | Tipo                | Descripción                                  |
|---------------|---------------------|----------------------------------------------|
| ID_Asiento    | INT, NN, FK, PK     | Identificador del asiento.                   |
| ID_Evento     | INT, NN, FK, PK     | Identificador del evento.                    |

### Ticket
| Campo         | Tipo                | Descripción                                  |
|---------------|---------------------|----------------------------------------------|
| ID_Ticket     | INT, Identity, PK   | Identificador único del ticket.              |
| ID_Evento     | INT, NN, FK         | Identificador del evento.                    |
| codigoTicket  | NVARCHAR(25), NN    | Código del ticket.                           |

### Compra
| Campo         | Tipo                | Descripción                                  |
|---------------|---------------------|----------------------------------------------|
| ID_Compra     | INT, Identity, PK   | Identificador único de la compra.            |
| ID_Usuario    | INT, NN, FK         | Identificador del usuario que realiza la compra. |
| ID_Ticket     | INT, NN, FK         | Identificador del ticket comprado.           |
| ID_MetodoPago | INT, Identity, FK   | Identificador del método de pago utilizado.  |
| iva           | NUMERIC(3,1), NN    | IVA aplicado a la compra.                    |
| codigoCompra  | NVARCHAR(25), NN    | Código de la compra.                         |
| fechaCompra   | DATE, NN            | Fecha de la compra.                          |

### Usuario
| Campo         | Tipo                | Descripción                                  |
|---------------|---------------------|----------------------------------------------|
| ID_Usuario    | INT, Identity, PK   | Identificador único del usuario.             |
| nombre        | NVARCHAR(25), NN    | Nombre del usuario.                          |
| apellido      | NVARCHAR(25), NN    | Apellido del usuario.                        |
| email         | NVARCHAR(25), NN, UNIQUE | Correo electrónico del usuario.      |
| telefono      | VARCHAR(10), UNIQUE | Teléfono del usuario.                        |
| cedula        | VARCHAR(10), UNIQUE | Cédula del usuario.                          |
| fechaNac      | DATE, NN            | Fecha de nacimiento del usuario.             |

### MetodoPago
| Campo         | Tipo                | Descripción                                  |
|---------------|---------------------|----------------------------------------------|
| ID_MetodoPago | INT, Identity, PK   | Identificador único del método de pago.      |
| metodo        | NVARCHAR(25), NN    | Método de pago (e.g., tarjeta de crédito, PayPal).  |