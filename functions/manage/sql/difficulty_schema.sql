CREATE TABLE difficulty (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	max_letter INTEGER UNIQUE,
	diff TEXT NOT NULL,
	sequence INTEGER 
);