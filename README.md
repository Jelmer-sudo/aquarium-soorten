# aquarium-soorten

Soortenlijst en afbeeldingen voor een persoonlijke Android-app om aquaria bij te houden. De app haalt `species.json` en de afbeeldingen hier op; zonder internet gebruikt ze de kopie die in de app zit.

## Wat erin staat

- `species.json`: 377 zoetwatersoorten (dieren en planten) met temperatuur, pH, grootte, minimale bakgrootte, groepsgrootte, karakter en verzorging. De waarden komen uit algemeen bekende aquariumkennis, gecontroleerd met openbare bronnen, en zijn in eigen woorden opgeschreven.
- `afbeeldingen/<id>.webp`: één afbeelding per soort, 512 × 512 pixels.

## Afbeeldingen en licenties

De meeste afbeeldingen zijn foto's van [Wikimedia Commons](https://commons.wikimedia.org/). Ze zijn vierkant bijgesneden en verkleind, en vallen onder hun eigen licentie (CC0, publiek domein, CC BY of CC BY-SA). Een bijgesneden CC BY-SA-foto valt onder dezelfde CC BY-SA-licentie. Maker, licentie en bron staan ook per soort in het veld `foto` van `species.json`.

Twee afbeeldingen zijn met AI gemaakt (lokale ComfyUI), omdat er geen bruikbare vrije foto van te vinden was.

| Soort | Maker | Licentie | Bron |
|---|---|---|---|
| Neontetra (*Paracheirodon innesi*) | Wojciech J. Płuciennik | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Paracheirodon_innesi_01.jpg) |
| Kardinaaltetra (*Paracheirodon axelrodi*) | CHUCAO | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cardinal_Paracheirodon_axelrodi_(1).jpg) |
| Zwarte neon (*Hyphessobrycon herbertaxelrodi*) | Brian Gratwicke | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon_herbertaxelrodi_Gratwicke.jpg) |
| Kongozalm (*Phenacogrammus interruptus*) | lwolfartist | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Congo_tetraNAB_3.17.jpg) |
| Citroentetra (*Hyphessobrycon pulchripinnis*) | Waugsberg | CC BY 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon_pulchripinnis.jpg) |
| Roodkopzalm (*Hemigrammus bleheri*) | Soulkeeper | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Petitella_bleheri_(Hemigrammus_bleheri).jpg) |
| Zebravis (*Danio rerio*) | Marrabbio2 | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Brachydanio_rerio.jpg) |
| Hemelse pareldanio (*Celestichthys margaritatus*) | Cisamarc | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Danio_margaritatus.jpg) |
| Kegelvlekbarbeel (*Trigonostigma heteromorpha*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cyprinidae_Trigonostigma_heteromorpha_3.jpg) |
| Chinese danio (*Tanichthys albonubes*) | Petrtyl | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Tanichthys_albonubes-kardinalka_cinska.jpg) |
| Sumatraanse barbeel (*Puntigrus tetrazona*) | André Karwath aka Aka | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Puntius_tetrazona_(aka).jpg) |
| Sherrybarbeel (*Puntius titteya*) | Brian Gratwicke | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cherry_barb,_Puntius_titteya.jpg) |
| Mosquito-rasbora (*Boraras brigittae*) | Fantomeno 14 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Rasbora-orné-3-min-2617071259.jpg) |
| Gup (*Poecilia reticulata*) | 5snake5 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Poecilia_reticulata_-_Guppy,_male,_cobra-green_morph.jpg) |
| Platy (*Xiphophorus maculatus*) | Usien | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xiphophorus_maculatus_Platy.JPG) |
| Zwaarddrager (*Xiphophorus hellerii*) | Wojciech J. Płuciennik | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xiphophorus_hellerii_young_male_01.jpg) |
| Molly (*Poecilia sphenops*) | Dnoerholm | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:PoeciliaSphenops.jpg) |
| Endlers guppy (*Poecilia wingei*) | Emilio17 | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Poecilia_wingei_Campoma_Guppy_male_008_en_20130428.jpg) |
| Gevlekte pantsermeerval (*Corydoras paleatus*) | Ude | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras_paleatus_in_current.jpg) |
| Bronzen pantsermeerval (*Corydoras aeneus*) | Andrew Keller | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Female_Bronze_Corydoras_(Corydoras_aeneus).jpg) |
| Sterbai-pantserwels (*Corydoras sterbai*) | Matthew Mannell | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras_Sterbai.jpg) |
| Dwergpantserwels (*Corydoras pygmaeus*) | Anastasiya Lvova | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Обитатели_петербургского_Океанариума_10_(cropped).jpg) |
| Pandapantsermeerval (*Corydoras panda*) | Chronotopian | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Panda_Corydoras.jpg) |
| Borstelneus (*Ancistrus cirrhosus*) | The Last 99 | CC BY-SA 3.0 de | [Commons](https://commons.wikimedia.org/wiki/File:Ancistrus_cirrhosus.jpg) |
| Dwergzuigmeerval (*Otocinclus affinis*) | Cisamarc | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Macrotocinclus_affinis_resting.jpg) |
| Maanvis (*Pterophyllum scalare*) | Versions111 | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pterophyllum_scalare_03.jpg) |
| Siamese kempvis (*Betta splendens*) | Henryk Niestrój | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Bojownik_syjamski.jpg) |
| Dwerggoerami (*Trichogaster lalius*) | Jvarszegi | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Dwarf_gourami_common_color_morph.jpg) |
| Blauwe spat (*Trichopodus trichopterus*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Trichopodus_trichopterus_A.jpg) |
| Parelgoerami (*Trichopodus leerii*) | h080 | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Trichopodus_leerii_h080.jpg) |
| Honinggoerami (*Trichogaster chuna*) | Eevaya | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Honey_gourami_red_variant.jpg) |
| Kersenbuik (*Pelvicachromis pulcher*) | Tino Strauss | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pelvicachromis_pulcher_(male)_02.jpg) |
| Antennebaarsje (*Mikrogeophagus ramirezi*) | Eric Mengel | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Mikrogeophagus_ramirezi,_2017.jpg) |
| Kakadu-dwergcichlide (*Apistogramma cacatuoides*) | Redspider | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Apistogramma_cacatuoides.jpg) |
| Pauwoogcichlide (*Astronotus ocellatus*) | Clément Bardot | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Oscar_fish_(Astronotus_ocellatus).jpg) |
| Dwergkogelvis (*Carinotetraodon travancoricus*) | 5snake5 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Carinotetraodon_travancoricus_Seitenansicht.jpg) |
| Goudvis (*Carassius auratus*) | James St. John | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Carassius_auratus_auratus_(goldfish)_1.jpg) |
| Zilverdollar (*Metynnis hypsauchen*) | Sesamehoneytart | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Metynnis_hypsauchen_small.jpg) |
| Ayamaru-regenboogvis (*Melanotaenia boesemani*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Melanotaeniidae_Melanotaenia_boesemani_1.jpg) |
| Clownbotia (*Chromobotia macracanthus*) | Gpasques | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Chromobotia_macracanthus_Aquarium_Nancy.jpg) |
| Indische modderkruiper (*Pangio kuhlii*) | Iidkk | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Kuhli_loach_in_aquarium.jpg) |
| Siamese algeneter (*Crossocheilus oblongus*) | aleander2137 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Siamese_algae_eater_(Crossocheilus_oblongus).jpg) |
| Red Cherry-garnaal (*Neocaridina davidi*) | DirkBlankenhaus | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Neocaridina-heteropoda-var-red.jpg) |
| Amanogarnaal (*Caridina multidentata*) | Seotaro | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Caridina_multidentata(Hamamatsu,Shizuoka,Japan,2007).jpg) |
| Crystal red garnaal (*Caridina cantonensis*) | Bahersayana | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Caridina_cf._cantonensis_(crysta_red_shrimp).JPG) |
| Bamboegarnaal (*Atyopsis moluccensis*) | Kacper Aleksander | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Atyopsis_moluccensis.jpg) |
| Grote posthorenslak (*Planorbarius corneus*) | Michel Langeveld | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Planorbarius_corneus_113462819.jpg) |
| Appelslak (*Pomacea bridgesii*) | MdE | CC BY-SA 3.0 de | [Commons](https://commons.wikimedia.org/wiki/File:Pomacea_bridgesii_MdE_1.jpg) |
| Slanke knobbelhoren (*Melanoides tuberculata*) | Dennis L. | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Melanoides_tuberculatus_2.png) |
| Zebranerietslak (*Neritina natalensis*) | TheJammingYam | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Zebra_Nerite_Snail_1.jpg) |
| Konijnenslak (*Tylomelania sp.*) | Bschlund | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Tylomelania_towutensis.jpg) |
| Helenaslak (*Clea helena*) | Peter Pfeiffer | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Clea_helena.jpg) |
| Oranje dwergkreeft (*Cambarellus patzcuarensis*) | Tommy Kronkvist | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cambarellus_patzcuarensis-feeding.jpg) |
| Floridarivierkreeft (*Procambarus alleni*) | Emőke Dénes | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Iz_-_Procambarus_alleni_-_1.jpg) |
| Japanse rijstvis (medaka) (*Oryzias latipes*) | Seotaro | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Oryzias_latipes.jpg) |
| Prachtbarbeel (*Pethia conchonius*) | Usien | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Pethia_conchonius_Prachtbarbe.JPG) |
| Buenos-Airestetra (*Psalidodon anisitsi*) | Mattia Nocciola | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Psalidodon_anisitsi_Natural_History_Museum_University_of_Pisa_(cropped_and_bright).jpg) |
| Roodvinzalm (*Aphyocharax anisitsi*) | Hemigrammus at German Wikipedia | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aphyocharax_anisitsi.jpg) |
| Paradijsvis (*Macropodus opercularis*) | André Karwath aka Aka | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Macropodus_opercularis_-_side_(aka).jpg) |
| Gouddanio (*Danio albolineatus*) | Павлик Лисицын | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Danio_albolineatus_254555018.jpg) |
| Chinese barbeel (goudbarbeel) (*Barbodes semifasciolatus*) | Chmee2 | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Puntius_semifasciolatus_in_Botanic_garden_in_Teplice.JPG) |
| Gevlekte bergbeekgrondel (*Sewellia lineolata*) | Spiketooth | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hillstream_Loach.JPG) |
| Vuurtetra (*Hyphessobrycon amandae*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon_amandae_A.jpg) |
| Vuurneon (*Hemigrammus erythrozonus*) | Gonzalo Valenzuela | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Tetra_Glowlight.jpg) |
| Zwarte tetra (*Gymnocorymbus ternetzi*) | D.W. | CC0 1.0 | [Commons](https://commons.wikimedia.org/wiki/File:Adulter_Trauermantelsalmer-Gymnocorymbus_ternetzi.jpg) |
| Roodoogtetra (*Moenkhausia sanctaefilomenae*) | Cedricguppy - Loury Cédric | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Moenkhausia_sanctaefilomenae_-_Tétra_yeux_rouge_-_Aqua_Porte_Dorée_01.JPG) |
| Serpae-tetra (*Hyphessobrycon eques*) | Francesco Loda | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon_serpae_-_Serpae_Tetra.jpg) |
| Bloedvlektetra (*Hyphessobrycon erythrostigma*) | 5snake5 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon_erythrostigma_-_Kirschflecksalmer.jpg) |
| Keizertetra (*Nematobrycon palmeri*) | 7TP (Krzysztof Bartosik) | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Nematobrycon_palmeri_1.jpg) |
| Florida-schijfhoren (*Planorbella duryi*) | 5snake5 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Planorbella_duryi_-_Posthornschnecke.jpg) |
| Hockeystick (*Thayeria boehlkei*) | Kkonstan | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Penguin_Tetra.jpg) |
| Lichtvisje (*Hemigrammus ocellifer*) | Deadlyballistics | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Head-&-Tail-Light-Tetra.jpg) |
| Valse roodneustetra (*Petitella rhodostoma*) | Bernat Arlandis | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Petitella_rhodostoma,_Bernat_Arlandis,_2013.jpg) |
| Blauwe neon (*Paracheirodon simulans*) | Sascha Biedermann | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Paracheirodon_simulans.jpg) |
| Zwarte fantoomzalm (*Hyphessobrycon megalopterus*) | R.workoran | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Black_phantom_tetra.jpg) |
| Rode fantoomzalm (*Hyphessobrycon sweglesi*) | harum.koh | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Amazon_fish,_Red_phantom_tetra_(Hyphessobrycon_sweglesi)_(15594713287).jpg) |
| Sierlijke tetra (*Hyphessobrycon bentosi*) | Holger Krisp | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Schmucksalmler_Hyphessobrycon_bentosi.jpg) |
| Hoornslak (*Clithon corona*) | Obsidian Soul | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Clithon_corona,_Horned_nerite_snail_from_the_Philippines_03.jpg) |
| Koperzalm (*Hasemania nana*) | Malene Thyssen | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Kobbertetra_Hasemania_nana.jpg) |
| Glasbloedvintetra (*Prionobrama filigera*) | Chronotopian | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Bloodfin_Glass_Tetra.jpg) |
| Gewone bijlzalm (*Gasteropelecus sternicla*) | Neale Monks | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Gasteropelecus_sternicla.JPG) |
| Gemarmerde bijlzalm (*Carnegiella strigata*) | Clinton & Charles Robertson | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Gasteropelecidae_Carnegiella_strigata_(5806481295).jpg) |
| Dwerg-potloodzalm (*Nannostomus marginatus*) | D.W. | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Nannostomus_marginatus,_adultes_Männchen.jpg) |
| Driestrepige potloodzalm (*Nannostomus trifasciatus*) | Tsunamicarlos | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Nannostomustrifasciatus.jpg) |
| Zebra-nerietslak (*Vittina turrita*) | Dat doris | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:GrumpySnail.jpg) |
| Luipaardpantserwels (*Corydoras trilineatus*) | Bob Jenkins | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras_trilineatus,_2010.jpg) |
| Venezolaanse dwergpantsermeerval (*Corydoras habrosus*) | D.W. | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras-habrosus-Männchen.jpeg) |
| Staartvlek-dwergpantserwels (*Corydoras hastatus*) | AquariaNR | CC BY-SA 3.0 de | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras_hastatus.jpg) |
| Schwartz-pantserwels (*Corydoras schwartzi*) | Thomas Land | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras_schwartzi_f.jpg) |
| Sierlijke pantserwels (*Corydoras elegans*) | Toniher | CC BY 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras_elegans.jpg) |
| Rabaut-pantserwels (*Corydoras rabauti*) | Jörg Vierke | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras_rabauti.jpg) |
| Zwartzeil-pantserwels (*Corydoras melanistius*) | Karsten Schönherr (karsten_s) | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras_melanistius_32268928.jpg) |
| Dubbele pantserwels (*Corydoras duplicareus*) | Marek Kriz | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras_duplicareus.jpg) |
| Baardpantserwels (*Scleromystax barbatus*) | Birger A | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Schleromystax_barbatus5015.jpg) |
| Smaragdpantserwels (*Brochis splendens*) | NonstickRon | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Brochis_splendens_NonstickRon_(cropped).jpg) |
| Aspidoras pauciradiatus (*Aspidoras pauciradiatus*) | Mike Noren | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aspidoras_pauciradiatus_1_DSC_0928.jpg) |
| Hoogvinkarper (*Poecilia velifera*) | Massysmith | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Poecilia_velifera.jpg) |
| Chinese mysteryslak (*Margarya chinensis*) | Ryan Hodnett | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Chinese_Mystery_Snail_(Cipangopaludina_chinensis)_-_Waterloo,_Ontario.jpg) |
| Variatus-platy (*Xiphophorus variatus*) | Livebearerguy | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xiphophorus_variatus_La_laguna_(1).jpg) |
| Bultrug-limia (*Limia nigrofasciata*) | Marie France Janelle | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Limia_nigrofasciata.JPG) |
| Cubaanse limia (*Limia vittata*) | Cardet co6cs | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Limia_vittata.jpg) |
| Dwerglevendbarende (*Heterandria formosa*) | Brian Gratwicke | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Dwarf_Livebearer_or_Least_Killifish_(Heterandria_formosa).jpg) |
| Eenvlek-levendbarende (*Phalloceros caudimaculatus*) | Haplochromis | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Phalloceros_caudimaculatus.JPG) |
| Purperkopbarbeel (*Pethia nigrofasciata*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cyprinidae_Pethia_nigrofasciata_1.jpg) |
| Odessabarbeel (*Pethia padamya*) | Cedricguppy - Loury Cédric | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pethia_padamya_-_male_-_AquaPorteDoree_01.JPG) |
| Gouden dwergbarbeel (*Pethia gelius*) | Beta Mahatvaraj | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pethia_gelius_hi_res.jpg) |
| Zwartvlekbarbeel (*Dawkinsia filamentosa*) | Marcus Knight | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Dawkinsia_filamentosa_-Marcus_Knight.tif) |
| Vijfstreepbarbeel (*Desmopuntius pentazona*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cyprinidae_Desmopuntius_pentazona_1.jpg) |
| Ruitvlekbarbeel (*Desmopuntius rhomboocellatus*) | Rupert A. Collins | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Puntius_rhomboocellatus.jpg) |
| Gestreepte dwergbarbeel (*Haludaria fasciata*) | Haplochromis | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pandabarben.jpg) |
| Dambordbarbeel (*Oliotius oligolepis*) | Dodoni | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Puntius_oligolepis.jpg) |
| Lijnbarbeel (*Striuntius lineatus*) | Staudacher | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Linienbarbe-puntius-lineatus.jpg) |
| Denison-barbeel (*Sahyadria denisonii*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cyprinidae_Sahyadria_denisonii_1.2.jpg) |
| Oranjevin-danio (*Danio kyathit*) | Il le faut | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Danio_kyathit.jpg) |
| Glowlight-danio (*Danio choprae*) | Sergev1001 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Glowlight_Danio_-_Danio_Choprae.JPG) |
| Gevlekte dwergdanio (*Danio nigrofasciatus*) | Lerdsuwa | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Danio_nigrofasciatus.jpg) |
| Reuzendanio (*Devario aequipinnatus*) | Faucon | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Devario_aequipinnatus.JPG) |
| Malabar-danio (*Devario malabaricus*) | Shifu Tanks | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Devario_malabaricus_-_left-facing_lateral_view_near_water_surface_(aquarium).jpg) |
| Bengaalse danio (*Devario devario*) | Beta Mahatvaraj | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Devario_devario_hi_res.jpg) |
| Kubota dwergrasbora (*Microdevario kubotai*) | BottomDog | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Microdevario_kubotai-hires.jpg) |
| Lamsrasbora (*Trigonostigma espei*) | AverageWalrus | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Trigonostigma_espei_2023.jpg) |
| Glowlight-rasbora (*Trigonostigma hengeli*) | -serwacy01- | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:T_hengeli.jpg) |
| Waigiu-nerietslak (*Vittina waigiensis*) | Obsidian Soul | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Red_racer_nerite,_Vittina_waigiensis_from_the_Philippines_04.jpg) |
| Hi-spot rasbora (*Brevibora dorsiocellata*) | Pseudogastromyzon | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Rasbora_dorsiocellata.jpg) |
| Briljantrasbora (*Rasbora einthovenii*) | -serwacy01- | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rasbora_e.jpg) |
| Clownrasbora (*Rasbora kalochroma*) | Factumquintus | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rasbora_kalochroma.jpg) |
| Roodstaartrasbora (*Rasbora borapetensis*) | Lerdsuwa | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rasbora_borapetensis.jpg) |
| Scissortail-rasbora (*Rasbora trilineata*) | Lerdsuwa | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rasbora_trilineata.jpg) |
| Grootvlekrasbora (*Rasbora caudimaculata*) | M.I.Norhakim | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rasbora_caudimaculata.jpg) |
| Kopstreep-rasbora (*Rasbora cephalotaenia*) | AMIRA.W | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:R.cephalotaenia.jpg) |
| Stippelrasbora (*Boraras maculatus*) | Atulbhats | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Boraras_Maculata.jpg) |
| Uitroeptekenrasbora (*Boraras urophthalmoides*) | R.workoran | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Boraras_uraphthalmoides_Thai.jpg) |
| Boraras merah (*Boraras merah*) | Andrewbogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Boraras_merah1.png) |
| Vliegende barbeel (*Esomus danrica*) | দিব্য দত্ত | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Esomus_Danrica_in_Assam.jpg) |
| Parelrasbora (*Rasboroides vaterifloris*) | Rupert A. Collins | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rasboroides_vaterifloris.jpg) |
| Gouden barbeel (*Laubuka dadiburjori*) | Beta Mahatvaraj | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Laubuka_dadiburjori_(Orange_Chela).jpg) |
| Gestreepte gourami (*Trichogaster fasciata*) | Sandipan Das | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Trichogaster_fasciata_179813241.jpg) |
| Maanlichtgourami (*Trichopodus microlepis*) | Greg Hume (Greg5030) | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Moonlight_Gourami.jpg) |
| Gewone draadgoerami (*Trichopodus pectoralis*) | BEDO (Thailand) | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Trichopodus_pectoralis.jpg) |
| Zoenvis (*Helostoma temminckii*) | Green Yoshi | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Helostoma_temminckii_in_aquarium.jpg) |
| Vreedzame betta (*Betta imbellis*) | DefenderRegina | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Betta_imbellis_(male)_20100512.jpg) |
| Smaragdbetta (*Betta smaragdina*) | Acapella | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Betta_smaragdina_pair1.jpg) |
| Javaanse betta (*Betta picta*) | Ganjar Cahyadi | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Betta_picta.jpg) |
| Neritina pulligera (*Neritina pulligera*) | Kacper Aleksander | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Neritina_pulligera.jpg) |
| Witrand-betta (*Betta albimarginata*) | BS Thurner Hof | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Betta_albimarginata_060311_8.jpg) |
| Knorgoerami (*Trichopsis vittata*) | Grimfilth | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Trichopsis_vittata_LCK_8707.JPG) |
| Dwergknorgoerami (*Trichopsis pumila*) | Dezinformator15 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Sparkling_gourami.jpg) |
| Luipaardbosvis (*Ctenopoma acutirostre*) | Fish91 | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Leopard_Bush_Fish.JPG) |
| Oranje bosvis (*Microctenopoma ansorgii*) | Juan Carlos Palau Díaz | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Microctenopoma_ansorgii_2.jpg) |
| Agassiz dwergcichlide (*Apistogramma agassizii*) | Cisamarc | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Apistogramma_agassizii_in_aquarium.jpg) |
| Borelli's dwergcichlide (*Apistogramma borellii*) | Gordon Axmann | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Apistogramma_borellii.jpg) |
| Zwarte duivelsslak (*Faunus ater*) | -serwacy01- | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Faunuster.jpg) |
| MacMaster dwergcichlide (*Apistogramma macmasteri*) | Cupr78up | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:AMacMasteri.jpg) |
| Nijssen dwergcichlide (*Apistogramma nijsseni*) | Sascha Biedermann | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Apistogramma_nijsseni_(m).jpg) |
| Hongslo dwergcichlide (*Apistogramma hongsloi*) | SamaelGMO | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Male_of_Apistogramma_hongsloi.jpg) |
| Driestrepige dwergcichlide (*Apistogramma trifasciata*) | oencage | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Apistogramma_trifasciata.jpg) |
| Panduro-dwergcichlide (*Apistogramma panduro*) | Cisamarc | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Apistogramma_Panduro_male.jpg) |
| Viejita-dwergcichlide (*Apistogramma viejita*) | lienyuan lee | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:維吉塔短鯛_Apistogamma_viejita_Kulland,_1979_-_panoramio.jpg) |
| Tweestrepige dwergcichlide (*Apistogramma bitaeniata*) | Britzke | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Apistogramma_bitaeniata.jpg) |
| Gestreepte prachtcichlide (*Pelvicachromis taeniatus*) | Ged~commonswiki (aangenomen) | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Pelvicachromis_taeniatus.jpg) |
| Oogvlek-prachtcichlide (*Pelvicachromis subocellatus*) | Udo12345 | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pelvicachromis_subocellatus_Moulondo_female.jpg) |
| Sprankelende vlagcichlide (*Laetacara curviceps*) | Dnoerholm | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Laetacara_Curviceps.jpg) |
| Blauwe acara (*Andinoacara pulcher*) | Loïc Tremblay | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aequidens_pulcher.jpg) |
| Gouden dwergcichlide (*Nannacara anomala*) | Borkowski.robert | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Nannacara_anomala_male1.jpg) |
| Dambordcichlide (*Dicrossus filamentosus*) | Clinton & Charles Robertson | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Dicrossus_filamentosus.jpg) |
| Boliviaanse ramcichlide (*Mikrogeophagus altispinosus*) | Corpse89 | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:A_Bolivian_Ram_-_Mikrogeophagus_altispinosus.JPG) |
| Candidi-dwergcichlide (*Taeniacara candidi*) | Gogoschinski | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Taeniacara_candidi_adult.jpg) |
| Sleutelgatcichlide (*Cleithracara maronii*) | D.W. | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Cleithracara_maronii-Seite.jpg) |
| Zebracichlide (*Amatitlania nigrofasciata*) | S. Olkowicz (gebruiker Hippocampus) | CC BY 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Archocentrus_nigrofasciatus_female.jpg) |
| Vuurkeelcichlide (*Thorichthys meeki*) | 5snake5 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Thorichthys_meeki_-_Feuermaulbuntbarsch.jpg) |
| Rode acara (*Hemichromis bimaculatus*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hemichromis_bimaculatus_A.jpg) |
| Severumcichlide (*Heros severus*) | Alexxx1979 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cichlasoma_severum_DSC00552_2200.jpg) |
| Roodborst-aardeneter (*Geophagus steindachneri*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Geophagus_steindachneri.jpg) |
| Satanoperca leucosticta (*Satanoperca leucosticta*) | Dr. David Midgley | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Satanoperca_leucosticta_(1).jpg) |
| Cupido-cichlide (*Biotodoma cupido*) | Gregdonohoe | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Biotodoma_cupido.png) |
| Zeilvin-zuigmeerval (*Pterygoplichthys gibbiceps*) | Soulkeeper | CC BY 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Sailfin-pleco.jpg) |
| Luipaard-zuigmeerval (*Pterygoplichthys pardalis*) | Ildar Sagdejev (Specious) | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:2004-02-02_Pterygoplichthys_pardalis_on_blue_gravel.jpg) |
| Blauwe antennewels (*Ancistrus dolichopterus*) | Emőke Dénes | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Siluriformes_-_Ancistrus_dolichopterus_-_1.jpg) |
| Naaldmeerval (*Farlowella acus*) | Haplochromis | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Farlowella_arcus_3.jpg) |
| Parotocinclus maculicauda (*Parotocinclus maculicauda*) | Diogo Luiz | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Parotocinclus_maculicauda_46530735.jpg) |
| Gestreepte Otocinclus (*Otocinclus vittatus*) | Chle (aangenomen) | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Otocinclus_vittatus.jpg) |
| Koninklijke twijgmeerval (*Sturisoma panamense*) | Daiju Azuma | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Sturisoma_panamense.jpg) |
| Grootvlek-Otocinclus (*Otocinclus macrospilus*) | Rainer Schmitt | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Otocinclus_macrospilus_2.jpg) |
| Chinese algenetende (*Gyrinocheilus aymonieri*) | Garthhh | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Gyrinocheilus_(Chinese_Algae_Eater)_in_Aquarium.jpg) |
| Regenbooghaai (*Epalzeorhynchos frenatum*) | MerlinSenger | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Fransenlipper.JPG) |
| Vuurstaartlabeo (*Epalzeorhynchos bicolor*) | Astellar87 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Epalzeorhynchos_bicolor1.jpg) |
| Towuti-slak (*Tylomelania towutensis*) | Bschlund | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Tylomelania_towutensis_2.jpg) |
| Balahaai (*Balantiocheilos melanopterus*) | 5snake5 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Balantiocheilos_melanopterus_-_Haibarbe.jpg) |
| Doktersvis (*Garra rufa*) | Dances | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Garra_Rufa.JPG) |
| Pictus-meerval (*Pimelodus pictus*) | Claire H. | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pimelodus_pictus.jpg) |
| Afrikaanse rugzwemmer (*Synodontis nigriventris*) | John P. Friel Ph.D. | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Synodontis_nigriventris_53146421.jpg) |
| Veervin-synodontis (*Synodontis eupterus*) | Clive Walford | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Synodontis_eupterus_1.jpg) |
| Tanganyika-synodontis (*Synodontis petricola*) | Mike Peel | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Frankfurt_Zoo_-_Synodontis_petricola.jpg) |
| Koekoeksmeerval (*Synodontis multipunctatus*) | Mario Rubio García | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Synodontis-multipunctatus.jpg) |
| Engelsmeerval (*Synodontis angelicus*) | Haps | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Synodontis_angelica.jpg) |
| Spookglasmeerval (*Kryptopterus vitreolus*) | Francesco Loda | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Kryptopterus_vitreolus_-_20080927.jpg) |
| Pratende meerval (*Platydoras armatulus*) | Astellar87 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Platydoras_armatulus_2.jpg) |
| Gevlekte raphael (*Agamyxis pectinifrons*) | Pit one (aangenomen) | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Dornwels.JPG) |
| Banjomeerval (*Bunocephalus coracoideus*) | Kacper Aleksander | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Banjo_cat.jpg) |
| Blauwe botia (*Yasuhikotakia modesta*) | Lerdsuwa | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Yasuhikotakia_modesta.jpg) |
| Skunkbotia (*Yasuhikotakia morleti*) | Lerdsuwa | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Yasuhikotakia_morleti.jpg) |
| Dwergbotia (*Ambastaia sidthimunki*) | Stefan Maurer | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Schachbrettschmerle.jpg) |
| Tijgerbotia (*Syncrossus hymenophysa*) | Julian augustine alexander | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Syncrossus_hymenophysa_2.jpg) |
| Zebrabotia (*Botia striata*) | Actuallychaos | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Botia_striata_in_a_home_aquarium.jpg) |
| Yoyobotia (*Botia almorhae*) | Orishas92 | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Yoyo_Loach.jpg) |
| Bengaalse botia (*Botia dario*) | Lerdsuwa | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Botia_dario.jpg) |
| Zwarte kuhli-aal (*Pangio oblonga*) | Marrabbio2 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pangio_oblonga_acquarium.jpg) |
| Clithon retropictum (*Clithon retropictum*) | Seotaro | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Clithon_retropictus(Hamamatsu,Shizuoka,Japan,2007).jpg) |
| Guntea-modderkruiper (*Lepidocephalichthys guntea*) | AravindManoj | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Guntea_loach.jpg) |
| Aziatische modderkruiper (*Misgurnus anguillicaudatus*) | Manoel Jr. | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Weather_loach.jpg) |
| Diamantregenboogvis (*Melanotaenia praecox*) | 7TP (Krzysztof Bartosik) | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Melanotaenia_praecox.jpg) |
| Turkooise regenboogvis (*Melanotaenia lacustris*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Melanotaenia_lacustris.jpg) |
| Driestrepige regenboogvis (*Melanotaenia trifasciata*) | OpenCage | CC BY 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Banded_rainbowfish_Melanotaenia_trifasciata.jpg) |
| Tebera-regenboogvis (*Melanotaenia herbertaxelrodi*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Melanotaenia_herbertaxelrodi.jpg) |
| Prachtregenboogvis (*Melanotaenia splendida*) | Emőke Dénes | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hal_-_Melanotaenia_splendida_-_1.jpg) |
| MacCulloch regenboogvis (*Melanotaenia maccullochi*) | Jesse de Vries | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Melanotaenia_maccullochi_187466468.jpg) |
| Rode regenboogvis (*Glossolepis incisus*) | Emőke Dénes | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hal_-_Glossolepis_incisus_-_1.jpg) |
| Draadvin-regenboogvis (*Iriatherina werneri*) | NRJMelvinT | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Iriatherina_werneri.jpg) |
| Gevlekte blauwoog (*Pseudomugil gertrudae*) | Atulbhats | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Getrudae_Rainbowfish.jpg) |
| Vorkstaart-blauwoog (*Pseudomugil furcatus*) | Dirk Godlinski | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pseudomugil_furcatus_m_Aquarium_DG.jpg) |
| Pacifische blauwoog (*Pseudomugil signifer*) | Julien Renoult | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pseudomugil_signifer_28436969.jpg) |
| Celebes-zeilvin (*Marosatherina ladigesi*) | Brent Tibbatts | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Celebes_Rainbowfish.jpg) |
| Amerikaanse schijfhoren (*Planorbella trivolvis*) | Onbekend (publiek domein) | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Planorbella_trivolvis.jpg) |
| Madagaskar-regenboogvis (*Bedotia geayi*) | Stan Shebs | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Bedotia_geayi_1.jpg) |
| Pauwoogkwabaal (*Tateurndina ocellicauda*) | Cisamarc | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Tateurndina_ocellicauda,_male.jpg) |
| Purpervlek-kwabaal (*Mogurnda adspersa*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Eleotridae_Mogurnda_adspersa_1.jpg) |
| Keizerkwabaal (*Hypseleotris compressa*) | Frank M. Greco | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hypseleotris_compressa.jpg) |
| Kaap-Lopez-killivis (*Aphyosemion australe*) | KKPCW | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aphyosemion_australe_in_Higashiyama_Zoo.jpg) |
| Günther killivis (*Nothobranchius guentheri*) | Jokuyken15 | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Nothobranchius_guentheri.jpg) |
| Rachow killivis (*Nothobranchius rachovii*) | Cisamarc | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rachovii.jpg) |
| Gardner killivis (*Fundulopanchax gardneri*) | Alexander Prokoshev | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Fundulopanchax_gardneri_gardneri.JPG) |
| Clownkillivis (*Epiplatys annulatus*) | Dornenwolf | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Ringelhechtling_-Epiplatys_annulatus.jpg) |
| Gestreepte panchax (*Aplocheilus lineatus*) | Christopher | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aplocheilus_lineatus_68014539.jpg) |
| Blauwe panchax (*Aplocheilus panchax*) | Vengolis | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aplocheilus_panchax_00849.jpg) |
| Floridatandkarper (*Jordanella floridae*) | nat_t | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Jordanella_floridae_182122551.jpg) |
| Blauwvin-killivis (*Lucania goodei*) | Brian Gratwicke | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Lucania_goodei.jpg) |
| Puntige blaashoren (*Physella acuta*) | Barbalalaika | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Physella_acuta_on_an_aquarium_plant.jpg) |
| Daisy's rijstvisje (*Oryzias woworae*) | Aquakeeper14 | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Daisy's_Ricefish.JPG) |
| Roodstaart-goodeide (*Xenotoca eiseni*) | Andrew Bogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xenotoca_eiseni_San_Marcos_Male.png) |
| Vlindergoodeide (*Ameca splendens*) | Usien | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Ameca_splendens_Jungtier_2016-12-11.JPG) |
| Mestandkarper (*Alfaro cultratus*) | Livebearerguy | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Alfaro_cultratus_(3).jpg) |
| Merry widow (*Phallichthys amates*) | Nick Tobler (Cowturtle) | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Merry_Widow,_Calle_Central,_Río_Cuarto,_Alajuela,_CR_imported_from_iNaturalist_photo_400705619.jpg) |
| Atlantische molly (*Poecilia mexicana*) | Elfabso | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Poecilia_mexicana_female.jpg) |
| Vlindervis (*Pantodon buchholzi*) | Toniher | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pantodon_buchholzi.jpg) |
| Senegalese kwastsnoek (*Polypterus senegalus*) | Tommy Andriollo | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Polypterus_senegalus_243650469.jpg) |
| Wimpelaal (*Erpetoichthys calabaricus*) | Tylwyth Eldar | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Erpetoichthys_calabaricus_01.jpg) |
| Prachtvinkwastsnoek (*Polypterus ornatipinnis*) | Bloopityboop | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Polypterus_ornatipinnis_VA_01.jpg) |
| Afrikaanse mesvis (*Xenomystus nigri*) | User:Haplochromis | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xenomystus_nigri_1.JPG) |
| Zwarte spookmesvis (*Apteronotus albifrons*) | Vassil | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Apteronotus_albifrons_Aquarium_tropical_du_Palais_de_la_Porte_Dorée_10_04_2016_2.jpg) |
| Amazone-bladvis (*Monocirrhus polyacanthus*) | Juergen goevert | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Blattfisch.JPG) |
| Blauwe badis (*Badis badis*) | Kennyannydenny | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Blauwe_badis_(vrouw).jpg) |
| Scharlaken badis (*Dario dario*) | ATuin-hek at English Wikipedia | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Dario_dario_male.jpg) |
| Schomburgk bladvis (*Polycentrus schomburgkii*) | karsten_s | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Polycentrus_schomburgkii_32045429.jpg) |
| Roodstaart-kogelvis (*Carinotetraodon lorteti*) | Павлик Лисицын | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Carinotetraodon_lorteti_248508857_2.jpg) |
| Carinotetraodon irrubesco (*Carinotetraodon irrubesco*) | Neale Monks at English Wikipedia | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Carinotetraodon_irrubesco_female.JPG) |
| Zuid-Amerikaanse kogelvis (*Colomesus asellus*) | O. Schneider | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Assel-Kugelfisch.jpg) |
| Ceylon-kogelvis (*Leiodon cutcutia*) | Sahat Ratmuangkhwang | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Tetraodon_cutcutia.jpg) |
| Zesbandige distichodus (*Distichodus sexfasciatus*) | Hectonichus | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Distichodontidae_-_Distichodus_sexfasciatus.JPG) |
| Roodoog-Afrikaanse tetra (*Arnoldichthys spilopterus*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Arnoldichthys_spilopterus_A.jpg) |
| Langvin-Afrikaanse tetra (*Brycinus longipinnis*) | Rufus46 | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Langflossensalmler_Brycinus_longipinnis_Tierpark_Hellabrunn-1.jpg) |
| Vuuraal (*Mastacembelus erythrotaenia*) | Llandor | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Ildaal.jpg) |
| Eenstrepige Afrikaanse zalm (*Nannaethiops unitaeniatus*) | Francois Libert | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:One-lined_African_Characin_-_Nannaethiops_unitaeniatus.jpg) |
| Glaskarpermeerval (*Alestopetersius caudalis*) | The Great Mule of Eupatoria | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Yellow_tailed_tetra.jpg) |
| Gestreepte kopstaander (*Anostomus anostomus*) | Brian Gratwicke | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Anostomus_anostomus,_striped_headstander.jpg) |
| Zwartgestreepte kopstaander (*Leporinus fasciatus*) | Bernard DUPONT | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Banded_Leporinus_(Leporinus_fasciatus)_(7124562451).jpg) |
| Hoogrug-kopstaander (*Abramites hypselonotus*) | Haplochromis | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Abramites_hypselonotus.jpg) |
| Gestippelde kopstaander (*Chilodus punctatus*) | Jørn | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Chilodus_punctatus.jpg) |
| Spatzalm (*Copella arnoldi*) | Zikamoi | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Copella_arnoldi.jpg) |
| Tweevlek-lebiasina (*Lebiasina bimaculata*) | Gustav Ywanaga | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Charcoca.jpg) |
| Metynnis argenteus (*Metynnis argenteus*) | Derek Ramsey (Ram-Man) | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Silver_dollar_fish_Metynnis_argenteus.jpg) |
| Zwartbandschijfzalm (*Myloplus schomburgkii*) | Ltshears | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Myleus_schomburgkii.jpg) |
| Koningstetra (*Inpaichthys kerri*) | SOK | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hane_av_kerritetra_Inpaichthys_kerri.jpg) |
| Diamantzalm (*Makunaima pittieri*) | Michael Palmer | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:A_diamond_tetra_fish.jpg) |
| Blauwe tetra (*Boehlkea fredcochui*) | Axel Zarske & D. Bork | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Boehlkea_fredcochui_(live).png) |
| Bucktooth-tetra (*Exodon paradoxus*) | Ltshears | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Bucktoothed_Tetra.jpg) |
| Rode rio (*Hyphessobrycon flammeus*) | Susanne Möller-Neukäter | CC BY 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon_flammeus.jpg) |
| Gele tetra (*Hyphessobrycon bifasciatus*) | D. Bork and A. Zarske | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon_bifasciatus_(standard)_(31134).png) |
| Loreto-tetra (*Hyphessobrycon loretoensis*) | A. Zarske, D. Bork, H.J. Franke | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon_loretoensis_(31536).png) |
| Roze tetra (*Megalamphodus rosaceus*) | karsten_s | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon_rosaceus_35474466.jpg) |
| Mooie tetra (*Holopristis pulchra*) | SOK | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hemigrammus_pulcher_1.jpg) |
| Tinfoilbarbeel (*Barbonymus schwanefeldii*) | Emke Dnes | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Barbonymus_schwanenfeldii_-_Cornwall_(aquarium).jpg) |
| Roodvinbarbeel (*Barbonymus altus*) | Vassil | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Aquarium_tropical_de_Pierrefitte-Nestalas_03082018_Barbus_à_queue_rouge_Barbonymus_altus_1.jpg) |
| Spanner-barbeel (*Striuntius lateristriga*) | opencage | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Puntius_lateristriga.jpg) |
| Arulius-barbeel (*Dawkinsia arulius*) | Marcus Knight | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Dawkinsia_arulius_-Marcus_Knight.jpg) |
| Stoliczka barbeel (*Pethia stoliczkana*) | The Great Mule of Eupatoria | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Pethia_stoliczkana_fahad.jpg) |
| Afrikaanse bandbarbeel (*Enteromius fasciolatus*) | Frank M. Greco | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Enteromius_fasciolatus_FMG.jpg) |
| Jae barbeel (*Enteromius jae*) | Udo Vornhusen | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Enteromius_jae.jpg) |
| Deissner gourami (*Parosphromenus deissneri*) | YIE BABEL | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Parosphromenus_deissneri.jpg) |
| Chocoladegoerami (*Sphaerichthys osphromenoides*) | Tsunamicarlos | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Sphaerichthys_osphromenoides.jpg) |
| Kamstaart-gourami (*Belontia signata*) | H. Zell | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Belontia_signata_-_Wilhelma_01.jpg) |
| Rode betta (*Betta coccina*) | Parostoteles | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Betta_coccina_"Jambi-Sumatra".JPG) |
| Ocellated-paradijsvis (*Macropodus ocellatus*) | Andrew Bogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Macropodus_ocellatus.png) |
| Specht paradijsvis (*Macropodus spechti*) | Andrew Bogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Macropodus_spechti_male.png) |
| Altum-schaarvis (*Pterophyllum altum*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cichlidae_Pterophyllum_altum_2.jpg) |
| Discusvis (*Symphysodon aequifasciatus*) | H. Zell | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Symphysodon_aequifasciatus_-_Karlsruhe_Zoo_03.jpg) |
| Symphysodon discus (*Symphysodon discus*) | Limesle | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Discus_heckel.jpg) |
| Uaru (*Uaru amphiacanthoides*) | Brent Tibbats | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Uaru_amphiacanthoides_Singapore.jpg) |
| Jurupari-aardeneter (*Satanoperca jurupari*) | Chrumps | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Satanoperca--jurupari.jpg) |
| Geophagus altifrons (*Geophagus altifrons*) | DIFish | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Altifrons.jpg) |
| Braziliaanse aardeneter (*Geophagus brasiliensis*) | Cezary Porycki | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Geophagus_brasiliensis_c01.jpg) |
| Groene terreur (*Andinoacara rivulatus*) | H. Zell | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Andinoacara_rivulatus_-_Karlsruhe_Zoo_01.jpg) |
| Jaguarcichlide (*Parachromis managuensis*) | George Chernilevsky | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Parachromis_managuensis_2012_G1.jpg) |
| Citroencichlide (*Amphilophus citrinellus*) | George Chernilevsky | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Amphilophus_citrinellus_2015_G5.jpg) |
| Bloedrode juweelcichlide (*Rubricatochromis lifalili*) | Nicolas COUTHOUIS | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Hemichromis_lifalili_(aquarium)3.jpg) |
| Rode zebra (*Maylandia estherae*) | Voytikof | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Maylandia_Estherae_Red-red.jpg) |
| Malawi-zebracichlide (*Maylandia zebra*) | Kai Squires | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Maylandia_zebra_61728832.jpg) |
| Gele labidochromis (*Labidochromis caeruleus*) | Jmatz | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Labidochromis_caeruleus_(male).jpg) |
| Demason cichlide (*Chindongo demasoni*) | lee Nachtigal | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pseudotropheus_demasoni.jpg) |
| Gouden mbuna (*Melanochromis auratus*) | Vlad Butsky | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Melanochromis_auratus_(male).jpg) |
| Baensch peacock (*Aulonocara baenschi*) | Rjcastillo | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aulonocara_baenschi_20241123.jpg) |
| Stuart Grant peacock (*Aulonocara stuartgranti*) | Mike Peel | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Frankfurt_Zoo_-_Aulonocara_stuartgranti_Usisya.jpg) |
| Poederblauwe mbuna (*Chindongo socolofi*) | Jutta234 | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pseudotropheus_socolofi_-_Zoo_Frankfurt.jpg) |
| Cynotilapia afra (*Cynotilapia afra*) | Alexandra Tyers | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cynotilapia_afra.jpg) |
| Slakkenhuiscichlide (*Neolamprologus multifasciatus*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cichlidae_Neolamprologus_multifasciatus_1.jpg) |
| Prinses van Burundi (*Neolamprologus pulcher*) | DenesFeri | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Neolamprologus_pulcher_-_aquarium_1.jpg) |
| Gouden Julidochromis (*Julidochromis ornatus*) | FakirNL | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Julidochromis_ornatus_in_Ouwehands_Dierenpark.jpg) |
| Julidochromis transcriptus (*Julidochromis transcriptus*) | Przemysław Malkowski | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Julidochromis_transcriptus.jpg) |
| Altolamprologus calvus (*Altolamprologus calvus*) | 5snake5 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Altolamprologus_calvus_-_Perlhuhn-Buntbarsch.jpg) |
| Lamprologus ocellatus (*Lamprologus ocellatus*) | Regani | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Lamprologus_ocellatus.jpg) |
| Cyprichromis leptosoma (*Cyprichromis leptosoma*) | Regani | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Cyprichromis_leptosoma.jpg) |
| Tropheus duboisi (*Tropheus duboisi*) | Manfred Werner / Tsui | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Tropheus_duboisi_Schoenbrunn2008.jpg) |
| Eretmodus cyanostictus (*Eretmodus cyanostictus*) | Jtanganyika | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Eretmodus-sp-kavala1.jpg) |
| Frontosa (*Cyphotilapia frontosa*) | Patrick Ch. Apfeld | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cyphotilapia frontosa Zoo Cologne.jpg) |
| Paracyprichromis nigripinnis (*Paracyprichromis nigripinnis*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Paracyprichromis nigripinnis A.jpg) |
| Goudnugget-zuigmeerval (L18) (*Baryancistrus xanthellus*) | Anne Blindheim | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Baryancistrus-L18.jpg) |
| Zebra-zuigmeerval (L46) (*Hypancistrus zebra*) | Birger A | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hypancistrus zebra4305.jpg) |
| Zonne-zuigmeerval (L14) (*Scobinancistrus aureatus*) | Gabriel Lelis Togni | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Scobinancistrus aureatus.jpg) |
| Luipaard-kaktusmeerval (*Pseudacanthicus leopardus*) | Sesamehoneytart | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pseudacanthicus leopardus.JPG) |
| Roze-staart-chalceus (*Chalceus macrolepidotus*) | opencage | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Chalceus macrolepidotus.jpg) |
| Zilveren arowana (*Osteoglossum bicirrhosum*) | Qwertzy2 | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Osteoglossum bicirrhosum.JPG) |
| Klonmesvis (*Chitala ornata*) | Mistvan | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Chitala ornata (Zoo Brno, Czech Republic).jpg) |
| Dario hysginon (*Dario hysginon*) | Crazyhund | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Dario Hysginon.jpg) |
| Gestreepte mesaal (*Gymnotus carapo*) | aquaportail.com | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Gymnotus Carapo en aquarium.jpg) |
| Platkopkwiekwie (*Callichthys callichthys*) | CHUCAO | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Callichthys callichthys.JPG) |
| Megalechis thoracata (*Megalechis thoracata*) | Danny Steaven | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hoplosternum-thoracatum-001.jpg) |
| Stroomlijnpantsermeerval (*Corydoras arcuatus*) | Pia Helminen | CC BY 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras arcuatus.jpg) |
| Goudtetra (*Hemigrammus rodwayi*) | Daiju Azuma | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hemigrammus rodwayi by DaijuAzuma.JPG) |
| Hyphessobrycon werneri (*Hyphessobrycon werneri*) | Axel Zarske | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon werneri (uncataloged import).png) |
| Axelrodia riesei (*Axelrodia riesei*) | Thomas Siems | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pfeffersalmler Axelrodia riesei (16467043916).jpg) |
| Mexicaanse tetra (*Astyanax mexicanus*) | Haplochromis | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Astyanax mexicanus.JPG) |
| Carnegiella marthae (*Carnegiella marthae*) | Dulcimerist | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Carnegiella marthae.jpg) |
| Nannostomus eques (*Nannostomus eques*) | Guérin Nicolas | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Nannostomus eques.JPG) |
| Metynnis lippincottianus (*Metynnis lippincottianus*) | Sortius | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Metynnis lippincottianus - Spotted Silver Dollar.jpg) |
| Olifantsvis (*Gnathonemus petersii*) | OpenCage | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Gnathonemus petersii by OpenCage.jpg) |
| Corydoras nattereri (*Corydoras nattereri*) | Diogo Luiz | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras nattereri 45975398.jpg) |
| Corydoras agassizii (*Corydoras agassizii*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Callichthyidae Corydoras agassizii 1.jpg) |
| Corydoras leopardus (*Corydoras leopardus*) | Frank M. Greco | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras leopardus.jpg) |
| Dawkinsia tambraparniei (*Dawkinsia tambraparniei*) | AravindManoj | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Dawkinsia Tambraparaniei.jpg) |
| Dawkinsia assimilis (*Dawkinsia assimilis*) | Rahul Gautam | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:D assimilis - Rahul Gautam.jpg) |
| Puntius vittatus (*Puntius vittatus*) | Smrithy Raj | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Bhava vittata.png) |
| Dwerganubias (*Anubias barteri var. nana*) | Krzysztof Ziarnek, Kenraiz | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Anubias_barteri_var._nana_kz01.jpg) |
| Javavaren (*Microsorum pteropus*) | Fhurzan | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Java_Fern_(Microsorum_pteropus)_growing_in_the_wild..jpg) |
| Bucephalandra (*Bucephalandra sp.*) | Manuel Werner | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Bluish_sheen_on_Bucephalandra_2_Foto_MWerner.jpg) |
| Cryptocoryne wendtii (*Cryptocoryne wendtii*) | John Robert McPherson | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cryptocoryne_wendtii_74_Sunbury_St_Geebung_P1070960.jpg) |
| Dwergcryptocoryne (*Cryptocoryne parva*) | AI-beeld, zelf gemaakt met ComfyUI | — | — |
| Vallisneria (*Vallisneria spiralis*) | Lamiot | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Vallisnérie_Vallisneria_spiralis_Brantôme-Dronne_2014_2.JPG) |
| Amazonezwaardplant (*Echinodorus bleheri*) | Brianza2008 | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Echinozziodestateyeah.JPG) |
| Dwergzwaardplant (*Echinodorus tenellus*) | Krzysztof Ziarnek, Kenraiz | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Helanthium_tenellum_kz02.jpg) |
| Ludwigia (*Ludwigia repens*) | Show_ryu | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Ludwigia_repens.JPG) |
| Rotala rotundifolia (*Rotala rotundifolia*) | Yercaud-elango | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rotala_rotundifolia_pink-2-veda_aquarium-bengaluru-India.jpg) |
| Indische waterkelk (*Hygrophila polysperma*) | Krzysztof Ziarnek, Kenraiz | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hygrophila_polysperma_kz01.jpg) |
| Waterwisteria (*Hygrophila difformis*) | Krzysztof Ziarnek, Kenraiz | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hygrophila_difformis_kz04.jpg) |
| Javamos (*Taxiphyllum barbieri*) | Xedoo | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Musgo-de-java-xedoo.jpg) |
| Kerstboommos (*Vesicularia ferriei*) | AI-beeld, zelf gemaakt met ComfyUI | — | — |
| Gewoon watervorkje (*Riccia fluitans*) | Piotr Kuczynski | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Riccia_fluitans_1_(Piotr_Kuczynski).jpg) |
| Amazonekikkerbeet (*Limnobium laevigatum*) | Cardex | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Limnobium_laevigatum.JPG) |
| Watersla (*Pistia stratiotes*) | Mokkie | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Water_Lettuce_(Pistia_stratiotes).jpg) |
| Hoornblad (*Ceratophyllum demersum*) | S.Tanaka | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Ceratophyllum_demersum_var.demersum..JPG) |
| Monte Carlo (*Micranthemum tweediei*) | Yercaud-elango | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Micranthemum_tweediei-1-veda_aquarium-bengaluru-India.jpg) |
| Glossostigma (*Glossostigma elatinoides*) | Billtsai1518 | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:矮珍珠.jpg) |
| Cabomba (*Cabomba caroliniana*) | Leslie J. Mehrhoff, University of Connecticut, Bugwood.org | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cabomba_caroliniana_5447120.jpg) |
| Waterhyssop (*Bacopa caroliniana*) | Krzysztof Ziarnek, Kenraiz | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Bacopa_caroliniana_kz01.jpg) |
| Staurogyne (*Staurogyne repens*) | 호로조 | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:S._repens_in_a_tank.jpg) |
| Downoi (*Pogostemon helferi*) | Yercaud-elango | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pogostemon_helferi-2-veda_aquarium-R.M.Nagar-bengaluru-India.jpg) |
| Rode papegaaienbladplant (*Alternanthera reineckii*) | V C balakrishnan | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Alternanthera_reineckii_(2).JPG_-_Photo_by_V_C_Balakrishnan.jpg) |
| Smal pijlkruid (*Sagittaria subulata*) | Krzysztof Ziarnek, Kenraiz | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Sagittaria_subulata_kz01.jpg) |
| Egeria (*Egeria densa*) | Ernst Schütte | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Wasserpest.jpg) |
