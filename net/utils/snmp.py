import time
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


def interfaces(host, comunity):
    retorno = []
    for _, _, _, varBinds in nextCmd(
            SnmpEngine(),
            CommunityData(comunity, mpModel=0),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity('iso.3.6.1.2.1.2.2.1.1')),
            ObjectType(ObjectIdentity('iso.3.6.1.2.1.2.2.1.2')),
            ObjectType(ObjectIdentity('iso.3.6.1.2.1.2.2.1.8')),
            ObjectType(ObjectIdentity('iso.3.6.1.2.1.2.2.1.10')),
            ObjectType(ObjectIdentity('iso.3.6.1.2.1.2.2.1.16')),
            lexicographicMode=False):
        id, descr, status, inoctets, outoctets = varBinds  # unpack the list of resolved objectTypes
        interface = {}
        interface['id'] = id[1].prettyPrint()  # access the objectSyntax and get its human-readable form
        interface['name'] = descr[1].prettyPrint()  # access the objectSyntax and get its human-readable form
        interface['status'] = status[1].prettyPrint()
        interface['inoctets'] = inoctets[1].prettyPrint()
        interface['outoctets'] = outoctets[1].prettyPrint()
        retorno.append(interface)
    return retorno


def interface(host, comunity, interface_number):
    valorin1 = int(snmp(host, comunity, 'iso.3.6.1.2.1.2.2.1.10.'+interface_number))
    valorout1 = int(snmp(host, comunity, 'iso.3.6.1.2.1.2.2.1.16.'+interface_number))
    time.sleep(1)
    valorin2 = int(snmp(host, comunity, 'iso.3.6.1.2.1.2.2.1.10.'+interface_number))
    valorout2 = int(snmp(host, comunity, 'iso.3.6.1.2.1.2.2.1.16.'+interface_number))
    retorno = {}
    retorno['traffic_in'] = ((valorin2-valorin1)*8)/1000000
    retorno['traffic_out'] = ((valorout2 - valorout1) * 8) / 1000000
    retorno['name'] = str(snmp(host, comunity, 'iso.3.6.1.2.1.2.2.1.2.'+interface_number))
    retorno['status'] = str(snmp(host, comunity, 'iso.3.6.1.2.1.2.2.1.8.' + interface_number))
    return retorno

"""
print(interface_traffic('10.4.0.205','public','3'))



for interface in interfaces('10.4.0.205', 'public'):
    print("Interface {iface} is {status} = in octets {inoct}. out {outoct}"
          .format(iface=interface['name'], status=interface['status'], inoct=interface['inoctets'],
                  outoct=interface['outoctets']))
"""