from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from math import *


def caso_L():

    # Unidades base
    m = 1.
    kg = 1.
    s = 1.

    #Unidades derivadas
    N = kg*m/s**2
    cm = 0.01*m
    mm = 0.001*m
    KN = 1000*N

    Pa = N / m**2
    KPa = 1000*Pa
    MPa = 1000*KPa
    GPa = 1000*MPa

    # Parametros

    L = 5.0 * m
    H = 3.5 * m
    B = 2.0 * m


    #Inicializar modelo
    ret = Reticulado()

    # Nodos
    for i in range (45):
        ret.agregar_nodo((i+1)*L, 0, 100)
    
    for i in range (45):
        ret.agregar_nodo((i+1)*L, 2, 100)

    for i in range (44):
        ret.agregar_nodo((i+1.5)*L, 1, 105)

    for i in range (44):
        ret.agregar_nodo((i+1.5)*L, 1,  95)
        
        
    # Barras
    
    densidad=0 * kg / m ** 3


    ret.agregar_barra(Barra(0, 1, 0.6720124801383052, 0.6720124801383052, 200 * GPa, densidad, 420 * MPa))       #barra n:0 
    ret.agregar_barra(Barra(1, 2, 0.6637074080456902, 0.6637074080456902, 200 * GPa, densidad, 420 * MPa))       #barra n:1 
    ret.agregar_barra(Barra(2, 3, 0.645576163462744, 0.645576163462744, 200 * GPa, densidad, 420 * MPa))       #barra n:2 
    ret.agregar_barra(Barra(3, 4, 0.6366718704640282, 0.6366718704640282, 200 * GPa, densidad, 420 * MPa))       #barra n:3 
    ret.agregar_barra(Barra(4, 5, 0.6168206984495894, 0.6168206984495894, 200 * GPa, densidad, 420 * MPa))       #barra n:4 
    ret.agregar_barra(Barra(5, 6, 0.6067970150785404, 0.6067970150785404, 200 * GPa, densidad, 420 * MPa))       #barra n:5 
    ret.agregar_barra(Barra(6, 7, 0.5833581659723431, 0.5833581659723431, 200 * GPa, densidad, 420 * MPa))       #barra n:6 
    ret.agregar_barra(Barra(7, 8, 0.5705606522900702, 0.5705606522900702, 200 * GPa, densidad, 420 * MPa))       #barra n:7 
    ret.agregar_barra(Barra(8, 9, 0.5331192812605885, 0.5331192812605885, 200 * GPa, densidad, 420 * MPa))       #barra n:8 
    ret.agregar_barra(Barra(9, 10, 0.584315253496107, 0.584315253496107, 200 * GPa, densidad, 420 * MPa))       #barra n:9 
    ret.agregar_barra(Barra(10, 11, 0.5843153314875015, 0.5843153314875015, 200 * GPa, densidad, 420 * MPa))       #barra n:10 
    ret.agregar_barra(Barra(11, 12, 0.5843194564184347, 0.5843194564184347, 200 * GPa, densidad, 420 * MPa))       #barra n:11 
    ret.agregar_barra(Barra(12, 13, 0.5898116217918112, 0.5898116217918112, 200 * GPa, densidad, 420 * MPa))       #barra n:12 
    ret.agregar_barra(Barra(13, 14, 0.5960251228834739, 0.5960251228834739, 200 * GPa, densidad, 420 * MPa))       #barra n:13 
    ret.agregar_barra(Barra(14, 15, 0.6066651055625798, 0.6066651055625798, 200 * GPa, densidad, 420 * MPa))       #barra n:14 
    ret.agregar_barra(Barra(15, 16, 0.6107269059805381, 0.6107269059805381, 200 * GPa, densidad, 420 * MPa))       #barra n:15 
    ret.agregar_barra(Barra(16, 17, 0.6176518963901642, 0.6176518963901642, 200 * GPa, densidad, 420 * MPa))       #barra n:16 
    ret.agregar_barra(Barra(17, 18, 0.6202217874958968, 0.6202217874958968, 200 * GPa, densidad, 420 * MPa))       #barra n:17 
    ret.agregar_barra(Barra(18, 19, 0.6243370382763597, 0.6243370382763597, 200 * GPa, densidad, 420 * MPa))       #barra n:18 
    ret.agregar_barra(Barra(19, 20, 0.6256953244818959, 0.6256953244818959, 200 * GPa, densidad, 420 * MPa))       #barra n:19 
    ret.agregar_barra(Barra(20, 21, 0.6273995137229428, 0.6273995137229428, 200 * GPa, densidad, 420 * MPa))       #barra n:20 
    ret.agregar_barra(Barra(21, 22, 0.6276658022264625, 0.6276658022264625, 200 * GPa, densidad, 420 * MPa))       #barra n:21 
    ret.agregar_barra(Barra(22, 23, 0.6271014554703835, 0.6271014554703835, 200 * GPa, densidad, 420 * MPa))       #barra n:22 
    ret.agregar_barra(Barra(23, 24, 0.6262972968287162, 0.6262972968287162, 200 * GPa, densidad, 420 * MPa))       #barra n:23 
    ret.agregar_barra(Barra(24, 25, 0.6234185158977332, 0.6234185158977332, 200 * GPa, densidad, 420 * MPa))       #barra n:24 
    ret.agregar_barra(Barra(25, 26, 0.6214770129770574, 0.6214770129770574, 200 * GPa, densidad, 420 * MPa))       #barra n:25 
    ret.agregar_barra(Barra(26, 27, 0.6160288177080321, 0.6160288177080321, 200 * GPa, densidad, 420 * MPa))       #barra n:26 
    ret.agregar_barra(Barra(27, 28, 0.6127631488791601, 0.6127631488791601, 200 * GPa, densidad, 420 * MPa))       #barra n:27 
    ret.agregar_barra(Barra(28, 29, 0.6041462926618659, 0.6041462926618659, 200 * GPa, densidad, 420 * MPa))       #barra n:28 
    ret.agregar_barra(Barra(29, 30, 0.5991342417518205, 0.5991342417518205, 200 * GPa, densidad, 420 * MPa))       #barra n:29 
    ret.agregar_barra(Barra(30, 31, 0.5859268345980706, 0.5859268345980706, 200 * GPa, densidad, 420 * MPa))       #barra n:30 
    ret.agregar_barra(Barra(31, 32, 0.5843184279824556, 0.5843184279824556, 200 * GPa, densidad, 420 * MPa))       #barra n:31 
    ret.agregar_barra(Barra(32, 33, 0.5843160060505543, 0.5843160060505543, 200 * GPa, densidad, 420 * MPa))       #barra n:32 
    ret.agregar_barra(Barra(33, 34, 0.5843157900236934, 0.5843157900236934, 200 * GPa, densidad, 420 * MPa))       #barra n:33 
    ret.agregar_barra(Barra(34, 35, 0.5456400942106223, 0.5456400942106223, 200 * GPa, densidad, 420 * MPa))       #barra n:34 
    ret.agregar_barra(Barra(35, 36, 0.5625855618219139, 0.5625855618219139, 200 * GPa, densidad, 420 * MPa))       #barra n:35 
    ret.agregar_barra(Barra(36, 37, 0.5899245656156787, 0.5899245656156787, 200 * GPa, densidad, 420 * MPa))       #barra n:36 
    ret.agregar_barra(Barra(37, 38, 0.6009557014009079, 0.6009557014009079, 200 * GPa, densidad, 420 * MPa))       #barra n:37 
    ret.agregar_barra(Barra(38, 39, 0.6222154531105258, 0.6222154531105258, 200 * GPa, densidad, 420 * MPa))       #barra n:38 
    ret.agregar_barra(Barra(39, 40, 0.6315819830817686, 0.6315819830817686, 200 * GPa, densidad, 420 * MPa))       #barra n:39 
    ret.agregar_barra(Barra(40, 41, 0.6504407838359317, 0.6504407838359317, 200 * GPa, densidad, 420 * MPa))       #barra n:40 
    ret.agregar_barra(Barra(41, 42, 0.6589717634308686, 0.6589717634308686, 200 * GPa, densidad, 420 * MPa))       #barra n:41 
    ret.agregar_barra(Barra(42, 43, 0.6763226873926724, 0.6763226873926724, 200 * GPa, densidad, 420 * MPa))       #barra n:42 
    ret.agregar_barra(Barra(43, 44, 0.001, 0.001, 200 * GPa, densidad, 420 * MPa))       #barra n:43 
    ret.agregar_barra(Barra(45, 46, 0.6765475234215197, 0.6765475234215197, 200 * GPa, densidad, 420 * MPa))       #barra n:44 
    ret.agregar_barra(Barra(46, 47, 0.6589892476687838, 0.6589892476687838, 200 * GPa, densidad, 420 * MPa))       #barra n:45 
    ret.agregar_barra(Barra(47, 48, 0.650429536104532, 0.650429536104532, 200 * GPa, densidad, 420 * MPa))       #barra n:46 
    ret.agregar_barra(Barra(48, 49, 0.6315653114212866, 0.6315653114212866, 200 * GPa, densidad, 420 * MPa))       #barra n:47 
    ret.agregar_barra(Barra(49, 50, 0.6221970500759763, 0.6221970500759763, 200 * GPa, densidad, 420 * MPa))       #barra n:48 
    ret.agregar_barra(Barra(50, 51, 0.6009333969295694, 0.6009333969295694, 200 * GPa, densidad, 420 * MPa))       #barra n:49 
    ret.agregar_barra(Barra(51, 52, 0.5898995336220341, 0.5898995336220341, 200 * GPa, densidad, 420 * MPa))       #barra n:50 
    ret.agregar_barra(Barra(52, 53, 0.5843159613555925, 0.5843159613555925, 200 * GPa, densidad, 420 * MPa))       #barra n:51 
    ret.agregar_barra(Barra(53, 54, 0.5843168001546075, 0.5843168001546075, 200 * GPa, densidad, 420 * MPa))       #barra n:52 
    ret.agregar_barra(Barra(54, 55, 0.5389338330162916, 0.5389338330162916, 200 * GPa, densidad, 420 * MPa))       #barra n:53 
    ret.agregar_barra(Barra(55, 56, 0.5554804548473137, 0.5554804548473137, 200 * GPa, densidad, 420 * MPa))       #barra n:54 
    ret.agregar_barra(Barra(56, 57, 0.578085531732916, 0.578085531732916, 200 * GPa, densidad, 420 * MPa))       #barra n:55 
    ret.agregar_barra(Barra(57, 58, 0.5859528588778686, 0.5859528588778686, 200 * GPa, densidad, 420 * MPa))       #barra n:56 
    ret.agregar_barra(Barra(58, 59, 0.5991567681742629, 0.5991567681742629, 200 * GPa, densidad, 420 * MPa))       #barra n:57 
    ret.agregar_barra(Barra(59, 60, 0.6041677194907484, 0.6041677194907484, 200 * GPa, densidad, 420 * MPa))       #barra n:58 
    ret.agregar_barra(Barra(60, 61, 0.6127829116110618, 0.6127829116110618, 200 * GPa, densidad, 420 * MPa))       #barra n:59 
    ret.agregar_barra(Barra(61, 62, 0.6160480127076463, 0.6160480127076463, 200 * GPa, densidad, 420 * MPa))       #barra n:60 
    ret.agregar_barra(Barra(62, 63, 0.6214953145843505, 0.6214953145843505, 200 * GPa, densidad, 420 * MPa))       #barra n:61 
    ret.agregar_barra(Barra(63, 64, 0.6234365187570955, 0.6234365187570955, 200 * GPa, densidad, 420 * MPa))       #barra n:62 
    ret.agregar_barra(Barra(64, 65, 0.6263148683556885, 0.6263148683556885, 200 * GPa, densidad, 420 * MPa))       #barra n:63 
    ret.agregar_barra(Barra(65, 66, 0.6271189006276854, 0.6271189006276854, 200 * GPa, densidad, 420 * MPa))       #barra n:64 
    ret.agregar_barra(Barra(66, 67, 0.6276831488775234, 0.6276831488775234, 200 * GPa, densidad, 420 * MPa))       #barra n:65 
    ret.agregar_barra(Barra(67, 68, 0.6274168776469663, 0.6274168776469663, 200 * GPa, densidad, 420 * MPa))       #barra n:66 
    ret.agregar_barra(Barra(68, 69, 0.6257129009144822, 0.6257129009144822, 200 * GPa, densidad, 420 * MPa))       #barra n:67 
    ret.agregar_barra(Barra(69, 70, 0.6243547906527119, 0.6243547906527119, 200 * GPa, densidad, 420 * MPa))       #barra n:68 
    ret.agregar_barra(Barra(70, 71, 0.6202401231124366, 0.6202401231124366, 200 * GPa, densidad, 420 * MPa))       #barra n:69 
    ret.agregar_barra(Barra(71, 72, 0.617670616989012, 0.617670616989012, 200 * GPa, densidad, 420 * MPa))       #barra n:70 
    ret.agregar_barra(Barra(72, 73, 0.6107467686139805, 0.6107467686139805, 200 * GPa, densidad, 420 * MPa))       #barra n:71 
    ret.agregar_barra(Barra(73, 74, 0.6066857121737749, 0.6066857121737749, 200 * GPa, densidad, 420 * MPa))       #barra n:72 
    ret.agregar_barra(Barra(74, 75, 0.596047977927409, 0.596047977927409, 200 * GPa, densidad, 420 * MPa))       #barra n:73 
    ret.agregar_barra(Barra(75, 76, 0.5898360399986355, 0.5898360399986355, 200 * GPa, densidad, 420 * MPa))       #barra n:74 
    ret.agregar_barra(Barra(76, 77, 0.5730670104566955, 0.5730670104566955, 200 * GPa, densidad, 420 * MPa))       #barra n:75 
    ret.agregar_barra(Barra(77, 78, 0.5625491339544668, 0.5625491339544668, 200 * GPa, densidad, 420 * MPa))       #barra n:76 
    ret.agregar_barra(Barra(78, 79, 0.5246082908155042, 0.5246082908155042, 200 * GPa, densidad, 420 * MPa))       #barra n:77 
    ret.agregar_barra(Barra(79, 80, 0.5843179337224761, 0.5843179337224761, 200 * GPa, densidad, 420 * MPa))       #barra n:78 
    ret.agregar_barra(Barra(80, 81, 0.5843146773874471, 0.5843146773874471, 200 * GPa, densidad, 420 * MPa))       #barra n:79 
    ret.agregar_barra(Barra(81, 82, 0.5843151048345461, 0.5843151048345461, 200 * GPa, densidad, 420 * MPa))       #barra n:80 
    ret.agregar_barra(Barra(82, 83, 0.6067766505240125, 0.6067766505240125, 200 * GPa, densidad, 420 * MPa))       #barra n:81 
    ret.agregar_barra(Barra(83, 84, 0.6168021419239091, 0.6168021419239091, 200 * GPa, densidad, 420 * MPa))       #barra n:82 
    ret.agregar_barra(Barra(84, 85, 0.6366564497294276, 0.6366564497294276, 200 * GPa, densidad, 420 * MPa))       #barra n:83 
    ret.agregar_barra(Barra(85, 86, 0.6455651630155954, 0.6455651630155954, 200 * GPa, densidad, 420 * MPa))       #barra n:84 
    ret.agregar_barra(Barra(86, 87, 0.6637249655149108, 0.6637249655149108, 200 * GPa, densidad, 420 * MPa))       #barra n:85 
    ret.agregar_barra(Barra(87, 88, 0.6722435298817167, 0.6722435298817167, 200 * GPa, densidad, 420 * MPa))       #barra n:86 
    ret.agregar_barra(Barra(88, 89, 0.001, 0.001, 200 * GPa, densidad, 420 * MPa))       #barra n:87 
    ret.agregar_barra(Barra(90, 91, 0.5085888367492917, 0.5085888367492917, 200 * GPa, densidad, 420 * MPa))       #barra n:88 
    ret.agregar_barra(Barra(91, 92, 0.5125116608630085, 0.5125116608630085, 200 * GPa, densidad, 420 * MPa))       #barra n:89 
    ret.agregar_barra(Barra(92, 93, 0.5146716000220265, 0.5146716000220265, 200 * GPa, densidad, 420 * MPa))       #barra n:90 
    ret.agregar_barra(Barra(93, 94, 0.5169535436799279, 0.5169535436799279, 200 * GPa, densidad, 420 * MPa))       #barra n:91 
    ret.agregar_barra(Barra(94, 95, 0.5183393177341998, 0.5183393177341998, 200 * GPa, densidad, 420 * MPa))       #barra n:92 
    ret.agregar_barra(Barra(95, 96, 0.5199695944476596, 0.5199695944476596, 200 * GPa, densidad, 420 * MPa))       #barra n:93 
    ret.agregar_barra(Barra(96, 97, 0.5209282244170972, 0.5209282244170972, 200 * GPa, densidad, 420 * MPa))       #barra n:94 
    ret.agregar_barra(Barra(97, 98, 0.5221527336784383, 0.5221527336784383, 200 * GPa, densidad, 420 * MPa))       #barra n:95 
    ret.agregar_barra(Barra(98, 99, 0.584314417451056, 0.584314417451056, 200 * GPa, densidad, 420 * MPa))       #barra n:96 
    ret.agregar_barra(Barra(99, 100, 0.5237339575043894, 0.5237339575043894, 200 * GPa, densidad, 420 * MPa))       #barra n:97 
    ret.agregar_barra(Barra(100, 101, 0.5843188369043054, 0.5843188369043054, 200 * GPa, densidad, 420 * MPa))       #barra n:98 
    ret.agregar_barra(Barra(101, 102, 0.5248285374133651, 0.5248285374133651, 200 * GPa, densidad, 420 * MPa))       #barra n:99 
    ret.agregar_barra(Barra(102, 103, 0.5843170987049431, 0.5843170987049431, 200 * GPa, densidad, 420 * MPa))       #barra n:100 
    ret.agregar_barra(Barra(103, 104, 0.525499212307772, 0.525499212307772, 200 * GPa, densidad, 420 * MPa))       #barra n:101 
    ret.agregar_barra(Barra(104, 105, 0.5843166215897502, 0.5843166215897502, 200 * GPa, densidad, 420 * MPa))       #barra n:102 
    ret.agregar_barra(Barra(105, 106, 0.5257790986487385, 0.5257790986487385, 200 * GPa, densidad, 420 * MPa))       #barra n:103 
    ret.agregar_barra(Barra(106, 107, 0.5843176932152078, 0.5843176932152078, 200 * GPa, densidad, 420 * MPa))       #barra n:104 
    ret.agregar_barra(Barra(107, 108, 0.5256809648904188, 0.5256809648904188, 200 * GPa, densidad, 420 * MPa))       #barra n:105 
    ret.agregar_barra(Barra(108, 109, 0.5843202916309462, 0.5843202916309462, 200 * GPa, densidad, 420 * MPa))       #barra n:106 
    ret.agregar_barra(Barra(109, 110, 0.5252004037857626, 0.5252004037857626, 200 * GPa, densidad, 420 * MPa))       #barra n:107 
    ret.agregar_barra(Barra(110, 111, 0.584316437127838, 0.584316437127838, 200 * GPa, densidad, 420 * MPa))       #barra n:108 
    ret.agregar_barra(Barra(111, 112, 0.5243147487760367, 0.5243147487760367, 200 * GPa, densidad, 420 * MPa))       #barra n:109 
    ret.agregar_barra(Barra(112, 113, 0.5843179670534377, 0.5843179670534377, 200 * GPa, densidad, 420 * MPa))       #barra n:110 
    ret.agregar_barra(Barra(113, 114, 0.5229772051869338, 0.5229772051869338, 200 * GPa, densidad, 420 * MPa))       #barra n:111 
    ret.agregar_barra(Barra(114, 115, 0.5219054780412344, 0.5219054780412344, 200 * GPa, densidad, 420 * MPa))       #barra n:112 
    ret.agregar_barra(Barra(115, 116, 0.52110201963094, 0.52110201963094, 200 * GPa, densidad, 420 * MPa))       #barra n:113 
    ret.agregar_barra(Barra(116, 117, 0.5196848233431289, 0.5196848233431289, 200 * GPa, densidad, 420 * MPa))       #barra n:114 
    ret.agregar_barra(Barra(117, 118, 0.5185266496195163, 0.5185266496195163, 200 * GPa, densidad, 420 * MPa))       #barra n:115 
    ret.agregar_barra(Barra(118, 119, 0.5166052053244019, 0.5166052053244019, 200 * GPa, densidad, 420 * MPa))       #barra n:116 
    ret.agregar_barra(Barra(119, 120, 0.514892158489307, 0.514892158489307, 200 * GPa, densidad, 420 * MPa))       #barra n:117 
    ret.agregar_barra(Barra(120, 121, 0.5120237977282545, 0.5120237977282545, 200 * GPa, densidad, 420 * MPa))       #barra n:118 
    ret.agregar_barra(Barra(121, 122, 0.5089952426723402, 0.5089952426723402, 200 * GPa, densidad, 420 * MPa))       #barra n:119 
    ret.agregar_barra(Barra(122, 123, 0.5024476671953467, 0.5024476671953467, 200 * GPa, densidad, 420 * MPa))       #barra n:120 
    ret.agregar_barra(Barra(123, 124, 0.5089078216340279, 0.5089078216340279, 200 * GPa, densidad, 420 * MPa))       #barra n:121 
    ret.agregar_barra(Barra(124, 125, 0.5132648295927996, 0.5132648295927996, 200 * GPa, densidad, 420 * MPa))       #barra n:122 
    ret.agregar_barra(Barra(125, 126, 0.5160939334209145, 0.5160939334209145, 200 * GPa, densidad, 420 * MPa))       #barra n:123 
    ret.agregar_barra(Barra(126, 127, 0.5191133879947007, 0.5191133879947007, 200 * GPa, densidad, 420 * MPa))       #barra n:124 
    ret.agregar_barra(Barra(127, 128, 0.5214027750326059, 0.5214027750326059, 200 * GPa, densidad, 420 * MPa))       #barra n:125 
    ret.agregar_barra(Barra(128, 129, 0.5843167743121437, 0.5843167743121437, 200 * GPa, densidad, 420 * MPa))       #barra n:126 
    ret.agregar_barra(Barra(129, 130, 0.5260055561677152, 0.5260055561677152, 200 * GPa, densidad, 420 * MPa))       #barra n:127 
    ret.agregar_barra(Barra(130, 131, 0.5843159522053423, 0.5843159522053423, 200 * GPa, densidad, 420 * MPa))       #barra n:128 
    ret.agregar_barra(Barra(131, 132, 0.5298959765737377, 0.5298959765737377, 200 * GPa, densidad, 420 * MPa))       #barra n:129 
    ret.agregar_barra(Barra(132, 133, 0.529770928036223, 0.529770928036223, 200 * GPa, densidad, 420 * MPa))       #barra n:130 
    ret.agregar_barra(Barra(134, 135, 0.5090136778474389, 0.5090136778474389, 200 * GPa, densidad, 420 * MPa))       #barra n:131 
    ret.agregar_barra(Barra(135, 136, 0.51199110012221, 0.51199110012221, 200 * GPa, densidad, 420 * MPa))       #barra n:132 
    ret.agregar_barra(Barra(136, 137, 0.5148554724338006, 0.5148554724338006, 200 * GPa, densidad, 420 * MPa))       #barra n:133 
    ret.agregar_barra(Barra(137, 138, 0.5165659331260806, 0.5165659331260806, 200 * GPa, densidad, 420 * MPa))       #barra n:134 
    ret.agregar_barra(Barra(138, 139, 0.5184860297735194, 0.5184860297735194, 200 * GPa, densidad, 420 * MPa))       #barra n:135 
    ret.agregar_barra(Barra(139, 140, 0.5196415184955525, 0.5196415184955525, 200 * GPa, densidad, 420 * MPa))       #barra n:136 
    ret.agregar_barra(Barra(140, 141, 0.5210568975318106, 0.5210568975318106, 200 * GPa, densidad, 420 * MPa))       #barra n:137 
    ret.agregar_barra(Barra(141, 142, 0.5218574520780319, 0.5218574520780319, 200 * GPa, densidad, 420 * MPa))       #barra n:138 
    ret.agregar_barra(Barra(142, 143, 0.5843157452308297, 0.5843157452308297, 200 * GPa, densidad, 420 * MPa))       #barra n:139 
    ret.agregar_barra(Barra(143, 144, 0.5234585883122375, 0.5234585883122375, 200 * GPa, densidad, 420 * MPa))       #barra n:140 
    ret.agregar_barra(Barra(144, 145, 0.5843160329470795, 0.5843160329470795, 200 * GPa, densidad, 420 * MPa))       #barra n:141 
    ret.agregar_barra(Barra(145, 146, 0.5245654359905031, 0.5245654359905031, 200 * GPa, densidad, 420 * MPa))       #barra n:142 
    ret.agregar_barra(Barra(146, 147, 0.5843183433495303, 0.5843183433495303, 200 * GPa, densidad, 420 * MPa))       #barra n:143 
    ret.agregar_barra(Barra(147, 148, 0.5252431068766226, 0.5252431068766226, 200 * GPa, densidad, 420 * MPa))       #barra n:144 
    ret.agregar_barra(Barra(148, 149, 0.584317853302236, 0.584317853302236, 200 * GPa, densidad, 420 * MPa))       #barra n:145 
    ret.agregar_barra(Barra(149, 150, 0.525525795696391, 0.525525795696391, 200 * GPa, densidad, 420 * MPa))       #barra n:146 
    ret.agregar_barra(Barra(150, 151, 0.5843150510447098, 0.5843150510447098, 200 * GPa, densidad, 420 * MPa))       #barra n:147 
    ret.agregar_barra(Barra(151, 152, 0.5254266879075461, 0.5254266879075461, 200 * GPa, densidad, 420 * MPa))       #barra n:148 
    ret.agregar_barra(Barra(152, 153, 0.5843155489115053, 0.5843155489115053, 200 * GPa, densidad, 420 * MPa))       #barra n:149 
    ret.agregar_barra(Barra(153, 154, 0.5249412274155836, 0.5249412274155836, 200 * GPa, densidad, 420 * MPa))       #barra n:150 
    ret.agregar_barra(Barra(154, 155, 0.5843176735881412, 0.5843176735881412, 200 * GPa, densidad, 420 * MPa))       #barra n:151 
    ret.agregar_barra(Barra(155, 156, 0.5240460326350115, 0.5240460326350115, 200 * GPa, densidad, 420 * MPa))       #barra n:152 
    ret.agregar_barra(Barra(156, 157, 0.5843151826525581, 0.5843151826525581, 200 * GPa, densidad, 420 * MPa))       #barra n:153 
    ret.agregar_barra(Barra(157, 158, 0.5226926556998631, 0.5226926556998631, 200 * GPa, densidad, 420 * MPa))       #barra n:154 
    ret.agregar_barra(Barra(158, 159, 0.584315662558249, 0.584315662558249, 200 * GPa, densidad, 420 * MPa))       #barra n:155 
    ret.agregar_barra(Barra(159, 160, 0.5207918203466905, 0.5207918203466905, 200 * GPa, densidad, 420 * MPa))       #barra n:156 
    ret.agregar_barra(Barra(160, 161, 0.5198215709349232, 0.5198215709349232, 200 * GPa, densidad, 420 * MPa))       #barra n:157 
    ret.agregar_barra(Barra(161, 162, 0.5181725426833902, 0.5181725426833902, 200 * GPa, densidad, 420 * MPa))       #barra n:158 
    ret.agregar_barra(Barra(162, 163, 0.5167670849490895, 0.5167670849490895, 200 * GPa, densidad, 420 * MPa))       #barra n:159 
    ret.agregar_barra(Barra(163, 164, 0.5144492521774159, 0.5144492521774159, 200 * GPa, densidad, 420 * MPa))       #barra n:160 
    ret.agregar_barra(Barra(164, 165, 0.5122463869629659, 0.5122463869629659, 200 * GPa, densidad, 420 * MPa))       #barra n:161 
    ret.agregar_barra(Barra(165, 166, 0.5082412925994356, 0.5082412925994356, 200 * GPa, densidad, 420 * MPa))       #barra n:162 
    ret.agregar_barra(Barra(166, 167, 0.501775197980615, 0.501775197980615, 200 * GPa, densidad, 420 * MPa))       #barra n:163 
    ret.agregar_barra(Barra(167, 168, 0.5096096182555221, 0.5096096182555221, 200 * GPa, densidad, 420 * MPa))       #barra n:164 
    ret.agregar_barra(Barra(168, 169, 0.513059610579347, 0.513059610579347, 200 * GPa, densidad, 420 * MPa))       #barra n:165 
    ret.agregar_barra(Barra(169, 170, 0.5164927360357954, 0.5164927360357954, 200 * GPa, densidad, 420 * MPa))       #barra n:166 
    ret.agregar_barra(Barra(170, 171, 0.5189715630524971, 0.5189715630524971, 200 * GPa, densidad, 420 * MPa))       #barra n:167 
    ret.agregar_barra(Barra(171, 172, 0.5217043968428375, 0.5217043968428375, 200 * GPa, densidad, 420 * MPa))       #barra n:168 
    ret.agregar_barra(Barra(172, 173, 0.584315219134907, 0.584315219134907, 200 * GPa, densidad, 420 * MPa))       #barra n:169 
    ret.agregar_barra(Barra(173, 174, 0.526264206300159, 0.526264206300159, 200 * GPa, densidad, 420 * MPa))       #barra n:170 
    ret.agregar_barra(Barra(174, 175, 0.5843158062043105, 0.5843158062043105, 200 * GPa, densidad, 420 * MPa))       #barra n:171 
    ret.agregar_barra(Barra(175, 176, 0.530790741870651, 0.530790741870651, 200 * GPa, densidad, 420 * MPa))       #barra n:172 
    ret.agregar_barra(Barra(176, 177, 0.5347556150314107, 0.5347556150314107, 200 * GPa, densidad, 420 * MPa))       #barra n:173 
    ret.agregar_barra(Barra(0, 45, 0.001, 0.001, 200 * GPa, densidad, 420 * MPa))       #barra n:174 
    ret.agregar_barra(Barra(1, 46, 0.504365800891649, 0.504365800891649, 200 * GPa, densidad, 420 * MPa))       #barra n:175 
    ret.agregar_barra(Barra(2, 47, 0.5043822382495528, 0.5043822382495528, 200 * GPa, densidad, 420 * MPa))       #barra n:176 
    ret.agregar_barra(Barra(3, 48, 0.5044536586681309, 0.5044536586681309, 200 * GPa, densidad, 420 * MPa))       #barra n:177 
    ret.agregar_barra(Barra(4, 49, 0.5043678297421056, 0.5043678297421056, 200 * GPa, densidad, 420 * MPa))       #barra n:178 
    ret.agregar_barra(Barra(5, 50, 0.5044553055098357, 0.5044553055098357, 200 * GPa, densidad, 420 * MPa))       #barra n:179 
    ret.agregar_barra(Barra(6, 51, 0.5043676418469625, 0.5043676418469625, 200 * GPa, densidad, 420 * MPa))       #barra n:180 
    ret.agregar_barra(Barra(7, 52, 0.5044553254688395, 0.5044553254688395, 200 * GPa, densidad, 420 * MPa))       #barra n:181 
    ret.agregar_barra(Barra(8, 53, 0.5043676393433109, 0.5043676393433109, 200 * GPa, densidad, 420 * MPa))       #barra n:182 
    ret.agregar_barra(Barra(9, 54, 0.5044553257196455, 0.5044553257196455, 200 * GPa, densidad, 420 * MPa))       #barra n:183 
    ret.agregar_barra(Barra(10, 55, 0.5043676393124306, 0.5043676393124306, 200 * GPa, densidad, 420 * MPa))       #barra n:184 
    ret.agregar_barra(Barra(11, 56, 0.5044553257232648, 0.5044553257232648, 200 * GPa, densidad, 420 * MPa))       #barra n:185 
    ret.agregar_barra(Barra(12, 57, 0.5043676393122518, 0.5043676393122518, 200 * GPa, densidad, 420 * MPa))       #barra n:186 
    ret.agregar_barra(Barra(13, 58, 0.5044553257232648, 0.5044553257232648, 200 * GPa, densidad, 420 * MPa))       #barra n:187 
    ret.agregar_barra(Barra(14, 59, 0.5043676393122518, 0.5043676393122518, 200 * GPa, densidad, 420 * MPa))       #barra n:188 
    ret.agregar_barra(Barra(15, 60, 0.5044553257232648, 0.5044553257232648, 200 * GPa, densidad, 420 * MPa))       #barra n:189 
    ret.agregar_barra(Barra(16, 61, 0.5043676393118901, 0.5043676393118901, 200 * GPa, densidad, 420 * MPa))       #barra n:190 
    ret.agregar_barra(Barra(17, 62, 0.5044553257232648, 0.5044553257232648, 200 * GPa, densidad, 420 * MPa))       #barra n:191 
    ret.agregar_barra(Barra(18, 63, 0.5043676393122518, 0.5043676393122518, 200 * GPa, densidad, 420 * MPa))       #barra n:192 
    ret.agregar_barra(Barra(19, 64, 0.5044553257231534, 0.5044553257231534, 200 * GPa, densidad, 420 * MPa))       #barra n:193 
    ret.agregar_barra(Barra(20, 65, 0.5043676393126133, 0.5043676393126133, 200 * GPa, densidad, 420 * MPa))       #barra n:194 
    ret.agregar_barra(Barra(21, 66, 0.5044553257232648, 0.5044553257232648, 200 * GPa, densidad, 420 * MPa))       #barra n:195 
    ret.agregar_barra(Barra(22, 67, 0.5043676393122518, 0.5043676393122518, 200 * GPa, densidad, 420 * MPa))       #barra n:196 
    ret.agregar_barra(Barra(23, 68, 0.5044553257232648, 0.5044553257232648, 200 * GPa, densidad, 420 * MPa))       #barra n:197 
    ret.agregar_barra(Barra(24, 69, 0.5043676393122518, 0.5043676393122518, 200 * GPa, densidad, 420 * MPa))       #barra n:198 
    ret.agregar_barra(Barra(25, 70, 0.5044553257232648, 0.5044553257232648, 200 * GPa, densidad, 420 * MPa))       #barra n:199 
    ret.agregar_barra(Barra(26, 71, 0.5043676393118901, 0.5043676393118901, 200 * GPa, densidad, 420 * MPa))       #barra n:200 
    ret.agregar_barra(Barra(27, 72, 0.5044553257229467, 0.5044553257229467, 200 * GPa, densidad, 420 * MPa))       #barra n:201 
    ret.agregar_barra(Barra(28, 73, 0.5043676393118901, 0.5043676393118901, 200 * GPa, densidad, 420 * MPa))       #barra n:202 
    ret.agregar_barra(Barra(29, 74, 0.5044553257231534, 0.5044553257231534, 200 * GPa, densidad, 420 * MPa))       #barra n:203 
    ret.agregar_barra(Barra(30, 75, 0.5043676393118901, 0.5043676393118901, 200 * GPa, densidad, 420 * MPa))       #barra n:204 
    ret.agregar_barra(Barra(31, 76, 0.5044553257232648, 0.5044553257232648, 200 * GPa, densidad, 420 * MPa))       #barra n:205 
    ret.agregar_barra(Barra(32, 77, 0.504367639311169, 0.504367639311169, 200 * GPa, densidad, 420 * MPa))       #barra n:206 
    ret.agregar_barra(Barra(33, 78, 0.5044553257300486, 0.5044553257300486, 200 * GPa, densidad, 420 * MPa))       #barra n:207 
    ret.agregar_barra(Barra(34, 79, 0.5043676392430955, 0.5043676392430955, 200 * GPa, densidad, 420 * MPa))       #barra n:208 
    ret.agregar_barra(Barra(35, 80, 0.5044553262743449, 0.5044553262743449, 200 * GPa, densidad, 420 * MPa))       #barra n:209 
    ret.agregar_barra(Barra(36, 81, 0.504367633825878, 0.504367633825878, 200 * GPa, densidad, 420 * MPa))       #barra n:210 
    ret.agregar_barra(Barra(37, 82, 0.5044553705519353, 0.5044553705519353, 200 * GPa, densidad, 420 * MPa))       #barra n:211 
    ret.agregar_barra(Barra(38, 83, 0.5043672233719078, 0.5043672233719078, 200 * GPa, densidad, 420 * MPa))       #barra n:212 
    ret.agregar_barra(Barra(39, 84, 0.5044589433829376, 0.5044589433829376, 200 * GPa, densidad, 420 * MPa))       #barra n:213 
    ret.agregar_barra(Barra(40, 85, 0.5043345102999452, 0.5043345102999452, 200 * GPa, densidad, 420 * MPa))       #barra n:214 
    ret.agregar_barra(Barra(41, 86, 0.5047321492082125, 0.5047321492082125, 200 * GPa, densidad, 420 * MPa))       #barra n:215 
    ret.agregar_barra(Barra(42, 87, 0.501, 0.501, 200 * GPa, densidad, 420 * MPa))       #barra n:216 
    ret.agregar_barra(Barra(43, 88, 0.001, 0.001, 200 * GPa, densidad, 420 * MPa))       #barra n:217 
    ret.agregar_barra(Barra(44, 89, 0.001, 0.001, 200 * GPa, densidad, 420 * MPa))       #barra n:218 
    ret.agregar_barra(Barra(0, 46, 0.5414461692649183, 0.5414461692649183, 200 * GPa, densidad, 420 * MPa))       #barra n:219 
    ret.agregar_barra(Barra(2, 48, 0.5394115739342102, 0.5394115739342102, 200 * GPa, densidad, 420 * MPa))       #barra n:220 
    ret.agregar_barra(Barra(4, 50, 0.5372806695728298, 0.5372806695728298, 200 * GPa, densidad, 420 * MPa))       #barra n:221 
    ret.agregar_barra(Barra(6, 52, 0.535020834531167, 0.535020834531167, 200 * GPa, densidad, 420 * MPa))       #barra n:222 
    ret.agregar_barra(Barra(8, 54, 0.5326047512200646, 0.5326047512200646, 200 * GPa, densidad, 420 * MPa))       #barra n:223 
    ret.agregar_barra(Barra(10, 56, 0.5299946760635385, 0.5299946760635385, 200 * GPa, densidad, 420 * MPa))       #barra n:224 
    ret.agregar_barra(Barra(12, 58, 0.5271346927144525, 0.5271346927144525, 200 * GPa, densidad, 420 * MPa))       #barra n:225 
    ret.agregar_barra(Barra(14, 60, 0.5239353811022179, 0.5239353811022179, 200 * GPa, densidad, 420 * MPa))       #barra n:226 
    ret.agregar_barra(Barra(16, 62, 0.5202364367045264, 0.5202364367045264, 200 * GPa, densidad, 420 * MPa))       #barra n:227 
    ret.agregar_barra(Barra(18, 64, 0.5156883475275744, 0.5156883475275744, 200 * GPa, densidad, 420 * MPa))       #barra n:228 
    ret.agregar_barra(Barra(20, 66, 0.5090958832963375, 0.5090958832963375, 200 * GPa, densidad, 420 * MPa))       #barra n:229 
    ret.agregar_barra(Barra(22, 68, 0.5089807484283625, 0.5089807484283625, 200 * GPa, densidad, 420 * MPa))       #barra n:230 
    ret.agregar_barra(Barra(24, 70, 0.5156218735351796, 0.5156218735351796, 200 * GPa, densidad, 420 * MPa))       #barra n:231 
    ret.agregar_barra(Barra(26, 72, 0.5201849455240335, 0.5201849455240335, 200 * GPa, densidad, 420 * MPa))       #barra n:232 
    ret.agregar_barra(Barra(28, 74, 0.5843160189715852, 0.5843160189715852, 200 * GPa, densidad, 420 * MPa))       #barra n:233 
    ret.agregar_barra(Barra(30, 76, 0.5843310546910487, 0.5843310546910487, 200 * GPa, densidad, 420 * MPa))       #barra n:234 
    ret.agregar_barra(Barra(32, 78, 0.5843167381937867, 0.5843167381937867, 200 * GPa, densidad, 420 * MPa))       #barra n:235 
    ret.agregar_barra(Barra(34, 80, 0.5843166069098111, 0.5843166069098111, 200 * GPa, densidad, 420 * MPa))       #barra n:236 
    ret.agregar_barra(Barra(36, 82, 0.5843251561408761, 0.5843251561408761, 200 * GPa, densidad, 420 * MPa))       #barra n:237 
    ret.agregar_barra(Barra(38, 84, 0.5843150955541659, 0.5843150955541659, 200 * GPa, densidad, 420 * MPa))       #barra n:238 
    ret.agregar_barra(Barra(40, 86, 0.5843187632042344, 0.5843187632042344, 200 * GPa, densidad, 420 * MPa))       #barra n:239 
    ret.agregar_barra(Barra(42, 88, 0.5843175284026874, 0.5843175284026874, 200 * GPa, densidad, 420 * MPa))       #barra n:240 
    ret.agregar_barra(Barra(2, 46, 0.5843180134621383, 0.5843180134621383, 200 * GPa, densidad, 420 * MPa))       #barra n:241 
    ret.agregar_barra(Barra(4, 48, 0.5843149665715047, 0.5843149665715047, 200 * GPa, densidad, 420 * MPa))       #barra n:242 
    ret.agregar_barra(Barra(6, 50, 0.5843153144148965, 0.5843153144148965, 200 * GPa, densidad, 420 * MPa))       #barra n:243 
    ret.agregar_barra(Barra(8, 52, 0.5843204707838118, 0.5843204707838118, 200 * GPa, densidad, 420 * MPa))       #barra n:244 
    ret.agregar_barra(Barra(10, 54, 0.5843179845757056, 0.5843179845757056, 200 * GPa, densidad, 420 * MPa))       #barra n:245 
    ret.agregar_barra(Barra(12, 56, 0.5843153667278854, 0.5843153667278854, 200 * GPa, densidad, 420 * MPa))       #barra n:246 
    ret.agregar_barra(Barra(14, 58, 0.5843170553992655, 0.5843170553992655, 200 * GPa, densidad, 420 * MPa))       #barra n:247 
    ret.agregar_barra(Barra(16, 60, 0.5843151719239076, 0.5843151719239076, 200 * GPa, densidad, 420 * MPa))       #barra n:248 
    ret.agregar_barra(Barra(18, 62, 0.5180481464172068, 0.5180481464172068, 200 * GPa, densidad, 420 * MPa))       #barra n:249 
    ret.agregar_barra(Barra(20, 64, 0.5127415269991339, 0.5127415269991339, 200 * GPa, densidad, 420 * MPa))       #barra n:250 
    ret.agregar_barra(Barra(22, 66, 0.5010210166417232, 0.5010210166417232, 200 * GPa, densidad, 420 * MPa))       #barra n:251 
    ret.agregar_barra(Barra(24, 68, 0.5128230833330418, 0.5128230833330418, 200 * GPa, densidad, 420 * MPa))       #barra n:252 
    ret.agregar_barra(Barra(26, 70, 0.5181058149187979, 0.5181058149187979, 200 * GPa, densidad, 420 * MPa))       #barra n:253 
    ret.agregar_barra(Barra(28, 72, 0.5221632527704261, 0.5221632527704261, 200 * GPa, densidad, 420 * MPa))       #barra n:254 
    ret.agregar_barra(Barra(30, 74, 0.5255851262780155, 0.5255851262780155, 200 * GPa, densidad, 420 * MPa))       #barra n:255 
    ret.agregar_barra(Barra(32, 76, 0.5286004855297971, 0.5286004855297971, 200 * GPa, densidad, 420 * MPa))       #barra n:256 
    ret.agregar_barra(Barra(34, 78, 0.53132693913738, 0.53132693913738, 200 * GPa, densidad, 420 * MPa))       #barra n:257 
    ret.agregar_barra(Barra(36, 80, 0.5338343904777015, 0.5338343904777015, 200 * GPa, densidad, 420 * MPa))       #barra n:258 
    ret.agregar_barra(Barra(38, 82, 0.53616841563657, 0.53616841563657, 200 * GPa, densidad, 420 * MPa))       #barra n:259 
    ret.agregar_barra(Barra(40, 84, 0.5383597040144315, 0.5383597040144315, 200 * GPa, densidad, 420 * MPa))       #barra n:260 
    ret.agregar_barra(Barra(42, 86, 0.5403598825142423, 0.5403598825142423, 200 * GPa, densidad, 420 * MPa))       #barra n:261 
    ret.agregar_barra(Barra(44, 88, 0.001, 0.001, 200 * GPa, densidad, 420 * MPa))       #barra n:262 
    ret.agregar_barra(Barra(0, 90, 0.5405769225142265, 0.5405769225142265, 200 * GPa, densidad, 420 * MPa))       #barra n:263 
    ret.agregar_barra(Barra(1, 91, 0.7035644779089967, 0.7035644779089967, 200 * GPa, densidad, 420 * MPa))       #barra n:264 
    ret.agregar_barra(Barra(2, 92, 0.7846554422383436, 0.7846554422383436, 200 * GPa, densidad, 420 * MPa))       #barra n:265 
    ret.agregar_barra(Barra(3, 93, 0.8463132117123929, 0.8463132117123929, 200 * GPa, densidad, 420 * MPa))       #barra n:266 
    ret.agregar_barra(Barra(4, 94, 0.8972271070074396, 0.8972271070074396, 200 * GPa, densidad, 420 * MPa))       #barra n:267 
    ret.agregar_barra(Barra(5, 95, 0.9408526318464312, 0.9408526318464312, 200 * GPa, densidad, 420 * MPa))       #barra n:268 
    ret.agregar_barra(Barra(6, 96, 0.9788549032844416, 0.9788549032844416, 200 * GPa, densidad, 420 * MPa))       #barra n:269 
    ret.agregar_barra(Barra(7, 97, 1.0122891451641027, 1.0122891451641027, 200 * GPa, densidad, 420 * MPa))       #barra n:270 
    ret.agregar_barra(Barra(8, 98, 1.0417515946889606, 1.0417515946889606, 200 * GPa, densidad, 420 * MPa))       #barra n:271 
    ret.agregar_barra(Barra(9, 99, 1.067722520970753, 1.067722520970753, 200 * GPa, densidad, 420 * MPa))       #barra n:272 
    ret.agregar_barra(Barra(10, 100, 1.0904716879641922, 1.0904716879641922, 200 * GPa, densidad, 420 * MPa))       #barra n:273 
    ret.agregar_barra(Barra(11, 101, 1.110267768288426, 1.110267768288426, 200 * GPa, densidad, 420 * MPa))       #barra n:274 
    ret.agregar_barra(Barra(12, 102, 1.1272465258566382, 1.1272465258566382, 200 * GPa, densidad, 420 * MPa))       #barra n:275 
    ret.agregar_barra(Barra(13, 103, 1.1415796136895384, 1.1415796136895384, 200 * GPa, densidad, 420 * MPa))       #barra n:276 
    ret.agregar_barra(Barra(14, 104, 1.153337592187547, 1.153337592187547, 200 * GPa, densidad, 420 * MPa))       #barra n:277 
    ret.agregar_barra(Barra(15, 105, 1.1626412060369962, 1.1626412060369962, 200 * GPa, densidad, 420 * MPa))       #barra n:278 
    ret.agregar_barra(Barra(16, 106, 1.1695253958607474, 1.1695253958607474, 200 * GPa, densidad, 420 * MPa))       #barra n:279 
    ret.agregar_barra(Barra(17, 107, 1.1740817065409452, 1.1740817065409452, 200 * GPa, densidad, 420 * MPa))       #barra n:280 
    ret.agregar_barra(Barra(18, 108, 1.1763238438776216, 1.1763238438776216, 200 * GPa, densidad, 420 * MPa))       #barra n:281 
    ret.agregar_barra(Barra(19, 109, 1.1763255253919251, 1.1763255253919251, 200 * GPa, densidad, 420 * MPa))       #barra n:282 
    ret.agregar_barra(Barra(20, 110, 1.1740867966233304, 1.1740867966233304, 200 * GPa, densidad, 420 * MPa))       #barra n:283 
    ret.agregar_barra(Barra(21, 111, 1.1696700753335252, 1.1696700753335252, 200 * GPa, densidad, 420 * MPa))       #barra n:284 
    ret.agregar_barra(Barra(22, 112, 1.1630658850981102, 1.1630658850981102, 200 * GPa, densidad, 420 * MPa))       #barra n:285 
    ret.agregar_barra(Barra(23, 113, 1.1543293626525037, 1.1543293626525037, 200 * GPa, densidad, 420 * MPa))       #barra n:286 
    ret.agregar_barra(Barra(24, 114, 1.1434437826199875, 1.1434437826199875, 200 * GPa, densidad, 420 * MPa))       #barra n:287 
    ret.agregar_barra(Barra(25, 115, 1.1304595836419065, 1.1304595836419065, 200 * GPa, densidad, 420 * MPa))       #barra n:288 
    ret.agregar_barra(Barra(26, 116, 1.115353920690578, 1.115353920690578, 200 * GPa, densidad, 420 * MPa))       #barra n:289 
    ret.agregar_barra(Barra(27, 117, 1.0981742628156463, 1.0981742628156463, 200 * GPa, densidad, 420 * MPa))       #barra n:290 
    ret.agregar_barra(Barra(28, 118, 1.078891874049852, 1.078891874049852, 200 * GPa, densidad, 420 * MPa))       #barra n:291 
    ret.agregar_barra(Barra(29, 119, 1.057552410017891, 1.057552410017891, 200 * GPa, densidad, 420 * MPa))       #barra n:292 
    ret.agregar_barra(Barra(30, 120, 1.0341205214045788, 1.0341205214045788, 200 * GPa, densidad, 420 * MPa))       #barra n:293 
    ret.agregar_barra(Barra(31, 121, 1.0086405835479701, 1.0086405835479701, 200 * GPa, densidad, 420 * MPa))       #barra n:294 
    ret.agregar_barra(Barra(32, 122, 0.9810685629544842, 0.9810685629544842, 200 * GPa, densidad, 420 * MPa))       #barra n:295 
    ret.agregar_barra(Barra(33, 123, 0.951446921692553, 0.951446921692553, 200 * GPa, densidad, 420 * MPa))       #barra n:296 
    ret.agregar_barra(Barra(34, 124, 0.919717982466676, 0.919717982466676, 200 * GPa, densidad, 420 * MPa))       #barra n:297 
    ret.agregar_barra(Barra(35, 125, 0.8859185135064604, 0.8859185135064604, 200 * GPa, densidad, 420 * MPa))       #barra n:298 
    ret.agregar_barra(Barra(36, 126, 0.8499643572686386, 0.8499643572686386, 200 * GPa, densidad, 420 * MPa))       #barra n:299 
    ret.agregar_barra(Barra(37, 127, 0.8118712951904838, 0.8118712951904838, 200 * GPa, densidad, 420 * MPa))       #barra n:300 
    ret.agregar_barra(Barra(38, 128, 0.7714869988088056, 0.7714869988088056, 200 * GPa, densidad, 420 * MPa))       #barra n:301 
    ret.agregar_barra(Barra(39, 129, 0.7287341962636656, 0.7287341962636656, 200 * GPa, densidad, 420 * MPa))       #barra n:302 
    ret.agregar_barra(Barra(40, 130, 0.6831901147166275, 0.6831901147166275, 200 * GPa, densidad, 420 * MPa))       #barra n:303 
    ret.agregar_barra(Barra(41, 131, 0.6341321396411734, 0.6341321396411734, 200 * GPa, densidad, 420 * MPa))       #barra n:304 
    ret.agregar_barra(Barra(42, 132, 0.5843177526621327, 0.5843177526621327, 200 * GPa, densidad, 420 * MPa))       #barra n:305 
    ret.agregar_barra(Barra(43, 133, 0.5843165380310437, 0.5843165380310437, 200 * GPa, densidad, 420 * MPa))       #barra n:306 
    ret.agregar_barra(Barra(45, 90, 0.5843144237963422, 0.5843144237963422, 200 * GPa, densidad, 420 * MPa))       #barra n:307 
    ret.agregar_barra(Barra(46, 91, 0.6968267072466825, 0.6968267072466825, 200 * GPa, densidad, 420 * MPa))       #barra n:308 
    ret.agregar_barra(Barra(47, 92, 0.7801167756232738, 0.7801167756232738, 200 * GPa, densidad, 420 * MPa))       #barra n:309 
    ret.agregar_barra(Barra(48, 93, 0.8427825255891979, 0.8427825255891979, 200 * GPa, densidad, 420 * MPa))       #barra n:310 
    ret.agregar_barra(Barra(49, 94, 0.8943228776083489, 0.8943228776083489, 200 * GPa, densidad, 420 * MPa))       #barra n:311 
    ret.agregar_barra(Barra(50, 95, 0.9383863252438314, 0.9383863252438314, 200 * GPa, densidad, 420 * MPa))       #barra n:312 
    ret.agregar_barra(Barra(51, 96, 0.9767260016680622, 0.9767260016680622, 200 * GPa, densidad, 420 * MPa))       #barra n:313 
    ret.agregar_barra(Barra(52, 97, 1.0104274615006181, 1.0104274615006181, 200 * GPa, densidad, 420 * MPa))       #barra n:314 
    ret.agregar_barra(Barra(53, 98, 1.0401156851797215, 1.0401156851797215, 200 * GPa, densidad, 420 * MPa))       #barra n:315 
    ret.agregar_barra(Barra(54, 99, 1.0662767793609382, 1.0662767793609382, 200 * GPa, densidad, 420 * MPa))       #barra n:316 
    ret.agregar_barra(Barra(55, 100, 1.08919562235298, 1.08919562235298, 200 * GPa, densidad, 420 * MPa))       #barra n:317 
    ret.agregar_barra(Barra(56, 101, 1.1091401932213745, 1.1091401932213745, 200 * GPa, densidad, 420 * MPa))       #barra n:318 
    ret.agregar_barra(Barra(57, 102, 1.1262566270019119, 1.1262566270019119, 200 * GPa, densidad, 420 * MPa))       #barra n:319 
    ret.agregar_barra(Barra(58, 103, 1.1407136119172478, 1.1407136119172478, 200 * GPa, densidad, 420 * MPa))       #barra n:320 
    ret.agregar_barra(Barra(59, 104, 1.1525899705459097, 1.1525899705459097, 200 * GPa, densidad, 420 * MPa))       #barra n:321 
    ret.agregar_barra(Barra(60, 105, 1.162002567282056, 1.162002567282056, 200 * GPa, densidad, 420 * MPa))       #barra n:322 
    ret.agregar_barra(Barra(61, 106, 1.1689935898515138, 1.1689935898515138, 200 * GPa, densidad, 420 * MPa))       #barra n:323 
    ret.agregar_barra(Barra(62, 107, 1.173650266037311, 1.173650266037311, 200 * GPa, densidad, 420 * MPa))       #barra n:324 
    ret.agregar_barra(Barra(63, 108, 1.1759930519035953, 1.1759930519035953, 200 * GPa, densidad, 420 * MPa))       #barra n:325 
    ret.agregar_barra(Barra(64, 109, 1.1760911612978782, 1.1760911612978782, 200 * GPa, densidad, 420 * MPa))       #barra n:326 
    ret.agregar_barra(Barra(65, 110, 1.1739511702325012, 1.1739511702325012, 200 * GPa, densidad, 420 * MPa))       #barra n:327 
    ret.agregar_barra(Barra(66, 111, 1.1696309009863919, 1.1696309009863919, 200 * GPa, densidad, 420 * MPa))       #barra n:328 
    ret.agregar_barra(Barra(67, 112, 1.1631274712780098, 1.1631274712780098, 200 * GPa, densidad, 420 * MPa))       #barra n:329 
    ret.agregar_barra(Barra(68, 113, 1.1544913655590723, 1.1544913655590723, 200 * GPa, densidad, 420 * MPa))       #barra n:330 
    ret.agregar_barra(Barra(69, 114, 1.1437127301066425, 1.1437127301066425, 200 * GPa, densidad, 420 * MPa))       #barra n:331 
    ret.agregar_barra(Barra(70, 115, 1.1308374020873022, 1.1308374020873022, 200 * GPa, densidad, 420 * MPa))       #barra n:332 
    ret.agregar_barra(Barra(71, 116, 1.1158499151362555, 1.1158499151362555, 200 * GPa, densidad, 420 * MPa))       #barra n:333 
    ret.agregar_barra(Barra(72, 117, 1.0987933626581512, 1.0987933626581512, 200 * GPa, densidad, 420 * MPa))       #barra n:334 
    ret.agregar_barra(Barra(73, 118, 1.0796472849567036, 1.0796472849567036, 200 * GPa, densidad, 420 * MPa))       #barra n:335 
    ret.agregar_barra(Barra(74, 119, 1.0584534277835342, 1.0584534277835342, 200 * GPa, densidad, 420 * MPa))       #barra n:336 
    ret.agregar_barra(Barra(75, 120, 1.035186327272378, 1.035186327272378, 200 * GPa, densidad, 420 * MPa))       #barra n:337 
    ret.agregar_barra(Barra(76, 121, 1.0098875219955081, 1.0098875219955081, 200 * GPa, densidad, 420 * MPa))       #barra n:338 
    ret.agregar_barra(Barra(77, 122, 0.9825257909696973, 0.9825257909696973, 200 * GPa, densidad, 420 * MPa))       #barra n:339 
    ret.agregar_barra(Barra(78, 123, 0.9531433178893527, 0.9531433178893527, 200 * GPa, densidad, 420 * MPa))       #barra n:340 
    ret.agregar_barra(Barra(79, 124, 0.9217011509142643, 0.9217011509142643, 200 * GPa, densidad, 420 * MPa))       #barra n:341 
    ret.agregar_barra(Barra(80, 125, 0.8882423743832754, 0.8882423743832754, 200 * GPa, densidad, 420 * MPa))       #barra n:342 
    ret.agregar_barra(Barra(81, 126, 0.8527155036642715, 0.8527155036642715, 200 * GPa, densidad, 420 * MPa))       #barra n:343 
    ret.agregar_barra(Barra(82, 127, 0.8151622645495937, 0.8151622645495937, 200 * GPa, densidad, 420 * MPa))       #barra n:344 
    ret.agregar_barra(Barra(83, 128, 0.7755047371983936, 0.7755047371983936, 200 * GPa, densidad, 420 * MPa))       #barra n:345 
    ret.agregar_barra(Barra(84, 129, 0.7337679398812436, 0.7337679398812436, 200 * GPa, densidad, 420 * MPa))       #barra n:346 
    ret.agregar_barra(Barra(85, 130, 0.6897898170890411, 0.6897898170890411, 200 * GPa, densidad, 420 * MPa))       #barra n:347 
    ret.agregar_barra(Barra(86, 131, 0.6434901245059692, 0.6434901245059692, 200 * GPa, densidad, 420 * MPa))       #barra n:348 
    ret.agregar_barra(Barra(87, 132, 0.5942554327648581, 0.5942554327648581, 200 * GPa, densidad, 420 * MPa))       #barra n:349 
    ret.agregar_barra(Barra(88, 133, 0.5218532484063501, 0.5218532484063501, 200 * GPa, densidad, 420 * MPa))       #barra n:350 
    ret.agregar_barra(Barra(1, 90, 0.6965676762031345, 0.6965676762031345, 200 * GPa, densidad, 420 * MPa))       #barra n:351 
    ret.agregar_barra(Barra(2, 91, 0.7799452901651927, 0.7799452901651927, 200 * GPa, densidad, 420 * MPa))       #barra n:352 
    ret.agregar_barra(Barra(3, 92, 0.8426541895995665, 0.8426541895995665, 200 * GPa, densidad, 420 * MPa))       #barra n:353 
    ret.agregar_barra(Barra(4, 93, 0.8942159678629193, 0.8942159678629193, 200 * GPa, densidad, 420 * MPa))       #barra n:354 
    ret.agregar_barra(Barra(5, 94, 0.9382986061695867, 0.9382986061695867, 200 * GPa, densidad, 420 * MPa))       #barra n:355 
    ret.agregar_barra(Barra(6, 95, 0.9766491437241791, 0.9766491437241791, 200 * GPa, densidad, 420 * MPa))       #barra n:356 
    ret.agregar_barra(Barra(7, 96, 1.0103629253891055, 1.0103629253891055, 200 * GPa, densidad, 420 * MPa))       #barra n:357 
    ret.agregar_barra(Barra(8, 97, 1.0400580492875107, 1.0400580492875107, 200 * GPa, densidad, 420 * MPa))       #barra n:358 
    ret.agregar_barra(Barra(9, 98, 1.0662283374393136, 1.0662283374393136, 200 * GPa, densidad, 420 * MPa))       #barra n:359 
    ret.agregar_barra(Barra(10, 99, 1.0891521388794052, 1.0891521388794052, 200 * GPa, densidad, 420 * MPa))       #barra n:360 
    ret.agregar_barra(Barra(11, 100, 1.1091042055638343, 1.1091042055638343, 200 * GPa, densidad, 420 * MPa))       #barra n:361 
    ret.agregar_barra(Barra(12, 101, 1.1262245142095608, 1.1262245142095608, 200 * GPa, densidad, 420 * MPa))       #barra n:362 
    ret.agregar_barra(Barra(13, 102, 1.1406879923194801, 1.1406879923194801, 200 * GPa, densidad, 420 * MPa))       #barra n:363 
    ret.agregar_barra(Barra(14, 103, 1.1525675957811559, 1.1525675957811559, 200 * GPa, densidad, 420 * MPa))       #barra n:364 
    ret.agregar_barra(Barra(15, 104, 1.161986094576775, 1.161986094576775, 200 * GPa, densidad, 420 * MPa))       #barra n:365 
    ret.agregar_barra(Barra(16, 105, 1.1689799975117419, 1.1689799975117419, 200 * GPa, densidad, 420 * MPa))       #barra n:366 
    ret.agregar_barra(Barra(17, 106, 1.1736422578272916, 1.1736422578272916, 200 * GPa, densidad, 420 * MPa))       #barra n:367 
    ret.agregar_barra(Barra(18, 107, 1.1759877542503427, 1.1759877542503427, 200 * GPa, densidad, 420 * MPa))       #barra n:368 
    ret.agregar_barra(Barra(19, 108, 1.1760913262958932, 1.1760913262958932, 200 * GPa, densidad, 420 * MPa))       #barra n:369 
    ret.agregar_barra(Barra(20, 109, 1.1739540245846571, 1.1739540245846571, 200 * GPa, densidad, 420 * MPa))       #barra n:370 
    ret.agregar_barra(Barra(21, 110, 1.1696392959597943, 1.1696392959597943, 200 * GPa, densidad, 420 * MPa))       #barra n:371 
    ret.agregar_barra(Barra(22, 111, 1.1631386816599036, 1.1631386816599036, 200 * GPa, densidad, 420 * MPa))       #barra n:372 
    ret.agregar_barra(Barra(23, 112, 1.154508372169552, 1.154508372169552, 200 * GPa, densidad, 420 * MPa))       #barra n:373 
    ret.agregar_barra(Barra(24, 113, 1.1437328348642732, 1.1437328348642732, 200 * GPa, densidad, 420 * MPa))       #barra n:374 
    ret.agregar_barra(Barra(25, 114, 1.1308637784380076, 1.1308637784380076, 200 * GPa, densidad, 420 * MPa))       #barra n:375 
    ret.agregar_barra(Barra(26, 115, 1.1158798782190056, 1.1158798782190056, 200 * GPa, densidad, 420 * MPa))       #barra n:376 
    ret.agregar_barra(Barra(27, 116, 1.0988303481896728, 1.0988303481896728, 200 * GPa, densidad, 420 * MPa))       #barra n:377 
    ret.agregar_barra(Barra(28, 117, 1.0796886232881606, 1.0796886232881606, 200 * GPa, densidad, 420 * MPa))       #barra n:378 
    ret.agregar_barra(Barra(29, 118, 1.0585029506108816, 1.0585029506108816, 200 * GPa, densidad, 420 * MPa))       #barra n:379 
    ret.agregar_barra(Barra(30, 119, 1.035241393361298, 1.035241393361298, 200 * GPa, densidad, 420 * MPa))       #barra n:380 
    ret.agregar_barra(Barra(31, 120, 1.0099525651067442, 1.0099525651067442, 200 * GPa, densidad, 420 * MPa))       #barra n:381 
    ret.agregar_barra(Barra(32, 121, 0.982598277492765, 0.982598277492765, 200 * GPa, densidad, 420 * MPa))       #barra n:382 
    ret.agregar_barra(Barra(33, 122, 0.9532286578654452, 0.9532286578654452, 200 * GPa, densidad, 420 * MPa))       #barra n:383 
    ret.agregar_barra(Barra(34, 123, 0.9217971568047517, 0.9217971568047517, 200 * GPa, densidad, 420 * MPa))       #barra n:384 
    ret.agregar_barra(Barra(35, 124, 0.8883561680143731, 0.8883561680143731, 200 * GPa, densidad, 420 * MPa))       #barra n:385 
    ret.agregar_barra(Barra(36, 125, 0.8528458904279353, 0.8528458904279353, 200 * GPa, densidad, 420 * MPa))       #barra n:386 
    ret.agregar_barra(Barra(37, 126, 0.8153198948679057, 0.8153198948679057, 200 * GPa, densidad, 420 * MPa))       #barra n:387 
    ret.agregar_barra(Barra(38, 127, 0.7756916097070641, 0.7756916097070641, 200 * GPa, densidad, 420 * MPa))       #barra n:388 
    ret.agregar_barra(Barra(39, 128, 0.7340035686984087, 0.7340035686984087, 200 * GPa, densidad, 420 * MPa))       #barra n:389 
    ret.agregar_barra(Barra(40, 129, 0.6900874603521305, 0.6900874603521305, 200 * GPa, densidad, 420 * MPa))       #barra n:390 
    ret.agregar_barra(Barra(41, 130, 0.6438618459352865, 0.6438618459352865, 200 * GPa, densidad, 420 * MPa))       #barra n:391 
    ret.agregar_barra(Barra(42, 131, 0.5945489623784215, 0.5945489623784215, 200 * GPa, densidad, 420 * MPa))       #barra n:392 
    ret.agregar_barra(Barra(43, 132, 0.5392393694446206, 0.5392393694446206, 200 * GPa, densidad, 420 * MPa))       #barra n:393 
    ret.agregar_barra(Barra(44, 133, 0.521853248463576, 0.521853248463576, 200 * GPa, densidad, 420 * MPa))       #barra n:394 
    ret.agregar_barra(Barra(46, 90, 0.7033779765809394, 0.7033779765809394, 200 * GPa, densidad, 420 * MPa))       #barra n:395 
    ret.agregar_barra(Barra(47, 91, 0.7845418460157579, 0.7845418460157579, 200 * GPa, densidad, 420 * MPa))       #barra n:396 
    ret.agregar_barra(Barra(48, 92, 0.8462255832245316, 0.8462255832245316, 200 * GPa, densidad, 420 * MPa))       #barra n:397 
    ret.agregar_barra(Barra(49, 93, 0.897160121772945, 0.897160121772945, 200 * GPa, densidad, 420 * MPa))       #barra n:398 
    ret.agregar_barra(Barra(50, 94, 0.940796391181252, 0.940796391181252, 200 * GPa, densidad, 420 * MPa))       #barra n:399 
    ret.agregar_barra(Barra(51, 95, 0.9788108498259482, 0.9788108498259482, 200 * GPa, densidad, 420 * MPa))       #barra n:400 
    ret.agregar_barra(Barra(52, 96, 1.012251503955048, 1.012251503955048, 200 * GPa, densidad, 420 * MPa))       #barra n:401 
    ret.agregar_barra(Barra(53, 97, 1.0417228265683307, 1.0417228265683307, 200 * GPa, densidad, 420 * MPa))       #barra n:402 
    ret.agregar_barra(Barra(54, 98, 1.067698262842648, 1.067698262842648, 200 * GPa, densidad, 420 * MPa))       #barra n:403 
    ret.agregar_barra(Barra(55, 99, 1.090454622495747, 1.090454622495747, 200 * GPa, densidad, 420 * MPa))       #barra n:404 
    ret.agregar_barra(Barra(56, 100, 1.1102542265614037, 1.1102542265614037, 200 * GPa, densidad, 420 * MPa))       #barra n:405 
    ret.agregar_barra(Barra(57, 101, 1.1272392404066336, 1.1272392404066336, 200 * GPa, densidad, 420 * MPa))       #barra n:406 
    ret.agregar_barra(Barra(58, 102, 1.1415753230441306, 1.1415753230441306, 200 * GPa, densidad, 420 * MPa))       #barra n:407 
    ret.agregar_barra(Barra(59, 103, 1.1533390334643137, 1.1533390334643137, 200 * GPa, densidad, 420 * MPa))       #barra n:408 
    ret.agregar_barra(Barra(60, 104, 1.1626453597349153, 1.1626453597349153, 200 * GPa, densidad, 420 * MPa))       #barra n:409 
    ret.agregar_barra(Barra(61, 105, 1.1695350345511546, 1.1695350345511546, 200 * GPa, densidad, 420 * MPa))       #barra n:410 
    ret.agregar_barra(Barra(62, 106, 1.1740939689226848, 1.1740939689226848, 200 * GPa, densidad, 420 * MPa))       #barra n:411 
    ret.agregar_barra(Barra(63, 107, 1.1763415277300668, 1.1763415277300668, 200 * GPa, densidad, 420 * MPa))       #barra n:412 
    ret.agregar_barra(Barra(64, 108, 1.1763458917973457, 1.1763458917973457, 200 * GPa, densidad, 420 * MPa))       #barra n:413 
    ret.agregar_barra(Barra(65, 109, 1.1741127119781467, 1.1741127119781467, 200 * GPa, densidad, 420 * MPa))       #barra n:414 
    ret.agregar_barra(Barra(66, 110, 1.1696988705718923, 1.1696988705718923, 200 * GPa, densidad, 420 * MPa))       #barra n:415 
    ret.agregar_barra(Barra(67, 111, 1.163100541202737, 1.163100541202737, 200 * GPa, densidad, 420 * MPa))       #barra n:416 
    ret.agregar_barra(Barra(68, 112, 1.1543672506397784, 1.1543672506397784, 200 * GPa, densidad, 420 * MPa))       #barra n:417 
    ret.agregar_barra(Barra(69, 113, 1.1434880538792211, 1.1434880538792211, 200 * GPa, densidad, 420 * MPa))       #barra n:418 
    ret.agregar_barra(Barra(70, 114, 1.130507642391604, 1.130507642391604, 200 * GPa, densidad, 420 * MPa))       #barra n:419 
    ret.agregar_barra(Barra(71, 115, 1.1154091630685197, 1.1154091630685197, 200 * GPa, densidad, 420 * MPa))       #barra n:420 
    ret.agregar_barra(Barra(72, 116, 1.0982341240910314, 1.0982341240910314, 200 * GPa, densidad, 420 * MPa))       #barra n:421 
    ret.agregar_barra(Barra(73, 117, 1.0789601151682038, 1.0789601151682038, 200 * GPa, densidad, 420 * MPa))       #barra n:422 
    ret.agregar_barra(Barra(74, 118, 1.0576265092148862, 1.0576265092148862, 200 * GPa, densidad, 420 * MPa))       #barra n:423 
    ret.agregar_barra(Barra(75, 119, 1.0342047938921781, 1.0342047938921781, 200 * GPa, densidad, 420 * MPa))       #barra n:424 
    ret.agregar_barra(Barra(76, 120, 1.0087326388320674, 1.0087326388320674, 200 * GPa, densidad, 420 * MPa))       #barra n:425 
    ret.agregar_barra(Barra(77, 121, 0.9811735780229767, 0.9811735780229767, 200 * GPa, densidad, 420 * MPa))       #barra n:426 
    ret.agregar_barra(Barra(78, 122, 0.9515628332201427, 0.9515628332201427, 200 * GPa, densidad, 420 * MPa))       #barra n:427 
    ret.agregar_barra(Barra(79, 123, 0.9198514607432333, 0.9198514607432333, 200 * GPa, densidad, 420 * MPa))       #barra n:428 
    ret.agregar_barra(Barra(80, 124, 0.88606837446776, 0.88606837446776, 200 * GPa, densidad, 420 * MPa))       #barra n:429 
    ret.agregar_barra(Barra(81, 125, 0.850140161815705, 0.850140161815705, 200 * GPa, densidad, 420 * MPa))       #barra n:430 
    ret.agregar_barra(Barra(82, 126, 0.8120743680648541, 0.8120743680648541, 200 * GPa, densidad, 420 * MPa))       #barra n:431 
    ret.agregar_barra(Barra(83, 127, 0.7717338196541983, 0.7717338196541983, 200 * GPa, densidad, 420 * MPa))       #barra n:432 
    ret.agregar_barra(Barra(84, 128, 0.7290348219106124, 0.7290348219106124, 200 * GPa, densidad, 420 * MPa))       #barra n:433 
    ret.agregar_barra(Barra(85, 129, 0.6835812554437095, 0.6835812554437095, 200 * GPa, densidad, 420 * MPa))       #barra n:434 
    ret.agregar_barra(Barra(86, 130, 0.6346537268537769, 0.6346537268537769, 200 * GPa, densidad, 420 * MPa))       #barra n:435 
    ret.agregar_barra(Barra(87, 131, 0.5843161509733461, 0.5843161509733461, 200 * GPa, densidad, 420 * MPa))       #barra n:436 
    ret.agregar_barra(Barra(88, 132, 0.5843144224141278, 0.5843144224141278, 200 * GPa, densidad, 420 * MPa))       #barra n:437 
    ret.agregar_barra(Barra(89, 133, 0.5230019107067932, 0.5230019107067932, 200 * GPa, densidad, 420 * MPa))       #barra n:438 
    ret.agregar_barra(Barra(0, 134, 0.5405769225142156, 0.5405769225142156, 200 * GPa, densidad, 420 * MPa))       #barra n:439 
    ret.agregar_barra(Barra(1, 135, 0.6967975169434923, 0.6967975169434923, 200 * GPa, densidad, 420 * MPa))       #barra n:440 
    ret.agregar_barra(Barra(2, 136, 0.7801352081179481, 0.7801352081179481, 200 * GPa, densidad, 420 * MPa))       #barra n:441 
    ret.agregar_barra(Barra(3, 137, 0.8427672655378364, 0.8427672655378364, 200 * GPa, densidad, 420 * MPa))       #barra n:442 
    ret.agregar_barra(Barra(4, 138, 0.8943361275001669, 0.8943361275001669, 200 * GPa, densidad, 420 * MPa))       #barra n:443 
    ret.agregar_barra(Barra(5, 139, 0.9383744092163027, 0.9383744092163027, 200 * GPa, densidad, 420 * MPa))       #barra n:444 
    ret.agregar_barra(Barra(6, 140, 0.9767369596031936, 0.9767369596031936, 200 * GPa, densidad, 420 * MPa))       #barra n:445 
    ret.agregar_barra(Barra(7, 141, 1.0104172273424676, 1.0104172273424676, 200 * GPa, densidad, 420 * MPa))       #barra n:446 
    ret.agregar_barra(Barra(8, 142, 1.0401253563627266, 1.0401253563627266, 200 * GPa, densidad, 420 * MPa))       #barra n:447 
    ret.agregar_barra(Barra(9, 143, 1.0662675535847983, 1.0662675535847983, 200 * GPa, densidad, 420 * MPa))       #barra n:448 
    ret.agregar_barra(Barra(10, 144, 1.0892044883764354, 1.0892044883764354, 200 * GPa, densidad, 420 * MPa))       #barra n:449 
    ret.agregar_barra(Barra(11, 145, 1.109131617236371, 1.109131617236371, 200 * GPa, densidad, 420 * MPa))       #barra n:450 
    ret.agregar_barra(Barra(12, 146, 1.1262649685184867, 1.1262649685184867, 200 * GPa, densidad, 420 * MPa))       #barra n:451 
    ret.agregar_barra(Barra(13, 147, 1.1407054582436342, 1.1407054582436342, 200 * GPa, densidad, 420 * MPa))       #barra n:452 
    ret.agregar_barra(Barra(14, 148, 1.1525979754693927, 1.1525979754693927, 200 * GPa, densidad, 420 * MPa))       #barra n:453 
    ret.agregar_barra(Barra(15, 149, 1.1619946766851705, 1.1619946766851705, 200 * GPa, densidad, 420 * MPa))       #barra n:454 
    ret.agregar_barra(Barra(16, 150, 1.1690013977458944, 1.1690013977458944, 200 * GPa, densidad, 420 * MPa))       #barra n:455 
    ret.agregar_barra(Barra(17, 151, 1.1736425143774352, 1.1736425143774352, 200 * GPa, densidad, 420 * MPa))       #barra n:456 
    ret.agregar_barra(Barra(18, 152, 1.1760007798637035, 1.1760007798637035, 200 * GPa, densidad, 420 * MPa))       #barra n:457 
    ret.agregar_barra(Barra(19, 153, 1.1760834311616803, 1.1760834311616803, 200 * GPa, densidad, 420 * MPa))       #barra n:458 
    ret.agregar_barra(Barra(20, 154, 1.1739589212563057, 1.1739589212563057, 200 * GPa, densidad, 420 * MPa))       #barra n:459 
    ret.agregar_barra(Barra(21, 155, 1.1696231001195443, 1.1696231001195443, 200 * GPa, densidad, 420 * MPa))       #barra n:460 
    ret.agregar_barra(Barra(22, 156, 1.1631353454074609, 1.1631353454074609, 200 * GPa, densidad, 420 * MPa))       #barra n:461 
    ret.agregar_barra(Barra(23, 157, 1.154483385885677, 1.154483385885677, 200 * GPa, densidad, 420 * MPa))       #barra n:462 
    ret.agregar_barra(Barra(24, 158, 1.143720844683815, 1.143720844683815, 200 * GPa, densidad, 420 * MPa))       #barra n:463 
    ret.agregar_barra(Barra(25, 159, 1.1308291211694381, 1.1308291211694381, 200 * GPa, densidad, 420 * MPa))       #barra n:464 
    ret.agregar_barra(Barra(26, 160, 1.115858397606928, 1.115858397606928, 200 * GPa, densidad, 420 * MPa))       #barra n:465 
    ret.agregar_barra(Barra(27, 161, 1.0987846404726538, 1.0987846404726538, 200 * GPa, densidad, 420 * MPa))       #barra n:466 
    ret.agregar_barra(Barra(28, 162, 1.0796562986897582, 1.0796562986897582, 200 * GPa, densidad, 420 * MPa))       #barra n:467 
    ret.agregar_barra(Barra(29, 163, 1.0584440689941386, 1.0584440689941386, 200 * GPa, densidad, 420 * MPa))       #barra n:468 
    ret.agregar_barra(Barra(30, 164, 1.0351960897394161, 1.0351960897394161, 200 * GPa, densidad, 420 * MPa))       #barra n:469 
    ret.agregar_barra(Barra(31, 165, 1.0098772752532907, 1.0098772752532907, 200 * GPa, densidad, 420 * MPa))       #barra n:470 
    ret.agregar_barra(Barra(32, 166, 0.982536619419558, 0.982536619419558, 200 * GPa, densidad, 420 * MPa))       #barra n:471 
    ret.agregar_barra(Barra(33, 167, 0.9531317864056095, 0.9531317864056095, 200 * GPa, densidad, 420 * MPa))       #barra n:472 
    ret.agregar_barra(Barra(34, 168, 0.9217135418578357, 0.9217135418578357, 200 * GPa, densidad, 420 * MPa))       #barra n:473 
    ret.agregar_barra(Barra(35, 169, 0.8882289234029177, 0.8882289234029177, 200 * GPa, densidad, 420 * MPa))       #barra n:474 
    ret.agregar_barra(Barra(36, 170, 0.8527303165924878, 0.8527303165924878, 200 * GPa, densidad, 420 * MPa))       #barra n:475 
    ret.agregar_barra(Barra(37, 171, 0.8151456828654108, 0.8151456828654108, 200 * GPa, densidad, 420 * MPa))       #barra n:476 
    ret.agregar_barra(Barra(38, 172, 0.7755236465940747, 0.7755236465940747, 200 * GPa, densidad, 420 * MPa))       #barra n:477 
    ret.agregar_barra(Barra(39, 173, 0.7337450226599243, 0.7337450226599243, 200 * GPa, densidad, 420 * MPa))       #barra n:478 
    ret.agregar_barra(Barra(40, 174, 0.6898111228426127, 0.6898111228426127, 200 * GPa, densidad, 420 * MPa))       #barra n:479 
    ret.agregar_barra(Barra(41, 175, 0.6433811997604947, 0.6433811997604947, 200 * GPa, densidad, 420 * MPa))       #barra n:480 
    ret.agregar_barra(Barra(42, 176, 0.5934465887543751, 0.5934465887543751, 200 * GPa, densidad, 420 * MPa))       #barra n:481 
    ret.agregar_barra(Barra(43, 177, 0.5843149648996823, 0.5843149648996823, 200 * GPa, densidad, 420 * MPa))       #barra n:482 
    ret.agregar_barra(Barra(45, 134, 0.5843144237964462, 0.5843144237964462, 200 * GPa, densidad, 420 * MPa))       #barra n:483 
    ret.agregar_barra(Barra(46, 135, 0.703536254045944, 0.703536254045944, 200 * GPa, densidad, 420 * MPa))       #barra n:484 
    ret.agregar_barra(Barra(47, 136, 0.7846735806315837, 0.7846735806315837, 200 * GPa, densidad, 420 * MPa))       #barra n:485 
    ret.agregar_barra(Barra(48, 137, 0.8462981060944376, 0.8462981060944376, 200 * GPa, densidad, 420 * MPa))       #barra n:486 
    ret.agregar_barra(Barra(49, 138, 0.8972402566674715, 0.8972402566674715, 200 * GPa, densidad, 420 * MPa))       #barra n:487 
    ret.agregar_barra(Barra(50, 139, 0.9408407814175421, 0.9408407814175421, 200 * GPa, densidad, 420 * MPa))       #barra n:488 
    ret.agregar_barra(Barra(51, 140, 0.9788658153244848, 0.9788658153244848, 200 * GPa, densidad, 420 * MPa))       #barra n:489 
    ret.agregar_barra(Barra(52, 141, 1.0122789460217567, 1.0122789460217567, 200 * GPa, densidad, 420 * MPa))       #barra n:490 
    ret.agregar_barra(Barra(53, 142, 1.041761237681074, 1.041761237681074, 200 * GPa, densidad, 420 * MPa))       #barra n:491 
    ret.agregar_barra(Barra(54, 143, 1.0677133222673385, 1.0677133222673385, 200 * GPa, densidad, 420 * MPa))       #barra n:492 
    ret.agregar_barra(Barra(55, 144, 1.090480538261375, 1.090480538261375, 200 * GPa, densidad, 420 * MPa))       #barra n:493 
    ret.agregar_barra(Barra(56, 145, 1.1102592046815707, 1.1102592046815707, 200 * GPa, densidad, 420 * MPa))       #barra n:494 
    ret.agregar_barra(Barra(57, 146, 1.1272548549086534, 1.1272548549086534, 200 * GPa, densidad, 420 * MPa))       #barra n:495 
    ret.agregar_barra(Barra(58, 147, 1.1415714728139368, 1.1415714728139368, 200 * GPa, densidad, 420 * MPa))       #barra n:496 
    ret.agregar_barra(Barra(59, 148, 1.1533455873261191, 1.1533455873261191, 200 * GPa, densidad, 420 * MPa))       #barra n:497 
    ret.agregar_barra(Barra(60, 149, 1.1626333195702987, 1.1626333195702987, 200 * GPa, densidad, 420 * MPa))       #barra n:498 
    ret.agregar_barra(Barra(61, 150, 1.1695332020882714, 1.1695332020882714, 200 * GPa, densidad, 420 * MPa))       #barra n:499 
    ret.agregar_barra(Barra(62, 151, 1.1740739556497075, 1.1740739556497075, 200 * GPa, densidad, 420 * MPa))       #barra n:500 
    ret.agregar_barra(Barra(63, 152, 1.1763315689885157, 1.1763315689885157, 200 * GPa, densidad, 420 * MPa))       #barra n:501 
    ret.agregar_barra(Barra(64, 153, 1.1763178032266386, 1.1763178032266386, 200 * GPa, densidad, 420 * MPa))       #barra n:502 
    ret.agregar_barra(Barra(65, 154, 1.1740945459765828, 1.1740945459765828, 200 * GPa, densidad, 420 * MPa))       #barra n:503 
    ret.agregar_barra(Barra(66, 155, 1.169662272420757, 1.169662272420757, 200 * GPa, densidad, 420 * MPa))       #barra n:504 
    ret.agregar_barra(Barra(67, 156, 1.1630737680425267, 1.1630737680425267, 200 * GPa, densidad, 420 * MPa))       #barra n:505 
    ret.agregar_barra(Barra(68, 157, 1.1543213788849906, 1.1543213788849906, 200 * GPa, densidad, 420 * MPa))       #barra n:506 
    ret.agregar_barra(Barra(69, 158, 1.143451901245495, 1.143451901245495, 200 * GPa, densidad, 420 * MPa))       #barra n:507 
    ret.agregar_barra(Barra(70, 159, 1.1304512960100834, 1.1304512960100834, 200 * GPa, densidad, 420 * MPa))       #barra n:508 
    ret.agregar_barra(Barra(71, 160, 1.1153624085511615, 1.1153624085511615, 200 * GPa, densidad, 420 * MPa))       #barra n:509 
    ret.agregar_barra(Barra(72, 161, 1.0981655299828605, 1.0981655299828605, 200 * GPa, densidad, 420 * MPa))       #barra n:510 
    ret.agregar_barra(Barra(73, 162, 1.0789009010703023, 1.0789009010703023, 200 * GPa, densidad, 420 * MPa))       #barra n:511 
    ret.agregar_barra(Barra(74, 163, 1.0575430366604035, 1.0575430366604035, 200 * GPa, densidad, 420 * MPa))       #barra n:512 
    ret.agregar_barra(Barra(75, 164, 1.034130303096204, 1.034130303096204, 200 * GPa, densidad, 420 * MPa))       #barra n:513 
    ret.agregar_barra(Barra(76, 165, 1.0086303129995957, 1.0086303129995957, 200 * GPa, densidad, 420 * MPa))       #barra n:514 
    ret.agregar_barra(Barra(77, 166, 0.981079423052595, 0.981079423052595, 200 * GPa, densidad, 420 * MPa))       #barra n:515 
    ret.agregar_barra(Barra(78, 167, 0.9514353461544058, 0.9514353461544058, 200 * GPa, densidad, 420 * MPa))       #barra n:516 
    ret.agregar_barra(Barra(79, 168, 0.9197304273683886, 0.9197304273683886, 200 * GPa, densidad, 420 * MPa))       #barra n:517 
    ret.agregar_barra(Barra(80, 169, 0.8859049740880968, 0.8859049740880968, 200 * GPa, densidad, 420 * MPa))       #barra n:518 
    ret.agregar_barra(Barra(81, 170, 0.8499792814080862, 0.8499792814080862, 200 * GPa, densidad, 420 * MPa))       #barra n:519 
    ret.agregar_barra(Barra(82, 171, 0.8118545373521427, 0.8118545373521427, 200 * GPa, densidad, 420 * MPa))       #barra n:520 
    ret.agregar_barra(Barra(83, 172, 0.7715061818976305, 0.7715061818976305, 200 * GPa, densidad, 420 * MPa))       #barra n:521 
    ret.agregar_barra(Barra(84, 173, 0.7287107784760937, 0.7287107784760937, 200 * GPa, densidad, 420 * MPa))       #barra n:522 
    ret.agregar_barra(Barra(85, 174, 0.6832121854234886, 0.6832121854234886, 200 * GPa, densidad, 420 * MPa))       #barra n:523 
    ret.agregar_barra(Barra(86, 175, 0.634015615910634, 0.634015615910634, 200 * GPa, densidad, 420 * MPa))       #barra n:524 
    ret.agregar_barra(Barra(87, 176, 0.5777428787472327, 0.5777428787472327, 200 * GPa, densidad, 420 * MPa))       #barra n:525 
    ret.agregar_barra(Barra(88, 177, 0.5843262045581223, 0.5843262045581223, 200 * GPa, densidad, 420 * MPa))       #barra n:526 
    ret.agregar_barra(Barra(1, 134, 0.7033675358099601, 0.7033675358099601, 200 * GPa, densidad, 420 * MPa))       #barra n:527 
    ret.agregar_barra(Barra(2, 135, 0.7845620366963053, 0.7845620366963053, 200 * GPa, densidad, 420 * MPa))       #barra n:528 
    ret.agregar_barra(Barra(3, 136, 0.8462106725907274, 0.8462106725907274, 200 * GPa, densidad, 420 * MPa))       #barra n:529 
    ret.agregar_barra(Barra(4, 137, 0.8971732929075312, 0.8971732929075312, 200 * GPa, densidad, 420 * MPa))       #barra n:530 
    ret.agregar_barra(Barra(5, 138, 0.9407845463659431, 0.9407845463659431, 200 * GPa, densidad, 420 * MPa))       #barra n:531 
    ret.agregar_barra(Barra(6, 139, 0.9788217596852791, 0.9788217596852791, 200 * GPa, densidad, 420 * MPa))       #barra n:532 
    ret.agregar_barra(Barra(7, 140, 1.0122413069747687, 1.0122413069747687, 200 * GPa, densidad, 420 * MPa))       #barra n:533 
    ret.agregar_barra(Barra(8, 141, 1.0417324654503546, 1.0417324654503546, 200 * GPa, densidad, 420 * MPa))       #barra n:534 
    ret.agregar_barra(Barra(9, 142, 1.0676890600390956, 1.0676890600390956, 200 * GPa, densidad, 420 * MPa))       #barra n:535 
    ret.agregar_barra(Barra(10, 143, 1.0904634722865278, 1.0904634722865278, 200 * GPa, densidad, 420 * MPa))       #barra n:536 
    ret.agregar_barra(Barra(11, 144, 1.1102456644826775, 1.1102456644826775, 200 * GPa, densidad, 420 * MPa))       #barra n:537 
    ret.agregar_barra(Barra(12, 145, 1.1272475687765344, 1.1272475687765344, 200 * GPa, densidad, 420 * MPa))       #barra n:538 
    ret.agregar_barra(Barra(13, 146, 1.141567178139511, 1.141567178139511, 200 * GPa, densidad, 420 * MPa))       #barra n:539 
    ret.agregar_barra(Barra(14, 147, 1.1533470291481087, 1.1533470291481087, 200 * GPa, densidad, 420 * MPa))       #barra n:540 
    ret.agregar_barra(Barra(15, 148, 1.1626374754926743, 1.1626374754926743, 200 * GPa, densidad, 420 * MPa))       #barra n:541 
    ret.agregar_barra(Barra(16, 149, 1.1695428364036724, 1.1695428364036724, 200 * GPa, densidad, 420 * MPa))       #barra n:542 
    ret.agregar_barra(Barra(17, 150, 1.174086215785944, 1.174086215785944, 200 * GPa, densidad, 420 * MPa))       #barra n:543 
    ret.agregar_barra(Barra(18, 151, 1.1763492505359205, 1.1763492505359205, 200 * GPa, densidad, 420 * MPa))       #barra n:544 
    ret.agregar_barra(Barra(19, 152, 1.1763381685276433, 1.1763381685276433, 200 * GPa, densidad, 420 * MPa))       #barra n:545 
    ret.agregar_barra(Barra(20, 153, 1.174120460585013, 1.174120460585013, 200 * GPa, densidad, 420 * MPa))       #barra n:546 
    ret.agregar_barra(Barra(21, 154, 1.1696910685347297, 1.1696910685347297, 200 * GPa, densidad, 420 * MPa))       #barra n:547 
    ret.agregar_barra(Barra(22, 155, 1.163108418993335, 1.163108418993335, 200 * GPa, densidad, 420 * MPa))       #barra n:548 
    ret.agregar_barra(Barra(23, 156, 1.1543592623599663, 1.1543592623599663, 200 * GPa, densidad, 420 * MPa))       #barra n:549 
    ret.agregar_barra(Barra(24, 157, 1.1434961746427263, 1.1434961746427263, 200 * GPa, densidad, 420 * MPa))       #barra n:550 
    ret.agregar_barra(Barra(25, 158, 1.1304993586286658, 1.1304993586286658, 200 * GPa, densidad, 420 * MPa))       #barra n:551 
    ret.agregar_barra(Barra(26, 159, 1.1154176512097314, 1.1154176512097314, 200 * GPa, densidad, 420 * MPa))       #barra n:552 
    ret.agregar_barra(Barra(27, 160, 1.0982253960689152, 1.0982253960689152, 200 * GPa, densidad, 420 * MPa))       #barra n:553 
    ret.agregar_barra(Barra(28, 161, 1.078969137691731, 1.078969137691731, 200 * GPa, densidad, 420 * MPa))       #barra n:554 
    ret.agregar_barra(Barra(29, 162, 1.0576171391800346, 1.0576171391800346, 200 * GPa, densidad, 420 * MPa))       #barra n:555 
    ret.agregar_barra(Barra(30, 163, 1.0342145704893624, 1.0342145704893624, 200 * GPa, densidad, 420 * MPa))       #barra n:556 
    ret.agregar_barra(Barra(31, 164, 1.008722370144636, 1.008722370144636, 200 * GPa, densidad, 420 * MPa))       #barra n:557 
    ret.agregar_barra(Barra(32, 165, 0.9811844343677689, 0.9811844343677689, 200 * GPa, densidad, 420 * MPa))       #barra n:558 
    ret.agregar_barra(Barra(33, 166, 0.9515512645518449, 0.9515512645518449, 200 * GPa, densidad, 420 * MPa))       #barra n:559 
    ret.agregar_barra(Barra(34, 167, 0.9198639014973962, 0.9198639014973962, 200 * GPa, densidad, 420 * MPa))       #barra n:560 
    ret.agregar_barra(Barra(35, 168, 0.8860548393181829, 0.8860548393181829, 200 * GPa, densidad, 420 * MPa))       #barra n:561 
    ret.agregar_barra(Barra(36, 169, 0.8501550830173581, 0.8501550830173581, 200 * GPa, densidad, 420 * MPa))       #barra n:562 
    ret.agregar_barra(Barra(37, 170, 0.8120576299225244, 0.8120576299225244, 200 * GPa, densidad, 420 * MPa))       #barra n:563 
    ret.agregar_barra(Barra(38, 171, 0.7717530487004265, 0.7717530487004265, 200 * GPa, densidad, 420 * MPa))       #barra n:564 
    ret.agregar_barra(Barra(39, 172, 0.7290120764050859, 0.7290120764050859, 200 * GPa, densidad, 420 * MPa))       #barra n:565 
    ret.agregar_barra(Barra(40, 173, 0.6836104301072918, 0.6836104301072918, 200 * GPa, densidad, 420 * MPa))       #barra n:566 
    ret.agregar_barra(Barra(41, 174, 0.6346236908787972, 0.6346236908787972, 200 * GPa, densidad, 420 * MPa))       #barra n:567 
    ret.agregar_barra(Barra(42, 175, 0.5791815772700588, 0.5791815772700588, 200 * GPa, densidad, 420 * MPa))       #barra n:568 
    ret.agregar_barra(Barra(43, 176, 0.5392393694446554, 0.5392393694446554, 200 * GPa, densidad, 420 * MPa))       #barra n:569 
    ret.agregar_barra(Barra(44, 177, 0.5266785880845203, 0.5266785880845203, 200 * GPa, densidad, 420 * MPa))       #barra n:570 
    ret.agregar_barra(Barra(46, 134, 0.6965568731338622, 0.6965568731338622, 200 * GPa, densidad, 420 * MPa))       #barra n:571 
    ret.agregar_barra(Barra(47, 135, 0.7799658138433887, 0.7799658138433887, 200 * GPa, densidad, 420 * MPa))       #barra n:572 
    ret.agregar_barra(Barra(48, 136, 0.8426391184844984, 0.8426391184844984, 200 * GPa, densidad, 420 * MPa))       #barra n:573 
    ret.agregar_barra(Barra(49, 137, 0.8942292380169122, 0.8942292380169122, 200 * GPa, densidad, 420 * MPa))       #barra n:574 
    ret.agregar_barra(Barra(50, 138, 0.9382866871715925, 0.9382866871715925, 200 * GPa, densidad, 420 * MPa))       #barra n:575 
    ret.agregar_barra(Barra(51, 139, 0.9766601038022368, 0.9766601038022368, 200 * GPa, densidad, 420 * MPa))       #barra n:576 
    ret.agregar_barra(Barra(52, 140, 1.0103526845209734, 1.0103526845209734, 200 * GPa, densidad, 420 * MPa))       #barra n:577 
    ret.agregar_barra(Barra(53, 141, 1.0400677215813392, 1.0400677215813392, 200 * GPa, densidad, 420 * MPa))       #barra n:578 
    ret.agregar_barra(Barra(54, 142, 1.0662191098953413, 1.0662191098953413, 200 * GPa, densidad, 420 * MPa))       #barra n:579 
    ret.agregar_barra(Barra(55, 143, 1.08916100573188, 1.08916100573188, 200 * GPa, densidad, 420 * MPa))       #barra n:580 
    ret.agregar_barra(Barra(56, 144, 1.1090956291862297, 1.1090956291862297, 200 * GPa, densidad, 420 * MPa))       #barra n:581 
    ret.agregar_barra(Barra(57, 145, 1.1262328561540713, 1.1262328561540713, 200 * GPa, densidad, 420 * MPa))       #barra n:582 
    ret.agregar_barra(Barra(58, 146, 1.1406798389552053, 1.1406798389552053, 200 * GPa, densidad, 420 * MPa))       #barra n:583 
    ret.agregar_barra(Barra(59, 147, 1.1525756009793038, 1.1525756009793038, 200 * GPa, densidad, 420 * MPa))       #barra n:584 
    ret.agregar_barra(Barra(60, 148, 1.1619781992045186, 1.1619781992045186, 200 * GPa, densidad, 420 * MPa))       #barra n:585 
    ret.agregar_barra(Barra(61, 149, 1.1689878063169195, 1.1689878063169195, 200 * GPa, densidad, 420 * MPa))       #barra n:586 
    ret.agregar_barra(Barra(62, 150, 1.1736345000232036, 1.1736345000232036, 200 * GPa, densidad, 420 * MPa))       #barra n:587 
    ret.agregar_barra(Barra(63, 151, 1.1759954797480627, 1.1759954797480627, 200 * GPa, densidad, 420 * MPa))       #barra n:588 
    ret.agregar_barra(Barra(64, 152, 1.1760835963188043, 1.1760835963188043, 200 * GPa, densidad, 420 * MPa))       #barra n:589 
    ret.agregar_barra(Barra(65, 153, 1.1739617749006293, 1.1739617749006293, 200 * GPa, densidad, 420 * MPa))       #barra n:590 
    ret.agregar_barra(Barra(66, 154, 1.1696314964002215, 1.1696314964002215, 200 * GPa, densidad, 420 * MPa))       #barra n:591 
    ret.agregar_barra(Barra(67, 155, 1.1631465561755354, 1.1631465561755354, 200 * GPa, densidad, 420 * MPa))       #barra n:592 
    ret.agregar_barra(Barra(68, 156, 1.154500391449505, 1.154500391449505, 200 * GPa, densidad, 420 * MPa))       #barra n:593 
    ret.agregar_barra(Barra(69, 157, 1.1437409507936918, 1.1437409507936918, 200 * GPa, densidad, 420 * MPa))       #barra n:594 
    ret.agregar_barra(Barra(70, 158, 1.1308554969546263, 1.1308554969546263, 200 * GPa, densidad, 420 * MPa))       #barra n:595 
    ret.agregar_barra(Barra(71, 159, 1.1158883638972854, 1.1158883638972854, 200 * GPa, densidad, 420 * MPa))       #barra n:596 
    ret.agregar_barra(Barra(72, 160, 1.098821627967627, 1.098821627967627, 200 * GPa, densidad, 420 * MPa))       #barra n:597 
    ret.agregar_barra(Barra(73, 161, 1.079697633192593, 1.079697633192593, 200 * GPa, densidad, 420 * MPa))       #barra n:598 
    ret.agregar_barra(Barra(74, 162, 1.0584935970184315, 1.0584935970184315, 200 * GPa, densidad, 420 * MPa))       #barra n:599 
    ret.agregar_barra(Barra(75, 163, 1.035251151566666, 1.035251151566666, 200 * GPa, densidad, 420 * MPa))       #barra n:600 
    ret.agregar_barra(Barra(76, 164, 1.0099423221049366, 1.0099423221049366, 200 * GPa, densidad, 420 * MPa))       #barra n:601 
    ret.agregar_barra(Barra(77, 165, 0.9826091050825916, 0.9826091050825916, 200 * GPa, densidad, 420 * MPa))       #barra n:602 
    ret.agregar_barra(Barra(78, 166, 0.953217133705476, 0.953217133705476, 200 * GPa, densidad, 420 * MPa))       #barra n:603 
    ret.agregar_barra(Barra(79, 167, 0.9218095396651517, 0.9218095396651517, 200 * GPa, densidad, 420 * MPa))       #barra n:604 
    ret.agregar_barra(Barra(80, 168, 0.888342716163419, 0.888342716163419, 200 * GPa, densidad, 420 * MPa))       #barra n:605 
    ret.agregar_barra(Barra(81, 169, 0.85286069639478, 0.85286069639478, 200 * GPa, densidad, 420 * MPa))       #barra n:606 
    ret.agregar_barra(Barra(82, 170, 0.8153033308254882, 0.8153033308254882, 200 * GPa, densidad, 420 * MPa))       #barra n:607 
    ret.agregar_barra(Barra(83, 171, 0.775710564113768, 0.775710564113768, 200 * GPa, densidad, 420 * MPa))       #barra n:608 
    ret.agregar_barra(Barra(84, 172, 0.7339813034252336, 0.7339813034252336, 200 * GPa, densidad, 420 * MPa))       #barra n:609 
    ret.agregar_barra(Barra(85, 173, 0.6901156341454762, 0.6901156341454762, 200 * GPa, densidad, 420 * MPa))       #barra n:610 
    ret.agregar_barra(Barra(86, 174, 0.6438337323608467, 0.6438337323608467, 200 * GPa, densidad, 420 * MPa))       #barra n:611 
    ret.agregar_barra(Barra(87, 175, 0.5947140633140591, 0.5947140633140591, 200 * GPa, densidad, 420 * MPa))       #barra n:612 
    ret.agregar_barra(Barra(88, 176, 0.584314416394987, 0.584314416394987, 200 * GPa, densidad, 420 * MPa))       #barra n:613 
    ret.agregar_barra(Barra(89, 177, 0.5256948165734985, 0.5256948165734985, 200 * GPa, densidad, 420 * MPa))       #barra n:614

    nodos_restrigidos=[0,43,44,45,88,89    ]    # Restricciones, agragar el numero de nodo restriccion en la lista
    for n in nodos_restrigidos:
        for i in range(3):
            ret.agregar_restriccion(n, i, 0)





                                            #Fuerzas a los nodos

    qL=400*kg/m**2
    A1=2.5*1 *m**2
    A2=5.0*1 *m**2
      
    for i in range(43):
        ret.agregar_fuerza(i+1, 2,  -qL*A2)
    for i in range(43):
        ret.agregar_fuerza(i+46, 2, -qL*A2)

    ret.agregar_fuerza(0, 2,  -qL*A1)
    ret.agregar_fuerza(44, 2, -qL*A1)
    ret.agregar_fuerza(45, 2, -qL*A1)
    ret.agregar_fuerza(89, 2, -qL*A1)




    peso1 = ret.calcular_peso_total()

    return ret
