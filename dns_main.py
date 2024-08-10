from dns_enumeration import DnsEnumeration
import argparse

def main(target):
    dnsEnum = DnsEnumeration(target)
    dnsEnum.registro()




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Herramienta para hacer enumeracion DNS")
    parser.add_argument("--target", type=str, required=True,
                        help="Especifica el domininio a analizar. EJEMPLO target dominio.com")
    args = parser.parse_args()
    main(target=args.target)