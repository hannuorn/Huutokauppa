# Käyttötapaukset ja SQL-kyselyt

Lista sisältää toistaiseksi vain ns. mielenkiintoiset kyselyt,
triviaalimmat tapaukset puuttuvat.

#### Kaikkien huutokauppojen listaus
    SELECT auction.id, auction.title, MAX(bid.amount)
    FROM auction LEFT JOIN bid ON bid.auction_id = auction.id
    GROUP BY auction.id;

#### Käyttäjän omien huutokauppojen listaus (parametrina käyttäjän id)
    SELECT auction.id, auction.title, MAX(bid.amount)
    FROM auction LEFT JOIN bid ON bid.auction_id = auction.id
    WHERE auction.account_id = (?)
    GROUP BY auction.id;

#### Huutokaupan huutojen listaus (parametrina huutokaupan id)
    SELECT bid.amount, account.name, bid.date_created
    FROM bid
    JOIN account ON bid.account_id = account.id
    WHERE (bid.auction_id = (?))
    ORDER BY bid.amount DESC;

#### Huutokaupan korkeimman huudon ja huutajan haku (parametrina huutokaupan id)
    SELECT account.name, bid.amount
    FROM account JOIN bid ON bid.account_id = account.id
    WHERE ((bid.auction_id = :auction_id) AND (bid.amount =
        (SELECT MAX(bid.amount) FROM bid
         WHERE bid.auction_id = :auction_id)));

#### Niiden huutokauppojen haku, joihin käyttäjä on osallistunut
    SELECT auction.id, auction.title, MAX(bid.amount)
    FROM auction JOIN bid ON bid.auction_id = auction.id
    WHERE bid.account_id = :account_id
    GROUP BY auction.id;
