-- Opprette database om den ikke eksistere, og sette den aktiv:
CREATE DATABASE IF NOT EXISTS
    dyrepensjonat;

-- Sette database aktiv
USE dyrepensjonat;

-- Sletter eksisterende tabeller dersom de finnes
DROP TABLE IF EXISTS stays;
DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS owners;


-- Opprette tabeller i databaser:
CREATE TABLE owners (
    owner_id INT AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(120) NOT NULL,
    PRIMARY KEY (owner_id)
);

CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT,
    room_number VARCHAR(10) NOT NULL,
    room_type VARCHAR(40) NOT NULL,
    daily_rate decimal(8,2) NOT NULL,
    PRIMARY KEY (room_id),
    UNIQUE (room_number)
);

CREATE TABLE pets (
    pet_id INT AUTO_INCREMENT,
    owner_id int NOT NULL,
    name VARCHAR(80) NOT NULL,
    species VARCHAR(40) NOT NULL,
    breed VARCHAR(80) NOT NULL,
    PRIMARY KEY (pet_id),
    FOREIGN KEY (owner_id) references owners(owner_id)
);

CREATE TABLE stays (
    stay_id INT AUTO_INCREMENT,
    pet_id INT NOT NULL,
    room_id int NOT NULL,
    check_in date NOT NULL,
    check_out date NOT NULL,
    PRIMARY KEY (stay_id),
    FOREIGN KEY (pet_id) references pets(pet_id),
    FOREIGN KEY (room_id) references rooms(room_id)
);


-- Legger inn eksempldata
INSERT INTO owners(name, phone, email)
VALUES ('Ole Hansen','+4799887766','ole.hansen@gmail.com'),
       ('Per Olsen','+4798765432','per.hansen@yahoo.com'),
       ('Kari Nilsen','+4744556677','kari.nilsen@outlook.com'),
       ('Trude Johansen','+4746791385','trude.johansen@online.no'),
       ('Frank Larsen','+4797643128','frank.larsen@hotmail.com');

INSERT INTO rooms(room_number, room_type, daily_rate)
VALUES ('A101','Hunderom',1499.00),
       ('A102','Katterom',999.00),
       ('B101','Hunderom',1499.00),
       ('B102','Katterom',999.00),
       ('C101','Fuglebur',790.00);

INSERT INTO pets(owner_id, name, species, breed)
VALUES (1, 'Billy','Hund','Golden Retriever'),
       (2, 'Tassen','Hund','Border Collie'),
       (3, 'Flekken','Hund','Labrador'),
       (2, 'Molly','Katt','Norsk Skogkatt'),
       (4, 'Jakob','Fugl','Undulat'),
       (5, 'Petra','Katt','Maine Coon');

INSERT INTO stays(pet_id, room_id, check_in, check_out)
VALUES (1,1,'2024-12-01','2024-12-03'),
       (2,3,'2025-03-03','2025-03-09'),
       (3,1,'2025-11-15','2025-12-02'),
       (5,5,'2026-06-09','2026-06-13'),
       (4,2,'2026-08-09','2026-08-10');