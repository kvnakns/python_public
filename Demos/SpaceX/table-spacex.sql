

CREATE TABLE kev.spacex_launches (
    name TEXT PRIMARY KEY,
    date_utc TIMESTAMP,
    rocket TEXT,
    success BOOLEAN,
	youtube_id TEXT,
    details TEXT
);
