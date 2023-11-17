from pprint import pprint as pp

# Task_1:
entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24      157.130.10.233         0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

entries = (entry1, entry2, entry3, entry4)

header = ("ip_prefix", "as_path")

# Task_2:
output = """
Interface       IP-Address  OK? Method  Status  Protocol
FastEthernet0   unassigned  YES unset   up      up
FastEthernet1   unassigned  YES unset   up      up
FastEthernet2   unassigned  YES unset   down    down
FastEthernet3   unassigned  YES unset   up      up
FastEthernet4   6.9.4.10    YES NVRAM   up      up
NVI0            6.9.4.10    YES unset   up      up
Tunnel1         16.25.253.2 YES NVRAM   up      down
Tunnel2         16.25.253.6 YES NVRAM   up      down
Vlan1           unassigned  YES NVRAM   down    down
Vlan10          10.220.88.1 YES NVRAM   up      up
Vlan20          192.168.0.1 YES NVRAM   down    down
Vlan100         10.220.84.1 YES NVRAM   up      up
"""


def show_interfaces(raw_data: str) -> list:
    lines = [line for line in output.split("\n") if line]
    result = []
    for line in lines:
        if line.split()[-1] == "up":
            int_name, ip, *_, status, protocol = line.split()
            result.append((int_name, ip, status, protocol))
    return result


def show_prefxs(entries, header=header) -> None:
    """
    Task_1
    Print pair prefix: as_path
    """
    print(*header, sep="\t")
    for entry in entries:
        prefix = entry.split()[1]
        _n1, _n2, _n3, _n4, *aspath, _n5 = entry.split()
        print(f"{prefix}\t{tuple(aspath)}")


if __name__ == "__main__":
    show_prefxs(entries=entries)
    print('\n'*2)
    pp(show_interfaces(raw_data=output))
    print('\n'*2)
    
