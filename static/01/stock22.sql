--
-- File generated with SQLiteStudio v3.2.1 on Mon Dec 30 16:57:43 2019
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: stock
CREATE TABLE "stock" ("TimeCreated" datetime NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "TimeDeleted" datetime NULL, "Deleted" bool NULL, "Symbol" varchar(10) NOT NULL, "Name" varchar(100) NOT NULL, "Sector" varchar(45) NULL, "Info" text NULL, "TimeModified" datetime NULL, "Creator" integer NULL REFERENCES "users" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO stock (TimeCreated, id, TimeDeleted, Deleted, Symbol, Name, Sector, Info, TimeModified, Creator) VALUES (NULL, 4, NULL, NULL, 'Symbol', 'Name', 'Sector', NULL, NULL, NULL);

-- Index: stock_Symbol_fb254eaf
CREATE INDEX "stock_Symbol_fb254eaf" ON "stock" ("Symbol");

-- Index: stock_Name_910a5a8a
CREATE INDEX "stock_Name_910a5a8a" ON "stock" ("Name");

-- Index: stock_Creator_57b387e9
CREATE INDEX "stock_Creator_57b387e9" ON "stock" ("Creator");

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
