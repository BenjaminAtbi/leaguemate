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
    on delete cascade
    /*constraint UserLeaugeID foreign key (LeagueID) references UserLeague(LeagueID)
    on update cascade
    on delete cascade*/
);

create table if not exists UserPerferMatch(
	Username varchar(50) not null,
    PerferredPosition char(10) not null,
    PerferredRankBottom int not null,
    PerferredRankTop int not null,
    PerferredType varchar(10),
    primary key (Username),
    constraint PerferUN foreign key (Username) references UserAccount(Username)
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
insert into UserAccount(AccountName, AccountPassword, Username) values
('TestAN1','testpw1','TestUN1'),
('TestAN2','testpw2','TestUN2'),
('TestAN3','testpw3','TestUN3'),
('TestAN4','testpw4','TestUN4'),
('TestAN5','testpw5','TestUN5');

insert into UserInfor(Username,Email,DateofBirth,Country) values
('TestUN1','testemail1@test.com','1990-01-01','Canada'),
('TestUN2','testemail2@test.com','1991-08-25','China'),
('TestUN3','testemail3@test.com','1993-05-21','American'),
('TestUN4','testemail4@test.com','1994-04-21','UK'),
('TestUN5','testemail5@test.com','1998-12-31','Japan');

insert into UserLeague(Username,GameServer,LeagueID) values
('TestUN1','NA','TestLID1'),
('TestUN2','NA','TestLID2'),
('TestUN3','NA','TestLID3'),
('TestUN4','NA','TestLID4'),
('TestUN5','NA','TestLID5');

insert into LeagueAccount(GameServer,LeagueID,GameLevel,AccountRank,QueueType,TFTrank,Position) values
('NA','TestLID1',50,0,'Solo/Duo',0,'Top'),
('NA','TestLID2',60,1,'Flax',1,'Jungle'),
('NA','TestLID3',70,2,'AnyType',2,'Middle'),
('NA','TestLID4',80,3,'TFT',3,'Bottom'),
('NA','TestLID5',90,4,'ARAM',4,'Support');

insert into UserPerferMatch(Username, PerferredPosition, PerferredRankBottom, PerferredRankTop,  PerferredType) values
('TestUN1','Bottom',0,4,'Flax'),
('TestUN2','Middle',0,3,'AnyType'),
('TestUN3','Top',1,4,'ARAM'),
('TestUN4','Jungle',2,3,'TFT'),
('TestUN5','Support',2,4,'Solo/Duo');

insert into UserGoodAt(Username,GoodAtPosition,GoodAtRole,GoodAtChamp) values
('TestUN1','Top','Tank','Ornn'),
('TestUN2','Jungle','Fighter','Warwick'),
('TestUN3','Middle','Mega','LeBlanc'),
('TestUN4','Bottom','Marksman','Jinx'),
('TestUN5','Support','Controller','Leona');

create table if not exists LeagueAccount(  GameServer varchar(10) not null,     LeaugeID varchar(50) not null,     GameLevel int not null,     AccountRank int not null,     QueueType varchar(10),     TFTRank int not null,     Position char(10),     primary key(GameServer, LeagueID),     constraint UserGameSer foreign key (GameServer) references UserLeague(Gameserver)     on update cascade     on delete cascade,     constraint UserLeaugeID foreign key (LeagueID) references UserLeague(LeagueID)     on update cascade     on delete cascade )
