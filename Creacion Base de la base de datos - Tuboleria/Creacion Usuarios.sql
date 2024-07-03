-- Rol de solo lectura
CREATE ROLE readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO readonly;

-- Rol con permisos de manipulación de datos
CREATE ROLE dataeditor;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO dataeditor;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO dataeditor;


CREATE USER reader_user WITH ENCRYPTED PASSWORD 'password123';
GRANT readonly TO reader_user;

CREATE USER editor_user WITH ENCRYPTED PASSWORD 'password456';
GRANT dataeditor TO editor_user;


CREATE USER reader_user WITH ENCRYPTED PASSWORD 'password123';
GRANT readonly TO reader_user;

CREATE USER editor_user WITH ENCRYPTED PASSWORD 'password456';
GRANT dataeditor TO editor_user;
