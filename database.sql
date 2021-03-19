drop table if exists LeagueAccount; 
drop table if exists LeagueAccountRank;
drop table if exists UserAccount; 
drop table if exists UserAccountFriendList; 
drop table if exists PreferMatch; 
drop table if exists Champions; 
drop table if exists Chat;
drop table if exists Match;
drop table if exists CreateChat;

CREATE TABLE LeagueAccount (
    leagueID int NOT NULL,
    gameLevel int,     	
    champion varchar(30),  
    gameRole varchar(20), 
    TFTrank varchar(10), 
    PRIMARY KEY (leagueID));

CREATE TABLE LeagueAccountRank (
    leagueID int NOT NULL,
    accountRank varchar(10),  
    rankQueue varchar(30),  
    rankValue varchar(20),  
    PRIMARY KEY (leagueID, accountRank),
    CONSTRAINT FK_leagueID FOREIGN KEY (leagueID) REFERENCES LeagueAccount(LeagueID) ON UPDATE CASCADE);

CREATE TABLE UserAccount (
    userID int NOT NULL,
    email varchar(50) NOT NULL,
    userName varchar(15)	NOT NULL,
    dateOfBirth	DATE,	          	
    gameServer varchar(50),
    userPassword varchar(30) NOT NULL,
    leagueID int NOT NULL,
    PRIMARY KEY (userID),
    --CONSTRAINT FOREIGN KEY (leagueID) REFERENCES LeagueAccount (leagueID) ON UPDATE CASCADE );

CREATE TABLE UserAccountFriendList (
    userID int NOT NULL,
    friendID int NOT NULL,
    friendName varchar(15) NOT NULL,
    PRIMARY KEY (userID, friendID),
/*     CONSTRAINT FOREIGN KEY (userID) REFERENCES UserAccount (userID) ON UPDATE CASCADE;
    CONSTRAINT FOREIGN KEY (friendID) REFERENCES UserAccount (userID) ON UPDATE CASCADE); */

CREATE TABLE PreferMatch (
    userID int NOT NULL,
    position varchar(8),
    rankRange varchar(15),
    PRIMARY KEY (userID, position, rankRange),
    CONSTRAINT FOREIGN KEY (userID) REFERENCES UserAccount (userID) ON UPDATE CASCADE);

CREATE TABLE Champions (
    userID int NOT NULL,
    champion varchar(15),
    PRIMARY KEY (userID, champion),
    CONSTRAINT FOREIGN KEY (userID) REFERENCES PreferMatch (userID) ON UPDATE CASCADE, );

CREATE TABLE Chat (
    chatTimestamp timestamp	NOT NULL,
    recepientID	int	NOT NULL,
    senderID int NOT NULL,
    PRIMARY KEY (recepientID));

CREATE TABLE Match ( 
    senderUID int NOT NULL,
    receiverUID	int	NOT NULL,
    PRIMARY KEY (senderID, receiverID),
    CONSTRAINT FOREIGN KEY (senderID, receiverID) REFERENCES UserAccount (userID) ON UPDATE CASCADE );

CREATE TABLE CreateChat ( 
    userID int NOT NULL,
    recepientID int	NOT NULL,
    PRIMARY KEY (userID, recepientID),
    CONSTRAINT FOREIGN KEY (userID) REFERENCES UserAccount (userID) ON DELETE CASCADE;
    CONSTRAINT FOREIGN KEY (recepientID) REFERENCES Chat (recepientID) ON UPDATE CASCADE );
