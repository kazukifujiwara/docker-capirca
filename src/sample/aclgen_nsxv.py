from pprint import pprint
from capirca.lib import naming
from capirca.lib import policy
from capirca.lib import nsxv

POLICY = './policies/pol/sample_nsxv.pol'
OUTPUT = './output/sample_nsxv.txt'

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
            if 'nsxv' in header.platforms:
                jcl = True
            if jcl:
                output = nsxv.Nsxv(pol, 1)
                print(output)
                f.write(str(output))