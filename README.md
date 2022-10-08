# Docker Capirca

## Running sample scripts

Enter a running container

```bash
docker-compose exec python3 /bin/bash
```

Change directory

```bash
cd sample/
```

### Cisco

```bash
python aclgen_cisco_lab.py
```

Output: output/sample_cisco_lab.txt

### Juniper

```bash
python aclgen_juniper_loopback.py
```

Output: output/sample_juniper_loopback.txt

### NSX-V

```bash
python aclgen_nsxv.py
```

Output: output/sample_nsxv.txt

### Palo Alto

```bash
python aclgen_paloalto.py
```

Output: output/sample_paloalto.txt

