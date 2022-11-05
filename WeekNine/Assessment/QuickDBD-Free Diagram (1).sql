-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/r7KrXd
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "gym" (
    "gym_ID" INTEGER   NOT NULL,
    "gym_Name" VARCHAR   NOT NULL,
    "address" VARCHAR   NOT NULL,
    "city" VARCHAR   NOT NULL,
    "zipcode" VARCHAR   NOT NULL,
    CONSTRAINT "pk_gym" PRIMARY KEY (
        "gym_ID"
     )
);

CREATE TABLE "trainers" (
    "trainer_id" INTEGER   NOT NULL,
    "gym_id" INTEGER   NOT NULL,
    "first_name" VARCHAR   NOT NULL,
    "last_name" VARCHAR   NOT NULL,
    CONSTRAINT "pk_trainers" PRIMARY KEY (
        "trainer_id"
     )
);

CREATE TABLE "members" (
    "member_id" INTEGER   NOT NULL,
    "gym_id" INTEGER   NOT NULL,
    "trainer_id" INTEGER   NOT NULL,
    "first_name" VARCHAR   NOT NULL,
    "last_name" VARCHAR   NOT NULL,
    "address" VARCHAR   NOT NULL,
    "city" VARCHAR   NOT NULL,
    CONSTRAINT "pk_members" PRIMARY KEY (
        "member_id"
     )
);

CREATE TABLE "payments" (
    "payment_id" INTEGER   NOT NULL,
    "member_id" INTEGER   NOT NULL,
    "billing_zip" INTEGER   NOT NULL,
    CONSTRAINT "pk_payments" PRIMARY KEY (
        "payment_id"
     )
);

ALTER TABLE "trainers" ADD CONSTRAINT "fk_trainers_gym_id" FOREIGN KEY("gym_id")
REFERENCES "gym" ("gym_ID");

ALTER TABLE "members" ADD CONSTRAINT "fk_members_gym_id" FOREIGN KEY("gym_id")
REFERENCES "gym" ("gym_ID");

ALTER TABLE "members" ADD CONSTRAINT "fk_members_trainer_id" FOREIGN KEY("trainer_id")
REFERENCES "trainers" ("trainer_id");

ALTER TABLE "payments" ADD CONSTRAINT "fk_payments_member_id" FOREIGN KEY("member_id")
REFERENCES "members" ("member_id");

