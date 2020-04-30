-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

DROP TABLE IF EXISTS "SAR_Statistics";
CREATE TABLE "SAR_Statistics" (
    "Year" VARCHAR(500)    NOT NULL,
    "State" VARCHAR(500)   NOT NULL,
    "Industry" VARCHAR(500)   NOT NULL,
    "Suspicious_Activity" VARCHAR(500)   NOT NULL,
    "Count" int NOT NULL
    
);
