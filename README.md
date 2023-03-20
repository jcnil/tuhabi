## Query para crear la tabla de usuario

 CREATE TABLE habi_db.user(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(40),
    password CHAR(12),
    first_name VARCHAR(150),
    last_name VARCHAR(150),
    email VARCHAR(150)
 );

## Se debe agregar el campo de estados a la tabal de property que no lo tiene para poder realizar la busqueda por el filtro de estados

ALTER TABLE habi_db.property
ADD state varchar(255);

## Consulta de la base de datos de los departemantos con status PRE_VENTA(3), EN_VENTA(4), VENDIDO(5)

SELECT p.address,
       p.city,
       p.price,
       p.description
                   FROM habi_db.property p 
                   INNER JOIN status_history sh 
                   ON p.id=sh.property_id 
                        WHERE sh.status_id in (3,4,5);
## 9

Para mejorar la inconsistencia de la informacion que se tiene se deben crear tablas con catalagos de las ciudades y estados cosa que no esta contemplada en el modelo actual de la base de datos, esto con la finalidad de que el usuario no tipee estos nombre si no que ya se les provea de un catalago precargado en en tablas.

## 10 
Para el servicio de Me gusta se debe crear una funcion para contar los Likes o Me gustas de cada de partamento de tal manera que se almacenen en un campo en la tabal de property como un numero, de igual forma se debe crear un contador para indicar la cantidad de likes por usuarios.
