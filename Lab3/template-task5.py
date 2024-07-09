{% for iface in interface_list %}
interface {{ iface }}
{%- if iface == "GigabitEthernet0/1" %}
 switchport mode trunk
{% else %}
 switchport access vlan 10
 
