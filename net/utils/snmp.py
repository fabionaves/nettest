from pysnmp.hlapi import *


def snmp(host, comunity,  oid):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(comunity, mpModel=0),
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        return False
    elif errorStatus:
        return False
    else:
        return str(varBinds[0]).split('=')[1]