from ping3 import ping


def ping_host(ip):
  ip_address = ip
  response = ping(ip_address)
  return response