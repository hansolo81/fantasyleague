BEGIN;
CREATE TABLE "base_position" (
    "id" integer NOT NULL PRIMARY KEY,
    "code" varchar(10) NOT NULL,
    "name" varchar(20) NOT NULL
)
;
CREATE TABLE "base_player" (
    "id" integer NOT NULL PRIMARY KEY,
    "firstname" varchar(200) NOT NULL,
    "lastname" varchar(200) NOT NULL,
    "value" decimal NOT NULL,
    "position_id" integer NOT NULL REFERENCES "base_position" ("id")
)
;
CREATE TABLE "base_venue" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(200) NOT NULL
)
;
CREATE TABLE "base_team" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(200) NOT NULL,
    "home_ground_id" integer NOT NULL REFERENCES "base_venue" ("id")
)
;
CREATE TABLE "base_teamplayer" (
    "id" integer NOT NULL PRIMARY KEY,
    "team_id" integer NOT NULL REFERENCES "base_team" ("id"),
    "player_id" integer NOT NULL REFERENCES "base_player" ("id"),
    "week_joined" integer NOT NULL,
    "week_departed" integer
)
;
CREATE TABLE "base_playerstats" (
    "id" integer NOT NULL PRIMARY KEY,
    "player_id" integer NOT NULL REFERENCES "base_player" ("id"),
    "week" integer NOT NULL,
    "goals" integer NOT NULL,
    "assists" integer NOT NULL,
    "conceded" integer NOT NULL,
    "saves" integer NOT NULL,
    "yellow_card" integer NOT NULL,
    "red_card" integer NOT NULL,
    "bonus" integer NOT NULL
)
;
CREATE TABLE "base_fixture" (
    "id" integer NOT NULL PRIMARY KEY,
    "week" integer NOT NULL,
    "home_team_id" integer NOT NULL REFERENCES "base_team" ("id"),
    "away_team_id" integer NOT NULL REFERENCES "base_team" ("id"),
    "home_score" integer NOT NULL,
    "away_score" integer NOT NULL
)
;
COMMIT;
