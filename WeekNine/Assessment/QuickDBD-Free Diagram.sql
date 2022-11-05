-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/r7KrXd
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "classes" (
    "class_id" int   NOT NULL,
    "trainer_id" int   NOT NULL,
    "gym_id" int   NOT NULL,
    "class_name" varchar(50)   NOT NULL,
    "commission_percentage" int   NOT NULL,
    CONSTRAINT "pk_classes" PRIMARY KEY (
        "class_id"
     )
);

CREATE TABLE "class_attendance" (
    "member_id" int   NOT NULL,
    "class_id" int   NOT NULL,
    CONSTRAINT "pk_class_attendance" PRIMARY KEY (
        "member_id"
     )
);

ALTER TABLE "classes" ADD CONSTRAINT "fk_classes_class_id" FOREIGN KEY("class_id")
REFERENCES "class_attendance" ("class_id");

