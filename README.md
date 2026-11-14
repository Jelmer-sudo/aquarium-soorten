# aquarium-soorten

Soortenlijst en afbeeldingen voor een persoonlijke Android-app om aquaria bij te houden. De app haalt `species.json` en de afbeeldingen hier op; zonder internet gebruikt ze de kopie die in de app zit.

## Wat erin staat

- `species.json`: 767 zoetwatersoorten (dieren en planten) met temperatuur, pH, grootte, minimale bakgrootte, groepsgrootte, karakter en verzorging. De waarden komen uit algemeen bekende aquariumkennis, gecontroleerd met openbare bronnen, en zijn in eigen woorden opgeschreven.
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
| Puntius bimaculatus (*Puntius bimaculatus*) | Beta Mahatvaraj | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Puntius bimaculatus.jpg) |
| Sawbwa resplendens (*Sawbwa resplendens*) | The Man On The Street | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Sawbwa resplendens.jpg) |
| Danio roseus (*Danio roseus*) | Lerdsuwa | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Danio roseus.jpg) |
| Danio dangila (*Danio dangila*) | Beta Mahatvaraj | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Danio dangila.jpg) |
| Rasbora elegans (*Rasbora elegans*) | Muhammad Rasul Abdullah Halim | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rasbora elegans.jpg) |
| Horadandia atukorali (*Horadandia atukorali*) | Frank M. Greco | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Green carplet.jpg) |
| Boraras naevus (*Boraras naevus*) | Andrew Bogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Boraras naevus.png) |
| Apistogramma steindachneri (*Apistogramma steindachneri*) | Jonathan Armbruster | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Apistogramma steindachneri Armbruster.jpg) |
| Laetacara araguaiae (*Laetacara araguaiae*) | Frank M. Greco | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Laetacara araguaiae.jpg) |
| Crenicichla lepidota (*Crenicichla lepidota*) | Hmsmariano | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Crenicichla lepidota male.jpg) |
| Pterophyllum leopoldi (*Pterophyllum leopoldi*) | Emőke Dénes | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Labroidei - Pterophyllum leopoldi - 1.jpg) |
| Gymnogeophagus balzanii (*Gymnogeophagus balzanii*) | CHUCAO | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Gymnogeophagus balzanii (1).JPG) |
| Satanoperca daemon (*Satanoperca daemon*) | Whaldener Endo | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Satanoperca daemon 205600127.jpg) |
| Thorichthys ellioti (*Thorichthys ellioti*) | Tommy Kronkvist | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Thorichthys ellioti.jpg) |
| Herotilapia multispinosa (*Herotilapia multispinosa*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Herotilapia multispinosa.jpg) |
| Anomalochromis thomasi (*Anomalochromis thomasi*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Anomalochromis thomasi A.jpg) |
| Steatocranus casuarius (*Steatocranus casuarius*) | 5snake5 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Steatocranus casuarius, male.jpg) |
| Labeotropheus fuelleborni (*Labeotropheus fuelleborni*) | Doronenko | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Labeotropheus fuelleborni 02.jpg) |
| Altolamprologus compressiceps (*Altolamprologus compressiceps*) | H. Zell | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Altolamprologus compressiceps - Karlsruhe Zoo 01.jpg) |
| Ambastaia nigrolineata (*Ambastaia nigrolineata*) | Lerdsuwa | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Yasuhikotakia nigrolineata.jpg) |
| Rhadinocentrus ornatus (*Rhadinocentrus ornatus*) | Dirk Godlinski | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rhadinocentrus ornatus Searys Ck male.JPG) |
| Nothobranchius furzeri (*Nothobranchius furzeri*) | Ugau | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Nothobranchius furzeri GRZ.jpg) |
| Limia melanogaster (*Limia melanogaster*) | Radek Sejkora | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Limia melanogaster.jpg) |
| Limia perugiae (*Limia perugiae*) | Livebearerguy | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Limia perugiae (1).jpg) |
| Xiphophorus montezumae (*Xiphophorus montezumae*) | Cedricguppy - Loury Cédric | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xiphophorus montezumae - AquaPorteDoree 04.JPG) |
| Channa gachua (*Channa gachua*) | 5snake5 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Channa gachua ♂.jpg) |
| Channa bleheri (*Channa bleheri*) | Mirko Hartig | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Channa bleheri.jpg) |
| Klimbaars (*Anabas testudineus*) | Abu Hamas | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Anabas testudineus 52464343.jpg) |
| Malpulutta kretseri (*Malpulutta kretseri*) | Klaus de Leuw | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Malpulutta kretseri.jpg) |
| Trichopsis schalleri (*Trichopsis schalleri*) | Baitoeytnt | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Trichopsis schalleri.jpg) |
| Macropodus erythropterus (*Macropodus erythropterus*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Macropodus erythropterus A.jpg) |
| Nandus nandus (*Nandus nandus*) | Beta Mahatvaraj | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Nandus nandus hi res.jpg) |
| Oryzias sarasinorum (*Oryzias sarasinorum*) | Guérin Nicolas | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xenopoecilus sarasinorum (Wroclaw Zoo).JPG) |
| Snoekkopgoerami (*Luciocephalus pulcher*) | BEDO (Thailand) | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Luciocephalus pulcher (Gray, 1830).jpg) |
| Cyrtocara moorii (*Cyrtocara moorii*) | Riftreef | CC BY 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Cyrtocara moorii.jpg) |
| Sciaenochromis fryeri (*Sciaenochromis fryeri*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cichlidae Sciaenochromis fryeri 1.jpg) |
| Elassoma evergladei (*Elassoma evergladei*) | Brian Gratwicke | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pygmy Sunfish, Elassoma evergladei.jpg) |
| Polypterus delhezi (*Polypterus delhezi*) | Steven G. Johnson | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Ornate bichir, Boston Aquarium.JPG) |
| Polypterus endlicherii (*Polypterus endlicherii*) | opencage | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Polypterus endlicherii.jpg) |
| Notopterus notopterus (*Notopterus notopterus*) | Xufanc | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Notopterus notopterus43.JPG) |
| Groene mesvis (*Eigenmannia virescens*) | Luis Ruiz Berti | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Eigenmannia virescens 000.jpg) |
| Apteronotus leptorhynchus (*Apteronotus leptorhynchus*) | Aidanreynolds03 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Brownghostknifefish.jpg) |
| Macrognathus pancalus (*Macrognathus pancalus*) | Haplochromis | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Indischer Zwergtachelaal.jpg) |
| Indostomus paradoxus (*Indostomus paradoxus*) | eric | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Indostomus paradoxus.JPG) |
| Lamprichthys tanganicanus (*Lamprichthys tanganicanus*) | Cedricguppy - Loury Cédric | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Lamprichthys tanganicanus - Femelle - AquaPorteDoree 01.JPG) |
| Indoplanorbis exustus (*Indoplanorbis exustus*) | Liang Liu e.a. | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Indoplanorbis exustus.jpg) |
| Petitella georgiae (*Petitella georgiae*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Characidae_Petitella_georgiae_1.jpg) |
| Corynopoma riisei (*Corynopoma riisei*) | AndrewBogott (WMF) | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corynopoma_riisei_1.png) |
| Hemigrammus stictus (*Hemigrammus stictus*) | Clinton & Charles Robertson | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hemigrammus_stictus.jpg) |
| Glansstreepzalm (*Hemigrammus bellottii*) | Haplochromis | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Hemigrammus_bellottii.jpg) |
| Hemigrammus schmardae (*Hemigrammus schmardae*) | Axel Zarske, Pierre-Yves Le Bail, and Jacques Géry | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hemigrammus_schmardae_(236594139).png) |
| Hyphessobrycon agulha (*Hyphessobrycon agulha*) | Oregon State University | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon_agulha_by_Rafael_Leitão.jpg) |
| Hyphessobrycon compressus (*Hyphessobrycon compressus*) | Carvalho, Malabarba, Endruweit, and Tobler | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon_compressus_(Marco_Endruweit).png) |
| Hyphessobrycon epicharis (*Hyphessobrycon epicharis*) | Axel Zarske (with help from Bastian, N. Khardina, and Bork) | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon_epicharis_(uncataloged_import).png) |
| Moenkhausia bonita (*Moenkhausia bonita*) | Felipe Alonso, Liliana Ciotek, and Miguel Albarenga | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Moenkhausia_bonita_(CI-FML_5351).png) |
| Poptella compressa (*Poptella compressa*) | Julien Renoult | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Poptella_compressa_11831742.jpg) |
| Ctenobrycon hauxwellianus (*Ctenobrycon hauxwellianus*) | Clinton & Charles Robertson | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Ctenobrycon_hauxwellianus.jpg) |
| Driepunt tetra (*Serrapinnus kriegi*) | Autóctonos de Uruguay | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Serrapinnus_kriegi.png) |
| Pracht roodvinzalm (*Aphyocharax rathbuni*) | Dirk-Peter Gartner | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aphyocharax_rathbuni_(12422).jpg) |
| Tetragonopterus argenteus (*Tetragonopterus argenteus*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Tetragonopterus_argenteus.jpg) |
| Triportheus angulatus (*Triportheus angulatus*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Triportheus_angulatus.jpg) |
| Bryconops caudomaculatus (*Bryconops caudomaculatus*) | Barry Chernoff and Antonio Machado-Allison | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Bryconops_caudomaculatus_(Potaro_River).png) |
| Bryconops affinis (*Bryconops affinis*) | Jonathan (Jon) Armbruster | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Bryconops_affinis_Armbruster.jpg) |
| Acestrorhynchus falcatus (*Acestrorhynchus falcatus*) | Vassil | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Acestrorhynchus_falcatus_Aquarium_tropical_du_Palais_de_la_Porte_Dor%C3%A9e_10_04_2016.jpg) |
| Salminus brasiliensis (*Salminus brasiliensis*) | Papa Pic from Eldorado, Argentina | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:DSC1052_(9272147265).jpg) |
| Pataka (*Hoplias malabaricus*) | Vassil | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Hoplias_Aquarium_tropical_du_Palais_de_la_Porte_Dor%C3%A9e_10_04_2016_1.jpg) |
| Characidium fasciatum (*Characidium fasciatum*) | User:Haplochromis | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Characidium_fasciatum_2.JPG) |
| Characidium rachovii (*Characidium rachovii*) | W.S.Serra | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Characidium_rachovii.jpg) |
| Hemiodus unimaculatus (*Hemiodus unimaculatus*) | Clinton & Charles Robertson | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hemiodus_unimaculatus.jpg) |
| Semaprochilodus insignis (*Semaprochilodus insignis*) | Jutta234 | CC BY-SA 3.0 de | [Commons](https://commons.wikimedia.org/wiki/File:Prochilodus_insignis_-_Zoo_Frankfurt_1.jpg) |
| Semaprochilodus taeniurus (*Semaprochilodus taeniurus*) | Vassil | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Aquarium_tropical_de_Pierrefitte-Nestalas_03082018_Semaprochilodus_1.jpg) |
| Roodbuikpiranha (*Pygocentrus nattereri*) | Coro | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:CAS-Aquarium-Piranha1.JPG) |
| Pygocentrus cariba (*Pygocentrus cariba*) | Sesamehoneytart | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pygocentrus_cariba.JPG) |
| Zwarte piranha (*Serrasalmus rhombeus*) | Ltshears | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:BlackPirahna2010.jpg) |
| Zwarte pacu (*Colossoma macropomum*) | Brian Gratwicke | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Black_pacu.jpg) |
| Mylossoma duriventre (*Mylossoma duriventre*) | larsjuh | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Mylossoma_duriventre_(7229293476).jpg) |
| Mylossoma aureum (*Mylossoma aureum*) | Clinton & Charles Robertson | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Mylossoma_aureum.jpg) |
| Roodvinschijfzalm (*Myloplus rubripinnis*) | Vassil | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Myloplus_rubripinnis_Scheveningen_Sea_Life_15022016_2.jpg) |
| Leporinus striatus (*Leporinus striatus*) | Donald Davesne | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Brevidens_striatus_584282406.jpg) |
| Gasteropelecus maculatus (*Gasteropelecus maculatus*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Gasteropelecidae_Gasteropelecus_maculatus_1.2.jpg) |
| Stiphodon percnopterygionus (*Stiphodon percnopterygionus*) | Laurent Pasteur | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Stiphodon_percnopterygionus.jpg) |
| Rhinogobius rubromaculatus (*Rhinogobius rubromaculatus*) | Andrewbogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rhinogobius_rubromaculatus_male.jpg) |
| Oxyeleotris marmorata (*Oxyeleotris marmorata*) | Yung-Lun Lin | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Oxyeleotris_marmorata_-_Yung-Lun_Lin_-_586219137.jpeg) |
| Hypseleotris cyprinoides (*Hypseleotris cyprinoides*) | Daiju Azuma | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hypseleotris_cyprinoides_by_Daiju_Azuma.jpg) |
| Melanotaenia fluviatilis (*Melanotaenia fluviatilis*) | Bahudhara | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Murray_River_Rainbow_Fish.jpg) |
| Melanotaenia parkinsoni (*Melanotaenia parkinsoni*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Melanotaenia_parkinsoni_2.jpg) |
| Melanotaenia pygmaea (*Melanotaenia pygmaea*) | Andrewbogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Melanotaenia_pygmaea_male.png) |
| Chilatherina fasciata (*Chilatherina fasciata*) | Dirk Godlinski | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Chilatherina_fasciata_male.jpg) |
| Cairnsichthys rhombosomoides (*Cairnsichthys rhombosomoides*) | Tim | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cairnsichthys_rhombosomoides_163093181.jpg) |
| Oryzias javanicus (*Oryzias javanicus*) | Ahsan A.H | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Oryzias_javanicus_3.jpg) |
| Oryzias mekongensis (*Oryzias mekongensis*) | Andrewbogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Oryzias_mekongensis_male.png) |
| Aphyosemion bivittatum (*Aphyosemion bivittatum*) | Mattus1990 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Kaprozubka_dvojp%C3%A1sa_-_aphyosemion_bivittatum.jpg) |
| Amiets vaandrager (*Fundulopanchax amieti*) | Andrew Bogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Fundulopanchax_amieti_Edea_Male.png) |
| Nothobranchius korthausae (*Nothobranchius korthausae*) | Andrew Bogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Nothobranchius_korthausae_male.png) |
| Nothobranchius eggersi (*Nothobranchius eggersi*) | Andrewbogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Nothobranchius_eggersi_Lasaba_TAN_19-24.png) |
| Pachypanchax omalonotus (*Pachypanchax omalonotus*) | Tino Strauss | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pachypanchax_omalonotus_01.jpg) |
| Pachypanchax sakaramyi (*Pachypanchax sakaramyi*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aplocheilidae_Pachypanchax_sakaramyi_1.jpg) |
| Epiplatys spilargyreius (*Epiplatys spilargyreius*) | Jan-Uwe Schmidt | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Epiplatys_spilargyreius_male_Malebo_Pool.jpg) |
| Austrolebias nigripinnis (*Austrolebias nigripinnis*) | Catxx | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Austrolebias_nigripinnis992.jpg) |
| Austrolebias adloffi (*Austrolebias adloffi*) | Luiz R. Malabarba | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Austrolebias_adloffi_male.jpg) |
| Poropanchax normani (*Poropanchax normani*) | Cisamarc | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Aplocheilichthys_normani_1.jpg) |
| Cyprinodon variegatus (*Cyprinodon variegatus*) | Smithsonian Environmental Research Center | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cyprinodon_variegatus_(S0103)_(12598764423).jpg) |
| Muskietenvisje (*Gambusia affinis*) | Fredlyfish4 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Female_Gambusia_affinis_UMFS_2015.jpg) |
| Gambusia holbrooki (*Gambusia holbrooki*) | Smithsonian Environmental Research Center | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Gambusia_holbrooki_-_SERC.jpg) |
| Gambusia yucatana (*Gambusia yucatana*) | Gaiacoyote | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Gambusia_yucatana.jpg) |
| Poeciliopsis gracilis (*Poeciliopsis gracilis*) | Andrewbogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Poeciliopsis_gracilis_male.png) |
| Priapella intermedia (*Priapella intermedia*) | Fiver, der Hellseher | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Blauaugenk%C3%A4rpfling_(Botanischer_Garten,_Dresden).jpg) |
| Priapella olmecae (*Priapella olmecae*) | Livebearerguy | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Priapella_olmecae_(1).jpg) |
| Neoheterandria elegans (*Neoheterandria elegans*) | Livebearerguy | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Neoheterandria_elegans_(1).jpg) |
| Priapichthys annectens (*Priapichthys annectens*) | Livebearerguy | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Priapichthys_annectens_(3)_(cropped).jpg) |
| Cnesterodon decemmaculatus (*Cnesterodon decemmaculatus*) | CHUCAO | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cnesterodon_decemmaculatus,_female_2.JPG) |
| Poecilia butleri (*Poecilia butleri*) | Finn Wigström | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Poecilia_butleri_male.jpg) |
| Poecilia vivipara (*Poecilia vivipara*) | Berbel-Filho WM et al. | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Poecilia_vivipara_(10.3897-zookeys.746.20960)_Figure_1.jpg) |
| Poecilia chica (*Poecilia chica*) | Charliemouse69 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Poecilia_Chica_Male_2.jpg) |
| Poecilia latipunctata (*Poecilia latipunctata*) | kjellnilsson1 | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Poecilia_latipunctata.jpg) |
| Limia tridens (*Limia tridens*) | Livebearerguy | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Limia_tridens_(4).jpg) |
| Limia sulphurophila (*Limia sulphurophila*) | Marcos Rodríguez Bobadilla | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Limia_sulphurophila_male_51046778938_187bb29cf3_o.jpg) |
| Limia islai (*Limia islai*) | JarroNevsbaru | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:A_male_Tiger_Limia_(Limia_islai).png) |
| Xiphophorus continens (*Xiphophorus continens*) | Volker Wirth | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xiphophorus_Continens_Young_Alpha_Male_(119157163).jpeg) |
| Xiphophorus cortezi (*Xiphophorus cortezi*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xiphophorus_cortezi.jpg) |
| Xiphophorus evelynae (*Xiphophorus evelynae*) | Livebearerguy | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xiphophorus_evelynae_(1).jpg) |
| Xiphophorus milleri (*Xiphophorus milleri*) | Charliemouse69 | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xyphopherous_Milleri_Male.jpg) |
| Xiphophorus nezahualcoyotl (*Xiphophorus nezahualcoyotl*) | Livebearerguy | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xiphophoorus_nezahualcoyotl_(4)_(cropped).jpg) |
| Xiphophorus nigrensis (*Xiphophorus nigrensis*) | Livebearerguy | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xiphophorus_nigrensis_male_1.jpg) |
| Xiphophorus pygmaeus (*Xiphophorus pygmaeus*) | Trondro tsara | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pygmy_Swordtail.jpg) |
| Xiphophorus signum (*Xiphophorus signum*) | Livebearerguy | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xiphophorus_signum_(2).jpg) |
| Skiffia multipunctata (*Skiffia multipunctata*) | Livebearerguy | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Skiffia_multipunctata_(3)_male.jpg) |
| Zoogoneticus tequila (*Zoogoneticus tequila*) | Cedricguppy - Loury Cédric | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Zoogoneticus_tequila_-_PorteDoreeParis_01.JPG) |
| Characodon lateralis (*Characodon lateralis*) | Cedricguppy - Loury Cédric | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Characodon_lateralis_-_AquaPorteDoree_01.JPG) |
| Xenoophorus captivus (*Xenoophorus captivus*) | Cedricguppy - Loury Cédric | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xenoophorus_captivus_-_Aquaportedor%C3%A9e_01.JPG) |
| Vieroogvis (*Anableps anableps*) | Quartl | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Anableps_anableps_qtl1.jpg) |
| Jenynsia multidentata (*Jenynsia multidentata*) | CHUCAO | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Jenynsia_multidentata_(1).JPG) |
| Betta anabatoides (*Betta anabatoides*) | Justin Philbois | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Betta_anabatoides_456455993_(cropped).jpg) |
| Betta edithae (*Betta edithae*) | Soulkeeper | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Betta_edithae_2.jpg) |
| Betta tussyae (*Betta tussyae*) | DefenderRegina | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Betta_tussyae_(male)_2010-05-09.jpg) |
| Parosphromenus harveyi (*Parosphromenus harveyi*) | Martin Fischer Parostoteles | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Parosphromenus_harveyi_2.jpg) |
| Goerami (*Osphronemus goramy*) | Vassil | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Aquarium_tropical_de_Pierrefitte-Nestalas_03082018_Gourami_g%C3%A9ant_2.jpg) |
| Osphronemus laticlavius (*Osphronemus laticlavius*) | Vassil | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Aquarium_tropical_de_Pierrefitte-Nestalas_03082018_Osphronemus_laticlavius_1.jpg) |
| Channa asiatica (*Channa asiatica*) | Jokuyken15 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Channa_asiatica_red.jpg) |
| Rode slangkopvis (*Channa micropeltes*) | George Chernilevsky | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Channa_micropeltes_2012_G1.jpg) |
| Channa maculata (*Channa maculata*) | Stephen Matthews | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Channa_maculata_279979517.jpg) |
| Channa aurantimaculata (*Channa aurantimaculata*) | 5snake5 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Channa aurantimaculata- lateral.jpg) |
| Channa orientalis (*Channa orientalis*) | Seriousgeeth | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Channa Orientalis.jpg) |
| Channa pleurophthalma (*Channa pleurophthalma*) | Atamari | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Channa pleurophthalma 0001.jpg) |
| Channa lucius (*Channa lucius*) | Totti | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Channa lucius Gifu.jpg) |
| Parachanna obscura (*Parachanna obscura*) | Cedricguppy - Loury Cédric | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Parachanna obscura - Aqua Porte Dorée 01.JPG) |
| Nannacara bimaculata (*Nannacara bimaculata*) | Jonathan (Jon) Armbruster | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Nannacara_bimaculata_Armbruster.jpg) |
| Acarichthys heckelii (*Acarichthys heckelii*) | Loury Cédric (Cedricguppy) | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Acarichthys_heckelii_-_subadulte_01.jpg) |
| Geophagus proximus (*Geophagus proximus*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Geophagus_proximus_A.jpg) |
| Surinaamse parelcichlide (*Geophagus surinamensis*) | Lerdsuwa | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Geophagus_surinamensis.jpg) |
| Gymnogeophagus gymnogenys (*Gymnogeophagus gymnogenys*) | W.S.Serra | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Gymnogeophagus_gymnogenys1.jpg) |
| Geophagus sveni (*Geophagus sveni*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Geophagus_sveni.jpg) |
| Gymnogeophagus rhabdotus (*Gymnogeophagus rhabdotus*) | W.S.Serra | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Gymnogeophagus_rhabdotus.jpg) |
| Gymnogeophagus meridionalis (*Gymnogeophagus meridionalis*) | Julián de Almeida | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Gymnogeophagus_meridionalis.jpg) |
| Gymnogeophagus labiatus (*Gymnogeophagus labiatus*) | W.S.Serra | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Gymnogeophagus_labiatus.jpg) |
| Gymnogeophagus tiraparae (*Gymnogeophagus tiraparae*) | W.S.Serra | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Gymnogeophagus_tiraparae.jpg) |
| Satanoperca lilith (*Satanoperca lilith*) | no rights reserved (iNaturalist) | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Satanoperca_lilith,_lago_robertinho_imported_from_iNaturalist_photo_431334604.jpg) |
| Ringstaartsnoekcichlide (*Saxatilia saxatilis*) | Julien Renoult | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Crenicichla_saxatilis_5587593.jpg) |
| Crenicichla alta (*Crenicichla alta*) | Jonathan (Jon) Armbruster | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Crenicichla_alta_GUY14-04_Amaila_black.jpg) |
| Lugubria marmorata (*Lugubria marmorata*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cichlidae_Crenicichla_marmorata_1.jpg) |
| Mesonauta insignis (*Mesonauta insignis*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Mesonauta_insignis.jpg) |
| Heros notatus (*Heros notatus*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Heros_notatus.jpg) |
| Pauwoogbaars (*Cichla ocellaris*) | Petruss | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cichla_ocellaris.jpg) |
| Cichla orinocensis (*Cichla orinocensis*) | JSutton93 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Orinoco_peacock_bass_(Cichla_orinocensis).jpg) |
| Acaronia nassa (*Acaronia nassa*) | Frank M Greco | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Acaronia_nassa.jpg) |
| Krobia guianensis (*Krobia guianensis*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Krobia_guianensis.jpg) |
| Hoplarchus psittacus (*Hoplarchus psittacus*) | Редько Юрій (Користувач:Mazapura) | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hoplarchus_psittacus-2.jpg) |
| Hypselecara temporalis (*Hypselecara temporalis*) | H. Zell | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hypselecara_temporalis_-_Karlsruhe_Zoo_01.jpg) |
| Boulengerella maculata (*Boulengerella maculata*) | H. Zell | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Boulengerella maculata - Karlsruhe Zoo 01.jpg) |
| Ctenolucius hujeta (*Ctenolucius hujeta*) | Tino Strauss | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Ctenolucius hujeta 2.jpg) |
| Erythrinus erythrinus (*Erythrinus erythrinus*) | Clinton & Charles Robertson | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Erythrinus erythrinus.jpg) |
| Hemigrammus hyanuary (*Hemigrammus hyanuary*) | Thomnight | CC BY-SA 2.0 de | [Commons](https://commons.wikimedia.org/wiki/File:Hemigrammus hyanuary thomnight 001.jpg) |
| Hyphessobrycon columbianus (*Hyphessobrycon columbianus*) | Marrabbio2 | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon colombianus.jpg) |
| Hyphessobrycon pyrrhonotus (*Hyphessobrycon pyrrhonotus*) | Thomnight | CC BY-SA 2.0 de | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon pyrrhonotus thomnight 001.jpg) |
| Gele fantoomzalm (*Hyphessobrycon roseus*) | karsten_s | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon roseus 321139470.jpg) |
| Iguanodectes geisleri (*Iguanodectes geisleri*) | Cedricguppy - Loury Cédric | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Iguanodectes geisleri - AquaPorteDoree.JPG) |
| Knodus borki (*Knodus borki*) | Axel Zarske and D. Bork | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Knodus borki (live).png) |
| Ladigesia roloffi (*Ladigesia roloffi*) | Cedricguppy - Loury Cédric | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Ladigesia roloffi - AquaPorteDoree 02.JPG) |
| Nannostomus mortenthaleri (*Nannostomus mortenthaleri*) | Brian Gratwicke | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Red Pencilfish.jpg) |
| Phenacogrammus aurantiacus (*Phenacogrammus aurantiacus*) | Tylwyth Eldar | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aquarium de la Porte Dorée - Poisson 21 (cropped).jpg) |
| Pristella maxillaris (*Pristella maxillaris*) | Richard Bartz, Munich Makro Freak | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Pristella maxillaris.jpg) |
| Danio kerri (*Danio kerri*) | Lerdsuwa | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Danio kerri.jpg) |
| Danio tinwini (*Danio tinwini*) | AverageWalrus | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Danio tinwini sparring males.jpg) |
| Dawkinsia rohani (*Dawkinsia rohani*) | Rahul Gautam | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:D rohani- Rahul Gautam.jpg) |
| Epalzeorhynchos kalopterum (*Epalzeorhynchos kalopterum*) | Mirko Hartig | CC BY-SA 2.0 de | [Commons](https://commons.wikimedia.org/wiki/File:Epalzeorhynchos kalopterus.jpg) |
| Garra flavatra (*Garra flavatra*) | Marcin Adrian | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Prachtalgenfresser (Panda Garra, Garra flavatra) by Marcin Adrian.jpg) |
| Leptobarbus hoevenii (*Leptobarbus hoevenii*) | Zahar AZ | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Juvenile Leptobarbus hoevenii.jpg) |
| Chinese zuigkarper (*Myxocyprinus asiaticus*) | 5snake5 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Myxocyprinus asiaticus - Wimpelkarpfen.jpg) |
| Opsarius pulchellus (*Opsarius pulchellus*) | Dwarren13 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:OP2.jpg) |
| Oreichthys crenuchoides (*Oreichthys crenuchoides*) | Beta Mahatvaraj | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Oreichthys crenuchoides (cropped).jpg) |
| Rasbora vulcanus (*Rasbora vulcanus*) | Andrewbogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rasbora vulcanus male.png) |
| Rhodeus sericeus (*Rhodeus sericeus*) | Gilles San Martin | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rhodeus sericeus - Bouvière - Amur bitterling.jpg) |
| Aulonocara hansbaenschi (*Aulonocara hansbaenschi*) | Radomil | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aulonocara hansbaenschi couple RB4.jpg) |
| Aulonocara steveni (*Aulonocara steveni*) | Lerdsuwa | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aulonocara steveni Usisya.jpg) |
| Benthochromis tricoti (*Benthochromis tricoti*) | MidgleyDJ | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Benthochromis tricoti.jpg) |
| Boulengerochromis microlepis (*Boulengerochromis microlepis*) | Dan Koehl | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:DKoehl Boulengerochromis microlepis.jpg) |
| Chalinochromis brichardi (*Chalinochromis brichardi*) | Entelognathus | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Chalinochromis Brichardi pair.jpg) |
| Copadichromis azureus (*Copadichromis azureus*) | Greg Hume | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Copadichromis azureus.jpg) |
| Copadichromis borleyi (*Copadichromis borleyi*) | Ed Schipul | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Copadichromis borleyi lake Malawi African Cichlid.jpg) |
| Cyphotilapia gibberosa (*Cyphotilapia gibberosa*) | George Berninger | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cyphotilapia gibberosa - GRB.jpg) |
| Dimidiochromis compressiceps (*Dimidiochromis compressiceps*) | Hectonichus | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cichlidae - Dimidiochromis compressiceps.JPG) |
| Etroplus canarensis (*Etroplus canarensis*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Etroplus canarensis.jpg) |
| Haplochromis aeneocolor (*Haplochromis aeneocolor*) | YFRag | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Haplochromis aeneocolor.jpg) |
| Haplochromis nyererei (*Haplochromis nyererei*) | Oliver Selz | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pundamilia nyererei.jpg) |
| Nannacara adoketa (*Nannacara adoketa*) | Birger A | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Ivanacara adoketa5265.jpg) |
| Julidochromis dickfeldi (*Julidochromis dickfeldi*) | regani (Wikimedia Commons) | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Julidochromis dickfeldi.jpg) |
| Julidochromis regani (*Julidochromis regani*) | Regani (Wikimedia Commons) | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Julidochromis regani.jpg) |
| Maylandia aurora (*Maylandia aurora*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Maylandia aurora.jpg) |
| Maylandia callainos (*Maylandia callainos*) | Alexandra Tyers | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Maylandia callainos.jpg) |
| Maylandia lombardoi (*Maylandia lombardoi*) | Toby Hudson | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Maylandia lombardoi male Lake Malawi Cichlid yellow.jpg) |
| Pseudotropheus cyaneorhabdos (*Pseudotropheus cyaneorhabdos*) | JanRehschuh | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Melanochromis Maingano Malawi cyaneorhabdos P1010034.JPG) |
| Labidochromis joanjohnsonae (*Labidochromis joanjohnsonae*) | Riftreef (Wikipedia Engels) | CC BY 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Melanochromis joanjohnsonae.jpg) |
| Neolamprologus similis (*Neolamprologus similis*) | berzentei, Yvonne Turkans | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Neolamprologus similis2.jpg) |
| Neolamprologus tretocephalus (*Neolamprologus tretocephalus*) | Chrumps | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Neolamprologus tretocephalus.jpg) |
| Parachromis dovii (*Parachromis dovii*) | Sesamehoneytart | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Parachromis dovii guapote.JPG) |
| Paretroplus menarambo (*Paretroplus menarambo*) | Hectonichus | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cichlidae - Paretroplus menarambo.JPG) |
| Petenia splendida (*Petenia splendida*) | Hectonichus | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cichlidae - Petenia splendida .JPG) |
| Protomelas fenestratus (*Protomelas fenestratus*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Protomelas fenestratus.jpg) |
| Protomelas taeniolatus (*Protomelas taeniolatus*) | Derek Ramsey | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Protomelas taeniolatus by Derek Ramsey.jpg) |
| Pseudocrenilabrus multicolor (*Pseudocrenilabrus multicolor*) | Julian Matz | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pseudocrenilabrus multicolor male.jpg) |
| Pseudotropheus crabro (*Pseudotropheus crabro*) | Nicolas COUTHOUIS | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Pseudotropheus Crabo Male.JPG) |
| Pseudotropheus johannii (*Pseudotropheus johannii*) | Stacnbake | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Melanochromis johanni Male.jpg) |
| Jack Dempsey (*Rocio octofasciata*) | Patrick Ch. Apfeld | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rocio octofasciata Zoo Schwerin.jpg) |
| Trachelyopterus fisheri (*Trachelyopterus fisheri*) | Ckf6412 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Trachelyopterus fisheri.jpg) |
| Trichromis salvini (*Trichromis salvini*) | Banteo | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Salvini4a.jpg) |
| Variabilichromis moorii (*Variabilichromis moorii*) | JBenoit | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Variabilichromis moorii en aquarium..jpg) |
| Xenotilapia flavipinnis (*Xenotilapia flavipinnis*) | Daiju Azuma | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xenotilapia flavipinnis by DaijuAzuma.jpg) |
| Aspidoras fuscoguttatus (*Aspidoras fuscoguttatus*) | Juan Felipe | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aspidoras fuscoguttatus.jpg) |
| Auchenoglanis occidentalis (*Auchenoglanis occidentalis*) | Liné1 | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Auchenoglanis occidentalis 01 by Line1.JPG) |
| Corydoras acutus (*Corydoras acutus*) | Frank M. Greco | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras acutus by Frank M. Greco.jpg) |
| Brochis delphax (*Brochis delphax*) | Frank M. Greco | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras delphax.jpg) |
| Osteogaster eques (*Osteogaster eques*) | Memelukas | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras eques.jpg) |
| Hoplisoma loxozonum (*Hoplisoma loxozonum*) | Soulkeeper | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras loxozonus 1.jpg) |
| Osteogaster melanotaenia (*Osteogaster melanotaenia*) | Karsten Schönherr | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras melanotaenia.JPG) |
| Brochis multiradiatus (*Brochis multiradiatus*) | Ltshears | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hog-nosedBrochis2010.jpg) |
| Corydoras semiaquilus (*Corydoras semiaquilus*) | Stan Shebs | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras semiaquilus 1.jpg) |
| Kryptopterus macrocephalus (*Kryptopterus macrocephalus*) | The Great Mule of Eupatoria | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:K macropterus 2.jpg) |
| Oxydoras niger (*Oxydoras niger*) | Tino Strauss | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pseudodoras niger 01.jpg) |
| Synodontis njassae (*Synodontis njassae*) | Paweł Cieśla (Staszek Szybki J) | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Synodontis njassae 01 ssj 20050321.jpg) |
| Phallichthys tico (*Phallichthys tico*) | Livebearerguy | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Phallichthys tico (1).jpg) |
| Betta burdigala (*Betta burdigala*) | YIE BABEL | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Betta Burdigala.jpg) |
| Betta persephone (*Betta persephone*) | Martin Fischer Parostoteles | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Betta persephone 1.jpg) |
| Betta rubra (*Betta rubra*) | Vycro567 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Polish 20240926 152819079.jpg) |
| Channa marulioides (*Channa marulioides*) | BEDO (Thailand) | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Channa marulioides.jpg) |
| Dario tigris (*Dario tigris*) | Nil NZ | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Female Dario tiris.jpg) |
| Nandus nebulosus (*Nandus nebulosus*) | R.workoran | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Bornean leafish.jpg) |
| Parasphaerichthys ocellatus (*Parasphaerichthys ocellatus*) | Andrew Bogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Parasphaerichthys ocellatus.png) |
| Glossolepis wanamensis (*Glossolepis wanamensis*) | Roan Art (Engelstalige Wikipedia) | CC BY 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Glossolepis wanamensis.jpg) |
| Melanotaenia parva (*Melanotaenia parva*) | Dirk Godlinski | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Melanotaenia parva male.jpg) |
| Aphyosemion ogoense (*Aphyosemion ogoense*) | Andrew Bogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aphyosemion ogoense.png) |
| Fundulopanchax scheeli (*Fundulopanchax scheeli*) | Violaine2, France | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Fundulopanchax scheeli.png) |
| Nothobranchius palmqvisti (*Nothobranchius palmqvisti*) | Andrewbogott | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Nothobranchius palmqvisti.jpg) |
| Acantopsis dialuzona (*Acantopsis dialuzona*) | Drachenschwertträger36 | CC BY-SA 2.0 de | [Commons](https://commons.wikimedia.org/wiki/File:Acantopsis dialuzona.jpg) |
| Beaufortia kweichowensis (*Beaufortia kweichowensis*) | Daiju Azuma | CC BY 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Beaufortia kweichowensis by DaijuAzuma.jpg) |
| Botia histrionica (*Botia histrionica*) | Lerdsuwa | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Botia histrionica.jpg) |
| Botia kubotai (*Botia kubotai*) | Pseudogastromyzon | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Botia kubotai3.jpg) |
| Pangio semicincta (*Pangio semicincta*) | AverageWalrus | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pangio semicincta.jpg) |
| Campylomormyrus tamandua (*Campylomormyrus tamandua*) | Carl Hopkins | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Campylomormyrus tamandua.png) |
| Catoprion mento (*Catoprion mento*) | Charles & Clint | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Catoprion mento (juvenile).jpeg) |
| Macrognathus tapirus (*Macrognathus tapirus*) | rukai95 | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Macrognathus tapirus 339373734.jpg) |
| Chanda pulcinella (*Chanda pulcinella*) | Puchatech K. | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Parambassis pulcinella (01).jpg) |
| Tetraodon lineatus (*Tetraodon lineatus*) | Earedien | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:TetraodonLineatus.JPG) |
| Mbu-kogelvis (*Tetraodon mbu*) | Cedricguppy - Loury Cédric | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Tetraodon mbu - aqua porte dorée 02.JPG) |
| Xenentodon cancila (*Xenentodon cancila*) | Guérin Nicolas | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Xenentodon cancila (Wroclaw zoo)-1.JPG) |
| Cambarellus diminutus (*Cambarellus diminutus*) | Hermann Junghans | CC BY-SA 3.0 de | [Commons](https://commons.wikimedia.org/wiki/File:Cambarella diminutus 1.jpg) |
| Cambarellus shufeldtii (*Cambarellus shufeldtii*) | Chris Lukhaup/USDA-FS | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Cambarellus shufeldtii.jpg) |
| Cherax peknyi (*Cherax peknyi*) | GeXeS | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cherax peknyi Zoo Brno 2020.jpg) |
| Kardinaalgarnaal (*Caridina dennerli*) | DirkBlankenhaus | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Caridina-dennerli.jpg) |
| Caridina loehae (*Caridina loehae*) | Planetinverts | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Orange delight shrimp sulawesi.jpg) |
| Caridina gracilirostris (*Caridina gracilirostris*) | Oorenotsoo | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Caridina gracilirostris.JPG) |
| Caridina thambipillai (*Caridina thambipillai*) | Andrew Bogott | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Caridina thambipillai, capitive raised.jpg) |
| Macrobrachium assamense (*Macrobrachium assamense*) | Tolderi | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Macrobrachium assamense male nearly adult.JPG) |
| Neocaridina zhangjiajiensis (*Neocaridina zhangjiajiensis*) | DirkBlankenhaus | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Neocaridina-cf-zhangjiajiensis-sp-white-pearl.jpg) |
| Macrobrachium lanchesteri (*Macrobrachium lanchesteri*) | Weimar Meneses | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Macrobrachium Lanchesteri (19306434602).jpg) |
| Macrobrachium dayanum (*Macrobrachium dayanum*) | Rejoice Gassah | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Macrobrachium dayanum.jpg) |
| Cambarellus puer (*Cambarellus puer*) | Brady Reed | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cambarellus puer 13203074.jpg) |
| Cambarellus lesliei (*Cambarellus lesliei*) | Chris Lukhaup/USDA-FS | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Cambarellus lesliei.jpg) |
| Procambarus enoplosternum (*Procambarus enoplosternum*) | Melunb | CC BY-SA 3.0 DE | [Commons](https://commons.wikimedia.org/wiki/File:Procambarus enoplosternum 10.jpg) |
| Cherax gherardii (*Cherax gherardii*) | 5snake5 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Cherax gherardii 'Blue Moon' male.jpg) |
| Aulonocara maylandi (*Aulonocara maylandi*) | Maha Dinesh | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Sulphurhead_cichlid.JPG) |
| Aulonocara nyassae (*Aulonocara nyassae*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aulonocara_nyassae_A.jpg) |
| Apistogramma cruzi (*Apistogramma cruzi*) | Mazapura | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Apistogramma_cruzi_(female).JPG) |
| Apistogramma erythrura (*Apistogramma erythrura*) | Britzke | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Apistogramma_erythrura.jpg) |
| Amatitlania siquia (*Amatitlania siquia*) | Haplochromis | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Amatitlania_siquia.jpg) |
| Australoheros facetus (*Australoheros facetus*) | CHUCAO | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Australoheros_facetus_-breeding_coloration-_(1).JPG) |
| Cyprichromis microlepidotus (*Cyprichromis microlepidotus*) | Rufus46 | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Kleinschuppiger_Kaerpflingsbuntbarsch_Cyprichromis_microlepidotus_Tierpark_Hellabrunn-1.jpg) |
| Fossorochromis rostratus (*Fossorochromis rostratus*) | Cedricguppy | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Fossorochromis_rostratus_-_mâle_en_aquarium_01.jpg) |
| Haplochromis sauvagei (*Haplochromis sauvagei*) | Haplochromis | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Haplochromis_sauvagei_male.jpg) |
| Haplotaxodon microlepis (*Haplotaxodon microlepis*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Haplotaxodon_microlepis_A.jpg) |
| Herichthys carpintis (*Herichthys carpintis*) | Theo Kruse | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pearlscale_cichlid_(Herichthys_carpintis).jpg) |
| Heros efasciatus (*Heros efasciatus*) | Rufus46 | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rotruecken-Augenfleck-Buntbarsch_Heros_efasciatus_Tierpark_Hellabrunn-1.jpg) |
| Lamprologus stappersi (*Lamprologus stappersi*) | onbekend | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Lamprologusstappersimalemcl.jpg) |
| Lepidiolamprologus cunningtoni (*Neolamprologus cunningtoni*) | Guérin Nicolas | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Lepidiolamprologus_cunningtoni_(Worclaw_zoo)-1.JPG) |
| Lethrinops lethrinus (*Lethrinops lethrinus*) | Alexandra Tyers | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Lethrinops_lethrinus_2.jpg) |
| Neolamprologus cylindricus (*Neolamprologus cylindricus*) | JBenoit | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Neolamprologus-cylindricus.jpg) |
| Neolamprologus longior (*Neolamprologus longior*) | Przemysław Malkowski | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Neolamprologus_longior_adult.jpg) |
| Neolamprologus sexfasciatus (*Neolamprologus sexfasciatus*) | Guérin Nicolas | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Neolamprologus_sexfasciatus_(Wroclaw_zoo).JPG) |
| Paratilapia polleni (*Paratilapia polleni*) | That Fish Place/That Pet Place | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Paratilapia_polleni_cichlid.jpg) |
| Pseudocrenilabrus philander (*Pseudocrenilabrus philander*) | Mahomed Desai | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pseudocrenilabrus_philander_70326936.jpg) |
| Simochromis diagramma (*Simochromis diagramma*) | H. Zell | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Simochromis_diagramma_-_Karlsruhe_Zoo_01.jpg) |
| Tanganicodus irsacae (*Tanganicodus irsacae*) | MidgleyDJ | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Tangicodus_irsacae.jpg) |
| Telmatochromis vittatus (*Telmatochromis vittatus*) | Eretmodus | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Telmato-vittat-congo0.1_(1).jpg) |
| Tylochromis lateralis (*Tylochromis lateralis*) | John P. Friel | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Tylochromis_lateralis_53146450.jpg) |
| Javaanse barbeel (*Barbonymus gonionotus*) | Yung-Lun Lin | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Barbonymus_gonionotus_-_Yung-Lun_Lin_-_586218900.jpeg) |
| Danio aesculapii (*Danio aesculapii*) | Andrewbogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Danio_aesculapii.png) |
| Devario maetaengensis (*Devario maetaengensis*) | Lerdsuwa | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Devario_maetaengensis.jpg) |
| Puntius chola (*Puntius chola*) | AravindManoj | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Puntiuschola.png) |
| Rasbora argyrotaenia (*Rasbora argyrotaenia*) | Abu Hamas | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rasbora_argyrotaenia_52466429.jpg) |
| Rasbora tornieri (*Rasbora tornieri*) | Ahsan al hidayat | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rasboratornieri.jpg) |
| Trigonostigma somphongsi (*Trigonostigma somphongsi*) | Lerdsuwa | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Trigonostigma_somphongsi.jpg) |
| Pangio pangia (*Pangio pangia*) | Beta Mahatvaraj | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pangio_pangia.jpg) |
| Schistura notostigma (*Schistura notostigma*) | Pieter Prins | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Spotback_Loach,_Sri_Lanka_imported_from_iNaturalist_photo_58771249.jpg) |
| Axelrodia stigmatias (*Axelrodia stigmatias*) | George Mattox, Camila S. Souza, Mônica Toledo-Piza, Ralf Britz, Claudio Oliveira | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Axelrodia_stigmatias_(Rio_Preto).png) |
| Jupiaba pinnata (*Jupiaba pinnata*) | Jonathan Armbruster | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Jupiaba_pinnata_Armbruster.jpg) |
| Micralestes acutidens (*Micralestes acutidens*) | Wynand Uys | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Micralestes_acutidens_15291392.jpg) |
| Mimagoniates microlepis (*Mimagoniates microlepis*) | Diogo Luiz | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Mimagoniates_microlepis.jpg) |
| Thayeria obliqua (*Thayeria obliqua*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Thayeria_obliqua.jpg) |
| Chaetostoma milesi (*Chaetostoma milesi*) | Frank Alvarez | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Chaetostoma_milesi.JPG) |
| Brochis imitator (*Brochis imitator*) | Soulkeeper | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras_imitator_5.jpg) |
| Hemiancistrus subviridis (*Hemiancistrus subviridis*) | 5snake5 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Hemiancistrus_subviridis_-_Gelber_Phantomwels.jpg) |
| Panaque nigrolineatus (*Panaque nigrolineatus*) | EvanBaldonado | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Royal_pleco_(Panaque_nigrolineatus)_at_the_California_Academy_of_Sciences.jpg) |
| Parotocinclus jumbo (*Parotocinclus jumbo*) | Haplochromis | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Parotocinclus_jumbo_2.jpg) |
| Peckoltia compta (*Peckoltia compta*) | Christian Dresel | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Peckoltia_compta_L134.jpg) |
| Sturisomatichthys aureus (*Sturisomatichthys aureus*) | NasserHalaweh | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Loricariidae_Sturisoma_aureum_1.2.jpg) |
| Gestreepte doornmeerval (*Platydoras costatus*) | Piotr Kuczynski | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Platydoras_costatus_1_(Piotr_Kuczynski).jpg) |
| Synodontis notatus (*Synodontis notatus*) | Frank M. Greco | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Synodontis_notatus.jpg) |
| Badis khwae (*Badis khwae*) | BEDO (Thailand) | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Badis_khwae_(Kullander_&_Britze,_2002).jpg) |
| Badis ruber (*Badis ruber*) | BEDO (Thailand) | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Badis_ruber_(Schreitmüller,_1923).jpg) |
| Badis siamensis (*Badis siamensis*) | BEDO (Thailand) | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Badis_siamensis_(Klausewitz,_1957).jpg) |
| Betta enisae (*Betta enisae*) | Jos Koster | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Betta_enisae.jpg) |
| Betta ferox (*Betta ferox*) | BEDO (Thailand) | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Betta_ferox.jpg) |
| Betta simplex (*Betta simplex*) | Andrewbogott | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Betta_simplex.jpg) |
| Parosphromenus paludicola (*Parosphromenus paludicola*) | BEDO (Thailand) | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Parosphronemus_paludicola.jpg) |
| Indische glasmeerval (*Kryptopterus bicirrhis*) | JC7001 | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Glass_Catfish_(Kryptopterus_bicirrhis)_(5520681894).jpg) |
| Betta pi (*Betta pi*) | BEDO (Thailand) | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Betta_pi.jpg) |
| Garcialebias viarius (*Garcialebias viarius*) | W.S.Serra | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Austrolebias_viarius.jpg) |
| Callopanchax occidentalis (*Callopanchax occidentalis*) | Andrew Bogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Callopanchax_occidentalis_Teme_Yella_SL89_DRCH,_Male.png) |
| Papiliolebias bitteri (*Papiliolebias bitteri*) | Facundo Bozza | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Papiliolebias_bitteri_chaco_salteño.jpg) |
| Poecilia salvatoris (*Poecilia salvatoris*) | Dnoerholm | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:PoeciliaSalvatoris.jpg) |
| Melanotaenia eachamensis (*Melanotaenia eachamensis*) | Martin F. Gomon | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:A_Lake_Eacham_Rainbowfish,_Melanotaenia_eachamensis,_in_an_aquarium.jpg) |
| Bedotia marojejy (*Bedotia marojejy*) | A. Saunders | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Bemar_m0.jpg) |
| Polypterus weeksii (*Polypterus weeksii*) | Stan Shebs | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Polypterus_weeksii_2.jpg) |
| Atya gabonensis (*Atya gabonensis*) | Citron | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Atya_gabonensis.JPG) |
| Neocaridina palmata (*Neocaridina palmata*) | DirkBlankenhaus | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Neocaridina-palmata.jpg) |
| Macrobrachium lar (*Macrobrachium lar*) | Totodu74 | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Macrobrachium_lar.jpg) |
| Cherax dispar (*Cherax dispar*) | Greg Tasney | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cherax_dispar,_Yarrabilba_QLD_4207,_Australia_imported_from_iNaturalist_photo_384264221.jpg) |
| Barbodes binotatus (*Barbodes binotatus*) | Abu Hamas | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Barbodes_binotatus_52313848.jpg) |
| Danio jaintianensis (*Danio jaintianensis*) | Beta Mahatvaraj | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Danio_jaintianensis.jpg) |
| Dawkinsia rubrotincta (*Dawkinsia rubrotincta*) | Factumquintus | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Puntius_rubrotinctus.jpg) |
| Danionella cerebrum (*Danionella cerebrum*) | AngryBurmese | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Danionella_cerebrum_Britz%2C_Conway_et_R%C3%BCber%2C_2021.jpg) |
| Pethia punctata (*Pethia punctata*) | Beta Mahatvaraj | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pethia_punctata.jpg) |
| Aphyosemion cameronense (*Aphyosemion cameronense*) | Jokuyken15 | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aphyosemion_cameronense.jpg) |
| Aphyosemion splendopleure (*Aphyosemion splendopleure*) | Andrew Bogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aphyosemion_splendopleure_'Tiko_green'_Male.png) |
| Neofundulus paraguayensis (*Neofundulus paraguayensis*) | Guyvir | Publiek domein | [Commons](https://commons.wikimedia.org/wiki/File:Neofundulus_paraguayensis_Ogun_Marcelino_AAK_12-03.jpg) |
| Pachypanchax patriciae (*Pachypanchax patriciae*) | KillisBS | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Pachypanchax_patriciae_blaue_Morphe.jpg) |
| Pachypanchax sparksorum (*Pachypanchax sparksorum*) | KillisBS | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:F6t2932p6696n9_UbXgPYyo.jpg) |
| Glossolepis maculosa (*Glossolepis maculosa*) | Dirk Godlinski | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Glossolepis_maculosus_m_Aquarium_DG.jpg) |
| Glossolepis ramuensis (*Glossolepis ramuensis*) | Dirk Godlinski | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Glossolepis_ramuensis_m_Aquarium_DG.jpg) |
| Melanotaenia lakamora (*Melanotaenia lakamora*) | Dirk Godlinski | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Melanotaenia_lakamora_male.jpg) |
| Melanotaenia sexlineata (*Melanotaenia sexlineata*) | Dirk Godlinski | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Melanotaenia_sexlineata_Kiunga.jpg) |
| Oryzias nigrimas (*Oryzias nigrimas*) | OpenCage | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Oryzias_nigrimas_by_OpenCage.jpg) |
| Hemigrammus barrigonae (*Hemigrammus barrigonae*) | D. Bork | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hemigrammus_barrigonae_(31499).png) |
| Hemigrammus ulreyi (*Hemigrammus ulreyi*) | Haplochromis | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hemigrammus_ulreyi.JPG) |
| Megalamphodus copelandi (*Megalamphodus copelandi*) | Gregoire Germeau | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Megalamphodus_copelandi.jpg) |
| Hyphessobrycon vilmae (*Hyphessobrycon vilmae*) | Andrewbogott | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hyphessobrycon_vilmae_dark_background.png) |
| Moenkhausia agnesae (*Moenkhausia agnesae*) | Cedricguppy - Loury Cédric | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Moenkhausia_agnesae_03.JPG) |
| Moenkhausia intermedia (*Moenkhausia intermedia*) | Julien Renoult | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Moenkhausia_intermedia_(5587910).jpg) |
| Nannostomus minimus (*Nannostomus minimus*) | Graham Ramsay | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Nannostomus_minimus.jpg) |
| Hoplisoma kanei (*Hoplisoma kanei*) | Whaldener Endo | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras_kanei_238028908.jpg) |
| Brochis pantanalensis (*Brochis pantanalensis*) | Christian Dresel | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras_pantanalensis.jpg) |
| Hoplisoma punctatum (*Hoplisoma punctatum*) | Karsten Schönherr | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Corydoras_punctatus_Gran_Rio.JPG) |
| Amphilius uranoscopus (*Amphilius uranoscopus*) | Andrew Deacon | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Amphilius_uranoscopus_15866397.jpg) |
| Baryancistrus demantoides (*Baryancistrus demantoides*) | Anne Blindheim | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Baryancistrus_demantoides.jpg) |
| Panaque armbrusteri (*Panaque armbrusteri*) | JSutton93 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Panaque_armbrusteri.jpg) |
| Jakkie (*Rhamdia quelen*) | Ictiologia Universidad Católica de Oriente | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rhamdia_quelen_(16335507449).jpg) |
| Sorubim lima (*Sorubim lima*) | Kambui | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Spatelwels_(Sorubim_lima)_(30145917290).jpg) |
| Aequidens diadema (*Aequidens diadema*) | Cichlidae | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Aequidens_Diadema_pair.jpg) |
| Aequidens pallidus (*Aequidens pallidus*) | David J. Stang | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Aequidens_pallidus_9zz.jpg) |
| Lugubria lenticulata (*Lugubria lenticulata*) | Clinton & Charles Robertson | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Crenicichla_lenticulata.jpg) |
| Geophagus brachybranchus (*Geophagus brachybranchus*) | Chrumps | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Geophagus_brachybranchus.jpg) |
| Hemichromis elongatus (*Hemichromis elongatus*) | Klaus Rudloff | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hemichromis_elongatus_B.jpg) |
| Thorichthys aureus (*Thorichthys aureus*) | Cedricguppy - Loury Cédric | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Thorichthys_aureus_-_AquaPorteDoree_03.JPG) |
| Betta pallifina (*Betta pallifina*) | Stacyh202 | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Male_Betta_Pallifina.jpg) |
| Dwergslangenkopvis (*Channa andrao*) | 5snake5 | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Channa_andrao_im_Aquarium.jpg) |
| Hubbsina turneri (*Hubbsina turneri*) | Arely Ramírez | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hubbsina_turneri_52071454.jpg) |
| Ilyodon furcidens (*Ilyodon furcidens*) | Andrewbogott | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Ilyodon_furcidens.jpg) |
| Neonoemacheilus labeosus (*Neonoemacheilus labeosus*) | Andy Gordon | CC BY 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Neonoemacheilus_labeosus.jpg) |
| Datnioides pulcher (*Datnioides pulcher*) | OpenCage | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Datnioides_pulcher_by_OpenCage.jpg) |
| Lepidocephalichthys thermalis (*Lepidocephalichthys thermalis*) | AravindManoj | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Thermalis.jpg) |
| Polypterus palmas (*Polypterus palmas*) | John P. Friel Ph.D. | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Polypterus_palmas_53146355.jpg) |
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
