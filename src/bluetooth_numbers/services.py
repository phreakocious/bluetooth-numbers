from uuid import UUID

from .utils import UUIDDict

service = UUIDDict(
    {
        0x1800: "Generic Access",
        0x1811: "Alert Notification Service",
        0x1815: "Automation IO",
        0x180F: "Battery Service",
        0x1810: "Blood Pressure",
        0x181B: "Body Composition",
        0x181E: "Bond Management Service",
        0x181F: "Continuous Glucose Monitoring",
        0x1805: "Current Time Service",
        0x1818: "Cycling Power",
        0x1816: "Cycling Speed and Cadence",
        0x180A: "Device Information",
        0x181A: "Environmental Sensing",
        0x1826: "Fitness Machine",
        0x1801: "Generic Attribute",
        0x1808: "Glucose",
        0x1809: "Health Thermometer",
        0x180D: "Heart Rate",
        0x1823: "HTTP Proxy",
        0x1812: "Human Interface Device",
        0x1802: "Immediate Alert",
        0x1821: "Indoor Positioning",
        0x183A: "Insulin Delivery",
        0x1820: "Internet Protocol Support Service",
        0x1803: "Link Loss",
        0x1819: "Location and Navigation",
        0x1827: "Mesh Provisioning Service",
        0x1828: "Mesh Proxy Service",
        0x1807: "Next DST Change Service",
        0x1825: "Object Transfer Service",
        0x180E: "Phone Alert Status Service",
        0x1822: "Pulse Oximeter Service",
        0x1829: "Reconnection Configuration",
        0x1806: "Reference Time Update Service",
        0x1814: "Running Speed and Cadence",
        0x1813: "Scan Parameters",
        0x1824: "Transport Discovery",
        0x1804: "Tx Power",
        0x181C: "User Data",
        0x181D: "Weight Scale",
        0x183B: "Binary Sensor",
        0x183C: "Emergency Configuration",
        0x183E: "Physical Activity Monitor",
        0x1843: "Audio Input Control",
        0x1844: "Volume Control",
        0x1845: "Volume Offset Control",
        0x1846: "Coordinated Set Identification",
        0x1847: "Device Time",
        0x1848: "Media Control",
        0x1849: "Generic Media Control",
        0x184A: "Constant Tone Extension",
        0x184B: "Telephone Bearer",
        0x184C: "Generic Telephone Bearer",
        0x184D: "Microphone Control",
        0x184E: "Audio Stream Control",
        0x184F: "Broadcast Audio Scan",
        0x1850: "Published Audio Capabilities",
        0x1851: "Basic Audio Announcement",
        0x1852: "Broadcast Audio Announcement",
        0x1853: "Common Audio",
        0x1854: "Hearing Access",
        0x1855: "TMAS",
        0xFE0F: "Signify Netherlands B.V. (formerly Phillips Lighting) Service",
        0xFEAA: "Eddystone",
        0xFE2C: "Fast Pair Service",
        0xFE59: "Secure DFU Service",
        0xFD6F: "Exposure Notification Service",
        0xFEBB: "File Transfer Service by Adafruit",
        0xFCC9: "SkyHawke Technologies",
        0xFCCA: "Cosmed s.r.l.",
        0xFCCB: "TOTO LTD.",
        0xFCCC: "WiFi Alliance",
        0xFCCD: "Zound Industries International AB",
        0xFCCE: "Luna Health, Inc.",
        0xFCCF: "Google LLC",
        0xFCD0: "Laerdal Medical AS",
        0xFCD1: "Shenzhen Benwei Media Co.,Ltd.",
        0xFCD2: "Allterco Robotics ltd",
        0xFCD3: "Fisher & Paykel Healthcare",
        0xFCD4: "OMRON HEALTHCARE",
        0xFCD5: "Nortek Security & Control",
        0xFCD6: "SWISSINNO SOLUTIONS AG",
        0xFCD7: "PowerPal Pty Ltd",
        0xFCD8: "Appex Factory S.L.",
        0xFCD9: "Huso, INC",
        0xFCDA: "Draeger",
        0xFCDB: "aconno GmbH",
        0xFCDC: "Amazon.com Services, LLC",
        0xFCDD: "Mobilaris AB",
        0xFCDE: "ARCTOP, INC.",
        0xFCDF: "NIO USA, Inc.",
        0xFCE0: "Akciju sabiedriba ”SAF TEHNIKA”",
        0xFCE1: "Sony Group Corporation",
        0xFCE2: "Baracoda Daily Healthtech",
        0xFCE3: "Smith & Nephew Medical Limited",
        0xFCE4: "Samsara Networks, Inc",
        0xFCE5: "Samsara Networks, Inc",
        0xFCE6: "Guard RFID Solutions Inc.",
        0xFCE7: "TKH Security B.V.",
        0xFCE8: "ITT Industries",
        0xFCE9: "MindRhythm, Inc.",
        0xFCEA: "Chess Wise B.V.",
        0xFCEB: "Avi­On",
        0xFCEC: "Griffwerk GmbH",
        0xFCED: "Workaround Gmbh",
        0xFCEE: "Velentium, LLC",
        0xFCEF: "Divesoft s.r.o.",
        0xFCF0: "Security Enhancement Systems, LLC",
        0xFCF1: "Google LLC",
        0xFCF2: "Bitwards Oy",
        0xFCF3: "Armatura LLC",
        0xFCF4: "Allegion",
        0xFCF5: "Trident Communication Technology, LLC",
        0xFCF6: "The Linux Foundation",
        0xFCF7: "Honor Device Co., Ltd.",
        0xFCF8: "Honor Device Co., Ltd.",
        0xFCF9: "Leupold & Stevens, Inc.",
        0xFCFA: "Leupold & Stevens, Inc.",
        0xFCFB: "Shenzhen Benwei Media Co., Ltd.",
        0xFCFC: "Barrot Technology Limited",
        0xFCFD: "Barrot Technology Limited",
        0xFCFE: "Sennheiser Consumer Audio GmbH",
        0xFCFF: "701x",
        0xFD00: "FUTEK Advanced Sensor Technology, Inc.",
        0xFD01: "Sanvita Medical Corporation",
        0xFD02: "LEGO System A/S",
        0xFD03: "Quuppa Oy",
        0xFD04: "Shure Inc.",
        0xFD05: "Qualcomm Technologies, Inc.",
        0xFD06: "RACE­AI LLC",
        0xFD07: "Swedlock AB",
        0xFD08: "Bull Group Incorporated Company",
        0xFD09: "Cousins and Sears LLC",
        0xFD0A: "Luminostics, Inc.",
        0xFD0B: "Luminostics, Inc.",
        0xFD0C: "OSM HK Limited",
        0xFD0D: "Blecon Ltd",
        0xFD0E: "HerdDogg, Inc",
        0xFD0F: "AEON MOTOR CO.,LTD.",
        0xFD10: "AEON MOTOR CO.,LTD.",
        0xFD11: "AEON MOTOR CO.,LTD.",
        0xFD12: "AEON MOTOR CO.,LTD.",
        0xFD13: "BRG Sports, Inc.",
        0xFD14: "BRG Sports, Inc.",
        0xFD15: "Panasonic Corporation",
        0xFD16: "Sensitech, Inc.",
        0xFD17: "LEGIC Identsystems AG",
        0xFD18: "LEGIC Identsystems AG",
        0xFD19: "Smith & Nephew Medical Limited",
        0xFD1A: "CSIRO",
        0xFD1B: "Helios Sports, Inc.",
        0xFD1C: "Brady Worldwide Inc.",
        0xFD1D: "Samsung Electronics Co., Ltd",
        0xFD1E: "Plume Design Inc.",
        0xFD1F: "3M",
        0xFD20: "GN Hearing A/S",
        0xFD21: "Huawei Technologies Co., Ltd.",
        0xFD22: "Huawei Technologies Co., Ltd.",
        0xFD23: "DOM Sicherheitstechnik GmbH & Co. KG",
        0xFD24: "GD Midea Air­Conditioning Equipment Co., Ltd.",
        0xFD25: "GD Midea Air­Conditioning Equipment Co., Ltd.",
        0xFD26: "Novo Nordisk A/S",
        0xFD27: "i2Systems",
        0xFD28: "Julius Blum GmbH",
        0xFD29: "Asahi Kasei Corporation",
        0xFD2A: "Sony Corporation",
        0xFD2B: "The Access Technologies",
        0xFD2C: "The Access Technologies",
        0xFD2D: "Xiaomi Inc.",
        0xFD2E: "Bitstrata Systems Inc.",
        0xFD2F: "Bitstrata Systems Inc.",
        0xFD30: "Sesam Solutions BV",
        0xFD31: "LG Electronics Inc.",
        0xFD32: "Gemalto Holding BV",
        0xFD33: "DashLogic, Inc.",
        0xFD34: "Aerosens LLC.",
        0xFD35: "Transsion Holdings Limited",
        0xFD36: "Google LLC",
        0xFD37: "TireCheck GmbH",
        0xFD38: "Danfoss A/S",
        0xFD39: "PREDIKTAS",
        0xFD3A: "Verkada Inc.",
        0xFD3B: "Verkada Inc.",
        0xFD3C: "Redline Communications Inc.",
        0xFD3D: "Woan Technology (Shenzhen) Co., Ltd.",
        0xFD3E: "Pure Watercraft, inc.",
        0xFD3F: "Cognosos, Inc",
        0xFD40: "Beflex Inc.",
        0xFD41: "Amazon Lab126",
        0xFD42: "Globe (Jiangsu) Co.,Ltd",
        0xFD43: "Apple Inc.",
        0xFD44: "Apple Inc.",
        0xFD45: "GB Solution co.,Ltd",
        0xFD46: "Lemco IKE",
        0xFD47: "Liberty Global Inc.",
        0xFD48: "Geberit International AG",
        0xFD49: "Panasonic Corporation",
        0xFD4A: "Sigma Elektro GmbH",
        0xFD4B: "Samsung Electronics Co., Ltd.",
        0xFD4C: "Adolf Wuerth GmbH & Co KG",
        0xFD4D: "70mai Co.,Ltd.",
        0xFD4E: "70mai Co.,Ltd.",
        0xFD4F: "Forkbeard Technologies AS",
        0xFD50: "Hangzhou Tuya Information Technology Co., Ltd",
        0xFD51: "UTC Fire and Security",
        0xFD52: "UTC Fire and Security",
        0xFD53: "PCI Private Limited",
        0xFD54: "Qingdao Haier Technology Co., Ltd.",
        0xFD55: "Braveheart Wireless, Inc.",
        0xFD56: "Resmed Ltd",
        0xFD57: "Volvo Car Corporation",
        0xFD58: "Volvo Car Corporation",
        0xFD59: "Samsung Electronics Co., Ltd.",
        0xFD5A: "Samsung Electronics Co., Ltd.",
        0xFD5B: "V2SOFT INC.",
        0xFD5C: "React Mobile",
        0xFD5D: "maxon motor ltd.",
        0xFD5E: "Tapkey GmbH",
        0xFD5F: "Oculus VR, LLC",
        0xFD60: "Sercomm Corporation",
        0xFD61: "Arendi AG",
        0xFD62: "Fitbit, Inc.",
        0xFD63: "Fitbit, Inc.",
        0xFD64: "INRIA",
        0xFD65: "Razer Inc.",
        0xFD66: "Zebra Technologies Corporation",
        0xFD67: "Montblanc Simplo GmbH",
        0xFD68: "Ubique Innovation AG",
        0xFD69: "Samsung Electronics Co., Ltd",
        0xFD6A: "Emerson",
        0xFD6B: "rapitag GmbH",
        0xFD6C: "Samsung Electronics Co., Ltd.",
        0xFD6D: "Sigma Elektro GmbH",
        0xFD6E: "Polidea sp. z o.o.",
        0xFD70: "GuangDong Oppo Mobile Telecommunications Corp., Ltd",
        0xFD71: "GN Hearing A/S",
        0xFD72: "Logitech International SA",
        0xFD73: "BRControls Products BV",
        0xFD74: "BRControls Products BV",
        0xFD75: "Insulet Corporation",
        0xFD76: "Insulet Corporation",
        0xFD77: "Withings",
        0xFD78: "Withings",
        0xFD79: "Withings",
        0xFD7A: "Withings",
        0xFD7B: "WYZE LABS, INC.",
        0xFD7C: "Toshiba Information Systems(Japan) Corporation",
        0xFD7D: "Center for Advanced Research Wernher Von Braun",
        0xFD7E: "Samsung Electronics Co., Ltd.",
        0xFD7F: "Husqvarna AB",
        0xFD80: "Phindex Technologies, Inc",
        0xFD81: "CANDY HOUSE, Inc.",
        0xFD82: "Sony Corporation",
        0xFD83: "iNFORM Technology GmbH",
        0xFD84: "Tile, Inc.",
        0xFD85: "Husqvarna AB",
        0xFD86: "Abbott",
        0xFD87: "Google LLC",
        0xFD88: "Urbanminded LTD",
        0xFD89: "Urbanminded LTD",
        0xFD8A: "Signify Netherlands B.V.",
        0xFD8B: "Jigowatts Inc.",
        0xFD8C: "Google LLC",
        0xFD8D: "quip NYC Inc.",
        0xFD8E: "Motorola Solutions",
        0xFD8F: "Matrix ComSec Pvt. Ltd.",
        0xFD90: "Guangzhou SuperSound Information Technology Co.,Ltd",
        0xFD91: "Groove X, Inc.",
        0xFD92: "Qualcomm Technologies International, Ltd. (QTIL)",
        0xFD93: "Bayerische Motoren Werke AG",
        0xFD94: "Hewlett Packard Enterprise",
        0xFD95: "Rigado",
        0xFD96: "Google LLC",
        0xFD97: "June Life, Inc.",
        0xFD98: "Disney Worldwide Services, Inc.",
        0xFD99: "ABB Oy",
        0xFD9A: "Huawei Technologies Co., Ltd.",
        0xFD9B: "Huawei Technologies Co., Ltd.",
        0xFD9C: "Huawei Technologies Co., Ltd.",
        0xFD9D: "Gastec Corporation",
        0xFD9E: "The Coca­Cola Company",
        0xFD9F: "VitalTech Affiliates LLC",
        0xFDA0: "Secugen Corporation",
        0xFDA1: "Groove X, Inc",
        0xFDA2: "Groove X, Inc",
        0xFDA3: "Inseego Corp.",
        0xFDA4: "Inseego Corp.",
        0xFDA5: "Neurostim OAB, Inc.",
        0xFDA6: "WWZN Information Technology Company Limited",
        0xFDA7: "WWZN Information Technology Company Limited",
        0xFDA8: "PSA Peugeot Citroën",
        0xFDA9: "Rhombus Systems, Inc.",
        0xFDAA: "Xiaomi Inc.",
        0xFDAB: "Xiaomi Inc.",
        0xFDAC: "Tentacle Sync GmbH",
        0xFDAD: "Houwa System Design, k.k.",
        0xFDAE: "Houwa System Design, k.k.",
        0xFDAF: "Wiliot LTD",
        0xFDB0: "Proxy Technologies, Inc.",
        0xFDB1: "Proxy Technologies, Inc.",
        0xFDB2: "Portable Multimedia Ltd",
        0xFDB3: "Audiodo AB",
        0xFDB4: "HP Inc",
        0xFDB5: "ECSG",
        0xFDB6: "GWA Hygiene GmbH",
        0xFDB7: "LivaNova USA Inc.",
        0xFDB8: "LivaNova USA Inc.",
        0xFDB9: "Comcast Cable Corporation",
        0xFDBA: "Comcast Cable Corporation",
        0xFDBB: "Profoto",
        0xFDBC: "Emerson",
        0xFDBD: "Clover Network, Inc.",
        0xFDBE: "California Things Inc.",
        0xFDBF: "California Things Inc.",
        0xFDC0: "Hunter Douglas",
        0xFDC1: "Hunter Douglas",
        0xFDC2: "Baidu Online Network Technology (Beijing) Co., Ltd",
        0xFDC3: "Baidu Online Network Technology (Beijing) Co., Ltd",
        0xFDC4: "Simavita (Aust) Pty Ltd",
        0xFDC5: "Automatic Labs",
        0xFDC6: "Eli Lilly and Company",
        0xFDC7: "Eli Lilly and Company",
        0xFDC8: "Hach – Danaher",
        0xFDC9: "Busch­Jaeger Elektro GmbH",
        0xFDCA: "Fortin Electronic Systems",
        0xFDCB: "Meggitt SA",
        0xFDCC: "Shoof Technologies",
        0xFDCD: "Qingping Technology (Beijing) Co., Ltd.",
        0xFDCE: "SENNHEISER electronic GmbH & Co. KG",
        0xFDCF: "Nalu Medical, Inc",
        0xFDD0: "Huawei Technologies Co., Ltd",
        0xFDD1: "Huawei Technologies Co., Ltd",
        0xFDD2: "Bose Corporation",
        0xFDD3: "FUBA Automotive Electronics GmbH",
        0xFDD4: "LX Solutions Pty Limited",
        0xFDD5: "Brompton Bicycle Ltd",
        0xFDD6: "Ministry of Supply",
        0xFDD7: "Emerson",
        0xFDD8: "Jiangsu Teranovo Tech Co., Ltd.",
        0xFDD9: "Jiangsu Teranovo Tech Co., Ltd.",
        0xFDDA: "MHCS",
        0xFDDB: "Samsung Electronics Co., Ltd.",
        0xFDDC: "4iiii Innovations Inc.",
        0xFDDD: "Arch Systems Inc",
        0xFDDE: "Noodle Technology Inc.",
        0xFDDF: "Harman International",
        0xFDE0: "John Deere",
        0xFDE1: "Fortin Electronic Systems",
        0xFDE2: "Google LLC",
        0xFDE3: "Abbott Diabetes Care",
        0xFDE4: "JUUL Labs, Inc.",
        0xFDE5: "SMK Corporation",
        0xFDE6: "Intelletto Technologies Inc",
        0xFDE7: "SECOM Co., LTD",
        0xFDE8: "Robert Bosch GmbH",
        0xFDE9: "Spacesaver Corporation",
        0xFDEA: "SeeScan, Inc",
        0xFDEB: "Syntronix Corporation",
        0xFDEC: "Mannkind Corporation",
        0xFDED: "Pole Star",
        0xFDEE: "Huawei Technologies Co., Ltd.",
        0xFDEF: "ART AND PROGRAM, INC.",
        0xFDF0: "Google LLC",
        0xFDF1: "LAMPLIGHT Co.,Ltd",
        0xFDF2: "AMICCOM Electronics Corporation",
        0xFDF3: "Amersports",
        0xFDF4: "O. E. M. Controls, Inc.",
        0xFDF5: "Milwaukee Electric Tools",
        0xFDF6: "AIAIAI ApS",
        0xFDF7: "HP Inc.",
        0xFDF8: "Onvocal",
        0xFDF9: "INIA",
        0xFDFA: "Tandem Diabetes Care",
        0xFDFB: "Tandem Diabetes Care",
        0xFDFC: "Optrel AG",
        0xFDFD: "RecursiveSoft Inc.",
        0xFDFE: "ADHERIUM(NZ) LIMITED",
        0xFDFF: "OSRAM GmbH",
        0xFE00: "Amazon.com Services, Inc.",
        0xFE01: "Duracell U.S. Operations Inc.",
        0xFE02: "Robert Bosch GmbH",
        0xFE03: "Amazon.com Services, Inc.",
        0xFE04: "OpenPath Security Inc",
        0xFE05: "CORE Transport Technologies NZ Limited",
        0xFE06: "Qualcomm Technologies, Inc.",
        0xFE07: "Sonos, Inc.",
        0xFE08: "Microsoft",
        0xFE09: "Pillsy, Inc.",
        0xFE0A: "ruwido austria gmbh",
        0xFE0B: "ruwido austria gmbh",
        0xFE0C: "Procter & Gamble",
        0xFE0D: "Procter & Gamble",
        0xFE0E: "Setec Pty Ltd",
        0xFE10: "LAPIS Technology Co., Ltd.",
        0xFE11: "GMC­I Messtechnik GmbH",
        0xFE12: "M­Way Solutions GmbH",
        0xFE13: "Apple Inc.",
        0xFE14: "Flextronics International USA Inc.",
        0xFE15: "Amazon.com Services, Inc..",
        0xFE16: "Footmarks, Inc.",
        0xFE17: "Telit Wireless Solutions GmbH",
        0xFE18: "Runtime, Inc.",
        0xFE19: "Google LLC",
        0xFE1A: "Tyto Life LLC",
        0xFE1B: "Tyto Life LLC",
        0xFE1C: "NetMedia, Inc.",
        0xFE1D: "Illuminati Instrument Corporation",
        0xFE1E: "Smart Innovations Co., Ltd",
        0xFE1F: "Garmin International, Inc.",
        0xFE20: "Emerson",
        0xFE21: "Bose Corporation",
        0xFE22: "Zoll Medical Corporation",
        0xFE23: "Zoll Medical Corporation",
        0xFE24: "August Home Inc",
        0xFE25: "Apple, Inc.",
        0xFE26: "Google LLC",
        0xFE27: "Google LLC",
        0xFE28: "Ayla Networks",
        0xFE29: "Gibson Innovations",
        0xFE2A: "DaisyWorks, Inc.",
        0xFE2B: "ITT Industries",
        0xFE2D: "SMART INNOVATION Co.,Ltd",
        0xFE2E: "ERi,Inc.",
        0xFE2F: "CRESCO Wireless, Inc",
        0xFE30: "Volkswagen AG",
        0xFE31: "Volkswagen AG",
        0xFE32: "Pro­Mark, Inc.",
        0xFE33: "CHIPOLO d.o.o.",
        0xFE34: "SmallLoop LLC",
        0xFE35: "HUAWEI Technologies Co., Ltd",
        0xFE36: "HUAWEI Technologies Co., Ltd",
        0xFE37: "Spaceek LTD",
        0xFE38: "Spaceek LTD",
        0xFE39: "TTS Tooltechnic Systems AG & Co. KG",
        0xFE3A: "TTS Tooltechnic Systems AG & Co. KG",
        0xFE3B: "Dolby Laboratories",
        0xFE3C: "alibaba",
        0xFE3D: "BD Medical",
        0xFE3E: "BD Medical",
        0xFE3F: "Friday Labs Limited",
        0xFE40: "Inugo Systems Limited",
        0xFE41: "Inugo Systems Limited",
        0xFE42: "Nets A/S",
        0xFE43: "Andreas Stihl AG & Co. KG",
        0xFE44: "SK Telecom",
        0xFE45: "Snapchat Inc",
        0xFE46: "B&O Play A/S",
        0xFE47: "General Motors",
        0xFE48: "General Motors",
        0xFE49: "SenionLab AB",
        0xFE4A: "OMRON HEALTHCARE Co., Ltd.",
        0xFE4B: "Signify Netherlands B.V. (formerly Philips Lighting B.V.)",
        0xFE4C: "Volkswagen AG",
        0xFE4D: "Casambi Technologies Oy",
        0xFE4E: "NTT docomo",
        0xFE4F: "Molekule, Inc.",
        0xFE50: "Google LLC",
        0xFE51: "SRAM",
        0xFE52: "SetPoint Medical",
        0xFE53: "3M",
        0xFE54: "Motiv, Inc.",
        0xFE55: "Google LLC",
        0xFE56: "Google LLC",
        0xFE57: "Dotted Labs",
        0xFE58: "Nordic Semiconductor ASA",
        0xFE5A: "Cronologics Corporation",
        0xFE5B: "GT­tronics HK Ltd",
        0xFE5C: "million hunters GmbH",
        0xFE5D: "Grundfos A/S",
        0xFE5E: "Plastc Corporation",
        0xFE5F: "Eyefi, Inc.",
        0xFE60: "Lierda Science & Technology Group Co., Ltd.",
        0xFE61: "Logitech International SA",
        0xFE62: "Indagem Tech LLC",
        0xFE63: "Connected Yard, Inc.",
        0xFE64: "Siemens AG",
        0xFE65: "CHIPOLO d.o.o.",
        0xFE66: "Intel Corporation",
        0xFE67: "Lab Sensor Solutions",
        0xFE68: "Qualcomm Life Inc",
        0xFE69: "Qualcomm Life Inc",
        0xFE6A: "Kontakt Micro­Location Sp. z o.o.",
        0xFE6B: "TASER International, Inc.",
        0xFE6C: "TASER International, Inc.",
        0xFE6D: "The University of Tokyo",
        0xFE6E: "The University of Tokyo",
        0xFE6F: "LINE Corporation",
        0xFE70: "Beijing Jingdong Century Trading Co., Ltd.",
        0xFE71: "Plume Design Inc",
        0xFE72: "Abbott (formerly St. Jude Medical, Inc.)",
        0xFE73: "Abbott (formerly St. Jude Medical, Inc.)",
        0xFE74: "unwire",
        0xFE75: "TangoMe",
        0xFE76: "TangoMe",
        0xFE77: "Hewlett­Packard Company",
        0xFE78: "Hewlett­Packard Company",
        0xFE79: "Zebra Technologies",
        0xFE7A: "Bragi GmbH",
        0xFE7B: "Orion Labs, Inc.",
        0xFE7C: "Telit Wireless Solutions (Formerly Stollmann E+V GmbH)",
        0xFE7D: "Aterica Health Inc.",
        0xFE7E: "Awear Solutions Ltd",
        0xFE7F: "Doppler Lab",
        0xFE80: "Doppler Lab",
        0xFE81: "Medtronic Inc.",
        0xFE82: "Medtronic Inc.",
        0xFE83: "Blue Bite",
        0xFE84: "RF Digital Corp",
        0xFE85: "RF Digital Corp",
        0xFE86: "HUAWEI Technologies Co., Ltd",
        0xFE87: "Qingdao Yeelink Information Technology Co., Ltd. ( 青岛亿联客信息技术有限公司 )",
        0xFE88: "SALTO SYSTEMS S.L.",
        0xFE89: "B&O Play A/S",
        0xFE8A: "Apple, Inc.",
        0xFE8B: "Apple, Inc.",
        0xFE8C: "TRON Forum",
        0xFE8D: "Interaxon Inc.",
        0xFE8E: "ARM Ltd",
        0xFE8F: "CSR",
        0xFE90: "JUMA",
        0xFE91: "Shanghai Imilab Technology Co.,Ltd",
        0xFE92: "Jarden Safety & Security",
        0xFE93: "OttoQ In",
        0xFE94: "OttoQ In",
        0xFE95: "Xiaomi Inc.",
        0xFE96: "Tesla Motors Inc.",
        0xFE97: "Tesla Motors Inc.",
        0xFE98: "Currant Inc",
        0xFE99: "Currant Inc",
        0xFE9A: "Estimote",
        0xFE9B: "Samsara Networks, Inc",
        0xFE9C: "GSI Laboratories, Inc.",
        0xFE9D: "Mobiquity Networks Inc",
        0xFE9E: "Dialog Semiconductor B.V.",
        0xFE9F: "Google LLC",
        0xFEA0: "Google LLC",
        0xFEA1: "Intrepid Control Systems, Inc.",
        0xFEA2: "Intrepid Control Systems, Inc.",
        0xFEA3: "ITT Industries",
        0xFEA4: "Paxton Access Ltd",
        0xFEA5: "GoPro, Inc.",
        0xFEA6: "GoPro, Inc.",
        0xFEA7: "UTC Fire and Security",
        0xFEA8: "Savant Systems LLC",
        0xFEA9: "Savant Systems LLC",
        0xFEAB: "Nokia",
        0xFEAC: "Nokia",
        0xFEAD: "Nokia",
        0xFEAE: "Nokia",
        0xFEAF: "Nest Labs Inc",
        0xFEB0: "Nest Labs Inc",
        0xFEB1: "Electronics Tomorrow Limited",
        0xFEB2: "Microsoft Corporation",
        0xFEB3: "Taobao",
        0xFEB4: "WiSilica Inc.",
        0xFEB5: "WiSilica Inc.",
        0xFEB6: "Vencer Co., Ltd",
        0xFEB7: "Meta Platforms, Inc.",
        0xFEB8: "Meta Platforms, Inc.",
        0xFEB9: "LG Electronics",
        0xFEBA: "Tencent Holdings Limited",
        0xFEBC: "Dexcom Inc",
        0xFEBD: "Clover Network, Inc",
        0xFEBE: "Bose Corporation",
        0xFEBF: "Nod, Inc.",
        0xFEC0: "KDDI Corporation",
        0xFEC1: "KDDI Corporation",
        0xFEC2: "Blue Spark Technologies, Inc.",
        0xFEC3: "360fly, Inc.",
        0xFEC4: "PLUS Location Systems",
        0xFEC5: "Realtek Semiconductor Corp.",
        0xFEC6: "Kocomojo, LLC",
        0xFEC7: "Apple, Inc.",
        0xFEC8: "Apple, Inc.",
        0xFEC9: "Apple, Inc.",
        0xFECA: "Apple, Inc.",
        0xFECB: "Apple, Inc.",
        0xFECC: "Apple, Inc.",
        0xFECD: "Apple, Inc.",
        0xFECE: "Apple, Inc.",
        0xFECF: "Apple, Inc.",
        0xFED0: "Apple, Inc.",
        0xFED1: "Apple, Inc.",
        0xFED2: "Apple, Inc.",
        0xFED3: "Apple, Inc.",
        0xFED4: "Apple, Inc.",
        0xFED5: "Plantronics Inc.",
        0xFED6: "Broadcom",
        0xFED7: "Broadcom",
        0xFED8: "Google LLC",
        0xFED9: "Pebble Technology Corporation",
        0xFEDA: "ISSC Technologies Corp.",
        0xFEDB: "Perka, Inc.",
        0xFEDC: "Jawbone",
        0xFEDD: "Jawbone",
        0xFEDE: "Coin, Inc.",
        0xFEDF: "Design SHIFT",
        0xFEE0: "Anhui Huami Information Technology Co., Ltd.",
        0xFEE1: "Anhui Huami Information Technology Co., Ltd.",
        0xFEE2: "Anki, Inc.",
        0xFEE3: "Anki, Inc.",
        0xFEE4: "Nordic Semiconductor ASA",
        0xFEE5: "Nordic Semiconductor ASA",
        0xFEE6: "Silvair, Inc.",
        0xFEE7: "Tencent Holdings Limited.",
        0xFEE8: "Quintic Corp.",
        0xFEE9: "Quintic Corp.",
        0xFEEA: "Swirl Networks, Inc.",
        0xFEEB: "Swirl Networks, Inc.",
        0xFEEC: "Tile, Inc.",
        0xFEED: "Tile, Inc.",
        0xFEEE: "Polar Electro Oy",
        0xFEEF: "Polar Electro Oy",
        0xFEF0: "Intel",
        0xFEF1: "CSR",
        0xFEF2: "CSR",
        0xFEF3: "Google LLC",
        0xFEF4: "Google LLC",
        0xFEF5: "Dialog Semiconductor GmbH",
        0xFEF6: "Wicentric, Inc.",
        0xFEF7: "Aplix Corporation",
        0xFEF8: "Aplix Corporation",
        0xFEF9: "PayPal, Inc.",
        0xFEFA: "PayPal, Inc.",
        0xFEFB: "Telit Wireless Solutions (Formerly Stollmann E+V GmbH)",
        0xFEFC: "Gimbal, Inc.",
        0xFEFD: "Gimbal, Inc.",
        0xFEFE: "GN ReSound A/S",
        0xFEFF: "GN Netcom",
        0xFFF3: "FiRa Consortium service",
        0xFFF4: "FiRa Consortium service",
        0xFFF5: "Car Connectivity Consortium, LLC service",
        0xFFF6: "ZigBee Alliance service",
        0xFFF7: "ZigBee Alliance service",
        0xFFF8: "Mopria Alliance BLE Service service",
        0xFFF9: "FIDO2 secure client-to-authenticator transport service",
        0xFFFA: "ASTM Remote ID service",
        0xFFFB: "Direct Thread Commissioning service",
        0xFFFC: "Wireless Power Transfer (WPT) Service service",
        0xFFFD: "Universal Second Factor Authenticator Service service",
        0xFFFE: "Wireless Power Transfer Service service",
        UUID(
            "932C32BD-0000-47A2-835A-A8D455B859DD"
        ): "Phillips Hue Light Control Service",
        UUID(
            "0000180A-0000-1000-8000-00805F9B34FB"
        ): "Phillips Hue Light Information Service",
        UUID(
            "B8843ADD-0000-4AA1-8794-C3F462030BDA"
        ): "Phillips Hue Light Update Service",
        UUID(
            "7905F431-B5CE-4E99-A40F-4B1E122D00D0"
        ): "Apple Notification Center Service",
        UUID("89D3502B-0F36-433A-8EF4-C502AD55F8DC"): "Apple Media Service",
        UUID("7DFC6000-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Service",
        UUID("7DFC7000-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Service",
        UUID("7DFC8000-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Service",
        UUID("7DFC9000-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Service",
        UUID("E95D0753-251D-470A-A062-FA1922DFA9A8"): "micro:bit Accelerometer Service",
        UUID("E95DF2D8-251D-470A-A062-FA1922DFA9A8"): "micro:bit Magnetometer Service",
        UUID("E95D9882-251D-470A-A062-FA1922DFA9A8"): "micro:bit Button Service",
        UUID("E95D127B-251D-470A-A062-FA1922DFA9A8"): "micro:bit IO Pin Service",
        UUID("E95DD91D-251D-470A-A062-FA1922DFA9A8"): "micro:bit LED Service",
        UUID("E95D93AF-251D-470A-A062-FA1922DFA9A8"): "micro:bit Event Service",
        UUID("E95D93B0-251D-470A-A062-FA1922DFA9A8"): "micro:bit DFU Control Service",
        UUID("E95D6100-251D-470A-A062-FA1922DFA9A8"): "micro:bit Temperature Service",
        UUID("EF680100-9B35-4933-9B10-52FFA9740042"): "Thingy Configuration Service",
        UUID("EF680200-9B35-4933-9B10-52FFA9740042"): "Thingy Weather Station Service",
        UUID("EF680300-9B35-4933-9B10-52FFA9740042"): "Thingy UI Service",
        UUID("EF680400-9B35-4933-9B10-52FFA9740042"): "Thingy Motion Service",
        UUID("EF680500-9B35-4933-9B10-52FFA9740042"): "Thingy Sound Service",
        UUID("00001523-1212-EFDE-1523-785FEABCD123"): "Nordic LED and Button Service",
        UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E"): "Nordic UART Service",
        UUID("A3C87500-8ED3-4BDF-8A39-A01BEBEDE295"): "Eddystone Configuration Service",
        UUID("00001530-1212-EFDE-1523-785FEABCD123"): "Legacy DFU Service",
        UUID(
            "8E400001-F315-4F60-9FB8-838830DAEA50"
        ): "Experimental Buttonless DFU Service",
        UUID(
            "E2A00001-EC31-4EC3-A97A-1C34D87E9878"
        ): "Edge Impulse Remote Management Service",
        UUID("8D53DC1D-1DB7-4CD3-868B-8A527460AA84"): "SMP Service",
        UUID(
            "00001623-1212-EFDE-1623-785FEABCD123"
        ): "LEGO® Wireless Protocol v3 Hub Service",
        UUID(
            "00001625-1212-EFDE-1623-785FEABCD123"
        ): "LEGO® Wireless Protocol v3 Bootloader Service",
        UUID("ADAF0100-C332-42A8-93BD-25E905756CB8"): "Adafruit Temperature Service",
        UUID("ADAF0200-C332-42A8-93BD-25E905756CB8"): "Adafruit Accelerometer Service",
        UUID("ADAF0300-C332-42A8-93BD-25E905756CB8"): "Adafruit Light Service",
        UUID("ADAF0400-C332-42A8-93BD-25E905756CB8"): "Adafruit Gyroscope Service",
        UUID("ADAF0500-C332-42A8-93BD-25E905756CB8"): "Adafruit Magnetometer Service",
        UUID("ADAF0600-C332-42A8-93BD-25E905756CB8"): "Adafruit Button Service",
        UUID("ADAF0700-C332-42A8-93BD-25E905756CB8"): "Adafruit Humidity Service",
        UUID("ADAF0800-C332-42A8-93BD-25E905756CB8"): "Adafruit Barometric Service",
        UUID("ADAF0900-C332-42A8-93BD-25E905756CB8"): "Adafruit Addressable Service",
        UUID("ADAF0A00-C332-42A8-93BD-25E905756CB8"): "Adafruit Color Service",
        UUID("ADAF0B00-C332-42A8-93BD-25E905756CB8"): "Adafruit Sound Service",
        UUID("ADAF0C00-C332-42A8-93BD-25E905756CB8"): "Adafruit Tone Service",
        UUID("ADAF0D00-C332-42A8-93BD-25E905756CB8"): "Adafruit Quaternion Service",
        UUID("ADAF0E00-C332-42A8-93BD-25E905756CB8"): "Adafruit Proximity Service",
        UUID(
            "F000FFC0-0451-4000-B000-000000000000"
        ): "Texas Instruments Over-the-Air Download (OAD) Service",
        UUID("0FDA92B2-44A2-4AF2-84F5-FA682BAA2B8D"): "Helium Hotspot Custom Service",
        UUID("54220000-F6A5-4007-A371-722F4EBD8436"): "Memfault Diagnostic Service",
    }
)
