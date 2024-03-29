nfl_headers = [
    "Game#",
    "Day",
    "Date",
    "Time",
    "Boxscore",
    "Result",
    "Overtime",
    "Rec",
    "HomeOrAway",
    "Opponent",
    "PointsFor",
    "PointsAgainst",
    "Off1stDowns",
    "OffTotYards",
    "OffPassYards",
    "OffRushYards",
    "OffTurnoverLost",
    "Opp1stDowns",
    "OppTotYards",
    "OppPassYards",
    "OppRushYards",
    "OppTurnoverLost",
    "ExpectedPointsOffense",
    "ExpectedPointsDefense",
    "ExpectedPointsSpTms",
]

nfl_teams = {
    "Arizona Cardinals": "crd",
    "Atlanta Falcons": "atl",
    "Baltimore Ravens": "rav",
    "Buffalo Bills": "buf",
    "Carolina Panthers": "car",
    "Chicago Bears": "chi",
    "Cincinnati Bengals": "cin",
    "Cleveland Browns": "cle",
    "Dallas Cowboys": "dal",
    "Denver Broncos": "den",
    "Detroit Lions": "det",
    "Green Bay Packers": "gnb",
    "Houston Texans": "htx",
    "Indianapolis Colts": "clt",
    "Jacksonville Jaguars": "jax",
    "Kansas City Chiefs": "kan",
    "Las Vegas Raiders": "rai",
    "Los Angeles Chargers": "sdg",
    "Los Angeles Rams": "ram",
    "Miami Dolphins": "mia",
    "Minnesota Vikings": "min",
    "New England Patriots": "nwe",
    "New Orleans Saints": "nor",
    "New York Giants": "nyg",
    "New York Jets": "nyj",
    "Philadelphia Eagles": "phi",
    "Pittsburgh Steelers": "pit",
    "San Francisco 49ers": "sfo",
    "Seattle Seahawks": "sea",
    "Tampa Bay Buccaneers": "tam",
    "Tennessee Titans": "oti",
    "Washington Football Team": "was",
}

ncaaf_headers = [
    "Game#",
    "Date",
    "Time",
    "Day",
    "School",
    "HomeOrAway",
    "Opponent",
    "Conference",
    "Result",
    "PointsFor",
    "PointsAgainst",
    "W",
    "L",
    "Streak",
    "Notes",
]

ncaaf_teams = {
    "Air Force": "air-force",
    "Akron": "akron",
    "Alabama": "alabama",
    "UAB": "alabama-birmingham",
    "Appalachian State": "appalachian-state",
    "Arizona": "arizona",
    "Arizona State": "arizona-state",
    "Arkansas": "arkansas",
    "Arkansas State": "arkansas-state",
    "Army": "army",
    "Auburn": "auburn",
    "Ball State": "ball-state",
    "Baylor": "baylor",
    "Boise State": "boise-state",
    "Boston College": "boston-college",
    "Bowling Green": "bowling-green-state",
    "BYU": "brigham-young",
    "Buffalo": "buffalo",
    "California": "california",
    "UCF": "central-florida",
    "Central Michigan": "central-michigan",
    "Charlotte": "charlotte",
    "Cincinnati": "cincinnati",
    "Clemson": "clemson",
    "Coastal Carolina": "coastal-carolina",
    "Colorado": "colorado",
    "Colorado State": "colorado-state",
    "Connecticut": "connecticut",
    "Duke": "duke",
    "East Carolina": "east-carolina",
    "Eastern Michigan": "eastern-michigan",
    "Florida": "florida",
    "Florida Atlantic": "florida-atlantic",
    "Florida International": "florida-international",
    "Florida State": "florida-state",
    "Fresno State": "fresno-state",
    "Georgia": "georgia",
    "Georgia Southern": "georgia-southern",
    "Georgia State": "georgia-state",
    "Georgia Tech": "georgia-tech",
    "Hawaii": "hawaii",
    "Houston": "houston",
    "Illinois": "illinois",
    "Indiana": "indiana",
    "Iowa": "iowa",
    "Iowa State": "iowa-state",
    "Kansas": "kansas",
    "Kansas State": "kansas-state",
    "Kent State": "kent-state",
    "Kentucky": "kentucky",
    "Liberty": "liberty",
    "Louisiana": "louisiana-lafayette",
    "Louisiana-Monroe": "louisiana-monroe",
    "LSU": "louisiana-state",
    "Louisiana Tech": "louisiana-tech",
    "Louisville": "louisville",
    "Marshall": "marshall",
    "Maryland": "maryland",
    "Massachusetts": "massachusetts",
    "Memphis": "memphis",
    "Miami (FL)": "miami-fl",
    "Miami (OH)": "miami-oh",
    "Michigan": "michigan",
    "Michigan State": "michigan-state",
    "Middle Tennessee State": "middle-tennessee-state",
    "Minnesota": "minnesota",
    "Ole Miss": "mississippi",
    "Mississippi State": "mississippi-state",
    "Missouri": "missouri",
    "Navy": "navy",
    "Nebraska": "nebraska",
    "Nevada": "nevada",
    "Nevada-Las Vegas": "nevada-las-vegas",
    "New Mexico": "new-mexico",
    "New Mexico State": "new-mexico-state",
    "North Carolina": "north-carolina",
    "North Carolina State": "north-carolina-state",
    "Northern Illinois": "northern-illinois",
    "North Texas": "north-texas",
    "Northwestern": "northwestern",
    "Notre Dame": "notre-dame",
    "Ohio": "ohio",
    "Ohio State": "ohio-state",
    "Oklahoma": "oklahoma",
    "Oklahoma State": "oklahoma-state",
    "Old Dominion": "old-dominion",
    "Oregon": "oregon",
    "Oregon State": "oregon-state",
    "Penn State": "penn-state",
    "Pitt": "pittsburgh",
    "Purdue": "purdue",
    "Rice": "rice",
    "Rutgers": "rutgers",
    "San Diego State": "san-diego-state",
    "San Jose State": "san-jose-state",
    "South Alabama": "south-alabama",
    "South Carolina": "south-carolina",
    "USC": "southern-california",
    "SMU": "southern-methodist",
    "Southern Mississippi": "southern-mississippi",
    "South Florida": "south-florida",
    "Stanford": "stanford",
    "Syracuse": "syracuse",
    "Temple": "temple",
    "Tennessee": "tennessee",
    "Texas": "texas",
    "Texas A&M": "texas-am",
    "Texas Christian": "texas-christian",
    "UTEP": "texas-el-paso",
    "UTSA": "texas-san-antonio",
    "Texas State": "texas-state",
    "Texas Tech": "texas-tech",
    "Toledo": "toledo",
    "Troy": "troy",
    "Tulane": "tulane",
    "Tulsa": "tulsa",
    "UCLA": "ucla",
    "Utah": "utah",
    "Utah State": "utah-state",
    "Vanderbilt": "vanderbilt",
    "Virginia": "virginia",
    "Virginia Tech": "virginia-tech",
    "Wake Forest": "wake-forest",
    "Washington": "washington",
    "Washington State": "washington-state",
    "Western Kentucky": "western-kentucky",
    "Western Michigan": "western-michigan",
    "West Virginia": "west-virginia",
    "Wisconsin": "wisconsin",
    "Wyoming": "wyoming",
}

ncaa_ranks = [
    "(1)",
    "(2)",
    "(3)",
    "(4)",
    "(5)",
    "(6)",
    "(7)",
    "(8)",
    "(9)",
    "(10)",
    "(11)",
    "(12)",
    "(13)",
    "(14)",
    "(15)",
    "(16)",
    "(17)",
    "(18)",
    "(19)",
    "(20)",
    "(21)",
    "(22)",
    "(23)",
    "(24)",
    "(25)",
]

mlb_teams = {
    "Arizona Diamondbacks": "ARI",
    "Atlanta Braves": "ATL",
    "Baltimore Orioles": "BAL",
    "Boston Red Sox": "BOS",
    "Chicago Cubs": "CHC",
    "Chicago White Sox": "CHW",
    "Cincinnati Reds": "CIN",
    "Cleveland Guardians": "CLE",
    "Colorado Rockies": "COL",
    "Detroit Tigers": "DET",
    "Houston Astros": "HOU",
    "Kansas City Royals": "KCR",
    "Los Angeles Angels": "LAA",
    "Los Angeles Dodgers": "LAD",
    "Miami Marlins": "MIA",
    "Milwaukee Brewers": "MIL",
    "Minnesota Twins": "MIN",
    "New York Mets": "NYM",
    "New York Yankees": "NYY",
    "Oakland Athletics": "OAK",
    "Philadelphia Phillies": "PHI",
    "Pittsburgh Pirates": "PIT",
    "San Diego Padres": "SDP",
    "San Francisco Giants": "SFG",
    "Seattle Mariners": "SEA",
    "St. Louis Cardinals": "STL",
    "Tampa Bay Rays": "TBR",
    "Texas Rangers": "TEX",
    "Toronto Blue Jays": "TOR",
    "Washington Nationals": "WSN",
}

mlb_headers = [
    "Game#",
    "Date",
    "Boxscore",
    "Home",
    "HomeOrAway",
    "Opponent",
    "Result",
    "PointsFor",
    "PointsAgainst",
    "Innings",
    "Rec",
    "Rank",
    "GamesBehind",
    "WinPitcher",
    "LossPitcher",
    "Save",
    "Duration",
    "DayOrNight",
    "Attendance",
    "CLI",
    "Streak",
    "Orig. Scheduled",
]

nba_teams = {
    "Atlanta Hawks": "ATL",
    "Boston Celtics": "BOS",
    "Brooklyn Nets": "BRK",
    "Charlotte Hornets": "CHO",
    "Chicago Bulls": "CHI",
    "Cleveland Cavaliers": "CLE",
    "Dallas Mavericks": "DAL",
    "Denver Nuggets": "DEN",
    "Detroit Pistons": "DET",
    "Golden State Warriors": "GSW",
    "Houston Rockets": "HOU",
    "Indiana Pacers": "IND",
    "Los Angeles Clippers": "LAC",
    "Los Angeles Lakers": "LAL",
    "Memphis Grizzlies": "MEM",
    "Miami Heat": "MIA",
    "Milwaukee Bucks": "MIL",
    "Minnesota Timberwolves": "MIN",
    "New Orleans Pelicans": "NOP",
    "New York Knicks": "NYK",
    "Oklahoma City Thunder": "OKC",
    "Orlando Magic": "ORL",
    "Philadelphia 76ers": "PHI",
    "Phoenix Suns": "PHO",
    "Portland Trail Blazers": "POR",
    "Sacramento Kings": "SAC",
    "San Antonio Spurs": "SAS",
    "Toronto Raptors": "TOR",
    "Utah Jazz": "UTA",
    "Washington Wizards": "WAS",
}

nba_headers = [
    "Game#",
    "Date",
    "Start",
    "Empty",
    "Boxscore",
    "HomeOrAway",
    "Opponent",
    "Result",
    "OT",
    "PointsFor",
    "PointsAgainst",
    "RecordW",
    "RecordL",
    "Streak",
    "Notes",
]

wnba_teams = {
    "Chicago Sky": "CHI",
    "Connecticut Sun": "CON",
    "Washington Mystics": "WAS",
    "Atlanta Dream": "ATL",
    "New York Liberty": "NYL",
    "Indiana Fever": "IND",
    "Las Vegas Aces": "LVA",
    "Seattle Storm": "SEA",
    "Los Angeles Sparks": "LAS",
    "Phoenix Mercury": "PHO",
    "Dallas Wings": "DAL",
    "Minnesota Lynx": "MIN",
}

wnba_headers = [
    "Game#",
    "Date",
    "HomeOrAway",
    "Opponent",
    "Result",
    "PointsFor",
    "PointsAgainst",
    "Wins",
    "Losses",
    "Streak",
]

nhl_teams = {
    "Seattle Kraken": "SEA",
    "Vegas Golden Knights": "VEG",
    "Columbus Blue Jackets": "CBJ",
    "Minnesota Wild": "MIN",
    "Winnipeg Jets": "WPG",
    "Nashville Predators": "NSH",
    "Anaheim Ducks": "ANA",
    "Florida Panthers": "FLA",
    "Ottawa Senators": "OTT",
    "Tampa Bay Lightning": "TBL",
    "San Jose Sharks": "SJS",
    "Arizona Coyotes": "ARI",
    "Carolina Hurricanes": "CAR",
    "Colorado Avalanche": "COL",
    "Edmonton Oilers": "EDM",
    "New Jersey Devils": "NJD",
    "Washington Capitals": "WSH",
    "Calgary Flames": "CGY",
    "New York Islanders": "NYI",
    "Buffalo Sabres": "BUF",
    "Vancouver Canucks": "VAN",
    "Dallas Stars": "DAL",
    "Los Angeles Kings": "LAK",
    "Philadelphia Flyers": "PHI",
    "Pittsburgh Penguins": "PIT",
    "St. Louis Blues": "STL",
    "Chicago Blackhawks": "CHI",
    "Detroit Red Wings": "DET",
    "New York Rangers": "NYR",
    "Boston Bruins": "BOS",
    "Montreal Canadiens": "MTL",
    "Toronto Maple Leafs": "TOR",
}

nhl_headers = [
    "Game#",
    "Date",
    "HomeOrAway",
    "Opponent",
    "PointsFor",
    "PointsAgainst",
    "Result",
    "Overtime",
    "Wins",
    "Losses",
    "OvertimeLosses",
    "Streak",
    "Attendance",
    "LengthOfGame",
    "Notes",
]

ncaam_teams = {
    "Bellarmine": "bellarmine",
    "Tarleton State": "tarleton-state",
    "UC San Diego": "california-san-diego",
    "St. Thomas (MN)": "st-thomas-mn",
    "Dixie State": "dixie-state",
    "Kentucky": "kentucky",
    "Duke": "duke",
    "Kansas": "kansas",
    "North Carolina": "north-carolina",
    "UCLA": "ucla",
    "Indiana": "indiana",
    "Louisville": "louisville",
    "Illinois": "illinois",
    "Purdue": "purdue",
    "Ohio State": "ohio-state",
    "Michigan State": "michigan-state",
    "Cincinnati": "cincinnati",
    "Iowa": "iowa",
    "Michigan": "michigan",
    "NC State": "north-carolina-state",
    "Villanova": "villanova",
    "Kansas State": "kansas-state",
    "Maryland": "maryland",
    "Notre Dame": "notre-dame",
    "Minnesota": "minnesota",
    "Syracuse": "syracuse",
    "Oklahoma": "oklahoma",
    "Arizona": "arizona",
    "Nevada-Las Vegas": "nevada-las-vegas",
    "Marquette": "marquette",
    "Memphis": "memphis",
    "Oklahoma State": "oklahoma-state",
    "Wisconsin": "wisconsin",
    "Missouri": "missouri",
    "Tennessee": "tennessee",
    "St. John's (NY)": "st-johns-ny",
    "Vanderbilt": "vanderbilt",
    "Utah": "utah",
    "Southern California": "southern-california",
    "Florida": "florida",
    "Wake Forest": "wake-forest",
    "Stanford": "stanford",
    "Brigham Young": "brigham-young",
    "Arkansas": "arkansas",
    "Florida State": "florida-state",
    "Providence": "providence",
    "Alabama": "alabama",
    "Washington": "washington",
    "West Virginia": "west-virginia",
    "Dayton": "dayton",
    "California": "california",
    "Virginia": "virginia",
    "Iowa State": "iowa-state",
    "Georgetown": "georgetown",
    "Connecticut": "connecticut",
    "Texas": "texas",
    "UAB": "alabama-birmingham",
    "Temple": "temple",
    "Oregon": "oregon",
    "Houston": "houston",
    "DePaul": "depaul",
    "Wichita State": "wichita-state",
    "Oregon State": "oregon-state",
    "Louisiana State": "louisiana-state",
    "Xavier": "xavier",
    "Auburn": "auburn",
    "Nebraska": "nebraska",
    "Georgia Tech": "georgia-tech",
    "Clemson": "clemson",
    "Virginia Commonwealth": "virginia-commonwealth",
    "Colorado": "colorado",
    "Pittsburgh": "pittsburgh",
    "Saint Louis": "saint-louis",
    "Tulsa Golden": "tulsa",
    "Arizona State": "arizona-state",
    "Texas Tech": "texas-tech",
    "Bradley": "bradley",
    "Mississippi State": "mississippi-state",
    "Missouri State": "missouri-state",
    "South Carolina": "south-carolina",
    "Virginia Tech": "virginia-tech",
    "Utah State": "utah-state",
    "Creighton": "creighton",
    "San Diego State": "san-diego-state",
    "Gonzaga": "gonzaga",
    "Georgia": "georgia",
    "Seton Hall": "seton-hall",
    "New Mexico": "new-mexico",
    "Saint Joseph's": "saint-josephs",
    "Northwestern": "northwestern",
    "Illinois State": "illinois-state",
    "Western Kentucky": "western-kentucky",
    "Miami (FL)": "miami-fl",
    "Washington State": "washington-state",
    "Charlotte": "charlotte",
    "Boston College": "boston-college",
    "Old Dominion": "old-dominion",
    "Colorado State": "colorado-state",
    "Wyoming": "wyoming",
    "Southern Methodist": "southern-methodist",
    "Mississippi": "mississippi",
    "Penn State": "penn-state",
    "UTEP": "texas-el-paso",
    "Southern Illinois": "southern-illinois",
    "La Salle": "la-salle",
    "San Francisco": "san-francisco",
    "Texas A&M": "texas-am",
    "Fresno State": "fresno-state",
    "South Dakota State": "south-dakota-state",
    "St. Bonaventure": "st-bonaventure",
    "Baylor": "baylor",
    "Miami (OH)": "miami-oh",
    "Duquesne": "duquesne",
    "Butler": "butler",
    "Hawaii": "hawaii",
    "Belmont": "belmont",
    "Santa Clara": "santa-clara",
    "Princeton": "princeton",
    "New Mexico State": "new-mexico-state",
    "Northern Iowa": "northern-iowa",
    "Drake": "drake",
    "South Florida": "south-florida",
    "Toledo": "toledo",
    "Seattle": "seattle",
    "College of Charleston": "college-of-charleston",
    "Evansville": "evansville",
    "Long Beach State": "long-beach-state",
    "Massachusetts": "massachusetts",
    "Boise State": "boise-state",
    "Ohio": "ohio",
    "Nevada": "nevada",
    "Louisiana": "louisiana-lafayette",
    "Oral Roberts": "oral-roberts",
    "TCU": "texas-christian",
    "Loyola (IL)": "loyola-il",
    "Weber State": "weber-state",
    "Southern Mississippi": "southern-mississippi",
    "Pennsylvania": "pennsylvania",
    "Louisiana Tech": "louisiana-tech",
    "George Washington": "george-washington",
    "Grand Canyon": "grand-canyon",
    "Detroit Mercy": "detroit-mercy",
    "North Dakota State": "north-dakota-state",
    "Akron": "akron",
    "UC Santa Barbara": "california-santa-barbara",
    "Indiana State": "indiana-state",
    "Murray State": "murray-state",
    "San Diego": "san-diego",
    "Bowling Green State": "bowling-green-state",
    "Rutgers": "rutgers",
    "Saint Mary's (CA)": "saint-marys-ca",
    "Rhode Island": "rhode-island",
    "Marshall": "marshall",
    "South Alabama": "south-alabama",
    "Tulane": "tulane",
    "Ball State": "ball-state",
    "Green Bay": "green-bay",
    "George Mason": "george-mason",
    "Pacific": "pacific",
    "UC Irvine": "california-irvine",
    "Wright State": "wright-state",
    "Oakland": "oakland",
    "Richmond": "richmond",
    "Kent State": "kent-state",
    "Cal State Fullerton": "cal-state-fullerton",
    "Pepperdine": "pepperdine",
    "Chattanooga": "chattanooga",
    "Holy Cross": "holy-cross",
    "James Madison": "james-madison",
    "Montana": "montana",
    "New Orleans": "new-orleans",
    "Davidson": "davidson",
    "Fordham": "fordham",
    "Air Force": "air-force",
    "UNC Wilmington": "north-carolina-wilmington",
    "Western Michigan": "western-michigan",
    "Niagara": "niagara",
    "Florida Gulf Coast": "florida-gulf-coast",
    "Illinois-Chicago": "illinois-chicago",
    "Northern Kentucky": "northern-kentucky",
    "Rice": "rice",
    "Eastern Michigan": "eastern-michigan",
    "Drexel": "drexel",
    "Little Rock": "arkansas-little-rock",
    "Cleveland State": "cleveland-state",
    "Central Florida": "central-florida",
    "Manhattan": "manhattan",
    "Arkansas State": "arkansas-state",
    "California Baptist": "california-baptist",
    "Jacksonville": "jacksonville",
    "Canisius": "canisius",
    "Middle Tennessee": "middle-tennessee",
    "Iona": "iona",
    "East Tennessee State": "east-tennessee-state",
    "Loyola Marymount": "loyola-marymount",
    "Northern Colorado": "northern-colorado",
    "Valparaiso": "valparaiso",
    "Siena": "siena",
    "Denver": "denver",
    "Northern Illinois": "northern-illinois",
    "Central Michigan": "central-michigan",
    "Milwaukee": "milwaukee",
    "South Dakota": "south-dakota",
    "San Jose State": "san-jose-state",
    "Buffalo": "buffalo",
    "Idaho": "idaho",
    "Northeastern": "northeastern",
    "North Texas": "north-texas",
    "Fairfield": "fairfield",
    "East Carolina": "east-carolina",
    "Wofford": "wofford",
    "Eastern Kentucky": "eastern-kentucky",
    "Cal State Bakersfield": "cal-state-bakersfield",
    "Navy": "navy",
    "Louisiana-Monroe": "louisiana-monroe",
    "Saint Peter's": "saint-peters",
    "Lamar": "lamar",
    "Montana State": "montana-state",
    "Portland": "portland",
    "Stephen F. Austin": "stephen-f-austin",
    "Utah Valley": "utah-valley",
    "Austin Peay": "austin-peay",
    "William & Mary": "william-mary",
    "Lipscomb": "lipscomb",
    "Morehead State": "morehead-state",
    "Cal State Northridge": "cal-state-northridge",
    "Hofstra": "hofstra",
    "American": "american",
    "Appalachian State": "appalachian-state",
    "Furman": "furman",
    "Eastern Washington": "eastern-washington",
    "UTSA": "texas-san-antonio",
    "UNC Greensboro": "north-carolina-greensboro",
    "Portland State": "portland-state",
    "UC Davis": "california-davis",
    "North Florida": "north-florida",
    "IUPUI": "iupui",
    "Stony Brook": "stony-brook",
    "Yale": "yale",
    "Purdue-Fort Wayne": "ipfw",
    "Idaho State": "idaho-state",
    "Boston University": "boston-university",
    "Georgia Southern": "georgia-southern",
    "Tennessee Tech": "tennessee-tech",
    "Sam Houston State": "sam-houston-state",
    "Texas A&M-Corpus Christi": "texas-am-corpus-christi",
    "Albany (NY)": "albany-ny",
    "Kansas City": "missouri-kansas-city",
    "Georgia State": "georgia-state",
    "Southern Utah": "southern-utah",
    "Winthrop": "winthrop",
    "Cal Poly": "cal-poly",
    "Omaha": "nebraska-omaha",
    "Marist": "marist",
    "Rider": "rider",
    "McNeese State": "mcneese-state",
    "UC Riverside": "california-riverside",
    "Troy": "troy",
    "Towson": "towson",
    "Mercer": "mercer",
    "Gardner-Webb": "gardner-webb",
    "Monmouth": "monmouth",
    "Cornell": "cornell",
    "Coastal Carolina": "coastal-carolina",
    "Columbia": "columbia",
    "Eastern Illinois": "eastern-illinois",
    "Texas State": "texas-state",
    "UT Arlington": "texas-arlington",
    "North Carolina Central": "north-carolina-central",
    "Florida International": "florida-international",
    "Harvard": "harvard",
    "Lafayette": "lafayette",
    "Northern Arizona": "northern-arizona",
    "Quinnipiac": "quinnipiac",
    "Elon": "elon",
    "Stetson": "stetson",
    "Bucknell": "bucknell",
    "Delaware": "delaware",
    "Texas-Rio Grande Valley": "texas-pan-american",
    "Youngstown State": "youngstown-state",
    "Abilene Christian": "abilene-christian",
    "Florida Atlantic": "florida-atlantic",
    "Western Carolina": "western-carolina",
    "North Dakota": "north-dakota",
    "Western Illinois": "western-illinois",
    "Tennessee State": "tennessee-state",
    "Jacksonville State": "jacksonville-state",
    "Southeast Missouri State": "southeast-missouri-state",
    "Hartford": "hartford",
    "Radford": "radford",
    "Loyola (MD)": "loyola-md",
    "Robert Morris": "robert-morris",
    "Merrimack": "merrimack",
    "Samford": "samford",
    "Liberty": "liberty",
    "Army": "army",
    "Mount St. Mary's": "mount-st-marys",
    "Long Island University": "long-island-university",
    "High Point": "high-point",
    "South Carolina Upstate": "south-carolina-upstate",
    "Saint Francis (PA)": "saint-francis-pa",
    "Hampton": "hampton",
    "Wagner": "wagner",
    "UNC Asheville": "north-carolina-asheville",
    "Vermont": "vermont",
    "Massachusetts-Lowell": "massachusetts-lowell",
    "Bryant": "bryant",
    "NJIT": "njit",
    "Northwestern State": "northwestern-state",
    "Fairleigh Dickinson": "fairleigh-dickinson",
    "Southern": "southern",
    "Texas Southern": "texas-southern",
    "North Alabama": "north-alabama",
    "Colgate": "colgate",
    "Dartmouth": "dartmouth",
    "Brown": "brown",
    "Norfolk State": "norfolk-state",
    "Maryland-Baltimore County": "maryland-baltimore-county",
    "Coppin State": "coppin-state",
    "Southeastern Louisiana": "southeastern-louisiana",
    "Sacred Heart": "sacred-heart",
    "Jackson State": "jackson-state",
    "Binghamton": "binghamton",
    "Tennessee-Martin": "tennessee-martin",
    "St. Francis (NY)": "st-francis-ny",
    "Nicholls State": "nicholls-state",
    "Houston Baptist": "houston-baptist",
    "Sacramento State": "sacramento-state",
    "Campbell": "campbell",
    "Maine": "maine",
    "North Carolina A&T": "north-carolina-at",
    "Virginia Military Institute": "virginia-military-institute",
    "Southern Illinois-Edwardsville": "southern-illinois-edwardsville",
    "The Citadel": "citadel",
    "Central Connecticut State": "central-connecticut-state",
    "Lehigh Mountain": "lehigh",
    "Alabama State": "alabama-state",
    "Kennesaw State": "kennesaw-state",
    "Charleston Southern": "charleston-southern",
    "Presbyterian": "presbyterian",
    "South Carolina State": "south-carolina-state",
    "Alcorn State": "alcorn-state",
    "Incarnate Word": "incarnate-word",
    "Central Arkansas": "central-arkansas",
    "Longwood": "longwood",
    "New Hampshire": "new-hampshire",
    "Mississippi Valley State": "mississippi-valley-state",
    "Howard": "howard",
    "Morgan State": "morgan-state",
    "Florida A&M": "florida-am",
    "Chicago State": "chicago-state",
    "Bethune-Cookman": "bethune-cookman",
    "Delaware State": "delaware-state",
    "Alabama A&M": "alabama-am",
    "Grambling": "grambling",
    "Arkansas-Pine Bluff": "arkansas-pine-bluff",
    "Maryland-Eastern Shore": "maryland-eastern-shore",
    "Prairie View": "prairie-view",
}

ncaam_headers = [
    "Game#",
    "Date",
    "Time",
    "Type",
    "HomeOrAway",
    "Opponent",
    "Conference",
    "Result",
    "PointsFor",
    "PointsAgainst",
    "Overtime",
    "Wins",
    "Losses",
    "Streak",
    "Arena",
]

ncaaw_teams = {}

ncaaw_headers = []

mls_teams = {}

mls_headers = []

nwsl_teams = {}

nwsl_headers = []

# "https://www.sports-reference.com/cbb/schools/{team_name}/{year}-schedule.html"


config_info = {
    "mlb": {
        "url_base": "https://www.baseball-reference.com/teams/{team_name}/{year}-schedule-scores.shtml",
        "expon": 1.83,
        "headers": mlb_headers,
        "teams": mlb_teams,
        "header_rows": [0],
        "html_table": -1,
    },
    "nba": {
        "url_base": "https://www.basketball-reference.com/teams/{team_name}/{year}_games.html",
        "expon": 13.91,
        "headers": nba_headers,
        "teams": nba_teams,
        "header_rows": [0],
        "html_table": 0,
    },
    "wnba": {
        "url_base": "https://www.basketball-reference.com/wnba/teams/{team_name}/{year}_games.html",
        "expon": 13.91,
        "headers": wnba_headers,
        "teams": wnba_teams,
        "header_rows": [0],
        "html_table": 0,
    },
    "nfl": {
        "url_base": "https://www.pro-football-reference.com/teams/{team_name}/{year}.htm",
        "expon": 2.37,
        "headers": nfl_headers,
        "teams": nfl_teams,
        "header_rows": [0, 1],
        "html_table": 1,
    },
    "ncaaf": {
        "url_base": "https://www.sports-reference.com/cfb/schools/{team_name}/{year}-schedule.html",
        "expon": 2.37,
        "headers": ncaaf_headers,
        "teams": ncaaf_teams,
        "header_rows": [0],
        "html_table": -1,
    },
    "nhl": {
        "url_base": "https://www.hockey-reference.com/teams/{team_name}/{year}_games.html",
        "expon": 2.15,
        "headers": nhl_headers,
        "teams": nhl_teams,
        "header_rows": [0],
        "html_table": -1,
    },
    "ncaam": {
        "url_base": "https://www.sports-reference.com/cbb/schools/{team_name}/{year}-schedule.html",
        "expon": 13.91,
        "headers": ncaam_headers,
        "teams": ncaam_teams,
        "header_rows": [0],
        "html_table": -1,
    },
}
