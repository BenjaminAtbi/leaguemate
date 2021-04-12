CREATE TABLE IF NOT EXISTS LeagueAccount (
    leagueID varchar(50) NOT NULL,
    gameLevel int,     	
    champion varchar(30),  
    gameRole varchar(20), 
    TFTrank varchar(10), 
    PRIMARY KEY (leagueID));

CREATE TABLE IF NOT EXISTS LeagueAccountRank (
    leagueID varchar(50) NOT NULL,
    accountRank varchar(20),  
    rankQueue varchar(30),  
    PRIMARY KEY (leagueID, accountRank),
    CONSTRAINT LeagueID_FK FOREIGN KEY (leagueID) REFERENCES LeagueAccount (leagueID) ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS UserAccount (
    userID int(9) NOT NULL,
    email varchar(50) NOT NULL,
    userName varchar(15) NOT NULL,
    dateOfBirth	DATE,	          	
    gameServer varchar(50),
    userPassword varchar(30) NOT NULL,
    leagueID varchar(50) NOT NULL,
    PRIMARY KEY (userID),
    CONSTRAINT UserLeagueID_FK FOREIGN KEY (leagueID) REFERENCES LeagueAccount (leagueID) ON UPDATE CASCADE
    CONSTRAINT limitConnectedAcct UNIQUE (userID, leagueID)
    );

CREATE TABLE IF NOT EXISTS UserAccountFriendList (
    userID int NOT NULL,
    friendID int NOT NULL,
    PRIMARY KEY (userID, friendID),
    CONSTRAINT userAcctID_FK FOREIGN KEY (userID) REFERENCES UserAccount (userID) 
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT friendAcctID_FK FOREIGN KEY (friendID) REFERENCES UserAccount (userID) 
        ON UPDATE CASCADE
        ON DELETE CASCADE);

CREATE TABLE IF NOT EXISTS PreferMatch (
    userID int NOT NULL,
    preferredPosition varchar(8),
    rankRange varchar(15),
    PRIMARY KEY (userID),
    CONSTRAINT userIDMatch_FK FOREIGN KEY (userID) REFERENCES UserAccount (userID) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE);

CREATE TABLE IF NOT EXISTS Champions (
    userID int NOT NULL,
    champion varchar(15),
    PRIMARY KEY (userID, champion),
    CONSTRAINT userIDChamp_FK FOREIGN KEY (userID) REFERENCES PreferMatch (userID) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE);

CREATE TABLE IF NOT EXISTS Chat (
    lastChatTimestamp timestamp	NOT NULL,    
    recipientID	int	NOT NULL,   
    senderID int NOT NULL,
    PRIMARY KEY (lastChatTimestamp));

CREATE TABLE IF NOT EXISTS MatchUsers ( 
    senderID int NOT NULL,
    receiverID	int	NOT NULL,
    PRIMARY KEY (senderID, receiverID),
    CONSTRAINT matchingSenderID_FK FOREIGN KEY (senderID) REFERENCES UserAccount (userID),
    CONSTRAINT matchingReceiverID_FK FOREIGN KEY (receiverID) REFERENCES UserAccount (userID));

CREATE TABLE IF NOT EXISTS CreateChat ( 
    userID int NOT NULL,
    recipientID int	NOT NULL,
    createdTimestamp timestamp,
    PRIMARY KEY (userID, createdTimestamp),
    FOREIGN KEY (recipientID) REFERENCES UserAccount (userID),
    CONSTRAINT createChatUserID_FK FOREIGN KEY (userID) REFERENCES UserAccount (userID)
        ON UPDATE CASCADE 
        ON DELETE CASCADE,
    CONSTRAINT createChatTimestamp_FK FOREIGN KEY (createdTimestamp) REFERENCES Chat (lastChatTimestamp) ON UPDATE CASCADE);


/* Populate tables*/

-- Adding values to table LeagueAccount
INSERT INTO LeagueAccount (leagueID, gameLevel, champion, gameRole, TFTrank) VALUES 
('Jamo1Yips', 23, 'Sona', 'Controller', 'N/A'),
('Saltern88', 122, 'Gnar', 'Specialist', 'N/A'),
('21preterite', 150, 'Nami', 'Controller', 'N/A'),
('Foofarraw', 88, 'RekSai', 'Fighter' , 'Silver II'),
('Versant', 200, 'Aphelios', 'Marksman', 'Diamond I');


-- Adding values to table LeagueAccount
INSERT INTO LeagueAccountRank (leagueID, accountRank, rankQueue) VALUES
('Jamo1Yips', 'N/A', 'N/A'),
('Saltern88', 'Platinum II', 'Solo/Duo'),
('21preterite', 'Diamond V', 'Flex'),
('Foofarraw', 'Gold IV', 'Flex'),
('Versant', 'Diamond I', 'Solo/Duo');

-- Adding values to table UserAccount
INSERT INTO UserAccount (userID, email, userName, dateOfBirth, gameServer, userPassword, leagueID) VALUES
(112345678, 'jamoyips@hotmail.com', 'Jun-soo Lee', '1998-07-09', 'North America', 'JunJamo111', 'Jamo1Yips'),
(123456789, 'saltern88@gmail.com', 'Bob Williams', '1996-02-18', 'North America', 'Bobjerrabd0', 'Saltern88'),
(234567890, 'antoniobrown7@hotmail.com', 'Antonio Brown', '1994-02-14', 'North America', 'anotoniobb21', '21preterite'),
(345678901, 'peterjones@gmail.com', 'Peter Jones', '1990-12-29', 'North America', 'foddpeterjones7', 'Foofarraw'),
(456789012, 'avarehonore@hotmail.com', 'Acare Honore', '1988-05-05', 'North America', 'versanthonore8', 'Versant');

-- Adding values to table UserAccountFriendList
INSERT INTO UserAccountFriendList (userID, friendID) VALUES
(123456789, 234567890),
(123456789, 345678901),
(123456789, 112345678),
(123456789, 456789012),
(456789012, 345678901);

-- Adding values to table PreferMatch
INSERT INTO PreferMatch (userID, preferredPosition, rankRange) VALUES
(112345678, 'Marksman', 'Iron'),
(123456789, 'Mage', 'Platinum'),
(234567890, 'Fighter', 'Diamond'),
(345678901, 'Marksman', 'Gold'),
(456789012, 'Controller', 'Diamond');

-- Adding values to table PreferMatch
INSERT INTO Champions (userID, champion) VALUES
(112345678, 'Sona'),
(123456789, 'Gnar'),
(234567890, 'Nami'),
(345678901, 'RekSai'),
(456789012, 'Aphelios');

-- Adding values to table Chat
INSERT INTO Chat (recipientID, senderID, lastChatTimestamp) VALUES
(123456789, 234567890, '2020-03-19 09:10:32'),
(123456789, 345678901, '2020-03-17 23:59:23'),
(123456789, 112345678, '2020-03-15 19:07:12'),
(123456789, 456789012, '2020-03-13 15:27:52'),
(456789012, 345678901, '2020-03-11 08:20:54');

-- Adding values to table MatchedUsers
INSERT INTO MatchUsers (senderID, receiverID) VALUES
(123456789, 234567890),
(123456789, 345678901),
(123456789, 112345678),
(123456789, 456789012),
(456789012, 345678901);

-- Adding values to table MatchedUsers
INSERT INTO CreateChat (userID, recipientID, createdTimestamp) VALUES
(123456789, 234567890, '2020-03-19 09:10:32'),
(123456789, 345678901, '2020-03-17 23:59:23'),
(123456789, 112345678, '2020-03-15 19:07:12'),
(123456789, 456789012, '2020-03-13 15:27:52'),
(456789012, 345678901, '2020-03-11 08:20:54');

