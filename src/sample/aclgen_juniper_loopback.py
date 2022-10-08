from pprint import pprint
from capirca.lib import naming
from capirca.lib import policy
from capirca.lib import juniper

POLICY = './policies/pol/sample_juniper_loopback.pol'
OUTPUT = './output/sample_juniper_loopback.txt'

if __name__ == '__main__':

    defs = naming.Naming('./def')
    #  pprint(defs)
    #  print(dir(defs))
    #  pprint(defs.GetServiceNames())

    with open(POLICY, 'r') as f:
        conf = f.read()

    pol = policy.ParsePolicy(conf, defs, optimize=True)

    with open(OUTPUT, "w") as f:
        for header in pol.headers:
            if 'juniper' in header.platforms:
                jcl = True
            if jcl:
                output = juniper.Juniper(pol, 1)
                print(output)
                f.write(str(output))