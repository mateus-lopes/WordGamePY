CREATE TABLE words (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	topic_id INTEGER,
	diff_id INTEGER,
	word TEXT NOT NULL,
	FOREIGN KEY(topic_id) REFERENCES topics(id),
	FOREIGN KEY(diff_id) REFERENCES difficult(id)
);