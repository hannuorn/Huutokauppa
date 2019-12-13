# Tietokantarakenteen kuvaus

Tietokannassa on neljä tietokantataulua. Tietokanta on normalisoitu.

## CREATE TABLE -lauseet

	CREATE TABLE account (
		id INTEGER NOT NULL, 
		date_created DATETIME, 
		date_modified DATETIME, 
		name VARCHAR(144) NOT NULL, 
		username VARCHAR(144) NOT NULL, 
		password VARCHAR(144) NOT NULL, 
		PRIMARY KEY (id), 
		UNIQUE (username)
	);

	CREATE TABLE auction (
		id INTEGER NOT NULL, 
		date_created DATETIME, 
		date_modified DATETIME, 
		date_ends DATETIME, 
		title VARCHAR(40) NOT NULL, 
		description VARCHAR(200) NOT NULL, 
		minimum_bid INTEGER, 
		account_id INTEGER NOT NULL, 
		PRIMARY KEY (id), 
		FOREIGN KEY(account_id) REFERENCES account (id)
	);

	CREATE TABLE bid (
		id INTEGER NOT NULL, 
		date_created DATETIME, 
		date_modified DATETIME, 
		auction_id INTEGER NOT NULL, 
		account_id INTEGER NOT NULL, 
		amount INTEGER NOT NULL, 
		PRIMARY KEY (id), 
		FOREIGN KEY(auction_id) REFERENCES auction (id), 
		FOREIGN KEY(account_id) REFERENCES account (id)
	);

	CREATE TABLE message (
		id INTEGER NOT NULL, 
		date_created DATETIME, 
		date_modified DATETIME, 
		auction_id INTEGER NOT NULL, 
		account_id INTEGER NOT NULL, 
		body VARCHAR(200) NOT NULL, 
		PRIMARY KEY (id), 
		FOREIGN KEY(auction_id) REFERENCES auction (id), 
		FOREIGN KEY(account_id) REFERENCES account (id)
	);
