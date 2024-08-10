import dns.resolver

class DnsEnumeration():

    def __init__(self, target_domain):
        self.target_domain = target_domain

    def registro(self):
        record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
        resolver = dns.resolver.Resolver()
        for record_type in record_types:
            try:
                respuesta = resolver.resolve(self.target_domain, record_type)
            except dns.resolver.NoAnswer:
                continue
            print(f'{record_type} registros para {self.target_domain}')
            for data in respuesta:
                print(f' {data}')

