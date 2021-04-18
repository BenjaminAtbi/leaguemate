CREATE TABLE IF NOT EXISTS UserAccount(
	AccountName VARCHAR(50) NOT NULL,
    AccountPassword VARCHAR(30) NOT NULL,
    Username VARCHAR(15) NOT NULL,
	PRIMARY KEY(AccountName),
    constraint UniqueUN unique (Username)
);

create table if not exists UserInfor(
	Username varchar(50) not null,
    Email varchar(50) default null,
    DateofBirth date not null,
    Country varchar(20) not null,
    primary key (Username),
    constraint InforUN foreign key (Username) references UserAccount(Username)
		on update cascade
        on delete cascade
);

create table if not exists UserLeague(
	Username varchar(50) not null,
    GameServer varchar(10) not null,
    LeagueID varchar(50) not null,
    primary key (UserName),
    constraint LeagueUN foreign key (Username) references UserAccount(Username)
		on update cascade
        on delete cascade,
	constraint UniqueID unique (GameServer, LeagueID)
);

create table if not exists RankName(
	RankLevel int not null,
    RankName char(20) not null,
    primary key (RankLevel)
);


create table if not exists LeagueAccount(
	GameServer varchar(10) not null,
    LeagueID varchar(50) not null,
    GameLevel int not null,
    AccountRank int not null,
    QueueType varchar(10),
    TFTRank int not null,
    Position char(10),
    primary key(GameServer, LeagueID),
    constraint UserGameSer foreign key (GameServer,LeagueID) references UserLeague(GameServer,LeagueID)
		on update cascade
		on delete cascade,
    constraint Rankmean foreign key (AccountRank) references RankName(RankLevel)
		on update cascade
        on delete cascade,
	constraint TFTRankmean foreign key (TFTRank) references RankName(RankLevel)
		on update cascade
        on delete cascade
);

create table if not exists UserPreferMatch(
	Username varchar(50) not null,
    PreferredPosition char(10) not null,
    PreferredRankBottom int not null,
    PreferredRankTop int not null,
    PreferredType varchar(10),
    primary key (Username),
    constraint PreferUN foreign key (Username) references UserAccount(Username)
		on update cascade
        on delete cascade,
	constraint Rankrangebottom foreign key (PreferredRankBottom) references RankName(RankLevel)
		on update cascade
        on delete cascade,
	constraint Rankrangetop foreign key (PreferredRankTop) references RankName(RankLevel)
		on update cascade
        on delete cascade
	
);

create table if not exists UserGoodAt(
	Username varchar(50) not null,
    GoodAtPosition varchar(10), 
    GoodAtRole varchar(20),
    GoodAtChamp varchar(20),
    primary key(Username),
    constraint GoodAtUN foreign key (Username) references UserAccount(Username)
		on update cascade
        on delete cascade
);



/* Populate tables*/
insert into RankName(RankLevel, RankName) values
(0,'No rank'),
(1,'Iron'),
(2,'Bronze'),
(3,'Silver'),
(4,'Gold'),
(5,'Platinum'),
(6,'Diamond'),
(7,'Master'),
(8,'GrandMaster'),
(9,'Challenger');

insert into UserAccount(AccountName, AccountPassword, Username) values
('TestAN1','testpw1','TestUN1'),
('TestAN2','testpw2','TestUN2'),
('TestAN3','testpw3','TestUN3'),
('TestAN4','testpw4','TestUN4'),
('TestAN5','testpw5','TestUN5'),
('TestAN6','testpw6','TestUN6'),
('TestAN7','testpw7','TestUN7'),
('TestAN8','testpw8','TestUN8'),
('TestAN9','testpw9','TestUN9'),
('TestAN10','testpw10','TestUN10'),
('TestAN11','testpw11','TestUN11'),
('TestAN12','testpw12','TestUN12'),
('TestAN13','testpw13','TestUN13'),
('TestAN14','testpw14','TestUN14'),
('TestAN15','testpw15','TestUN15');

insert into UserInfor(Username,Email,DateofBirth,Country) values
('TestUN1','testemail1@test.com','1990-01-01','Canada'),
('TestUN2','testemail2@test.com','1991-08-25','China'),
('TestUN3','testemail3@test.com','1993-05-21','America'),
('TestUN4','testemail4@test.com','1994-04-21','UK'),
('TestUN5','testemail5@test.com','1972-12-31','Canada'),
('TestUN6','testemail6@test.com','1999-01-31','China'),
('TestUN7','testemail7@test.com','1980-12-11','American'),
('TestUN8','testemail8@test.com','2001-05-12','Canada'),
('TestUN9','testemail9@test.com','1997-10-14','Canada'),
('TestUN10','testemail10@test.com','1985-02-19','Canada'),
('TestUN11','testemail11@test.com','1979-04-21','America'),
('TestUN12','testemail12@test.com','1991-10-27','Canada'),
('TestUN13','testemail13@test.com','1992-11-16','Canada'),
('TestUN14','testemail14@test.com','1994-07-05','Canada'),
('TestUN15','testemail15@test.com','1996-08-03','America');

insert into UserLeague(Username,GameServer,LeagueID) values
('TestUN1','NA','TestLID1'),
('TestUN2','NA','TestLID2'),
('TestUN3','NA','TestLID3'),
('TestUN4','NA','TestLID4'),
('TestUN5','NA','TestLID5'),
('TestUN6','NA','TestLID6'),
('TestUN7','NA','TestLID7'),
('TestUN8','NA','TestLID8'),
('TestUN9','NA','TestLID9'),
('TestUN10','NA','TestLID10'),
('TestUN11','NA','TestLID11'),
('TestUN12','NA','TestLID12'),
('TestUN13','NA','TestLID13'),
('TestUN14','NA','TestLID14'),
('TestUN15','NA','TestLID15');

insert into LeagueAccount(GameServer,LeagueID,GameLevel,AccountRank,QueueType,TFTrank,Position) values
('NA','TestLID1',50,0,'Solo/Duo',0,'Top'),
('NA','TestLID2',60,1,'Flex',1,'Jungle'),
('NA','TestLID3',70,2,'AnyType',2,'Middle'),
('NA','TestLID4',80,3,'TFT',3,'Bottom'),
('NA','TestLID5',90,4,'ARAM',4,'Support'),
('NA','TestLID6',55,6,'Solo/Duo',0,'Support'),
('NA','TestLID7',65,7,'Flex',1,'Middle'),
('NA','TestLID8',75,8,'AnyType',2,'Buttom'),
('NA','TestLID9',85,9,'Flex',3,'Fill'),
('NA','TestLID10',95,5,'ARAM',4,'Jungle'),
('NA','TestLID11',150,5,'Solo/Duo',0,'Top'),
('NA','TestLID12',160,4,'Flex',1,'Top'),
('NA','TestLID13',170,3,'AnyType',2,'Jungle'),
('NA','TestLID14',180,2,'Solo/Duo',3,'Top'),
('NA','TestLID15',190,5,'Solo/Duo',4,'Fill');

insert into UserPreferMatch(Username, PreferredPosition, PreferredRankBottom, PreferredRankTop,  PreferredType) values
('TestUN1','Bottom',0,4,'Flex'),
('TestUN2','Middle',0,3,'AnyType'),
('TestUN3','Top',1,4,'ARAM'),
('TestUN4','Jungle',2,3,'TFT'),
('TestUN5','Support',2,4,'Solo/Dou'),
('TestUN6','Fill',4,7,'Flex'),
('TestUN7','Fill',3,6,'AnyType'),
('TestUN8','Top',2,8,'ARAM'),
('TestUN9','Jungle',4,5,'TFT'),
('TestUN10','Support',1,7,'Solo/Dou'),
('TestUN11','Bottom',4,8,'Flex'),
('TestUN12','Fill',1,7,'AnyType'),
('TestUN13','Top',1,6,'ARAM'),
('TestUN14','Jungle',3,4,'TFT'),
('TestUN15','Support',2,7,'Solo/Dou');

insert into UserGoodAt(Username,GoodAtPosition,GoodAtRole,GoodAtChamp) values
('TestUN1','Top','Tank','Ornn'),
('TestUN2','Jungle','Fighter','Warwick'),
('TestUN3','Middle','Mega','LeBlanc'),
('TestUN4','Bottom','Fighter','Yasuo'),
('TestUN5','Support','Support','Leona'),
('TestUN6','Support','Tank','Ornn'),
('TestUN7','Middle','Fighter','Yasuo'),
('TestUN8','Middle','Mega','LeBlanc'),
('TestUN9','Bottom','Marksman','Jinx'),
('TestUN10','Jungle','Support','Leona'),
('TestUN11','Top','Tank','Ornn'),
('TestUN12','Top','Fighter','Yasuo'),
('TestUN13','Jungle','Mega','LeBlanc'),
('TestUN14','Top','Marksman','Teemo'),
('TestUN15','Support','Support','Sona');
