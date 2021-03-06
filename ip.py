#!/usr/bin/python
import csv
from geoip import geolite2

#ISO2 country code replacements
replacements = (
('AF','Afghanistan'),
('AX','Aland Islands'),
('AL','Albania'),
('DZ','Algeria'),
('AS','American Samoa'),
('AD','Andorra'),
('AO','Angola'),
('AI','Anguilla'),
('AQ','Antarctica'),
#('AG','Antigua and Barbuda'),
('AG','Antigua'),
('AR','Argentina'),
('AM','Armenia'),
('AW','Aruba'),
('AU','Australia'),
('AT','Austria'),
('AZ','Azerbaijan'),
('BS','Bahamas'),
('BH','Bahrain'),
('BD','Bangladesh'),
('BB','Barbados'),
('BY','Belarus'),
('BE','Belgium'),
('BZ','Belize'),
('BJ','Benin'),
('BM','Bermuda'),
('BT','Bhutan'),
#('BO','Bolivia, Plurinational State of'),
('BO','Bolivia'),
#('BQ','Bonaire, Sint Eustatius and Saba'),
('BQ','Bonaire'),
#('BA','Bosnia and Herzegovina'),
('BA','Bosnia'),
('BW','Botswana'),
('BV','Bouvet Island'),
('BR','Brazil'),
#('IO','British Indian Ocean Territory'),
('IO','Indian Ocean'),
('BN','Brunei Darussalam'),
('BG','Bulgaria'),
('BF','Burkina Faso'),
('BI','Burundi'),
('KH','Cambodia'),
('CM','Cameroon'),
('CA','Canada'),
('CV','Cape Verde'),
('KY','Cayman Islands'),
('CF','Central African Republic'),
('TD','Chad'),
('CL','Chile'),
('CN','China'),
('CX','Christmas Island'),
#('CC','Cocos (Keeling) Islands'),
('CC','Keeling Islands'),
('CO','Colombia'),
('KM','Comoros'),
('CG','Congo'),
#('CD','Congo, The Democratic Republic of the'),
('CD','Congo'),
('CK','Cook Islands'),
('CR','Costa Rica'),
('CI','Cote dIvoire'),
('HR','Croatia'),
('CU','Cuba'),
('CW','Curacao'),
('CY','Cyprus'),
('CZ','Czech Republic'),
('DK','Denmark'),
('DJ','Djibouti'),
('DM','Dominica'),
('DO','Dominican Republic'),
('EC','Ecuador'),
('EG','Egypt'),
('SV','El Salvador'),
('GQ','Equatorial Guinea'),
('ER','Eritrea'),
('EE','Estonia'),
('ET','Ethiopia'),
#('FK','Falkland Islands (Malvinas)'),
('FK','Falkland Islands'),
('FO','Faroe Islands'),
('FJ','Fiji'),
('FI','Finland'),
('FR','France'),
('GF','French Guiana'),
('PF','French Polynesia'),
('TF','French Southern Territories'),
('GA','Gabon'),
('GM','Gambia'),
('GE','Georgia'),
('DE','Germany'),
('GH','Ghana'),
('GI','Gibraltar'),
('GR','Greece'),
('GL','Greenland'),
('GD','Grenada'),
('GP','Guadeloupe'),
('GU','Guam'),
('GT','Guatemala'),
('GG','Guernsey'),
('GN','Guinea'),
('GW','Guinea-Bissau'),
('GY','Guyana'),
('HT','Haiti'),
('HM','Heard Island and McDonald Islands'),
#('VA','Holy See (Vatican City State)'),
('VA','Vatican City'),
('HN','Honduras'),
('HK','Hong Kong'),
('HU','Hungary'),
('IS','Iceland'),
('IN','India'),
('ID','Indonesia'),
#('IR','Iran, Islamic Republic of'),
('IR','Iran'),
('IQ','Iraq'),
('IE','Ireland'),
('IM','Isle of Man'),
('IL','Israel'),
('IT','Italy'),
('JM','Jamaica'),
('JP','Japan'),
('JE','Jersey'),
('JO','Jordan'),
('KZ','Kazakhstan'),
('KE','Kenya'),
('KI','Kiribati'),
#('KP','Korea, Democratic Peoples Republic of'),
('KP','North Korea'),
#('KR','Korea, Republic of'),
('KR','South Korea'),
('KW','Kuwait'),
('KG','Kyrgyzstan'),
#('LA','Lao Peoples Democratic Republic'),
('LA','Laos'),
('LV','Latvia'),
('LB','Lebanon'),
('LS','Lesotho'),
('LR','Liberia'),
('LY','Libya'),
('LI','Liechtenstein'),
('LT','Lithuania'),
('LU','Luxembourg'),
('MO','Macao'),
#('MK','Macedonia, Republic of'),
('MK','Macedonia'),
('MG','Madagascar'),
('MW','Malawi'),
('MY','Malaysia'),
('MV','Maldives'),
('ML','Mali'),
('MT','Malta'),
('MH','Marshall Islands'),
('MQ','Martinique'),
('MR','Mauritania'),
('MU','Mauritius'),
('YT','Mayotte'),
('MX','Mexico'),
#('FM','Micronesia, Federated States of'),
('FM','Micronesia'),
#('MD','Moldova, Republic of'),
('MD','Moldova'),
('MC','Monaco'),
('MN','Mongolia'),
('ME','Montenegro'),
('MS','Montserrat'),
('MA','Morocco'),
('MZ','Mozambique'),
('MM','Myanmar'),
('NA','Namibia'),
('NR','Nauru'),
('NP','Nepal'),
('NL','Netherlands'),
('NC','New Caledonia'),
('NZ','New Zealand'),
('NI','Nicaragua'),
('NE','Niger'),
('NG','Nigeria'),
('NU','Niue'),
('NF','Norfolk Island'),
('MP','Northern Mariana Islands'),
('NO','Norway'),
('OM','Oman'),
('PK','Pakistan'),
('PW','Palau'),
#('PS','Palestinian Territory, Occupied'),
('PS','Palestine'),
('PA','Panama'),
('PG','Papua New Guinea'),
('PY','Paraguay'),
('PE','Peru'),
('PH','Philippines'),
('PN','Pitcairn'),
('PL','Poland'),
('PT','Portugal'),
('PR','Puerto Rico'),
('QA','Qatar'),
('RE','Reunion'),
('RO','Romania'),
#('RU','Russian Federation'),
('RU','Russia'),
('RW','Rwanda'),
('BL','Saint Barthelemy'),
#('SH','Saint Helena, Ascension and Tristan da Cunha'),
('SH','Saint Helena'),
('KN','Saint Kitts and Nevis'),
('LC','Saint Lucia'),
#('MF','Saint Martin (French part)'),
('MF','Saint Martin'),
('PM','Saint Pierre and Miquelon'),
('VC','Saint Vincent and the Grenadines'),
('WS','Samoa'),
('SM','San Marino'),
('ST','Sao Tome and Principe'),
('SA','Saudi Arabia'),
('SN','Senegal'),
('RS','Serbia'),
('SC','Seychelles'),
('SL','Sierra Leone'),
('SG','Singapore'),
#('SX','Sint Maarten (Dutch part)'),
('SX','Sint Maarten'),
('SK','Slovakia'),
('SI','Slovenia'),
('SB','Solomon Islands'),
('SO','Somalia'),
('ZA','South Africa'),
('GS','South Georgia and the South Sandwich Islands'),
('ES','Spain'),
('LK','Sri Lanka'),
('SD','Sudan'),
('SR','Suriname'),
('SS','South Sudan'),
('SJ','Svalbard and Jan Mayen'),
('SZ','Swaziland'),
('SE','Sweden'),
('CH','Switzerland'),
#('SY','Syrian Arab Republic'),
('SY','Syria'),
#('TW','Taiwan, Province of China'),
('TW','Taiwan'),
('TJ','Tajikistan'),
#('TZ','Tanzania, United Republic of'),
('TZ','Tanzania'),
('TH','Thailand'),
('TL','Timor-Leste'),
('TG','Togo'),
('TK','Tokelau'),
('TO','Tonga'),
('TT','Trinidad and Tobago'),
('TN','Tunisia'),
('TR','Turkey'),
('TM','Turkmenistan'),
('TC','Turks and Caicos Islands'),
('TV','Tuvalu'),
('UG','Uganda'),
('UA','Ukraine'),
('AE','United Arab Emirates'),
('GB','United Kingdom'),
('US','United States'),
('UM','United States Minor Outlying Islands'),
('UY','Uruguay'),
('UZ','Uzbekistan'),
('VU','Vanuatu'),
#('VE','Venezuela, Bolivarian Republic of'),
('VE','Venezuela'),
('VN','Viet Nam'),
('VG','Virgin Islands, British'),
('VI','Virgin Islands, U.S.'),
('WF','Wallis and Futuna'),
('EH','Western Sahara'),
('YE','Yemen'),
('ZM','Zambia'),
('ZW','Zimbabwe')
)


iplist = []
clist = []

with open('ip.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
#        print ', '.join(row)
        ip = ', '.join(row)
	try:
        	match = geolite2.lookup(ip)
		c = match.country

		iplist.append(ip)
		clist.append(c)

	except AttributeError:
		print '...'
		iplist.append(ip)
		clist.append('null')

# This code replaces ISO short codes with full names.
# Comment out to keep short codes
#---------------------
k = 0
for c in clist:
  for old, new in replacements:
    try:
      clist[k] = clist[k].replace(old, new)
      print clist[k]
    except AttributeError:
      print '...'
  k += 1
#--------------------


with open('countries.csv', 'w') as csvfile:
        fieldnames = ['IP', 'Country']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

	k=0
	for i in iplist:
       		writer.writerow({'IP': iplist[k], 'Country': clist[k]})
		k+=1
