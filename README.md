# aquarium-soorten

Soortenlijst en afbeeldingen voor een persoonlijke Android-app om aquaria bij te houden. De app haalt `species.json` en de afbeeldingen hier op; zonder internet gebruikt ze de kopie die in de app zit.

## Wat erin staat

- `species.json`: 179 zoetwatersoorten (dieren en planten) met temperatuur, pH, grootte, minimale bakgrootte, groepsgrootte, karakter en verzorging. De waarden komen uit algemeen bekende aquariumkennis, gecontroleerd met openbare bronnen, en zijn in eigen woorden opgeschreven.
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
