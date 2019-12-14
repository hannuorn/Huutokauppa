# Käyttötapaukset ja SQL-kyselyt


#### Aktiivisten huutokauppojen listaus

    SELECT auction.id, auction.title, bid.amount, account.name, DATE(auction.date_ends)
    FROM auction
    LEFT JOIN bid ON bid.auction_id = auction.id
    LEFT JOIN account ON account.id = bid.account_id
    WHERE (auction.date_ends > CURRENT_TIMESTAMP) AND
    (bid.amount IS NULL or (bid.amount =
        (SELECT MAX(bid.amount) FROM bid
         WHERE bid.auction_id = auction.id)))
         ORDER BY auction.date_ends;


#### Päättyneiden huutokauppojen listaus

    SELECT auction.id, auction.title, bid.amount, account.name, DATE(auction.date_ends)
    FROM auction
    LEFT JOIN bid ON bid.auction_id = auction.id
    LEFT JOIN account ON account.id = bid.account_id
    WHERE (auction.date_ends < CURRENT_TIMESTAMP) AND
    (bid.amount IS NULL or (bid.amount =
        (SELECT MAX(bid.amount) FROM bid
         WHERE bid.auction_id = auction.id)))
         ORDER BY auction.date_ends DESC;


#### Käyttäjän omien huutokauppojen listaus

    SELECT auction.id, auction.title, MAX(bid.amount)
    FROM auction LEFT JOIN bid ON bid.auction_id = auction.id
    WHERE auction.account_id = :account_id
    GROUP BY auction.id;


#### Huutokaupan huutojen listaus

    SELECT bid.amount, account.name, bid.date_created
    FROM bid
    JOIN account ON bid.account_id = account.id
    WHERE bid.auction_id = :auction_id
    ORDER BY bid.amount DESC;


#### Huutokaupan korkeimman huudon ja huutajan haku
    SELECT account.name, bid.amount
    FROM account JOIN bid ON bid.account_id = account.id
    WHERE (bid.auction_id = :auction_id) AND (bid.amount =
        (SELECT MAX(bid.amount) FROM bid
         WHERE bid.auction_id = :auction_id));


#### Niiden huutokauppojen haku, joihin käyttäjä on tehnyt huutoja
    SELECT auction.id, auction.title, MAX(bid.amount)
    FROM auction JOIN bid ON bid.auction_id = auction.id
    WHERE bid.account_id = :account_id
    GROUP BY auction.id;

#### Viestien listaus

    SELECT message.id, message.date_created, message.date_modified,
    account.id, account.name, message.body
    FROM message
    JOIN account ON message.account_id = account.id
    WHERE (message.auction_id = :auction_id)
    ORDER BY message.date_created DESC;
