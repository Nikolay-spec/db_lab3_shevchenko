--Команди створення таблиць:
CREATE TABLE Players
(
  player_id         int           UNIQUE NOT NULL,
  player_photo      char(100)     UNIQUE NOT NULL,
  player_workrate   char(50)      NOT NULL,
  player_name       char(50)      NOT NULL,
  player_age        int           NOT NULL, 
  player_wage       char(10)      NOT NULL,
  country_id        int           NOT NULL,
  team_id           int           NOT NULL 
);

CREATE TABLE Countries
(
  country_id        int           UNIQUE NOT NULL,
  country_name      char(50)      NULL
);

CREATE TABLE Clubs
(
  team_id           int           UNIQUE NOT NULL,
  team_name         char(50)      UNIQUE NOT NULL
);

--Команди налаштування первинних та зовнішніх ключів:
ALTER TABLE Clubs ADD CONSTRAINT PK_Clubs PRIMARY KEY (team_id);
ALTER TABLE Countries ADD CONSTRAINT PK_Countries PRIMARY KEY (country_id);
ALTER TABLE Players ADD CONSTRAINT PK_Players PRIMARY KEY (player_id);

ALTER TABLE Players ADD CONSTRAINT FK_Players_Clubs FOREIGN KEY (team_id) REFERENCES Clubs (team_id);
ALTER TABLE Players ADD CONSTRAINT FK_Players_Countries FOREIGN KEY (country_id) REFERENCES Countries (country_id);
