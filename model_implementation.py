from models import *
from images import *

player = Fisherman()
player.add_images(fisherman_idle_img, fisherman_fishing_img) #fisherman_idle_img

fishArea1 = FishArea()
fishArea1.set_location_random()
fishArea2 = FishArea()
fishArea2.set_location_random()
fishArea3 = FishArea()
fishArea3.set_location_random()
fishArea4 = FishArea()
fishArea4.set_location_random()
fishArea5 = FishArea()
fishArea5.set_location_random()

'''
oceanWaves = Waves()
oceanWaves.set_location_random()
oceanWaves2 = Waves()
oceanWaves2.set_location_random()
oceanWaves3 = Waves()
oceanWaves3.set_location_random()
oceanWaves4 = Waves()
oceanWaves4.set_location_random()
oceanWaves5 = Waves()
oceanWaves5.set_location_random()
'''

enemy = Enemy()
enemy.add_images(shadow_moving1, shadow_moving2, shadow_moving3)

barrelPowerup = Powerup()
barrelPowerup.health_bonus = 1
barrelPowerup.add_image(barrel_img_more_left, barrel_img_left, barrel_img, barrel_img_right, barrel_img_more_right)

oarPowerup = Powerup()
oarPowerup.speed_bonus = 1
oarPowerup.add_image(oar_img_more_left, oar_img_left, oar_img, oar_img_right, oar_img_more_right)

buoyObstacle = BuoyObstacle()
buoyObstacle.add_image(buoy_img1, buoy_img2, buoy_img3, buoy_img_left1, buoy_img_left2, buoy_img_left3, buoy_img_right1, buoy_img_right2, buoy_img_right3)
buoyObstacle2 = BuoyObstacle()
buoyObstacle2.add_image(buoy_img1, buoy_img2, buoy_img3, buoy_img_left1, buoy_img_left2, buoy_img_left3, buoy_img_right1, buoy_img_right2, buoy_img_right3)

# CAMBRIAN PERIOD CREATURES #
p1c1 = Creature()
p1c2 = Creature()
p1c3 = Creature()
p1c4 = Creature()
p1c5 = Creature()

p1c1.add_image(redlichia_img)
p1c1.id = 0
p1c1.genus = 'Genus: Redlichia'
p1c1.family = 'Family: Redlichiidae'
p1c1.order = 'Order: Redlichiida'
p1c1.class_ = 'Class: Trilobita'
p1c1.phylum = 'Phylum: Arthropoda'
p1c1.prestige = 'Prestige: * / ***'
p1c1.min_length = 0.60
p1c1.max_length_increment = 80
p1c1.min_weight = 1.4
p1c1.max_weight_increment = 150
p1c1.description = 'Large to very large species of trilobite found in the Lower to Middle Cambrian. '
p1c1.description += 'These trilobites were deposit feeders and lived on the ocean floor. '
p1c1.description += 'One distinct species, Redlichia Rex, was especially large, carnivorous, and potentially cannibalistic.'
p1c1.rarity = 0

p1c2.add_image(peytoia_img)
p1c2.id = 1
p1c2.genus = 'Genus: Peytoia'
p1c2.family = 'Family: Hurdiidae'
p1c2.order = 'Order: Radiodonta'
p1c2.class_ = 'Class: Dinocaridida'
p1c2.phylum = 'Phylum: Arthropoda'
p1c2.prestige = 'Prestige: * / ***'
p1c2.min_length = 0.60
p1c2.max_length_increment = 60
p1c2.min_weight = 1.2
p1c2.max_weight_increment = 100
p1c2.description = 'Peytoia was a genus of an early diverging order of stem-group arthropods. '
p1c2.description += 'These creatures were fast-moving carnivores that had two frontal appendages with long spines. '
p1c2.description += 'It was first believed that the Peytoia used their frontal appendages to sift through sediment for food; '
p1c2.description += 'although, it was later determined that a more logical explanation would be that the Peytoia '
p1c2.description += 'was a predator and used their frontal appendages to capture slow-moving prey. '
p1c2.rarity = 0

p1c3.add_image(titanokorys_img)
p1c3.id = 2
p1c3.genus = 'Genus: Titanokorys'
p1c3.family = 'Family: Hurdiidae'
p1c3.order = 'Order: Radiodonta'
p1c3.class_ = 'Class: Dinocaridida'
p1c3.phylum = 'Phylum: Arthropoda'
p1c3.prestige = 'Prestige: ** / ***'
p1c3.min_length = 1
p1c3.max_length_increment = 75
p1c3.min_weight = 2.5
p1c3.max_weight_increment = 350
p1c3.description = 'This animal was the largest member of the Hurdiidae family and one of the largest animals of the Cambrian Period. '
p1c3.description += 'Titanokorys\' were primarily found in the Middle Cambrian and sifted through sand on the ocean floor to find prey. '
p1c3.description += 'It bears similar resemblance to another genus of the Hurdiidae family: the Cambroraster.'
p1c3.rarity = 1

p1c4.add_image(paradoxide_img)
p1c4.id = 3
p1c4.genus = 'Genus: Paradoxide'
p1c4.family = 'Family: Paradoxididae'
p1c4.order = 'Order: Redlichiida'
p1c4.class_ = 'Class: Trilobita'
p1c4.phylum = 'Phylum: Arthropoda'
p1c4.prestige = 'Prestige: ** / ***'
p1c4.min_length = 1
p1c4.max_length_increment = 50
p1c4.min_weight = 3
p1c4.max_weight_increment = 400
p1c4.description = 'Large to very large species of trilobite found all over the world during the Middle Cambrian. '
p1c4.rarity = 1

p1c5.add_image(anomalocaris_img)
p1c5.id = 4
p1c5.genus = 'Genus: Anomalocaris \'abnormal shrimp\''
p1c5.family = 'Family: Anomalocarididae'
p1c5.order = 'Order: Radiodonta'
p1c5.class_ = 'Class: Dinocaridida'
p1c5.phylum = 'Phylum: Arthropoda'
p1c5.prestige = 'Prestige: *** / ***'
p1c5.min_length = 0.80
p1c5.max_length_increment = 45
p1c5.min_weight = 2.25
p1c5.max_weight_increment = 100
p1c5.description = 'The first apex predator ever to exist. Anomalocaris dominated the Cambrian seas and '
p1c5.description += 'preyed on hard-bodied animals such as trilobites. '
p1c5.description += 'Their body structure included a row of swimming flaps on either side, large compound eyes, and two frontal appendages.'
p1c5.rarity = 2

# ORDOVICIAN PERIOD CREATURES #
p2c1 = Creature()
p2c2 = Creature()
p2c3 = Creature()
p2c4 = Creature()
p2c5 = Creature()

p2c1.add_image(arandaspis_img)
p2c1.id = 5
p2c1.genus = 'Genus: Arandaspis'
p2c1.family = 'Family: Arandaspididae'
p2c1.order = 'Order: Arandaspidida'
p2c1.class_ = 'Class: Pteraspidomorphi'
p2c1.phylum = 'Phylum: Chordata'
p2c1.prestige = 'Prestige: * / ***'
p2c1.min_length = 0.42
p2c1.max_length_increment = 21
p2c1.min_weight = 0.75
p2c1.max_weight_increment = 35
p2c1.description = 'Jawless fish from the Ordovician Period. '
p2c1.description += 'With no fins present, this fish used its flat tail to propel itself, similar to the movement of a tadpole.'
p2c1.rarity = 0

p2c2.add_image(aphetoceras_img)
p2c2.id = 6
p2c2.genus = 'Genus: Aphetoceras'
p2c2.family = 'Family: Estonioceratidae'
p2c2.order = 'Order: Tarphycerida'
p2c2.class_ = 'Class: Cephalopoda'
p2c2.phylum = 'Phylum: Mollusca'
p2c2.prestige = 'Prestige: * / ***'
p2c2.min_length = 0.80
p2c2.max_length_increment = 40
p2c2.min_weight = 4.4
p2c2.max_weight_increment = 220
p2c2.description = 'Cephalopod of the Lower Ordovician.'
p2c2.rarity = 0

p2c3.add_image(isoletus_img)
p2c3.id = 7
p2c3.genus = 'Genus: Isotelus'
p2c3.family = 'Family: Asaphidae'
p2c3.order = 'Order: Asaphida'
p2c3.class_ = 'Class: Trilobita'
p2c3.phylum = 'Phylum: Arthropoda'
p2c3.prestige = 'Prestige: ** / ***'
p2c3.min_length = 1
p2c3.max_length_increment = 30
p2c3.min_weight = 1.8
p2c3.max_weight_increment = 230
p2c3.description = 'Species of trilobite from the Middle to Upper Ordovician. '
p2c3.description += 'Includes a species (Isoletus rex) that currently holds the world record '
p2c3.description += 'for the largest complete trilobite fossil ever found. '
p2c3.rarity = 1

p2c4.add_image(megalograptus_img)
p2c4.id = 8
p2c4.genus = 'Genus: Megalograptus'
p2c4.family = 'Family: Megalograptidae'
p2c4.order = 'Order: Eurypterida'
p2c4.class_ = 'Class: [ ? ]'
p2c4.phylum = 'Phylum: Arthropoda'
p2c4.prestige = 'Prestige: ** / ***'
p2c4.min_length = 1.8
p2c4.max_length_increment = 120
p2c4.min_weight = 5
p2c4.max_weight_increment = 330
p2c4.description = 'Species of large predatory eurypterids that lived close to the shore. '
p2c4.rarity = 1

p2c5.add_image(aegirocassis_img)
p2c5.id = 9
p2c5.genus = 'Genus: Aegirocassis'
p2c5.family = 'Family: Hurdiidae'
p2c5.order = 'Order: Radiodonta'
p2c5.class_ = 'Class: Dinocaridida'
p2c5.phylum = 'Phylum: Arthropoda'
p2c5.prestige = 'Prestige: *** / ***'
p2c5.min_length = 6
p2c5.max_length_increment = 200
p2c5.min_weight = 46
p2c5.max_weight_increment = 1500
p2c5.description = 'Species of giant filter-feeder from the Lower Ordovician. '
p2c5.rarity = 2

# SILURIAN PERIOD CREATURES #
p3c1 = Creature()
p3c2 = Creature()
p3c3 = Creature()
p3c4 = Creature()
p3c5 = Creature()

p3c1.add_image(creature_placeholder_img)
p3c1.id = 10
p3c1.genus = 'Genus: Birkenia'
p3c1.family = 'Family: Birkeniidae'
p3c1.order = 'Order: Birkeniiformes'
p3c1.class_ = 'Class: Anaspida'
p3c1.phylum = 'Phylum: 	Chordata'
p3c1.prestige = 'Prestige: * / ***'
p3c1.min_length = 1
p3c1.max_length_increment = 1
p3c1.min_weight = 1
p3c1.max_weight_increment = 1
p3c1.description = 'Jawless fish from the Middle Silurian.'
p3c1.rarity = 0

p3c2.add_image(creature_placeholder_img)
p3c2.id = 11
p3c2.genus = 'Genus: Poraspis'
p3c2.family = 'Family: Cyathaspidae'
p3c2.order = 'Order: Cyathaspidiformes'
p3c2.class_ = 'Class: Pteraspidomorphi'
p3c2.phylum = 'Phylum: Chordata'
p3c2.prestige = 'Prestige: * / ***'
p3c2.min_length = 1
p3c2.max_length_increment = 1
p3c2.min_weight = 1
p3c2.max_weight_increment = 1
p3c2.description = 'Jawless fish from the the Late Silurian. '
p3c2.description += 'This fish was covered in plates and scales that provided protection. '
p3c2.description += 'These species resembled armored tadpoles. '
p3c2.rarity = 0

p3c3.add_image(creature_placeholder_img)
p3c3.id = 12
p3c3.genus = 'Genus: Entelognathus'
p3c3.family = 'Family: [ ? ]'
p3c3.order = 'Order: [ ? ]'
p3c3.class_ = 'Class: Placodermi'
p3c3.phylum = 'Phylum: Chordata'
p3c3.prestige = 'Prestige: ** / ***'
p3c3.min_length = 1
p3c3.max_length_increment = 1
p3c3.min_weight = 1
p3c3.max_weight_increment = 1
p3c3.description = 'Earlier species of armored and jawed-fish from the Late Silurian. '
p3c3.rarity = 1

p3c4.add_image(creature_placeholder_img)
p3c4.id = 13
p3c4.genus = 'Genus: Sphooceras'
p3c4.family = 'Family: Sphooceratidae'
p3c4.order = 'Order: Orthocerida'
p3c4.class_ = 'Class: Cephalopoda'
p3c4.phylum = 'Phylum: Mollusca'
p3c4.prestige = 'Prestige: ** / ***'
p3c4.min_length = 1
p3c4.max_length_increment = 1
p3c4.min_weight = 1
p3c4.max_weight_increment = 1
p3c4.description = 'Species of primitive cephalopod from the Silurian Period. '
p3c4.description += 'Among the earliest cephalopods to have a fully-covered mantle.'
p3c4.rarity = 1

p3c5.add_image(creature_placeholder_img)
p3c5.id = 14
p3c5.genus = 'Genus: Megamastax \'big mouth\''
p3c5.family = 'Family: [ ? ]'
p3c5.order = 'Order: [ ? ]'
p3c5.class_ = 'Class: [ ? ]'
p3c5.phylum = 'Phylum: Chordata'
p3c5.prestige = 'Prestige: *** / ***'
p3c5.min_length = 1
p3c5.max_length_increment = 1
p3c5.min_weight = 1
p3c5.max_weight_increment = 1
p3c5.description = 'Species of lobe-finned fish from the Late Silurian. '
p3c5.description += 'Due to its large size and predatory lifestyle, the Megamastax is believed to be the first vertebrate apex predator.'
p3c5.rarity = 2

# DEVONIAN PERIOD CREATURES #
p4c1 = Creature()
p4c2 = Creature()
p4c3 = Creature()
p4c4 = Creature()
p4c5 = Creature()

p4c1.add_image(creature_placeholder_img)
p4c1.id = 15
p4c1.genus = 'Genus: Bothriolepis'
p4c1.family = 'Family: Bothriolepididae'
p4c1.order = 'Order: Antiarchi'
p4c1.class_ = 'Class: Placodermi'
p4c1.phylum = 'Phylum: Chordata'
p4c1.prestige = 'Prestige: * / ***'
p4c1.min_length = 1
p4c1.max_length_increment = 1
p4c1.min_weight = 1
p4c1.max_weight_increment = 1
p4c1.description = ''
p4c1.rarity = 0

p4c2.add_image(creature_placeholder_img)
p4c2.id = 16
p4c2.genus = 'Genus: Cladoselache'
p4c2.family = 'Family: Cladoselachidae'
p4c2.order = 'Order: Symmoriiformes'
p4c2.class_ = 'Class: Chondrichthyes'
p4c2.phylum = 'Phylum: Chordata'
p4c2.prestige = 'Prestige: * / ***'
p4c2.min_length = 1
p4c2.max_length_increment = 1
p4c2.min_weight = 1
p4c2.max_weight_increment = 1
p4c2.description = ''
p4c2.rarity = 0

p4c3.add_image(creature_placeholder_img)
p4c3.id = 17
p4c3.genus = 'Genus: Gemuendina'
p4c3.family = 'Family: Asterosteidae'
p4c3.order = 'Order: Rhenanida'
p4c3.class_ = 'Class: Placodermi'
p4c3.phylum = 'Phylum: Chordata'
p4c3.prestige = 'Prestige: ** / ***'
p4c3.min_length = 1
p4c3.max_length_increment = 1
p4c3.min_weight = 1
p4c3.max_weight_increment = 1
p4c3.description = ''
p4c3.rarity = 1

p4c4.add_image(creature_placeholder_img)
p4c4.id = 18
p4c4.genus = 'Genus: Xenacanthus'
p4c4.family = 'Family: Xenacanthidae'
p4c4.order = 'Order: Xenacanthida'
p4c4.class_ = 'Class: Chondrichthyes'
p4c4.phylum = 'Phylum: Chordata'
p4c4.prestige = 'Prestige: ** / ***'
p4c4.min_length = 1
p4c4.max_length_increment = 1
p4c4.min_weight = 1
p4c4.max_weight_increment = 1
p4c4.description = ''
p4c4.rarity = 1

p4c5.add_image(creature_placeholder_img)
p4c5.id = 19
p4c5.genus = 'Genus: Onychodus'
p4c5.family = 'Family: Onychodontidae'
p4c5.order = 'Order: Onychodontida'
p4c5.class_ = 'Class: Sarcopterygii'
p4c5.phylum = 'Phylum: Chordata'
p4c5.prestige = 'Prestige: *** / ***'
p4c5.min_length = 1
p4c5.max_length_increment = 1
p4c5.min_weight = 1
p4c5.max_weight_increment = 1
p4c5.description = ''
p4c5.rarity = 2

# CARBONIFEROUS PERIOD CREATURES #
p5c1 = Creature()
p5c2 = Creature()
p5c3 = Creature()
p5c4 = Creature()
p5c5 = Creature()

p5c1.add_image(creature_placeholder_img)
p5c1.id = 20
p5c1.genus = 'Genus: Tristychius'
p5c1.family = 'Family: Tristychiidae'
p5c1.order = 'Order: Hybodontiformes'
p5c1.class_ = 'Class: Chondrichthyes'
p5c1.phylum = 'Phylum: Chordata'
p5c1.prestige = 'Prestige: * / ***'
p5c1.min_length = 1
p5c1.max_length_increment = 1
p5c1.min_weight = 1
p5c1.max_weight_increment = 1
p5c1.description = ''
p5c1.rarity = 0

p5c2.add_image(creature_placeholder_img)
p5c2.id = 21
p5c2.genus = 'Genus: Dracopristis'
p5c2.family = 'Family: [ ? ]'
p5c2.order = 'Order: Ctenacanthiformes'
p5c2.class_ = 'Class: Chondrichthyes'
p5c2.phylum = 'Phylum: Chordata'
p5c2.prestige = 'Prestige: * / ***'
p5c2.min_length = 1
p5c2.max_length_increment = 1
p5c2.min_weight = 1
p5c2.max_weight_increment = 1
p5c2.description = ''
p5c2.rarity = 0

p5c3.add_image(creature_placeholder_img)
p5c3.id = 22
p5c3.genus = 'Genus: Rhizodus'
p5c3.family = 'Family: Rhizodontidae'
p5c3.order = 'Order: Rhizodontiformes'
p5c3.class_ = 'Class: Rhizodontida'
p5c3.phylum = 'Phylum: Chordata'
p5c3.prestige = 'Prestige: ** / ***'
p5c3.min_length = 1
p5c3.max_length_increment = 1
p5c3.min_weight = 1
p5c3.max_weight_increment = 1
p5c3.description = ''
p5c3.rarity = 1

p5c4.add_image(creature_placeholder_img)
p5c4.id = 23
p5c4.genus = 'Genus: Orthacanthus'
p5c4.family = 'Family: Orthacanthidae'
p5c4.order = 'Order: Xenacanthida'
p5c4.class_ = 'Class: Chondrichthyes'
p5c4.phylum = 'Phylum: Chordata'
p5c4.prestige = 'Prestige: ** / ***'
p5c4.min_length = 1
p5c4.max_length_increment = 1
p5c4.min_weight = 1
p5c4.max_weight_increment = 1
p5c4.description = ''
p5c4.rarity = 1

p5c5.add_image(creature_placeholder_img)
p5c5.id = 24
p5c5.genus = 'Genus: Diplocaulus'
p5c5.family = 'Family: Diplocaulidae'
p5c5.order = 'Order: Nectridea'
p5c5.class_ = 'Subclass: Lepospondyli'
p5c5.phylum = 'Phylum: Chordata'
p5c5.prestige = 'Prestige: *** / ***'
p5c5.min_length = 1
p5c5.max_length_increment = 1
p5c5.min_weight = 1
p5c5.max_weight_increment = 1
p5c5.description = ''
p5c5.rarity = 2

# PERMIAN PERIOD CREATURES #
p6c1 = Creature()
p6c2 = Creature()
p6c3 = Creature()
p6c4 = Creature()
p6c5 = Creature()

p6c1.add_image(creature_placeholder_img)
p6c1.id = 20
p6c1.genus = 'Genus: '
p6c1.family = 'Family: '
p6c1.order = 'Order: '
p6c1.class_ = 'Class: '
p6c1.phylum = 'Phylum: '
p6c1.prestige = 'Prestige: * / ***'
p6c1.min_length = 1
p6c1.max_length_increment = 1
p6c1.min_weight = 1
p6c1.max_weight_increment = 1
p6c1.description = ''
p6c1.rarity = 0

p6c2.add_image(creature_placeholder_img)
p6c2.id = 21
p6c2.genus = 'Genus: '
p6c2.family = 'Family: '
p6c2.order = 'Order: '
p6c2.class_ = 'Class: '
p6c2.phylum = 'Phylum: '
p6c2.prestige = 'Prestige: * / ***'
p6c2.min_length = 1
p6c2.max_length_increment = 1
p6c2.min_weight = 1
p6c2.max_weight_increment = 1
p6c2.description = ''
p6c2.rarity = 0

p6c3.add_image(creature_placeholder_img)
p6c3.id = 22
p6c3.genus = 'Genus: '
p6c3.family = 'Family: '
p6c3.order = 'Order: '
p6c3.class_ = 'Class: '
p6c3.phylum = 'Phylum: '
p6c3.prestige = 'Prestige: ** / ***'
p6c3.min_length = 1
p6c3.max_length_increment = 1
p6c3.min_weight = 1
p6c3.max_weight_increment = 1
p6c3.description = ''
p6c3.rarity = 1

p6c4.add_image(creature_placeholder_img)
p6c4.id = 23
p6c4.genus = 'Genus: '
p6c4.family = 'Family: '
p6c4.order = 'Order: '
p6c4.class_ = 'Class: '
p6c4.phylum = 'Phylum: '
p6c4.prestige = 'Prestige: ** / ***'
p6c4.min_length = 1
p6c4.max_length_increment = 1
p6c4.min_weight = 1
p6c4.max_weight_increment = 1
p6c4.description = ''
p6c4.rarity = 1

p6c5.add_image(creature_placeholder_img)
p6c5.id = 24
p6c5.genus = 'Genus: '
p6c5.family = 'Family: '
p6c5.order = 'Order: '
p6c5.class_ = 'Class: '
p6c5.phylum = 'Phylum: '
p6c5.prestige = 'Prestige: *** / ***'
p6c5.min_length = 1
p6c5.max_length_increment = 1
p6c5.min_weight = 1
p6c5.max_weight_increment = 1
p6c5.description = ''
p6c5.rarity = 2


creatures_list = []
for i in range(6):
    row = []
    for j in range(5):
        row.append(Creature())
    creatures_list.append(row)

creatures_list[0][0] = p1c1
creatures_list[0][1] = p1c2
creatures_list[0][2] = p1c3
creatures_list[0][3] = p1c4
creatures_list[0][4] = p1c5

creatures_list[1][0] = p2c1
creatures_list[1][1] = p2c2
creatures_list[1][2] = p2c3
creatures_list[1][3] = p2c4
creatures_list[1][4] = p2c5

creatures_list[2][0] = p3c1
creatures_list[2][1] = p3c2
creatures_list[2][2] = p3c3
creatures_list[2][3] = p3c4
creatures_list[2][4] = p3c5

creatures_list[3][0] = p4c1
creatures_list[3][1] = p4c2
creatures_list[3][2] = p4c3
creatures_list[3][3] = p4c4
creatures_list[3][4] = p4c5

creatures_list[4][0] = p5c1
creatures_list[4][1] = p5c2
creatures_list[4][2] = p5c3
creatures_list[4][3] = p5c4
creatures_list[4][4] = p5c5

creatures_list[5][0] = p6c1
creatures_list[5][1] = p6c2
creatures_list[5][2] = p6c3
creatures_list[5][3] = p6c4
creatures_list[5][4] = p6c5


# CAMBRIAN PERIOD #
camPeriod = Period()
camPeriod.period_val = 0

camPeriod.period += 'Cambrian Period'

camPeriod.timeframe += '541mya to 485mya (56 million years)'

camPeriod.description = 'The Cambrian Period is the first period of the Paleozoic Era. '
camPeriod.description += 'This period is best known for the Cambrian Explosion, an event characterized by '
camPeriod.description += 'an incredible spike in the emergence and diversification of many marine lifeforms.\n\n'
camPeriod.description += 'Land was dispersed between 8 small continents and one supercontinent called Gondwana.\n\n'
camPeriod.description += 'The climate was warm and wet with no changing seasons and an average global temperature of 72 degrees Fahrenheit. '
camPeriod.description += 'There were no polar ice caps and there was little glaciation anywhere.\n\n'
camPeriod.description += 'Land plants and animals did not exist yet...\n\nbut marine life thrived. '

# ORDOVICIAN PERIOD #
ordPeriod = Period()
ordPeriod.period_val = 1

ordPeriod.period += 'Ordovician Period'

ordPeriod.timeframe += '485mya to 444mya (41 million years)'

ordPeriod.description = 'The Ordovician Period is best known for the Ordovician Radiation or Great Ordovician Biodiversification Event (GOBE), '
ordPeriod.description += 'a continuation of the Cambrian Explosion, featuring further diversification and evolution of life throughout the Ordovician Period. '
ordPeriod.description += 'This period is refered to as the \'Rise of Fish\' because the first, true '
ordPeriod.description += 'fish appeared (as jawless vertebrates). Additionally, '
ordPeriod.description += 'the first gastropods, cephalopods, and jointed brachiopods evolved. '
ordPeriod.description += 'Species were typically confined to a specific region, a concept known as endemism. '
ordPeriod.description += 'New marine habitats also began to appear and develop during this period including '
ordPeriod.description += 'reefs, hardgrounds, and bryozoan thickets.\n\n'
ordPeriod.description += 'Major predator of this period include both large cephalopods and giant eurypterids, \'sea scorpions\'. '
ordPeriod.description += 'Neither the water column nor the sea floor was safe.\n\n'
ordPeriod.description += 'Like the Cambrian Period, the climate was warm and wet with Gondwana remaining the dominant landmass.\n\n'
ordPeriod.description += 'The end-Ordovician is a mass extinction event at the end of this period involving an ice age, caused by Gondwana moving toward the South Pole, which killed '
ordPeriod.description += 'roughly 80'+'%'+' of species living in shallow seas (which is where most marine life existed at the time). '
ordPeriod.description += 'However, this extinction was only the second largest in the history of Earth...\n\n'
ordPeriod.description += 'the largest mass extinction event is yet to come.'

# SILURIAN PERIOD #
silPeriod = Period()
silPeriod.period_val = 2

silPeriod.period += 'Silurian Period'

silPeriod.timeframe += '444mya to 419mya (25 million years)'

silPeriod.description = 'The Silurian Period begins with the end of the end-Ordovician ice age as Gondwana moved '
silPeriod.description += 'away from the South Pole. Climate began to adjust to that of modern day with glaciers and '
silPeriod.description += 'cold weater at the South Pole and warmer weather at the equator. As the ice age ended, glaciers melted and shallow seas returned as water levels rose. '
silPeriod.description += 'Aside from Gondwana there were about 6 continents in a ring at the equator.\n\n'
silPeriod.description += 'Large coral reefs appeared in shallow, tropical seas and '
silPeriod.description += 'jawless fish evolved significantly. Additionally, the first freshwater/brackish water fish appeared. '
silPeriod.description += 'Some species of animals began to distribute globally. '
silPeriod.description += 'Eurypterids (sea scorpions) reached their peak in abudance and diversity in this period.\n\n'
silPeriod.description += 'While the inner-lands of continents remained barren, vacular plants '
silPeriod.description += 'colonized coastal lowlands. The first fully-terrestrial organisms to appear were fungi (at least the first preserved in fossil). '

# DEVONIAN PERIOD #
devPeriod = Period()
devPeriod.period_val = 3

devPeriod.period += 'Devonian Period'

devPeriod.timeframe += '419mya to 359mya (60 million years)'

devPeriod.description = 'The Devonian Period is known as the \'Age of Fish\' due to the vast diversity and abundance of creatures that roamed the seas.\n\nThere were 3 major landmasses with an ocean covering 85'+'%'+' of the globe. '
devPeriod.description += 'The three continental masses include the North America/Europe continent near the equator, the modern Siberia continent in the North, '
devPeriod.description += 'and Gondwana taking up much of the southern hemisphere. The Rheic Ocean was the body of water that dominated the Earth. '
devPeriod.description += 'Sea levels were high and most land was under shallow seas. The majority of land that wasn\'t submerged was near the equator which created a warm '
devPeriod.description += 'and mild climate. Due to this the Devonian Period was also known as a \'Greenhouse Age\'.\n\n'
devPeriod.description += 'This period featured a lot of firsts and progressions in life on Earth.\n'
devPeriod.description += 'In the water: shallow, tropical seas hosted an abundance of life, the first large coral reefs formed, and the first lobe-finned fish evolved.\nOn the land: the first '
devPeriod.description += 'insects and centipedes appeared, the first trees and forests developed, and the first seed-producing plants appeared.\n\n'
devPeriod.description += 'However, this flourishing of life would not last forever. The end of the Devonian Period came with a series of oxygen-related '
devPeriod.description += 'extinction events killing 96'+'%'+' of marine invertebrates. Arthropods, trilobites, and ammonites were heavily impacted by this. '
devPeriod.description += 'Placoderms, a class of armored fish that thrived and dominated the oceans from the Silurian Period through the Devonian Period would be completely wiped out.\n\n'
devPeriod.description += 'Yet another cycle of life and evolution... complete.'

# CARBONIFEROUS PERIOD #
carPeriod = Period()
carPeriod.period_val = 4

carPeriod.period += 'Carboniferous Period'

carPeriod.timeframe += '359mya to 299mya (60 million years)'

carPeriod.description = ''

# PERMIAN PERIOD #
perPeriod = Period()
perPeriod.period_val = 5

perPeriod.period += 'Permian Period'

perPeriod.timeframe += '299mya to 252mya (47 million years)'

perPeriod.description = ''
