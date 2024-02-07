import math

# Les modules RSA n_alice et n_bob
n_alice = 93145558017597242451057840020003423492065036505715635939073421584870064178836557007438920905568366141278155363295217244442270120551665563816731464612225841456174904661719015967457696683736586858513914335501922092345895701281682242489324726462415020945038049322877151602626496388802926568113827098181488546541
n_bob = 130627775975870619265103967461863569685393719623259606834494161761353696231137838485596006850409649916631767658717771142397327842476766835551088514711108732237134464583834085414090472465465656901718533120526240047672780456483182231171430047581628792398849389571220237028177673312592572286345009761324975840273

# Calcul du PGCD
pgcd = math.gcd(n_alice, n_bob)

# Vérification si le PGCD est supérieur à 1
if pgcd > 1:
    # p est égal au PGCD
    p = pgcd

    # Diviser n_alice et n_bob par p pour obtenir q1 et q2
    q1 = n_alice // p
    q2 = n_bob // p

    print("Le facteur premier commun p est :", p)
    print("q1 (pour Alice) est :", q1)
    print("q2 (pour Bob) est :", q2)
else:
    print("Aucun facteur premier commun n'a été trouvé.")