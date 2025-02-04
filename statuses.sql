DROP TABLE IF EXISTS statues;
DROP TABLE IF EXISTS statuses;

CREATE TABLE statuses (
        status_id INTEGER primary key,
        name_status INTEGER
);

INSERT INTO statuses (status_id,name_status) VALUES(1,"Получена");
INSERT INTO statuses (status_id,name_status) VALUES(2,"Выполнена");
INSERT INTO statuses (status_id,name_status) VALUES(3,"Выполнена удаленно");
INSERT INTO statuses (status_id,name_status) VALUES(4,"Выполнена bitrix24");
INSERT INTO statuses (status_id,name_status) VALUES(5,"Выполнена планово");
INSERT INTO statuses (status_id,name_status) VALUES(6,"Отложена");
INSERT INTO statuses (status_id,name_status) VALUES(7,"Передана");
INSERT INTO statuses (status_id,name_status) VALUES(8,"Снята");
INSERT INTO statuses (status_id,name_status) VALUES(100,"Неизвестно");



