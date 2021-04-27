import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# palette = sns.color_palette('Paired', 8)
# sns.set_palette(palette)
palette = sns.color_palette()

plt.rcParams["font.size"] = 17
plt.rcParams["axes.labelsize"] = 19
plt.rcParams["lines.markersize"] = 11
plt.rcParams["lines.linewidth"] = 4.0
plt.rcParams["legend.handlelength"] = 2.25
plt.rcParams["axes.grid"] = True
sns.set_style({"axes.spines.right": False, "axes.spines.top": False})

MARKER_NAMES_DICT = {
    "nc": "o",
    "pf": "*",
    "smore": "x",
    "fe": "^",
    "fp": "s",
    "pfws": "+",
    "pf-oracle": "d",
}


LINE_STYLES_DICT = {
    "nc": "-",
    "pf": "--",
    "smore": "-.",
    "fe": ":",
    "fp": "--",
    "pfws": "-.",
    "pf-oracle": ":",
}

COLOR_NAMES_DICT = {
    "nc": palette[0],
    "pf": palette[1],
    "smore": palette[2],
    "fe": palette[3],
    "fp": palette[4],
    "pfws": palette[9],
    "pf-oracle": palette[6],
}

LABEL_NAMES_DICT = {
    "nc": "NCFlow",
    "pf": "$\mathrm{PF}_4$",
    "pfws": "$\mathrm{PF}_{4{\sf w}}$",
    "pf-oracle": "Instant $\mathrm{PF}_4$",
    "smore": "SMORE",
    #'fe': 'Fleischer-Edge, $\epsilon = 0.5$',
    "fe": "Fleischer's Algorithm",
    "fp": "Fleischer-Path, $\epsilon = 0.5$",
}

PROBLEM_NAMES_DICT = {
    "AttMpls.graphml": "AttMpls",
    "Cogentco.graphml": "Cogentco",
    "Colt.graphml": "Colt",
    "Deltacom.graphml": "Deltacom",
    "DialtelecomCz.graphml": "DialtelecomCz",
    "GtsCe.graphml": "GtsCe",
    "Interoute.graphml": "Interoute",
    "Ion.graphml": "Ion",
    "Kdl.graphml": "Kdl",
    "TataNld.graphml": "TataNld",
    "UsCarrier.graphml": "UsCarrier",
    "Uninett2010.graphml": "Uninett2010",
    "msft-8075.json": "PrivateSmall",
    "one-wan-bidir.json": "PrivateLarge",
}

# TODO: this should be imported from benchmarks.benchmark_consts, but
# it causes a segmentation fault
PATH_FORM_HYPERPARAMS = (4, True, "inv-cap")
NCI_HYPERPARAMS = {
    "GtsCe.graphml": (4, True, "inv-cap", "fm_partitioning", 36.0),
    "UsCarrier.graphml": (4, True, "inv-cap", "fm_partitioning", 36.0),
    "Cogentco.graphml": (4, True, "inv-cap", "fm_partitioning", 42.0),
    "Colt.graphml": (4, True, "inv-cap", "fm_partitioning", 36.0),
    "TataNld.graphml": (4, True, "inv-cap", "fm_partitioning", 36.0),
    "Deltacom.graphml": (4, True, "inv-cap", "fm_partitioning", 30.0),
    "DialtelecomCz.graphml": (4, True, "inv-cap", "fm_partitioning", 33.0),
    "Uninett2010.graphml": (4, True, "inv-cap", "fm_partitioning", 24.0),
    "Interoute.graphml": (4, True, "inv-cap", "spectral_clustering", 20.0),
    "Ion.graphml": (4, True, "inv-cap", "fm_partitioning", 33.0),
    "msft-8075.json": (4, True, "inv-cap", "fm_partitioning", 42.0),
    "Kdl.graphml": (4, True, "inv-cap", "fm_partitioning", 81.0),
    "one-wan-bidir.json": (4, True, "inv-cap", "fm_partitioning", 31.0),
}
SMORE_HYPERPARAMS = 4


def save_figure(filename, extra_artists=None, tight=True, ext=".pdf"):
    filename = filename.replace(".", "-")
    filename += ext
    if extra_artists:
        if ext == ".png":
            if tight:
                plt.tight_layout()
            plt.savefig(
                filename,
                bbox_extra_artists=extra_artists,
                bbox_inches="tight",
                transparent=True,
            )
        else:
            if tight:
                plt.tight_layout()
            plt.savefig(filename, bbox_extra_artists=extra_artists, bbox_inches="tight")
    else:
        if tight:
            plt.tight_layout()
        if ext == ".png":
            plt.savefig(filename, transparent=True)
        else:
            plt.savefig(filename)


POISSON_HIGH_INTRA = set(
    [
        1002931420,
        1003544367,
        1007510484,
        1011993125,
        1015885682,
        1019158999,
        1021533148,
        1021894572,
        1022383118,
        1025088167,
        1032633174,
        1033170170,
        1033313530,
        1034066240,
        1036345481,
        1038093168,
        1038492235,
        1042565974,
        1042638461,
        1045673165,
        1049066647,
        1050463301,
        1050547667,
        1054314477,
        1055550134,
        1058989507,
        105962599,
        1061024865,
        1062186554,
        1067709734,
        1069460682,
        1071487659,
        1073063731,
        1079049780,
        1080562725,
        1082014999,
        1082657135,
        1085112592,
        1089022695,
        1093097496,
        1097464667,
        109777138,
        1100381358,
        1101444395,
        1102254649,
        1106519384,
        1107391624,
        1110454223,
        111046807,
        112056917,
        112435160,
        1125808873,
        112729686,
        1127535847,
        113188206,
        1135833945,
        1137569267,
        1144433792,
        1145557794,
        1146817059,
        1149123775,
        1149913654,
        1150691397,
        1153039731,
        1154717281,
        1155638621,
        1158533055,
        1159341176,
        1172428746,
        1172507251,
        1175120150,
        1175375784,
        1179616255,
        1188681870,
        1189583644,
        1190847892,
        1196923204,
        1205288297,
        12054572,
        1218360499,
        12186945,
        1222029913,
        1224807907,
        1226838406,
        1228117678,
        1228227765,
        1232066967,
        1238195151,
        1238890617,
        1240494465,
        124151864,
        1243630499,
        1249833039,
        1251410255,
        1256218318,
        1258701445,
        1261820024,
        1263989187,
        1264644244,
        12686533,
        127271115,
        1274978453,
        1278613659,
        1281112752,
        1285067027,
        1295203664,
        1300289033,
        1300591861,
        1303852474,
        1305281104,
        1307779861,
        1312327694,
        1315123963,
        1317749462,
        1322107138,
        1328770710,
        1331273334,
        1338487316,
        1339063684,
        1339955285,
        1341798177,
        1345169058,
        1348472415,
        1355098143,
        1357975221,
        1360150725,
        136212320,
        1367122618,
        1367969278,
        1371218786,
        1387987552,
        138976,
        1393991705,
        1397879277,
        1400199617,
        1401335476,
        1414806121,
        14200283,
        1425803190,
        1426689663,
        1435832918,
        143622066,
        1436882959,
        1447519106,
        1449057126,
        1449357265,
        145379456,
        145429002,
        1458651690,
        1470391217,
        1470965366,
        1472447487,
        1477228679,
        1477287172,
        1480195529,
        1480899410,
        1492342640,
        1525703876,
        1529720562,
        1539952746,
        155651259,
        1559345129,
        156393036,
        1565600716,
        1566620452,
        1572671302,
        157365495,
        1576230634,
        1577136507,
        1585509162,
        1586957041,
        1589731348,
        1592195407,
        1593050004,
        1594521824,
        1596242378,
        1599732338,
        1603704828,
        1615967756,
        1617947158,
        1619772163,
        163652842,
        1645273719,
        1649918355,
        1663049590,
        1665220802,
        1672169014,
        1676458720,
        1682307307,
        1685565187,
        1685738665,
        1686367964,
        1686874698,
        1700967992,
        1702715061,
        1710997455,
        1711543621,
        1712887538,
        1721804299,
        1733633080,
        1737159786,
        1738164271,
        1742051311,
        1748306513,
        1752869944,
        1754261003,
        1758448648,
        1761527370,
        1764935867,
        1766667804,
        1771706265,
        1772123042,
        1773116991,
        1774811707,
        1776689782,
        1777320387,
        1777560748,
        1791652155,
        1793424251,
        1795526148,
        1796336846,
        1798413854,
        1803472122,
        180370087,
        1808532206,
        181259577,
        1821938788,
        1823958742,
        1823986426,
        1826611136,
        1826972742,
        1827392369,
        1840038819,
        1841473521,
        1849081370,
        1853261743,
        1855883284,
        1857227358,
        1866184501,
        1872295673,
        1872498839,
        1876248036,
        1876700047,
        1880272062,
        188073448,
        1881393215,
        1886669028,
        1905349082,
        1905801619,
        1908745180,
        1912932602,
        1913798584,
        19143788,
        191740532,
        1918450001,
        1921615116,
        1924161815,
        193065792,
        1931835019,
        1934157648,
        1938444629,
        1945077275,
        1948266490,
        1959922915,
        196489953,
        1967163961,
        1969840077,
        1975840851,
        197821998,
        1984419778,
        1986346842,
        1986469865,
        1988329396,
        1991505716,
        2007519458,
        2007856936,
        2019696542,
        2025106663,
        2026088488,
        2028106250,
        2029701573,
        2031508820,
        2042157777,
        2042653758,
        2046117136,
        2050044787,
        2051675095,
        2056659174,
        2057224701,
        2063242091,
        2066203998,
        2074852194,
        2075712807,
        2082893782,
        20885368,
        2092593095,
        2097523677,
        2098474194,
        2101667180,
        2102502064,
        2103651850,
        2106624845,
        2106704319,
        2107114367,
        2108839184,
        2117473788,
        2118039675,
        2122039067,
        2122910556,
        2125082318,
        2129968268,
        2134270066,
        2134340254,
        2138223900,
        2138770918,
        2141470671,
        2145497975,
        222783850,
        227304644,
        231874905,
        241511213,
        241705948,
        242095915,
        243298086,
        247238164,
        250449194,
        251744525,
        253195552,
        254885041,
        2624916,
        262837270,
        270938292,
        274353361,
        279878188,
        280269550,
        284603353,
        292353693,
        292512017,
        295250739,
        30109003,
        301718092,
        305884540,
        326133639,
        331503324,
        334458675,
        335635440,
        337919928,
        342280625,
        342531836,
        343193664,
        359033500,
        36734755,
        379215465,
        380385976,
        384165115,
        386936791,
        395536091,
        399443329,
        401515162,
        404708338,
        410352520,
        413750282,
        414543227,
        416055854,
        416711229,
        427668966,
        431897711,
        432406464,
        434791799,
        435269991,
        43563071,
        435929582,
        441581426,
        444740338,
        449857954,
        454732957,
        464913731,
        471335891,
        473581428,
        473632137,
        476970525,
        477363648,
        488059214,
        490925185,
        492248441,
        495639730,
        500021415,
        500428956,
        502409491,
        504155744,
        507827707,
        509075389,
        512285539,
        51349962,
        529831180,
        531800598,
        532877070,
        543747037,
        545758279,
        551776487,
        557147877,
        557261919,
        558924033,
        565206942,
        565728315,
        572347129,
        575046467,
        577089124,
        580391779,
        581143141,
        581796794,
        585568778,
        585783065,
        586322489,
        588046220,
        596686094,
        597679699,
        611079315,
        613698079,
        622085358,
        626455977,
        632211587,
        637634316,
        638392001,
        638904137,
        638922411,
        639810511,
        646065073,
        648632546,
        654173155,
        654787652,
        661753271,
        663466855,
        673863578,
        676476515,
        688368894,
        691630724,
        704719360,
        714168413,
        714954972,
        715397138,
        715947948,
        71756406,
        719974166,
        72065952,
        725838081,
        731818741,
        732032683,
        738104248,
        740846870,
        742629757,
        751755363,
        756112912,
        756629062,
        758637260,
        763605099,
        765423586,
        771670619,
        772127844,
        77363401,
        773660988,
        785052613,
        78611027,
        787817358,
        792530379,
        792575728,
        796504210,
        796732039,
        797177001,
        797274094,
        813727337,
        821433068,
        829974770,
        833372892,
        834654282,
        83576924,
        837392660,
        839546080,
        846444316,
        848192382,
        860640320,
        862703935,
        867158782,
        867830502,
        870260517,
        874800671,
        898083423,
        907101536,
        908836297,
        909696223,
        910273883,
        910313927,
        910638527,
        911888029,
        914449931,
        915070514,
        917747800,
        937219031,
        945943696,
        946847852,
        953015887,
        976223947,
        979144766,
        982334438,
        985092127,
        987491959,
        993438722,
        993897016,
    ]
)

POISSON_HIGH_INTER = set(
    [
        1011338330,
        101382938,
        1035695445,
        1035746292,
        104382396,
        1048517467,
        1051917258,
        1052377849,
        1052617384,
        1057970354,
        1059503539,
        1061595861,
        1068408805,
        1075641342,
        1082461213,
        1087014204,
        1087312007,
        1087564464,
        1091150716,
        1095193191,
        109801559,
        1098771085,
        1102269350,
        1105954826,
        1106233548,
        1108449992,
        1109860411,
        1113602095,
        1116586565,
        1121370383,
        1123942708,
        1124114946,
        1125445501,
        1125514555,
        1130417803,
        1134799086,
        113766835,
        1141540565,
        1143481924,
        1144845239,
        1153208586,
        1158352545,
        1164103636,
        1165451306,
        1168556047,
        1168726174,
        1171717505,
        1172243968,
        1175139186,
        1185923933,
        11863330,
        1188592100,
        1189264762,
        1192860264,
        1195140350,
        1196212852,
        1196909975,
        1200184678,
        120189501,
        1203873963,
        1211034344,
        1220129336,
        1226323835,
        1228027199,
        1228906045,
        12301708,
        1232271742,
        1233000047,
        1237153255,
        1239489459,
        1249101529,
        1252172072,
        1255092240,
        1256686325,
        1266761171,
        1266841991,
        1275811472,
        1282526031,
        1288133334,
        1288694355,
        1289161728,
        1291225773,
        1296637462,
        1302925072,
        130479128,
        1313216986,
        1313388181,
        1317974376,
        1318011676,
        132828506,
        1328474713,
        133137047,
        1333812558,
        1336782856,
        1336992439,
        1341317936,
        1341427862,
        1344514302,
        13466461,
        1346843764,
        1353382228,
        1360186100,
        1363618620,
        1363727071,
        1379764409,
        1384571556,
        1386462693,
        1391425892,
        1400141081,
        1400727102,
        1406802175,
        1408091073,
        141164578,
        1412474423,
        1423134657,
        143002740,
        1436200825,
        1443340436,
        1446428659,
        1449623635,
        1451850708,
        1454829579,
        1459981827,
        1461046291,
        1468800279,
        1469409279,
        1470495283,
        1483102118,
        1485723312,
        1486650207,
        1497988131,
        1498097623,
        1506113288,
        1508133469,
        1525999001,
        1527903593,
        1530883616,
        1533110410,
        1538824632,
        1540335938,
        1543216432,
        1547553653,
        1557206717,
        1561772761,
        1565745910,
        1566077844,
        1573140806,
        1582092201,
        1582282039,
        1582479584,
        1588211110,
        1591671513,
        1592994282,
        1600030150,
        1601745368,
        1604097841,
        1614948515,
        1616765395,
        1618377143,
        1618479832,
        1619947957,
        1620381080,
        1626954996,
        1633210612,
        1640571417,
        1641825716,
        1642256467,
        1647893671,
        1671857184,
        167254480,
        1675246932,
        1676508722,
        1685312171,
        1685911815,
        168645232,
        1690273086,
        169043057,
        1690751249,
        1694129634,
        1694948951,
        1705137037,
        1708264619,
        1708951837,
        1712264344,
        1714847716,
        1717122791,
        1723825483,
        1724228606,
        1724363866,
        172562938,
        1729695939,
        1729788451,
        173164146,
        1733297565,
        1733469710,
        1736341861,
        1737725365,
        1742078690,
        1742241093,
        1743461466,
        1745949401,
        174835392,
        1752256466,
        1755648162,
        1755951733,
        1758646282,
        1762404741,
        1777218028,
        1778035043,
        1778203363,
        1785268493,
        1786313756,
        1788112198,
        179035290,
        1795053320,
        1796366340,
        1802404217,
        1810642229,
        181646178,
        1818593123,
        1821165905,
        1823525419,
        1828212552,
        1832877504,
        1833822262,
        1834455766,
        1844213203,
        1845405959,
        1845449925,
        1846813542,
        1846849502,
        1850624489,
        1852243799,
        1855819565,
        1857279712,
        1858163378,
        1861675654,
        1863891015,
        186863027,
        187252379,
        187590413,
        1886672008,
        1888745795,
        1894258982,
        1895823572,
        1896072550,
        1898106156,
        1909927562,
        1914148387,
        1925784455,
        1930002159,
        1931102819,
        1943020180,
        1944932416,
        1947419052,
        1952600322,
        1957329812,
        1957383362,
        1957729114,
        1958207939,
        1960200664,
        1967936237,
        1968499152,
        1977660080,
        1978589222,
        1983480209,
        1983719917,
        1985286667,
        1986708651,
        1993786805,
        1997347413,
        2002134059,
        2003719375,
        2008515142,
        2013435223,
        2019177111,
        2020130301,
        2035531455,
        2036592032,
        203835177,
        2054670548,
        205674050,
        2057545803,
        2059009494,
        205942148,
        2062049084,
        2067061299,
        2072714296,
        2072735175,
        208092658,
        2089696249,
        209339453,
        2097237814,
        2099728541,
        2114300095,
        2114770191,
        2117162007,
        2123473059,
        2123777862,
        2125639104,
        2129612982,
        2131166144,
        2146920679,
        219098099,
        219388368,
        220154671,
        221671510,
        22217080,
        22544623,
        226869488,
        229221089,
        241774435,
        242322788,
        24311218,
        248972077,
        255865383,
        266453373,
        269738721,
        270902597,
        271284790,
        273182008,
        27622304,
        283998076,
        287220969,
        287889795,
        298472283,
        30115925,
        307277143,
        30894293,
        310877990,
        313736226,
        321366202,
        3246708,
        326007689,
        328566660,
        329065179,
        333257346,
        333347046,
        33893777,
        339227343,
        343558094,
        344581029,
        345998781,
        34680347,
        347931167,
        350851643,
        351735224,
        352643540,
        354395183,
        362625067,
        367548193,
        368595621,
        370923790,
        386268953,
        392472174,
        392659891,
        396720268,
        402816275,
        404831256,
        423436714,
        425751729,
        425825684,
        428529914,
        43112753,
        431572985,
        432164199,
        43640132,
        437524940,
        440177831,
        449712512,
        452633592,
        465478956,
        479485660,
        480401927,
        481014765,
        483071560,
        483897406,
        491978366,
        496831792,
        498273744,
        499733992,
        503071114,
        511204666,
        511704445,
        513242937,
        51435200,
        51736697,
        518773330,
        521117367,
        52376180,
        539768726,
        540186284,
        544272035,
        544327153,
        545508392,
        549051130,
        55268184,
        554495792,
        55632909,
        561583798,
        562847718,
        578269764,
        584086235,
        585784232,
        585839857,
        589761608,
        589778868,
        597217382,
        600642615,
        60306504,
        603098036,
        608767531,
        608821270,
        614446626,
        614749082,
        61856004,
        618860969,
        623306622,
        633366117,
        633695223,
        640461,
        644981296,
        645040376,
        649506895,
        6510108,
        651039017,
        65254461,
        654127701,
        65691597,
        668782070,
        669629095,
        670447958,
        674611273,
        679861388,
        681317975,
        685549144,
        685590929,
        686672740,
        699882009,
        701759740,
        710106656,
        71212245,
        713190598,
        714023565,
        71743742,
        722447233,
        724455575,
        726114899,
        742618994,
        754694846,
        759298435,
        765479692,
        767253773,
        77066746,
        77094040,
        772387326,
        77815410,
        779667040,
        784848775,
        785970044,
        78920596,
        791562586,
        793186660,
        79382295,
        794082333,
        799447776,
        802603339,
        803813411,
        806873762,
        810046772,
        813884790,
        818548037,
        821401671,
        827391017,
        833977151,
        841119697,
        849149404,
        850549917,
        868043453,
        870540743,
        876000506,
        884158982,
        887688332,
        888579231,
        889867746,
        894439811,
        895190326,
        897078250,
        898315341,
        903101614,
        906165488,
        91263941,
        912709720,
        914167205,
        914304353,
        914753409,
        918227658,
        919593047,
        919679269,
        921622263,
        924791650,
        930541071,
        930904244,
        935592331,
        937761623,
        949885885,
        965306133,
        970533677,
        978869975,
        978911507,
        982754451,
        986298082,
        987366357,
        989765178,
        989843509,
        992220541,
        996494061,
        99719879,
        997398384,
        998126965,
    ]
)


def change_poisson_in_df(df):
    df["tm_model"] = df.apply(
        lambda row: "poisson-high-inter"
        if row["traffic_seed"] in POISSON_HIGH_INTER
        else row["tm_model"],
        axis=1,
    )
    df["tm_model"] = df.apply(
        lambda row: "poisson-high-intra"
        if row["traffic_seed"] in POISSON_HIGH_INTRA
        else row["tm_model"],
        axis=1,
    )
    return df


def filter_by_hyperparams(per_iter_fname):
    return (
        pd.read_csv(per_iter_fname)
        .groupby(["problem", "num_partitions"])
        .filter(lambda x: x.name[-1] == NCI_HYPERPARAMS[x.name[0]][-1])
    )
