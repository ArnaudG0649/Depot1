CREATE TABLE "pokemon" (
  "pokemon_id" integer PRIMARY KEY,
  "name" varchar(50) NOT NULL,
  "name_de" varchar(100),
  "generation" smallint NOT NULL,
  "height" float,
  "weight" float
);

CREATE TABLE "pokemon_type" (
  "pokemon_id" integer,
  "type_id" integer,
  PRIMARY KEY ("pokemon_id", "type_id")
);

CREATE TABLE "type" (
  "type_id" integer PRIMARY KEY,
  "name" varchar(20) NOT NULL
);

ALTER TABLE "pokemon_type" ADD FOREIGN KEY ("pokemon_id") REFERENCES "pokemon" ("pokemon_id");

ALTER TABLE "pokemon_type" ADD FOREIGN KEY ("type_id") REFERENCES "type" ("type_id");


/*ALTER TABLE "pokemon" (
  "name" varchar(50) NOT NULL,
  "name_de" varchar(100),
);*/
