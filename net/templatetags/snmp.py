from django import template
from net.utils.snmp import snmp

register = template.Library()


@register.simple_tag
def snmptag(host, template, comunidade, oid):
    valor = str(snmp(host, comunidade, oid))
    #valor = "90"
    return template.replace("{{value}}",valor)
