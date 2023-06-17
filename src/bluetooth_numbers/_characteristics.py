"""Module with UUIDs and names for Bluetooth characteristics.

Usage:

>>> from bluetooth_numbers import characteristic
>>> from uuid import UUID
>>> characteristic[0x2A37]
'Heart Rate Measurement'
>>> characteristic[UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")]
'UART RX Characteristic'
"""
from uuid import UUID

from bluetooth_numbers.dicts import UUIDDict

characteristic = UUIDDict(
    {
        0x2A7E: "Aerobic Heart Rate Lower Limit",
        0x2A84: "Aerobic Heart Rate Upper Limit",
        0x2A7F: "Aerobic Threshold",
        0x2A80: "Age",
        0x2A5A: "Aggregate",
        0x2A43: "Alert Category ID",
        0x2A42: "Alert Category ID Bit Mask",
        0x2A06: "Alert Level",
        0x2A44: "Alert Notification Control Point",
        0x2A3F: "Alert Status",
        0x2AB3: "Altitude",
        0x2A81: "Anaerobic Heart Rate Lower Limit",
        0x2A82: "Anaerobic Heart Rate Upper Limit",
        0x2A83: "Anaerobic Threshold",
        0x2A58: "Analog",
        0x2A59: "Analog Output",
        0x2A73: "Apparent Wind Direction",
        0x2A72: "Apparent Wind Speed",
        0x2A01: "Appearance",
        0x2AA3: "Barometric Pressure Trend",
        0x2A19: "Battery Level",
        0x2A1B: "Battery Level State",
        0x2A1A: "Battery Power State",
        0x2A49: "Blood Pressure Feature",
        0x2A35: "Blood Pressure Measurement",
        0x2A9B: "Body Composition Feature",
        0x2A9C: "Body Composition Measurement",
        0x2A38: "Body Sensor Location",
        0x2AA4: "Bond Management Control Point",
        0x2AA5: "Bond Management Features",
        0x2A22: "Boot Keyboard Input Report",
        0x2A32: "Boot Keyboard Output Report",
        0x2A33: "Boot Mouse Input Report",
        0x2AA6: "Central Address Resolution",
        0x2AA8: "CGM Feature",
        0x2AA7: "CGM Measurement",
        0x2AAB: "CGM Session Run Time",
        0x2AAA: "CGM Session Start Time",
        0x2AAC: "CGM Specific Ops Control Point",
        0x2AA9: "CGM Status",
        0x2ACE: "Cross Trainer Data",
        0x2A5C: "CSC Feature",
        0x2A5B: "CSC Measurement",
        0x2A2B: "Current Time",
        0x2A66: "Cycling Power Control Point",
        0x2A65: "Cycling Power Feature",
        0x2A63: "Cycling Power Measurement",
        0x2A64: "Cycling Power Vector",
        0x2A99: "Database Change Increment",
        0x2A85: "Date of Birth",
        0x2A86: "Date of Threshold Assessment",
        0x2A08: "Date Time",
        0x2A0A: "Day Date Time",
        0x2A09: "Day of Week",
        0x2A7D: "Descriptor Value Changed",
        0x2A00: "Device Name",
        0x2A7B: "Dew Point",
        0x2A56: "Digital",
        0x2A57: "Digital Output",
        0x2A0D: "DST Offset",
        0x2A6C: "Elevation",
        0x2A87: "Email Address",
        0x2A0B: "Exact Time 100",
        0x2A0C: "Exact Time 256",
        0x2A88: "Fat Burn Heart Rate Lower Limit",
        0x2A89: "Fat Burn Heart Rate Upper Limit",
        0x2A26: "Firmware Revision String",
        0x2A8A: "First Name",
        0x2AD9: "Fitness Machine Control Point",
        0x2ACC: "Fitness Machine Feature",
        0x2ADA: "Fitness Machine Status",
        0x2A8B: "Five Zone Heart Rate Limits",
        0x2AB2: "Floor Number",
        0x2A8C: "Gender",
        0x2A51: "Glucose Feature",
        0x2A18: "Glucose Measurement",
        0x2A34: "Glucose Measurement Context",
        0x2A74: "Gust Factor",
        0x2A27: "Hardware Revision String",
        0x2A39: "Heart Rate Control Point",
        0x2A8D: "Heart Rate Max",
        0x2A37: "Heart Rate Measurement",
        0x2A7A: "Heat Index",
        0x2A8E: "Height",
        0x2A4C: "HID Control Point",
        0x2A4A: "HID Information",
        0x2A8F: "Hip Circumference",
        0x2ABA: "HTTP Control Point",
        0x2AB9: "HTTP Entity Body",
        0x2AB7: "HTTP Headers",
        0x2AB8: "HTTP Status Code",
        0x2ABB: "HTTPS Security",
        0x2A6F: "Humidity",
        0x2B22: "IDD Annunciation Status",
        0x2B25: "IDD Command Control Point",
        0x2B26: "IDD Command Data",
        0x2B23: "IDD Features",
        0x2B28: "IDD History Data",
        0x2B27: "IDD Record Access Control Point",
        0x2B21: "IDD Status",
        0x2B20: "IDD Status Changed",
        0x2B24: "IDD Status Reader Control Point",
        0x2A2A: "IEEE 11073-20601 Regulatory Certification Data List",
        0x2AD2: "Indoor Bike Data",
        0x2AAD: "Indoor Positioning Configuration",
        0x2A36: "Intermediate Cuff Pressure",
        0x2A1E: "Intermediate Temperature",
        0x2A77: "Irradiance",
        0x2AA2: "Language",
        0x2A90: "Last Name",
        0x2AAE: "Latitude",
        0x2A6B: "LN Control Point",
        0x2A6A: "LN Feature",
        0x2AB1: "Local East Coordinate",
        0x2AB0: "Local North Coordinate",
        0x2A0F: "Local Time Information",
        0x2A67: "Location and Speed Characteristic",
        0x2AB5: "Location Name",
        0x2AAF: "Longitude",
        0x2A2C: "Magnetic Declination",
        0x2AA0: "Magnetic Flux Density - 2D",
        0x2AA1: "Magnetic Flux Density - 3D",
        0x2A29: "Manufacturer Name String",
        0x2A91: "Maximum Recommended Heart Rate",
        0x2A21: "Measurement Interval",
        0x2A24: "Model Number String",
        0x2A68: "Navigation",
        0x2A3E: "Network Availability",
        0x2A46: "New Alert",
        0x2AC5: "Object Action Control Point",
        0x2AC8: "Object Changed",
        0x2AC1: "Object First-Created",
        0x2AC3: "Object ID",
        0x2AC2: "Object Last-Modified",
        0x2AC6: "Object List Control Point",
        0x2AC7: "Object List Filter",
        0x2ABE: "Object Name",
        0x2AC4: "Object Properties",
        0x2AC0: "Object Size",
        0x2ABF: "Object Type",
        0x2ABD: "OTS Feature",
        0x2A04: "Peripheral Preferred Connection Parameters",
        0x2A02: "Peripheral Privacy Flag",
        0x2A5F: "PLX Continuous Measurement Characteristic",
        0x2A60: "PLX Features",
        0x2A5E: "PLX Spot-Check Measurement",
        0x2A50: "PnP ID",
        0x2A75: "Pollen Concentration",
        0x2A2F: "Position 2D",
        0x2A30: "Position 3D",
        0x2A69: "Position Quality",
        0x2A6D: "Pressure",
        0x2A4E: "Protocol Mode",
        0x2A62: "Pulse Oximetry Control Point",
        0x2A78: "Rainfall",
        0x2B1D: "RC Feature",
        0x2B1E: "RC Settings",
        0x2A03: "Reconnection Address",
        0x2B1F: "Reconnection Configuration Control Point",
        0x2A52: "Record Access Control Point",
        0x2A14: "Reference Time Information",
        0x2A3A: "Removable",
        0x2A4D: "Report",
        0x2A4B: "Report Map",
        0x2AC9: "Resolvable Private Address Only",
        0x2A92: "Resting Heart Rate",
        0x2A40: "Ringer Control point",
        0x2A41: "Ringer Setting",
        0x2AD1: "Rower Data",
        0x2A54: "RSC Feature",
        0x2A53: "RSC Measurement",
        0x2A55: "SC Control Point",
        0x2A4F: "Scan Interval Window",
        0x2A31: "Scan Refresh",
        0x2A3C: "Scientific Temperature Celsius",
        0x2A10: "Secondary Time Zone",
        0x2A5D: "Sensor Location",
        0x2A05: "Service Changed",
        0x2A0E: "Time Zone",
        0x2A11: "Time with DST",
        0x2A12: "Time Accuracy",
        0x2A13: "Time Source",
        0x2A15: "Time Broadcast",
        0x2A16: "Time Update Control Point",
        0x2A17: "Time Update State",
        0x2A25: "Serial Number String",
        0x2A3B: "Service Required",
        0x2A28: "Software Revision String",
        0x2A93: "Sport Type for Aerobic and Anaerobic Thresholds",
        0x2AD0: "Stair Climber Data",
        0x2ACF: "Step Climber Data",
        0x2A3D: "String",
        0x2AD7: "Supported Heart Rate Range",
        0x2AD5: "Supported Inclination Range",
        0x2A47: "Supported New Alert Category",
        0x2AD8: "Supported Power Range",
        0x2AD6: "Supported Resistance Level Range",
        0x2AD4: "Supported Speed Range",
        0x2A48: "Supported Unread Alert Category",
        0x2A23: "System ID",
        0x2ABC: "TDS Control Point",
        0x2A6E: "Temperature",
        0x2A1F: "Temperature Celsius",
        0x2A20: "Temperature Fahrenheit",
        0x2A1C: "Temperature Measurement",
        0x2A1D: "Temperature Type",
        0x2A94: "Three Zone Heart Rate Limits",
        0x2A70: "True Wind Speed",
        0x2A71: "True Wind Direction",
        0x2A95: "Two Zone Heart Rate Limit",
        0x2A07: "Tx Power Level",
        0x2AB4: "Uncertainty",
        0x2A45: "Unread Alert Status",
        0x2AB6: "URI",
        0x2A9F: "User Control Point",
        0x2A9A: "User Index",
        0x2A76: "UV Index",
        0x2A79: "Wind Chill",
        0x2A96: "VO2 Max",
        0x2A97: "Waist Circumference",
        0x2A98: "Weight",
        0x2A9D: "Weight Measurement",
        0x2A9E: "Weight Scale Feature",
        0x2ACD: "Treadmill Data",
        0x2AD3: "Training Status",
        0x2AE0: "Average Current",
        0x2AE1: "Average Voltage",
        0x2AE2: "Boolean",
        0x2AE3: "Chromatic Distance From Planckian",
        0x2AE4: "Chromaticity Coordinates",
        0x2AE5: "Chromaticity In CCT And Duv Values",
        0x2AE6: "Chromaticity Tolerance",
        0x2AE7: "CIE 13.3-1995 Color Rendering Index",
        0x2AE8: "Coefficient",
        0x2AE9: "Correlated Color Temperature",
        0x2AEA: "Count 16",
        0x2AEB: "Count 24",
        0x2AEC: "Country Code",
        0x2AED: "Date UTC",
        0x2AEE: "Electric Current",
        0x2AEF: "Electric Current Range",
        0x2AF0: "Electric Current Specification",
        0x2AF1: "Electric Current Statistics",
        0x2AF2: "Energy",
        0x2AF3: "Energy In A Period Of Day",
        0x2AF4: "Event Statistics",
        0x2AF5: "Fixed String 16",
        0x2AF6: "Fixed String 24",
        0x2AF7: "Fixed String 36",
        0x2AF8: "Fixed String 8",
        0x2AF9: "Generic Level",
        0x2AFA: "Global Trade Item Number",
        0x2AFB: "Illuminance",
        0x2AFC: "Luminous Efficacy",
        0x2AFD: "Luminous Energy",
        0x2AFE: "Luminous Exposure",
        0x2AFF: "Luminous Flux",
        0x2B00: "Luminous Flux Range",
        0x2B01: "Luminous Intensity",
        0x2B02: "B02 Mass Flow",
        0x2B03: "Perceived Lightness",
        0x2B04: "Percentage 8",
        0x2B05: "Power",
        0x2B06: "Power Specification",
        0x2B07: "Relative Runtime In A Current Range",
        0x2B08: "Relative Runtime In A Generic Level Range",
        0x2B09: "Relative Value In A Voltage Range",
        0x2B0A: "Relative Value In An Illuminance Range",
        0x2B0B: "Relative Value In A Period Of Day",
        0x2B0C: "Relative Value In A Temperature Range",
        0x2B0D: "Temperature 8",
        0x2B0E: "Temperature 8 In A Period Of Day",
        0x2B0F: "Temperature 8 Statistics",
        0x2B10: "Temperature Range",
        0x2B11: "Temperature Statistics",
        0x2B12: "Time Decihour 8",
        0x2B13: "Time Exponential 8",
        0x2B14: "Time Hour 24",
        0x2B15: "Time Millisecond 24",
        0x2B16: "Time Second 16",
        0x2B17: "Time Second 8",
        0x2B18: "Voltage",
        0x2B19: "Voltage Specification",
        0x2B1A: "Voltage Statistics",
        0x2B1B: "Volume Flow",
        0x2B1C: "Chromaticity Coordinate",
        0x2B29: "Client Supported Features",
        0x2B2A: "Database Hash",
        0x2B2B: "BSS Control Point",
        0x2B2C: "BSS Response",
        0x2B2D: "Emergency ID",
        0x2B2E: "Emergency Text",
        0x2B34: "Enhanced Blood Pressure Measurement",
        0x2B35: "Enhanced Intermediate Cuff Pressure",
        0x2B36: "Blood Pressure Record",
        0x2B38: "BR-EDR Handover Data",
        0x2B39: "Bluetooth SIG Data",
        0x2B3A: "Server Supported Features",
        0x2B3B: "Physical Activity Monitor Features",
        0x2B3C: "General Activity Instantaneous Data",
        0x2B3D: "General Activity Summary Data",
        0x2B3E: "CardioRespiratory Activity Instantaneous Data",
        0x2B3F: "CardioRespiratory Activity Summary Data",
        0x2B40: "Step Counter Activity Summary Data",
        0x2B41: "Sleep Activity Instantaneous Data",
        0x2B42: "Sleep Activity Summary Data",
        0x2B43: "Physical Activity Monitor Control Point",
        0x2B44: "Activity Current Session",
        0x2B45: "Physical Activity Session Descriptor",
        0x2B46: "Preferred Units",
        0x2B47: "High Resolution Height",
        0x2B48: "Middle Name",
        0x2B49: "Stride Length",
        0x2B4A: "Handedness",
        0x2B4B: "Device Wearing Position",
        0x2B4C: "Four Zone Heart Rate Limits",
        0x2B4D: "High Intensity Exercise Threshold",
        0x2B4E: "Activity Goal",
        0x2B4F: "Sedentary Interval Notification",
        0x2B50: "Caloric Intake",
        0x2B51: "TMAP Role",
        0x2B77: "Audio Input State",
        0x2B78: "Gain Settings Attribute",
        0x2B79: "Audio Input Type",
        0x2B7A: "Audio Input Status",
        0x2B7B: "Audio Input Control Point",
        0x2B7C: "Audio Input Description",
        0x2B7D: "Volume State",
        0x2B7E: "Volume Control Point",
        0x2B7F: "Volume Flags",
        0x2B80: "Volume Offset State",
        0x2B81: "Audio Location",
        0x2B82: "Volume Offset Control Point",
        0x2B83: "Audio Output Description",
        0x2B84: "Set Identity Resolving Key",
        0x2B85: "Coordinated Set Size",
        0x2B86: "Set Member Lock",
        0x2B87: "Set Member Rank",
        0x2B8E: "Device Time Feature",
        0x2B8F: "Device Time Parameters",
        0x2B90: "Device Time",
        0x2B91: "Device Time Control Point",
        0x2B92: "Time Change Log Data",
        0x2B93: "Media Player Name",
        0x2B94: "Media Player Icon Object ID",
        0x2B95: "Media Player Icon URL",
        0x2B96: "Track Changed",
        0x2B97: "Track Title",
        0x2B98: "Track Duration",
        0x2B99: "Track Position",
        0x2B9A: "Playback Speed",
        0x2B9B: "Seeking Speed",
        0x2B9C: "Current Track Segments Object ID",
        0x2B9D: "Current Track Object ID",
        0x2B9E: "Next Track Object ID",
        0x2B9F: "Parent Group Object ID",
        0x2BA0: "Current Group Object ID",
        0x2BA1: "Playing Order",
        0x2BA2: "Playing Orders Supported",
        0x2BA3: "Media State",
        0x2BA4: "Media Control Point",
        0x2BA5: "Media Control Point Opcodes Supported",
        0x2BA6: "Search Results Object ID",
        0x2BA7: "Search Control Point",
        0x2BA9: "Media Player Icon Object Type",
        0x2BAA: "Track Segments Object Type",
        0x2BAB: "Track Object Type",
        0x2BAC: "Group Object Type",
        0x2BAD: "Constant Tone Extension Enable",
        0x2BAE: "Advertising Constant Tone Extension Minimum Length",
        0x2BAF: "Advertising Constant Tone Extension Minimum Transmit Count",
        0x2BB0: "Advertising Constant Tone Extension Transmit Duration",
        0x2BB1: "Advertising Constant Tone Extension Interval",
        0x2BB2: "Advertising Constant Tone Extension PHY",
        0x2BB3: "Bearer Provider Name",
        0x2BB4: "Bearer UCI",
        0x2BB5: "Bearer Technology",
        0x2BB6: "Bearer URI Schemes Supported List",
        0x2BB7: "Bearer Signal Strength",
        0x2BB8: "Bearer Signal Strength Reporting Interval",
        0x2BB9: "Bearer List Current Calls",
        0x2BBA: "Content Control ID",
        0x2BBB: "Status Flags",
        0x2BBC: "Incoming Call Target Bearer URI",
        0x2BBD: "Call State",
        0x2BBE: "Call Control Point",
        0x2BBF: "Call Control Point Optional Opcodes",
        0x2BC0: "Termination Reason",
        0x2BC1: "Incoming Call",
        0x2BC2: "Call Friendly Name",
        0x2BC3: "Mute",
        0x2BC4: "Sink ASE",
        0x2BC5: "Source ASE",
        0x2BC6: "ASE Control Point",
        0x2BC7: "Broadcast Audio Scan Control Point",
        0x2BC8: "Broadcast Receive State",
        0x2BC9: "Sink PAC",
        0x2BCA: "Sink Audio Locations",
        0x2BCB: "Source PAC",
        0x2BCC: "Source Audio Locations",
        0x2BCD: "Available Audio Contexts",
        0x2BCE: "Supported Audio Contexts",
        0x2BCF: "Ammonia Concentration",
        0x2BD0: "Carbon Monoxide Concentration",
        0x2BD1: "Methane Concentration",
        0x2BD2: "Nitrogen Dioxide Concentration",
        0x2BD3: "Non-Methane Volatile Organic Compounds Concentration",
        0x2BD4: "Ozone Concentration",
        0x2BD5: "Particulate Matter - PM1 Concentration",
        0x2BD6: "Particulate Matter - PM2.5 Concentration",
        0x2BD7: "Particulate Matter - PM10 Concentration",
        0x2BD8: "Sulfur Dioxide Concentration",
        0x2BD9: "Sulfur Hexafluoride Concentration",
        0x2BDA: "Hearing Aid Features",
        0x2BDB: "Hearing Aid Preset Control Point",
        0x2BDC: "Active Preset Index",
        0x1233: "Deprecated Fast Pair Model ID",
        0x1234: "Deprecated Fast Pair Key-based Pairing",
        0x1235: "Deprecated Fast Pair Passkey",
        0x1236: "Deprecated Fast Pair Account Key",
        0x1237: "Deprecated Fast Pair Data",
        0x2ADB: "Mesh Provisioning Data In",
        0x2ADC: "Mesh Provisioning Data Out",
        0x2ADD: "Mesh Proxy Data In",
        0x2ADE: "Mesh Proxy Data Out",
        UUID("00001524-1212-EFDE-1523-785FEABCD123"): "Blinky Button State",
        UUID("00001525-1212-EFDE-1523-785FEABCD123"): "Blinky LED State",
        UUID("00001531-1212-EFDE-1523-785FEABCD123"): "Legacy DFU Control Point",
        UUID("00001532-1212-EFDE-1523-785FEABCD123"): "Legacy DFU Packet",
        UUID("00001534-1212-EFDE-1523-785FEABCD123"): "Legacy DFU Version",
        UUID("8EC90001-F315-4F60-9FB8-838830DAEA50"): "DFU Control Point",
        UUID("8EC90002-F315-4F60-9FB8-838830DAEA50"): "DFU Packet",
        UUID("8EC90003-F315-4F60-9FB8-838830DAEA50"): "Buttonless DFU Without Bonds",
        UUID("8EC90004-F315-4F60-9FB8-838830DAEA50"): "Buttonless DFU With Bonds",
        UUID("8E400001-F315-4F60-9FB8-838830DAEA50"): "Experimental Buttonless DFU",
        UUID("DA2E7828-FBCE-4E01-AE9E-261174997C48"): "SMP Characteristic",
        UUID("932C32BD-0002-47A2-835A-A8D455B859DD"): "Philips Hue Light On/Off Toggle",
        UUID(
            "932C32BD-0003-47A2-835A-A8D455B859DD",
        ): "Philips Hue Light Brightness Level",
        UUID("932C32BD-0005-47A2-835A-A8D455B859DD"): "Philips Hue Light Color",
        UUID("EF680101-9B35-4933-9B10-52FFA9740042"): "Thingy Device Name",
        UUID("EF680102-9B35-4933-9B10-52FFA9740042"): "Thingy Advertising Parameters",
        UUID("EF680104-9B35-4933-9B10-52FFA9740042"): "Thingy Connection Parameters",
        UUID("EF680105-9B35-4933-9B10-52FFA9740042"): "Thingy Eddystone URL",
        UUID("EF680106-9B35-4933-9B10-52FFA9740042"): "Thingy Cloud Token",
        UUID("EF680107-9B35-4933-9B10-52FFA9740042"): "Thingy FW Version",
        UUID("EF680108-9B35-4933-9B10-52FFA9740042"): "Thingy MTU Request",
        UUID("EF680201-9B35-4933-9B10-52FFA9740042"): "Thingy Temperature",
        UUID("EF680202-9B35-4933-9B10-52FFA9740042"): "Thingy Pressure",
        UUID("EF680203-9B35-4933-9B10-52FFA9740042"): "Thingy Humidity",
        UUID("EF680204-9B35-4933-9B10-52FFA9740042"): "Thingy Air Quality",
        UUID("EF680205-9B35-4933-9B10-52FFA9740042"): "Thingy Color",
        UUID("EF680206-9B35-4933-9B10-52FFA9740042"): "Thingy Configuration",
        UUID("EF680301-9B35-4933-9B10-52FFA9740042"): "Thingy LED State",
        UUID("EF680302-9B35-4933-9B10-52FFA9740042"): "Thingy Button State",
        UUID("EF680303-9B35-4933-9B10-52FFA9740042"): "Thingy EXT Pin",
        UUID("EF680401-9B35-4933-9B10-52FFA9740042"): "Thingy Motion Config",
        UUID("EF680402-9B35-4933-9B10-52FFA9740042"): "Thingy Tap",
        UUID("EF680403-9B35-4933-9B10-52FFA9740042"): "Thingy Orientation",
        UUID("EF680404-9B35-4933-9B10-52FFA9740042"): "Thingy Quaternion",
        UUID("EF680405-9B35-4933-9B10-52FFA9740042"): "Thingy Pedometer",
        UUID("EF680406-9B35-4933-9B10-52FFA9740042"): "Thingy Raw Data",
        UUID("EF680407-9B35-4933-9B10-52FFA9740042"): "Thingy Euler",
        UUID("EF680408-9B35-4933-9B10-52FFA9740042"): "Thingy Rotation Matrix",
        UUID("EF680409-9B35-4933-9B10-52FFA9740042"): "Thingy Heading",
        UUID("EF68040A-9B35-4933-9B10-52FFA9740042"): "Thingy Gravity Vector",
        UUID("EF680501-9B35-4933-9B10-52FFA9740042"): "Thingy Sound Config",
        UUID("EF680502-9B35-4933-9B10-52FFA9740042"): "Thingy Speaker Data",
        UUID("EF680503-9B35-4933-9B10-52FFA9740042"): "Thingy Speaker Status",
        UUID("EF680504-9B35-4933-9B10-52FFA9740042"): "Thingy Microphone",
        UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E"): "UART RX Characteristic",
        UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E"): "UART TX Characteristic",
        UUID("57A70001-9350-11ED-A1EB-0242AC120002"): "Status Characteristic",
        UUID(
            "E2A00002-EC31-4EC3-A97A-1C34D87E9878",
        ): "Edge Impulse Remote Management RX Characteristic",
        UUID(
            "E2A00003-EC31-4EC3-A97A-1C34D87E9878",
        ): "Edge Impulse Remote Management TX Characteristic",
        UUID("A3C87501-8ED3-4BDF-8A39-A01BEBEDE295"): "Eddystone Capabilities",
        UUID("A3C87502-8ED3-4BDF-8A39-A01BEBEDE295"): "Eddystone Active Slot",
        UUID("A3C87503-8ED3-4BDF-8A39-A01BEBEDE295"): "Eddystone Advertising Interval",
        UUID("A3C87504-8ED3-4BDF-8A39-A01BEBEDE295"): "Eddystone Radio Tx Power",
        UUID(
            "A3C87505-8ED3-4BDF-8A39-A01BEBEDE295",
        ): "Eddystone (Advanced) Advertised Tx Power",
        UUID("A3C87506-8ED3-4BDF-8A39-A01BEBEDE295"): "Eddystone Lock State",
        UUID("A3C87507-8ED3-4BDF-8A39-A01BEBEDE295"): "Eddystone Unlock",
        UUID("A3C87508-8ED3-4BDF-8A39-A01BEBEDE295"): "Eddystone Public ECDH Key",
        UUID("A3C87509-8ED3-4BDF-8A39-A01BEBEDE295"): "Eddystone EID Identity Key",
        UUID("A3C8750A-8ED3-4BDF-8A39-A01BEBEDE295"): "Eddystone ADV Slot Data",
        UUID(
            "A3C8750B-8ED3-4BDF-8A39-A01BEBEDE295",
        ): "Eddystone Advanced Factory Reset",
        UUID(
            "A3C8750C-8ED3-4BDF-8A39-A01BEBEDE295",
        ): "Eddystone (Advanced) Remain Connectable",
        UUID("FE2C1233-8366-4814-8EB0-01DE32100BEA"): "Fast Pair Model ID",
        UUID("FE2C1234-8366-4814-8EB0-01DE32100BEA"): "Fast Pair Key-based Pairing",
        UUID("FE2C1235-8366-4814-8EB0-01DE32100BEA"): "Fast Pair Passkey",
        UUID("FE2C1236-8366-4814-8EB0-01DE32100BEA"): "Fast Pair Account Key",
        UUID("FE2C1237-8366-4814-8EB0-01DE32100BEA"): "Fast Pair Data",
        UUID("9FBF120D-6301-42D9-8C58-25E699A21DBD"): "Apple Notification Source",
        UUID("69D1D8F3-45E1-49A8-9821-9BBDFDAAD9D9"): "Apple Control Point",
        UUID("22EAC6E9-24D6-4BB5-BE44-B36ACE7C7BFB"): "Apple Data Source",
        UUID("9B3C81D8-57B1-4A8A-B8DF-0E56F7CA51C2"): "Apple Remote Command",
        UUID("2F7CABCE-808D-411F-9A0C-BB92BA96C102"): "Apple Entity Update",
        UUID("C6B2F38C-23AB-46D8-A6AB-A3A870BBD5D7"): "Apple Entity Attribute",
        UUID("7DFC6001-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC6002-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC6003-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC6004-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC6005-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC6101-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC6102-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC6103-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC6104-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC6105-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC6106-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC6107-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC6108-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC6201-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC6202-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC6203-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC8003-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC7004-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC7005-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC7006-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC7007-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC7008-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC7009-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC700A-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC700B-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC700C-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC7103-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC7104-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC7105-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC7106-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC7107-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC7108-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC7109-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC710B-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC710C-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC710D-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC8004-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("7DFC9001-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Characteristic",
        UUID("E95DCA4B-251D-470A-A062-FA1922DFA9A8"): "micro:bit Accelerometer Data",
        UUID("E95DFB24-251D-470A-A062-FA1922DFA9A8"): "micro:bit Accelerometer Period",
        UUID("E95DFB11-251D-470A-A062-FA1922DFA9A8"): "micro:bit Magnetometer Data",
        UUID("E95D386C-251D-470A-A062-FA1922DFA9A8"): "micro:bit Magnetometer Period",
        UUID("E95D9715-251D-470A-A062-FA1922DFA9A8"): "micro:bit Magnetometer Bearing",
        UUID("E95DDA90-251D-470A-A062-FA1922DFA9A8"): "micro:bit Button A State",
        UUID("E95DDA91-251D-470A-A062-FA1922DFA9A8"): "micro:bit Button B State",
        UUID("E95D8D00-251D-470A-A062-FA1922DFA9A8"): "micro:bit Pin Data",
        UUID("E95D5899-251D-470A-A062-FA1922DFA9A8"): "micro:bit Pin AD Configuration",
        UUID("E95DB9FE-251D-470A-A062-FA1922DFA9A8"): "micro:bit Pin I/O Configuration",
        UUID("E95DD822-251D-470A-A062-FA1922DFA9A8"): "micro:bit PWM Control",
        UUID("E95D7B77-251D-470A-A062-FA1922DFA9A8"): "micro:bit LED Matrix State",
        UUID("E95D93EE-251D-470A-A062-FA1922DFA9A8"): "micro:bit LED Text",
        UUID("E95D0D2D-251D-470A-A062-FA1922DFA9A8"): "micro:bit Scrolling Delay",
        UUID("E95DB84C-251D-470A-A062-FA1922DFA9A8"): "micro:bit Requirements",
        UUID("E95D9775-251D-470A-A062-FA1922DFA9A8"): "micro:bit Event",
        UUID("E95D23C4-251D-470A-A062-FA1922DFA9A8"): "micro:bit Client Requirements",
        UUID("E95D5404-251D-470A-A062-FA1922DFA9A8"): "micro:bit Client Event",
        UUID("E95D93B1-251D-470A-A062-FA1922DFA9A8"): "micro:bit DFU Control",
        UUID("E95D9250-251D-470A-A062-FA1922DFA9A8"): "micro:bit Temperature",
        UUID("E95D1B25-251D-470A-A062-FA1922DFA9A8"): "micro:bit Temperature Period",
        UUID(
            "00001624-1212-EFDE-1623-785FEABCD123",
        ): "LEGO® Wireless Protocol v3 Hub Characteristic",
        UUID(
            "00001626-1212-EFDE-1623-785FEABCD123",
        ): "LEGO® Wireless Protocol v3 Bootloader Characteristic",
        UUID(
            "ADAF0001-C332-42A8-93BD-25E905756CB8",
        ): "Adafruit Sensor Measurement Period",
        UUID("ADAF0002-C332-42A8-93BD-25E905756CB8"): "Adafruit Sensor Service Version",
        UUID("ADAF0101-C332-42A8-93BD-25E905756CB8"): "Adafruit Temperature",
        UUID("ADAF0201-C332-42A8-93BD-25E905756CB8"): "Adafruit Acceleration",
        UUID("ADAF0301-C332-42A8-93BD-25E905756CB8"): "Adafruit Light Level",
        UUID("ADAF0401-C332-42A8-93BD-25E905756CB8"): "Adafruit Gyro",
        UUID("ADAF0501-C332-42A8-93BD-25E905756CB8"): "Adafruit Magnetic",
        UUID("ADAF0601-C332-42A8-93BD-25E905756CB8"): "Adafruit Pressed",
        UUID("ADAF0701-C332-42A8-93BD-25E905756CB8"): "Adafruit Humidity",
        UUID("ADAF0801-C332-42A8-93BD-25E905756CB8"): "Adafruit Pressure",
        UUID("ADAF0901-C332-42A8-93BD-25E905756CB8"): "Adafruit Pixel Pin",
        UUID("ADAF0902-C332-42A8-93BD-25E905756CB8"): "Adafruit Pixel Pin Type",
        UUID("ADAF0903-C332-42A8-93BD-25E905756CB8"): "Adafruit Pixel Data",
        UUID("ADAF0904-C332-42A8-93BD-25E905756CB8"): "Adafruit Pixel Buffer Size",
        UUID("ADAF0A01-C332-42A8-93BD-25E905756CB8"): "Adafruit Color",
        UUID("ADAF0B01-C332-42A8-93BD-25E905756CB8"): "Adafruit Sound Samples",
        UUID("ADAF0B02-C332-42A8-93BD-25E905756CB8"): "Adafruit Number of Channels",
        UUID("ADAF0C01-C332-42A8-93BD-25E905756CB8"): "Adafruit Tone",
        UUID("ADAF0D01-C332-42A8-93BD-25E905756CB8"): "Adafruit Quaternions",
        UUID("ADAF0D02-C332-42A8-93BD-25E905756CB8"): "Adafruit Calibration In",
        UUID("ADAF0D03-C332-42A8-93BD-25E905756CB8"): "Adafruit Calibration Out",
        UUID("ADAF0E01-C332-42A8-93BD-25E905756CB8"): "Adafruit Proximity",
        UUID("ADAF0100-4669-6C65-5472-616E73666572"): "Adafruit Version",
        UUID("ADAF0200-4669-6C65-5472-616E73666572"): "Adafruit Raw TX/RX",
        UUID(
            "F000FFC1-0451-4000-B000-000000000000",
        ): "Texas Instruments Image Identify",
        UUID("F000FFC2-0451-4000-B000-000000000000"): "Texas Instruments Image Block",
        UUID("F000FFC5-0451-4000-B000-000000000000"): "Texas Instruments OAD Control",
        UUID("D083B2BD-BE16-4600-B397-61512CA2F5AD"): "Helium Hotspot Onboarding Key",
        UUID("0A852C59-50D3-4492-BFD3-22FE58A24F01"): "Helium Hotspot Public Key",
        UUID("D7515033-7E7B-45BE-803F-C8737B171A29"): "Helium Hotspot WiFi Services",
        UUID("B833D34F-D871-422C-BF9E-8E6EC117D57E"): "Helium Hotspot Diagnostics",
        UUID("9C4314F2-8A0C-45FD-A58D-D4A7E64C3A57"): "Helium Hotspot WiFi MAC Address",
        UUID("180EFDEF-7579-4B4A-B2DF-72733B7FA2FE"): "Helium Hotspot Lights",
        UUID("7731DE63-BC6A-4100-8AB1-89B2356B038B"): "Helium Hotspot WiFi SSID",
        UUID("D435F5DE-01A4-4E7D-84BA-DFD347F60275"): "Helium Hotspot Assert Location",
        UUID("DF3B16CA-C985-4DA2-A6D2-9B9B9ABDB858"): "Helium Hotspot Add Gateway",
        UUID("398168AA-0111-4EC0-B1FA-171671270608"): "Helium Hotspot WiFi Connect",
        UUID("E5866BD6-0288-4476-98CA-EF7DA6B4D289"): "Helium Hotspot Ethernet Online",
        UUID("8CC6E0B3-98C5-40CC-B1D8-692940E6994B"): "Helium Hotspot WiFi Remove",
        UUID(
            "E125BDA4-6FB8-11EA-BC55-0242AC130003",
        ): "Helium Hotspot WiFi Configured Services",
        UUID(
            "54220001-F6A5-4007-A371-722F4EBD8436",
        ): "MDS Supported Features Characteristic",
        UUID(
            "54220002-F6A5-4007-A371-722F4EBD8436",
        ): "MDS Device Identifier Characteristic",
        UUID(
            "54220003-F6A5-4007-A371-722F4EBD8436",
        ): "MDS Device Data URI Characteristic",
        UUID(
            "54220004-F6A5-4007-A371-722F4EBD8436",
        ): "MDS Device Authorization Characteristic",
        UUID(
            "54220005-F6A5-4007-A371-722F4EBD8436",
        ): "MDS Device Data Export Characteristic",
    },
)
