from sqlalchemy import (Column, Integer, String, Numeric, ForeignKey, 
                        UniqueConstraint, Date)
from sqlalchemy.orm import relationship

from . import Base


class TeamMatchStats(Base):
    __tablename__ = 'teams_stats'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True, nullable=False)
    match = relationship('Match', backref='teams_stats')
    team_id = Column(ForeignKey('teams.id'), index=True, nullable=False)
    team = relationship('Team', backref='matches_stats')

    MP = Column(Numeric)
    OPOS = Column(Numeric)
    DPOS = Column(Numeric)

    FG = Column(Integer, nullable=True)
    FGA = Column(Integer, nullable=True)
    FGP = Column(Numeric, nullable=True)
    PTS = Column(Integer, nullable=True)
    TWO = Column(Integer, nullable=True)
    TWOA = Column(Integer, nullable=True)
    TWOP = Column(Numeric, nullable=True)
    TWOAr = Column(Numeric, nullable=True)
    THR = Column(Integer, nullable=True)
    THRA = Column(Integer, nullable=True)
    THRP = Column(Numeric, nullable=True)
    THRAr = Column(Numeric, nullable=True)
    FT = Column(Integer, nullable=True)
    FTA = Column(Integer, nullable=True)
    FTP = Column(Numeric, nullable=True)
    FTAr = Column(Numeric, nullable=True)
    FT_to_FGA = Column(Numeric, nullable=True)
    EFGP = Column(Numeric, nullable=True)
    TSA = Column(Numeric, nullable=True)
    TSP = Column(Numeric, nullable=True)
    FIC = Column(Numeric, nullable=True)
    PACE = Column(Numeric, nullable=True)

    ORB = Column(Integer, nullable=True)
    ORBr = Column(Numeric, nullable=True)
    DRB = Column(Integer, nullable=True)
    DRBr = Column(Numeric, nullable=True)
    TRB = Column(Integer, nullable=True)
    AST = Column(Integer, nullable=True)
    AST_to_TOV = Column(Numeric, nullable=True)
    STL = Column(Integer, nullable=True)
    STL_to_TOV = Column(Numeric, nullable=True)
    BLK = Column(Integer, nullable=True)
    TOV = Column(Integer, nullable=True)
    PF = Column(Integer, nullable=True)

    ORBP = Column(Numeric, nullable=True)
    DRBP = Column(Numeric, nullable=True)
    TRBP = Column(Numeric, nullable=True)
    ASTP = Column(Numeric, nullable=True)
    STLP = Column(Numeric, nullable=True)
    BLKP = Column(Numeric, nullable=True)
    TOVP = Column(Numeric, nullable=True)
    USGP = Column(Numeric, nullable=True)
    ORtg = Column(Numeric, nullable=True)
    AORtg = Column(Numeric, nullable=True)
    DRtg = Column(Numeric, nullable=True)
    ADRtg = Column(Numeric, nullable=True)

    PLUS_MINUS = Column(Integer, nullable=True)

    UniqueConstraint(match_id, team_id)

    def __repr__(self):
        return '{date: %s, league: %s, team: %s}' \
                    % (self.match.date, self.match.league.name, self.team.name)


class PlayerMatchStats(Base):
    __tablename__ = 'players_stats'

    id = Column(Integer, primary_key=True)
    player_id = Column(ForeignKey('players.id'), index=True, nullable=False)
    player = relationship('Player', backref='stats')
    match_id = Column(ForeignKey('matches.id'), index=True, nullable=False)
    match = relationship('Match', backref='players_stats')
    team_id = Column(ForeignKey('teams.id'), index=True, nullable=False)
    team = relationship('Team', backref='players_matches_stats')

    MP = Column(Numeric)
    OPOS = Column(Numeric)
    DPOS = Column(Numeric)

    FG = Column(Integer, nullable=True)
    FGA = Column(Integer, nullable=True)
    FGP = Column(Numeric, nullable=True)
    PTS = Column(Integer, nullable=True)
    TWO = Column(Integer, nullable=True)
    TWOA = Column(Integer, nullable=True)
    TWOP = Column(Numeric, nullable=True)
    TWOAr = Column(Numeric, nullable=True)
    THR = Column(Integer, nullable=True)
    THRA = Column(Integer, nullable=True)
    THRP = Column(Numeric, nullable=True)
    THRAr = Column(Numeric, nullable=True)
    FT = Column(Integer, nullable=True)
    FTA = Column(Integer, nullable=True)
    FTP = Column(Numeric, nullable=True)
    FTAr = Column(Numeric, nullable=True)
    FT_to_FGA = Column(Numeric, nullable=True)
    EFGP = Column(Numeric, nullable=True)
    TSA = Column(Numeric, nullable=True)
    TSP = Column(Numeric, nullable=True)
    HOB = Column(Numeric, nullable=True)
    FIC = Column(Numeric, nullable=True)
    PACE = Column(Numeric, nullable=True)

    ORB = Column(Integer, nullable=True)
    ORBr = Column(Numeric, nullable=True)
    DRB = Column(Integer, nullable=True)
    DRBr = Column(Numeric, nullable=True)
    TRB = Column(Integer, nullable=True)
    AST = Column(Integer, nullable=True)
    AST_to_TOV = Column(Numeric, nullable=True)
    STL = Column(Integer, nullable=True)
    STL_to_TOV = Column(Numeric, nullable=True)
    BLK = Column(Integer, nullable=True)
    TOV = Column(Integer, nullable=True)
    PF = Column(Integer, nullable=True)

    ORBP = Column(Numeric, nullable=True)
    DRBP = Column(Numeric, nullable=True)
    TRBP = Column(Numeric, nullable=True)
    ASTP = Column(Numeric, nullable=True)
    STLP = Column(Numeric, nullable=True)
    BLKP = Column(Numeric, nullable=True)
    TOVP = Column(Numeric, nullable=True)
    USGP = Column(Numeric, nullable=True)
    ORtg = Column(Numeric, nullable=True)
    AORtg = Column(Numeric, nullable=True)
    DRtg = Column(Numeric, nullable=True)
    ADRtg = Column(Numeric, nullable=True)

    PLUS_MINUS = Column(Integer, nullable=True)

    UniqueConstraint(player_id, match_id)

    def __repr__(self):
        return '{date: %s, league: %s, team: %s, player: %s}' \
                    % (self.match.date, self.match.league.name, self.team.name,
                            self.player.name)


class TeamSeasonStats(Base):
    __tablename__ = 'teams_seasons_stats'

    id = Column(Integer, primary_key=True)
    team_id = Column(ForeignKey('teams.id'), index=True, nullable=False)
    team = relationship('Team')
    league_id = Column(ForeignKey('leagues.id'), index=True, nullable=False)
    league = relationship('League')
    date = Column(Date)
    type = Column(String)

    MP = Column(Numeric)
    OPOS = Column(Numeric)
    DPOS = Column(Numeric)

    FG = Column(Integer, nullable=True)
    FGA = Column(Integer, nullable=True)
    FGP = Column(Numeric, nullable=True)
    PTS = Column(Integer, nullable=True)
    TWO = Column(Integer, nullable=True)
    TWOA = Column(Integer, nullable=True)
    TWOP = Column(Numeric, nullable=True)
    TWOAr = Column(Numeric, nullable=True)
    THR = Column(Integer, nullable=True)
    THRA = Column(Integer, nullable=True)
    THRP = Column(Numeric, nullable=True)
    THRAr = Column(Numeric, nullable=True)
    FT = Column(Integer, nullable=True)
    FTA = Column(Integer, nullable=True)
    FTP = Column(Numeric, nullable=True)
    FTAr = Column(Numeric, nullable=True)
    FT_to_FGA = Column(Numeric, nullable=True)
    EFGP = Column(Numeric, nullable=True)
    TSA = Column(Numeric, nullable=True)
    TSP = Column(Numeric, nullable=True)
    FIC = Column(Numeric, nullable=True)
    PACE = Column(Numeric, nullable=True)

    ORB = Column(Integer, nullable=True)
    ORBr = Column(Numeric, nullable=True)
    DRB = Column(Integer, nullable=True)
    DRBr = Column(Numeric, nullable=True)
    TRB = Column(Integer, nullable=True)
    AST = Column(Integer, nullable=True)
    AST_to_TOV = Column(Numeric, nullable=True)
    STL = Column(Integer, nullable=True)
    STL_to_TOV = Column(Numeric, nullable=True)
    BLK = Column(Integer, nullable=True)
    TOV = Column(Integer, nullable=True)
    PF = Column(Integer, nullable=True)

    ORBP = Column(Numeric, nullable=True)
    DRBP = Column(Numeric, nullable=True)
    TRBP = Column(Numeric, nullable=True)
    ASTP = Column(Numeric, nullable=True)
    STLP = Column(Numeric, nullable=True)
    BLKP = Column(Numeric, nullable=True)
    TOVP = Column(Numeric, nullable=True)
    USGP = Column(Numeric, nullable=True)
    ORtg = Column(Numeric, nullable=True)
    AORtg = Column(Numeric, nullable=True)
    DRtg = Column(Numeric, nullable=True)
    ADRtg = Column(Numeric, nullable=True)

    PLUS_MINUS = Column(Integer, nullable=True)

    STREAK = Column(Integer, nullable=True)
    DIST_7 = Column(Numeric, nullable=True)
    MATCHES_PLAYED_7 = Column(Numeric, nullable=True)

    UniqueConstraint(team_id, date, type)


class TeamSeasonHomeStats(Base):
    __tablename__ = 'teams_seasons_home_stats'

    id = Column(Integer, primary_key=True)
    team_id = Column(ForeignKey('teams.id'), index=True, nullable=False)
    team = relationship('Team')
    league_id = Column(ForeignKey('leagues.id'), index=True, nullable=False)
    league = relationship('League')
    date = Column(Date)
    type = Column(String)

    MP = Column(Numeric)
    OPOS = Column(Numeric)
    DPOS = Column(Numeric)

    FG = Column(Integer, nullable=True)
    FGA = Column(Integer, nullable=True)
    FGP = Column(Numeric, nullable=True)
    PTS = Column(Integer, nullable=True)
    TWO = Column(Integer, nullable=True)
    TWOA = Column(Integer, nullable=True)
    TWOP = Column(Numeric, nullable=True)
    TWOAr = Column(Numeric, nullable=True)
    THR = Column(Integer, nullable=True)
    THRA = Column(Integer, nullable=True)
    THRP = Column(Numeric, nullable=True)
    THRAr = Column(Numeric, nullable=True)
    FT = Column(Integer, nullable=True)
    FTA = Column(Integer, nullable=True)
    FTP = Column(Numeric, nullable=True)
    FTAr = Column(Numeric, nullable=True)
    FT_to_FGA = Column(Numeric, nullable=True)
    EFGP = Column(Numeric, nullable=True)
    TSA = Column(Numeric, nullable=True)
    TSP = Column(Numeric, nullable=True)
    FIC = Column(Numeric, nullable=True)
    PACE = Column(Numeric, nullable=True)

    ORB = Column(Integer, nullable=True)
    ORBr = Column(Numeric, nullable=True)
    DRB = Column(Integer, nullable=True)
    DRBr = Column(Numeric, nullable=True)
    TRB = Column(Integer, nullable=True)
    AST = Column(Integer, nullable=True)
    AST_to_TOV = Column(Numeric, nullable=True)
    STL = Column(Integer, nullable=True)
    STL_to_TOV = Column(Numeric, nullable=True)
    BLK = Column(Integer, nullable=True)
    TOV = Column(Integer, nullable=True)
    PF = Column(Integer, nullable=True)

    ORBP = Column(Numeric, nullable=True)
    DRBP = Column(Numeric, nullable=True)
    TRBP = Column(Numeric, nullable=True)
    ASTP = Column(Numeric, nullable=True)
    STLP = Column(Numeric, nullable=True)
    BLKP = Column(Numeric, nullable=True)
    TOVP = Column(Numeric, nullable=True)
    USGP = Column(Numeric, nullable=True)
    ORtg = Column(Numeric, nullable=True)
    AORtg = Column(Numeric, nullable=True)
    DRtg = Column(Numeric, nullable=True)
    ADRtg = Column(Numeric, nullable=True)

    PLUS_MINUS = Column(Integer, nullable=True)

    STREAK = Column(Integer, nullable=True)
    DIST_7 = Column(Numeric, nullable=True)
    MATCHES_PLAYED_7 = Column(Numeric, nullable=True)

    UniqueConstraint(team_id, date, type)


class TeamSeasonAwayStats(Base):
    __tablename__ = 'teams_seasons_away_stats'

    id = Column(Integer, primary_key=True)
    team_id = Column(ForeignKey('teams.id'), index=True, nullable=False)
    team = relationship('Team')
    league_id = Column(ForeignKey('leagues.id'), index=True, nullable=False)
    league = relationship('League')
    date = Column(Date)
    type = Column(String)

    MP = Column(Numeric)
    OPOS = Column(Numeric)
    DPOS = Column(Numeric)

    FG = Column(Integer, nullable=True)
    FGA = Column(Integer, nullable=True)
    FGP = Column(Numeric, nullable=True)
    PTS = Column(Integer, nullable=True)
    TWO = Column(Integer, nullable=True)
    TWOA = Column(Integer, nullable=True)
    TWOP = Column(Numeric, nullable=True)
    TWOAr = Column(Numeric, nullable=True)
    THR = Column(Integer, nullable=True)
    THRA = Column(Integer, nullable=True)
    THRP = Column(Numeric, nullable=True)
    THRAr = Column(Numeric, nullable=True)
    FT = Column(Integer, nullable=True)
    FTA = Column(Integer, nullable=True)
    FTP = Column(Numeric, nullable=True)
    FTAr = Column(Numeric, nullable=True)
    FT_to_FGA = Column(Numeric, nullable=True)
    EFGP = Column(Numeric, nullable=True)
    TSA = Column(Numeric, nullable=True)
    TSP = Column(Numeric, nullable=True)
    FIC = Column(Numeric, nullable=True)
    PACE = Column(Numeric, nullable=True)

    ORB = Column(Integer, nullable=True)
    ORBr = Column(Numeric, nullable=True)
    DRB = Column(Integer, nullable=True)
    DRBr = Column(Numeric, nullable=True)
    TRB = Column(Integer, nullable=True)
    AST = Column(Integer, nullable=True)
    AST_to_TOV = Column(Numeric, nullable=True)
    STL = Column(Integer, nullable=True)
    STL_to_TOV = Column(Numeric, nullable=True)
    BLK = Column(Integer, nullable=True)
    TOV = Column(Integer, nullable=True)
    PF = Column(Integer, nullable=True)

    ORBP = Column(Numeric, nullable=True)
    DRBP = Column(Numeric, nullable=True)
    TRBP = Column(Numeric, nullable=True)
    ASTP = Column(Numeric, nullable=True)
    STLP = Column(Numeric, nullable=True)
    BLKP = Column(Numeric, nullable=True)
    TOVP = Column(Numeric, nullable=True)
    USGP = Column(Numeric, nullable=True)
    ORtg = Column(Numeric, nullable=True)
    AORtg = Column(Numeric, nullable=True)
    DRtg = Column(Numeric, nullable=True)
    ADRtg = Column(Numeric, nullable=True)

    PLUS_MINUS = Column(Integer, nullable=True)

    STREAK = Column(Integer, nullable=True)
    DIST_7 = Column(Numeric, nullable=True)
    MATCHES_PLAYED_7 = Column(Numeric, nullable=True)

    UniqueConstraint(team_id, date, type)

class PlayerSeasonStats(Base):
    __tablename__ = 'players_seasons_stats'

    id = Column(Integer, primary_key=True)
    team_id = Column(ForeignKey('teams.id'), index=True, nullable=False)
    team = relationship('Team')
    league_id = Column(ForeignKey('leagues.id'), index=True, nullable=False)
    league = relationship('League')
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player')
    date = Column(Date)

    MP = Column(Numeric)
    OPOS = Column(Numeric)
    DPOS = Column(Numeric)

    FG = Column(Integer, nullable=True)
    FGA = Column(Integer, nullable=True)
    FGP = Column(Numeric, nullable=True)
    PTS = Column(Integer, nullable=True)
    TWO = Column(Integer, nullable=True)
    TWOA = Column(Integer, nullable=True)
    TWOP = Column(Numeric, nullable=True)
    TWOAr = Column(Numeric, nullable=True)
    THR = Column(Integer, nullable=True)
    THRA = Column(Integer, nullable=True)
    THRP = Column(Numeric, nullable=True)
    THRAr = Column(Numeric, nullable=True)
    FT = Column(Integer, nullable=True)
    FTA = Column(Integer, nullable=True)
    FTP = Column(Numeric, nullable=True)
    FTAr = Column(Numeric, nullable=True)
    FT_to_FGA = Column(Numeric, nullable=True)
    EFGP = Column(Numeric, nullable=True)
    TSA = Column(Numeric, nullable=True)
    TSP = Column(Numeric, nullable=True)
    HOB = Column(Numeric, nullable=True)
    FIC = Column(Numeric, nullable=True)
    PACE = Column(Numeric, nullable=True)

    ORB = Column(Integer, nullable=True)
    ORBr = Column(Numeric, nullable=True)
    DRB = Column(Integer, nullable=True)
    DRBr = Column(Numeric, nullable=True)
    TRB = Column(Integer, nullable=True)
    AST = Column(Integer, nullable=True)
    AST_to_TOV = Column(Numeric, nullable=True)
    STL = Column(Integer, nullable=True)
    STL_to_TOV = Column(Numeric, nullable=True)
    BLK = Column(Integer, nullable=True)
    TOV = Column(Integer, nullable=True)
    PF = Column(Integer, nullable=True)

    ORBP = Column(Numeric, nullable=True)
    DRBP = Column(Numeric, nullable=True)
    TRBP = Column(Numeric, nullable=True)
    ASTP = Column(Numeric, nullable=True)
    STLP = Column(Numeric, nullable=True)
    BLKP = Column(Numeric, nullable=True)
    TOVP = Column(Numeric, nullable=True)
    USGP = Column(Numeric, nullable=True)
    ORtg = Column(Numeric, nullable=True)
    AORtg = Column(Numeric, nullable=True)
    DRtg = Column(Numeric, nullable=True)
    ADRtg = Column(Numeric, nullable=True)

    PLUS_MINUS = Column(Integer, nullable=True)

    STREAK = Column(Integer, nullable=True)
    DIST_7 = Column(Numeric, nullable=True)
    MATCHES_PLAYED_7 = Column(Numeric, nullable=True)

    UniqueConstraint(player_id, date)


class PlayerSeasonHomeStats(Base):
    __tablename__ = 'players_seasons_home_stats'

    id = Column(Integer, primary_key=True)
    team_id = Column(ForeignKey('teams.id'), index=True, nullable=False)
    team = relationship('Team')
    league_id = Column(ForeignKey('leagues.id'), index=True, nullable=False)
    league = relationship('League')
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player')
    date = Column(Date)

    MP = Column(Numeric)
    OPOS = Column(Numeric)
    DPOS = Column(Numeric)

    FG = Column(Integer, nullable=True)
    FGA = Column(Integer, nullable=True)
    FGP = Column(Numeric, nullable=True)
    PTS = Column(Integer, nullable=True)
    TWO = Column(Integer, nullable=True)
    TWOA = Column(Integer, nullable=True)
    TWOP = Column(Numeric, nullable=True)
    TWOAr = Column(Numeric, nullable=True)
    THR = Column(Integer, nullable=True)
    THRA = Column(Integer, nullable=True)
    THRP = Column(Numeric, nullable=True)
    THRAr = Column(Numeric, nullable=True)
    FT = Column(Integer, nullable=True)
    FTA = Column(Integer, nullable=True)
    FTP = Column(Numeric, nullable=True)
    FTAr = Column(Numeric, nullable=True)
    FT_to_FGA = Column(Numeric, nullable=True)
    EFGP = Column(Numeric, nullable=True)
    TSA = Column(Numeric, nullable=True)
    TSP = Column(Numeric, nullable=True)
    HOB = Column(Numeric, nullable=True)
    FIC = Column(Numeric, nullable=True)
    PACE = Column(Numeric, nullable=True)

    ORB = Column(Integer, nullable=True)
    ORBr = Column(Numeric, nullable=True)
    DRB = Column(Integer, nullable=True)
    DRBr = Column(Numeric, nullable=True)
    TRB = Column(Integer, nullable=True)
    AST = Column(Integer, nullable=True)
    AST_to_TOV = Column(Numeric, nullable=True)
    STL = Column(Integer, nullable=True)
    STL_to_TOV = Column(Numeric, nullable=True)
    BLK = Column(Integer, nullable=True)
    TOV = Column(Integer, nullable=True)
    PF = Column(Integer, nullable=True)

    ORBP = Column(Numeric, nullable=True)
    DRBP = Column(Numeric, nullable=True)
    TRBP = Column(Numeric, nullable=True)
    ASTP = Column(Numeric, nullable=True)
    STLP = Column(Numeric, nullable=True)
    BLKP = Column(Numeric, nullable=True)
    TOVP = Column(Numeric, nullable=True)
    USGP = Column(Numeric, nullable=True)
    ORtg = Column(Numeric, nullable=True)
    AORtg = Column(Numeric, nullable=True)
    DRtg = Column(Numeric, nullable=True)
    ADRtg = Column(Numeric, nullable=True)

    PLUS_MINUS = Column(Integer, nullable=True)

    STREAK = Column(Integer, nullable=True)
    DIST_7 = Column(Numeric, nullable=True)
    MATCHES_PLAYED_7 = Column(Numeric, nullable=True)

    UniqueConstraint(player_id, date)


class PlayerSeasonAwayStats(Base):
    __tablename__ = 'players_seasons_away_stats'

    id = Column(Integer, primary_key=True)
    team_id = Column(ForeignKey('teams.id'), index=True, nullable=False)
    team = relationship('Team')
    league_id = Column(ForeignKey('leagues.id'), index=True, nullable=False)
    league = relationship('League')
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player')
    date = Column(Date)

    MP = Column(Numeric)
    OPOS = Column(Numeric)
    DPOS = Column(Numeric)

    FG = Column(Integer, nullable=True)
    FGA = Column(Integer, nullable=True)
    FGP = Column(Numeric, nullable=True)
    PTS = Column(Integer, nullable=True)
    TWO = Column(Integer, nullable=True)
    TWOA = Column(Integer, nullable=True)
    TWOP = Column(Numeric, nullable=True)
    TWOAr = Column(Numeric, nullable=True)
    THR = Column(Integer, nullable=True)
    THRA = Column(Integer, nullable=True)
    THRP = Column(Numeric, nullable=True)
    THRAr = Column(Numeric, nullable=True)
    FT = Column(Integer, nullable=True)
    FTA = Column(Integer, nullable=True)
    FTP = Column(Numeric, nullable=True)
    FTAr = Column(Numeric, nullable=True)
    FT_to_FGA = Column(Numeric, nullable=True)
    EFGP = Column(Numeric, nullable=True)
    TSA = Column(Numeric, nullable=True)
    TSP = Column(Numeric, nullable=True)
    HOB = Column(Numeric, nullable=True)
    FIC = Column(Numeric, nullable=True)
    PACE = Column(Numeric, nullable=True)

    ORB = Column(Integer, nullable=True)
    ORBr = Column(Numeric, nullable=True)
    DRB = Column(Integer, nullable=True)
    DRBr = Column(Numeric, nullable=True)
    TRB = Column(Integer, nullable=True)
    AST = Column(Integer, nullable=True)
    AST_to_TOV = Column(Numeric, nullable=True)
    STL = Column(Integer, nullable=True)
    STL_to_TOV = Column(Numeric, nullable=True)
    BLK = Column(Integer, nullable=True)
    TOV = Column(Integer, nullable=True)
    PF = Column(Integer, nullable=True)

    ORBP = Column(Numeric, nullable=True)
    DRBP = Column(Numeric, nullable=True)
    TRBP = Column(Numeric, nullable=True)
    ASTP = Column(Numeric, nullable=True)
    STLP = Column(Numeric, nullable=True)
    BLKP = Column(Numeric, nullable=True)
    TOVP = Column(Numeric, nullable=True)
    USGP = Column(Numeric, nullable=True)
    ORtg = Column(Numeric, nullable=True)
    AORtg = Column(Numeric, nullable=True)
    DRtg = Column(Numeric, nullable=True)
    ADRtg = Column(Numeric, nullable=True)

    PLUS_MINUS = Column(Integer, nullable=True)

    STREAK = Column(Integer, nullable=True)
    DIST_7 = Column(Numeric, nullable=True)
    MATCHES_PLAYED_7 = Column(Numeric, nullable=True)

    UniqueConstraint(player_id, date)


class Score(Base):
    __tablename__ = 'scores'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True, unique=True, nullable=False)
    match = relationship('Match', backref='score', uselist=False)
    home_1 = Column(Integer)
    away_1 = Column(Integer)
    home_2 = Column(Integer)
    away_2 = Column(Integer)
    home_3 = Column(Integer)
    away_3 = Column(Integer)
    home_4 = Column(Integer)
    away_4 = Column(Integer)
    home_t = Column(Integer)
    away_t = Column(Integer)



class MatchOfficial(Base):
    __tablename__ = 'matches_officials'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True, nullable=False)
    match = relationship('Match')
    official_id = Column(ForeignKey('officials.id'), index=True, nullable=False)
    official = relationship('Official')
