##Tabla Sanidad
OPTIONS_B = [
    (1, 'Cepillo y crema dental'),
    (2, 'Ademas Ceda dental'),
    (3, 'No'),
    (3, 'No refiere'),
    (5, 'Sin dato'),
]

OPTIONS_HE = [
    (1, 'Cepillo de diente'),
    (2, 'Máquina de afeitar'),
    (3, 'Toallas'),
    (3, 'No'),
    (5, 'No refiere'),
    (6, 'Sin dato'),
]

OPTIONS_H = [
    (1, 'Con agua y jabon'),
    (2, 'Solo agua'),
    (3, 'No'),
]

##Tabla de Bienestar

OPTIONS_AH = [
    (1, 'No'),
    (2, 'Medicina indigena'),
    (3, 'Homeopatía'),
    (3, 'Medicina tradicional china'),
    (5, 'Acupuntura'),
    (6, 'Quiropraxia'),
    (7, 'Otro'),
    (8, 'Sin dato'),
]

OPTIONS_LS = [
    (1, 'Sedenatrismo'),
    (2, 'Actividad Fisica'),
    (3, 'Consumo de cigarrillo'),
    (3, 'Consumo de Acohol'),
    (5, 'Consumo de otras SPA'),
    (6, 'Inadecuadas Prácticas alimentarias y nutricionales'),
]

OPTIONS_TR = [
    (1, 'Permanente'),
    (2, 'Permanece Fuera de la ciudad'),
    (3, 'Sin dato'),
]

OPTIONS_T = [
    (1, 'Propia'),
    (2, 'Propia Pagando'),
    (3, 'Anticresis'),
    (3, 'Arriendo'),
    (5, 'Subarriendo'),
    (6, 'Prestada sin costo'),
]

#  Tabla de Miembro
ROLE = [
    (1, 'Jefe(a) de Familia'),
    (2, 'Conyuge o Compañero(a)'),
    (3, 'Hijo'),
    (3, 'Hermano'),
    (5, 'Padre o Madre'),
    (6, 'Otros'),
]

SEX = [
    (1, 'Hombre'),
    (2, 'Mujer'),
    (3, 'Indeterminado'),
]

TYPE_ID = [
    ('CC', 'Cedula de ciudadania'),
    ('CD', 'Carnet diplomatico'),
    ('CE', 'Cedula extranjera'),
    ('MS', 'Menor sin identificaicon'),
    ('CN', 'Certificado de Nacido vivo'),
    ('PA', 'Pasaporte'),
    ('PE', 'Permiso especial de permanencia'),
    ('PT', 'Permiso de proteccion temporal'),
    ('RC', 'Registro civil'),
    ('TI', 'Tarjeta de identidad')
]

##

OPTIONS_SW = [
    (1, 'Recolección por parte del servicio de aseo distrital o municipal'),
    (2, 'Enterramiento'),
    (3, 'Quema a campo abierto'),
    (3, 'Disposición en fuentes de agua cercana'),
    (5, 'Disposición a campo abierto'),
    (6, 'Otro'),
]

OPTIONS_W = [
    (1, 'Alcantarillado'),
    (2, 'Pozo séptico'),
    (3, 'Campo de oxidación'),
    (3, 'Biofiltro'),
    (5, 'Fuente hídrica'),
    (6, 'Campo abierto'),
    (7, 'Otro')
]

OPTIONS_DS = [
    (1, 'Sanitario conectado al alcantarillado'),
    (2, 'Sanitario y letrina'),
    (3, 'Sanitario conectado a pozo séptico'),
    (3, 'Sanitario ecológico seco'),
    (5, 'Sanitario sin conexión'),
    (6, 'Sanitario con disposición a fuente hídrica'),
    (7, 'Campo abierto'),
    (8, 'Otro')
]


OPTIONS_SS = [
    (1, 'Acueducto administrado por empresa prestadora (ESP)'),
    (2, 'Agua embotellada o en bolsa'),
    (3, 'Acueducto veredal o comunitario'),
    (3, 'Pila pública'),
    (5, 'Carro tanque'),
    (6, 'Abasto con distribución comunitaria'),
    (7, 'Pozo con bomba'),
    (8, 'Pozo sin bomba, aljibe, jagüey o barreno'),
    (9, 'Laguna o jagüey'),
    (10, 'Río, quebrada, manantial o nacimiento'),
    (11, 'Aguas lluvias'),
    (12, 'Aguatero'),
    (13, 'Otro')
]

OPTIONS_A = [
    (1, 'Perros'),
    (2, 'Gatos'),
    (3, 'Porcinos'),
    (3, 'Bóvidos: Búfalos, vacas, toros'),
    (5, 'Equidos: Asnos, mulas, caballos, burros'),
    (6, 'Ovinos / caprino'),
    (7, 'Aves de producción'),
    (8, 'Aves ornamentales'),
    (9, 'Peces ornamentales, hamster'),
    (10, 'Cobayos, conejos'),
    (11, 'Animales silvestres'),
    (12, 'Otro'),
    (13, 'Ninguno')
]


OPTIONS_OE = [
    (1, 'Cultivos'),
    (2, 'Apriscos'),
    (3, 'Porquerizas'),
    (4, 'Galpones'),
    (5, 'Terrenos baldíos'),
    (6, 'Presencia de Plagas: roedores, cucarachas, zancudos, etc.'),
    (7, 'Ruido o sonidos desagradables'),
    (8, 'Malos olores'),
    (9, 'Sitios satélites de disposición de excretas'),
    (10, 'Rellenos sanitarios/botaderos'),
    (11, 'Industrias Contaminantes (del sector energético, minero, transporte, construcción, manufacturera, entre otros)'),
    (12, 'Contaminación visual'),
    (13, 'Río o quebrada'),
    (14, 'Planta de tratamiento de agua residual'),
    (15, 'Extracción minera'),
    (16, 'Canales de agua lluvia'),
    (17, 'Vías de tráfico vehicular'),
    (18, 'Quemas a cielo abierto'),
    (19, 'Otro'),
    (20, 'Ninguno'),
]


OPTIONS_TV = [
    (1, 'Concreto'),
    (2, 'Teja de Barro'),
    (3, 'Fibrocemento'),
    (3, 'Zinc'),
    (5, 'Palma o Paja'),
    (6, 'Plastico'),
    (7, 'Desechos (cartón, lata, tela, sacos, etc)'),
    (8, 'Otro'),
    (9, 'Concreto'),
    (10, 'Teja de Barro'),
    (11, 'Fibrocemento'),
    (12, 'Zinc'),
    (13, 'Palma o Paja'),
]

OPTIONS_SI = [
    (1, 'Objetos cortantes o punzantes al alcance de los niños'),
    (2, 'Sustancias químicas al alcance de los niños'),
    (3, 'Medicamentos al alcance de los niños'),
    (3, 'Velas, velones, incienso encendido en la vivienda'),
    (5, 'Conexiones eléctricas en mal estado o sobrecargadas'),
    (6, 'Botones, canicas entre otros objetos pequeños o con piezas que puedan desmontarse, al alcance de los niños'),
    (7, 'Pasillos obstruidos con juguetes, sillas u otros objetos'),
    (8, 'Superficies resbaladizas, suelos con agua, grasas, aceites, entre otros'),
    (9, 'Tanques o recipientes de almacenamiento de agua sin tapa'),
    (10, 'Escaleras sin protección'),
]

OPTIONS_FS = [
    (1, 'Electricidad'),
    (2, 'Gas natural'),
    (3, 'Gas Licuado del petróleo (gas propano)'),
    (3, 'Leña, madera o carbón de leña'),
    (5, 'Petróleo, gasolina, kerosén, alcohol'),
    (6, 'Carbón mineral'),
    (7, 'Materiales de desecho'),
    (8, 'Otro'),
]

OPTIONS_AC = [
    (1, 'Medios de transporte (Buses, autos, camiones, lanchas, etc)'),
    (2, 'Parques, y áreas deportivas, Centros sociales y/o recreacionales'),
    (3, 'Instituciones educativas'),
    (3, 'Servicios de salud'),
    (5, 'Ninguna'),
]

OPTIONS_RM = [
    (1, 'Concreto'),
    (2, 'Teja de Barro'),
    (3, 'Fibrocemento'),
    (3, 'Zinc'),
    (5, 'Palma o Paja'),
    (6, 'Plastico'),
    (7, 'Desechos (cartón, lata, tela, sacos, etc)'),
    (8, 'Otro'),
]

OPTIONS_FM = [
    (1, 'Alfombra o tapete, mármol, parque, madera pulida y lacada'),
    (2, 'Baldosa, vinilo, tableta, ladrillo'),
    (3, 'Cemento, gravilla'),
    (3, 'Madera burda, madera en mal estado, tabla, tablón'),
    (5, 'Tierra o arena'),
    (6, 'Otro'),
]

OPTIONS_SM = [
    (1, 'Bloque, ladrillo, piedra, madera pulida'),
    (2, 'Tapia pisada, adobe'),
    (3, 'Bahareque'),
    (3, 'Material prefabricado'),
    (5, 'Madera burda, tabla, tablón'),
    (6, 'Guadua, casa, esterilla, otro vegetal'),
    (7, 'Zinc, tela, lona, cartón, latas, desechos, plástico'),
    (8, 'Otro'),
    (9, 'Sin pared'),
]

OPTIONS_HT = [
    (1, 'Casa'),
    (2, 'Casa indigena'),
    (3, 'Carpa'),
    (3, 'Apartamento'),
    (5, 'Pieza/Cuarto en Inclinato'),
    (6, 'Contenedor'),
    (7, 'Embarcacion'),
    (8, 'Vagon'),
    (9, 'Refugio Natural'),
    (10, 'Cueva'),
    (11, 'Puente'),
    (12, 'Otro'),
]

OPTIONS_SF = [
    (1, 'Cultiva'),
    (2, 'Cria de animales'),
    (3, 'Caseria'),
    (3, 'Recoleccion de alimentos'),
    (5, 'Trueque o intercambio'),
    (6, 'Compra'),
    (7, 'Asistencia del estado'),
    (8, 'Ayuda humanitaria'),
    (9, 'Otro'),
]

OPTIONS_PI = [
    (1, 'TP'),
    (2, 'Lepra'),
    (3, 'Escabiosis, enfermedades infecciosas en la piel u otras'),
    (3, 'Malaria'),
    (5, 'Dengue'),
    (6, 'Changas'),
    (7, 'Epatitis A'),
    (8, 'Algunas enfermedades hinmunoprevenible'),
]

OPTIONS_STR = [
    (1, 'Bajo bajo'),
    (2, 'Bajo'),
    (3, 'Medio-bajo'),
    (4, 'Medio'),
    (5, 'Medio-alto'),
    (6, 'Alto')
]

OPTIONS_ECO = [
    (1, 'Positivo'),
    (2, 'Tenue'),
    (3, 'Estresante'),
    (3, 'Fluye'),
    (5, 'Intenso'),
]

OPTIONS_ZT = [
    (1, 'Ausencia de sobrecarga'),
    (2, 'Sobrecarga ligera'),
    (3, 'Sobrecarga intensa'),
]

OPTIONS_YN = [
    (1, 'Si'),
    (2, 'No'),
]

OPTIONS_APGAR = [
    (1, 'Normal'),
    (2, 'Disfuncion leve'),
    (3, 'Disfuncion moderada'),
    (3, 'Disfuncion severa'),
]

OPTIONS_FG = [
    (1, 'Biologicos'),
    (2, 'Psicologicos'),
    (3, 'Sociales'),
]

OPTIONS_FT = [
    (1, 'Nuclear biparental'),
    (2, 'Nuclear monoparental'),
    (3, 'Extenso biparental'),
    (3, 'Extenso monoparental'),
    (5, 'Compuesto biparental'),
    (6, 'Compuesto monoparental'),
    (7, 'Uniparental'),
]
