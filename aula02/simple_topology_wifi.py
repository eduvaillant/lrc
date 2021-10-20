#!/usr/bin/python
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology(remote_controller):
    "Create a network."
    net = Mininet_wifi()

    info("* Adding Servidores\n")

    # Servers
    server1 = net.addHost("server1", ip="10.0.1.10", mac="00:00:00:00:01:0a")
    server2 = net.addHost("server2", ip="10.0.1.11", mac="00:00:00:00:01:0b")

    # Stations
    info("* Adding Stations\n")

    sta01 = net.addStation(
        "sta01",
        ip="10.0.1.21",
        mac="00:00:00:00:02:21",
        position="35,230,0",
    )

    sta02 = net.addStation(
        "sta02",
        ip="10.0.1.22",
        mac="00:00:00:00:02:22",
        position="35,160,0",
    )

    sta03 = net.addStation(
        "sta03",
        ip="10.0.1.23",
        mac="00:00:00:00:02:23",
        position="35,80,0",
    )

    sta04 = net.addStation(
        "sta04",
        ip="10.0.1.24",
        mac="00:00:00:00:02:24",
        position="35,10,0",
    )

    # Bloco 2
    sta05 = net.addStation(
        "sta05",
        ip="10.0.1.25",
        mac="00:00:00:00:02:25",
        position="125,230,0",
    )

    sta06 = net.addStation(
        "sta06",
        ip="10.0.1.26",
        mac="00:00:00:00:02:26",
        position="125,160,0",
    )

    sta07 = net.addStation(
        "sta07",
        ip="10.0.1.27",
        mac="00:00:00:00:02:27",
        position="125,80,0",
    )

    sta08 = net.addStation(
        "sta08",
        ip="10.0.1.28",
        mac="00:00:00:00:02:28",
        position="125,10,0",
    )

    # Bloco 3
    sta09 = net.addStation(
        "sta09",
        ip="10.0.1.29",
        mac="00:00:00:00:02:29",
        position="225,230,0",
    )

    sta10 = net.addStation(
        "sta10",
        ip="10.0.1.30",
        mac="00:00:00:00:02:30",
        position="225,160,0",
    )

    sta11 = net.addStation(
        "sta11",
        ip="10.0.1.31",
        mac="00:00:00:00:02:31",
        position="225,80,0",
    )

    sta12 = net.addStation(
        "sta12",
        ip="10.0.1.32",
        mac="00:00:00:00:02:32",
        position="225,10,0",
    )

    # Bloco 4
    sta13 = net.addStation(
        "sta13",
        ip="10.0.1.33",
        mac="00:00:00:00:02:33",
        position="315,230,0",
    )

    sta14 = net.addStation(
        "sta14",
        ip="10.0.1.34",
        mac="00:00:00:00:02:34",
        position="315,160,0",
    )

    sta15 = net.addStation(
        "sta15",
        ip="10.0.1.35",
        mac="00:00:00:00:02:35",
        position="315,80,0",
    )

    sta16 = net.addStation(
        "sta16",
        ip="10.0.1.36",
        mac="00:00:00:00:02:36",
        position="315,10,0",
    )

    # Bloco 5
    sta17 = net.addStation(
        "sta17",
        ip="10.0.1.37",
        mac="00:00:00:00:02:37",
        position="405,230,0",
    )

    sta18 = net.addStation(
        "sta18",
        ip="10.0.1.38",
        mac="00:00:00:00:02:38",
        position="405,160,0",
    )

    sta19 = net.addStation(
        "sta19",
        ip="10.0.1.39",
        mac="00:00:00:00:02:39",
        position="405,80,0",
    )

    sta20 = net.addStation(
        "sta20",
        ip="10.0.1.40",
        mac="00:00:00:00:02:40",
        position="405,10,0",
    )

    info("* Adicionando AccessPoints\n")

    # Access Points
    # Bloco1
    ap01 = net.addAccessPoint(
        "ap01-B1",
        failMode="standalone",
        mac="00:00:00:00:00:10",
        ssid="BLOCO1-AP01",
        mode="g",
        channel="1",
        position="10,190,0",
    )

    ap02 = net.addAccessPoint(
        "ap02-B1",
        failMode="standalone",
        mac="00:00:00:00:00:11",
        ssid="BLOCO1-AP02",
        mode="g",
        channel="6",
        position="10,50,0",
    )

    # Bloco 2
    ap03 = net.addAccessPoint(
        "ap03-B2",
        failMode="standalone",
        mac="00:00:00:00:00:12",
        ssid="BLOCO2-AP03",
        mode="g",
        channel="2",
        position="100,190,0",
    )

    ap04 = net.addAccessPoint(
        "ap04-B2",
        failMode="standalone",
        mac="00:00:00:00:00:13",
        ssid="BLOCO2-AP04",
        mode="g",
        channel="7",
        position="100,50,0",
    )

    # Bloco 3
    ap05 = net.addAccessPoint(
        "ap05-B3",
        failMode="standalone",
        mac="00:00:00:00:00:14",
        ssid="BLOCO3-AP05",
        mode="g",
        channel="3",
        position="190,190,0",
    )

    ap06 = net.addAccessPoint(
        "ap06-B3",
        failMode="standalone",
        mac="00:00:00:00:00:15",
        ssid="BLOCO3-AP06",
        mode="g",
        channel="8",
        position="190,50,0",
    )

    # Bloco 4
    ap07 = net.addAccessPoint(
        "ap07-B4",
        failMode="standalone",
        mac="00:00:00:00:00:16",
        ssid="BLOCO4-AP07",
        mode="g",
        channel="4",
        position="280,190,0",
    )

    ap08 = net.addAccessPoint(
        "ap08-B4",
        failMode="standalone",
        mac="00:00:00:00:00:17",
        ssid="BLOCO4-AP08",
        mode="g",
        channel="9",
        position="280,50,0",
    )

    # Bloco 5
    ap09 = net.addAccessPoint(
        "ap09-B5",
        failMode="standalone",
        mac="00:00:00:00:00:18",
        ssid="BLOCO5-AP09",
        mode="g",
        channel="5",
        position="370,190,0",
    )

    ap10 = net.addAccessPoint(
        "ap10-B5",
        failMode="standalone",
        mac="00:00:00:00:00:19",
        ssid="BLOCO5-AP10",
        mode="g",
        channel="10",
        position="370,50,0",
    )

    info("* Adding P4Switches\n")

    # Switches
    switch1 = net.addSwitch("switch1")
    switch2 = net.addSwitch("switch2")
    switch3 = net.addSwitch("switch3")
    switch4 = net.addSwitch("switch4")
    switch5 = net.addSwitch("switch5")
    # Sao os dois primeiros, largura de banda diferente
    switchdc0 = net.addSwitch("switchdc0")
    switchag1 = net.addSwitch("switchag1")

    info("* Configurando o modelo de propagação\n")
    net.setPropagationModel(model="logDistance", exp=4)

    info("* Configurando nós WiFi/n ")
    net.configureWifiNodes()

    info("* Criando links\n")

    # Links 10Gbs

    net.addLink(server1, switchdc0, bw=10000)
    net.addLink(server2, switchdc0, bw=10000)
    net.addLink(switchag1, switchdc0, bw=10000)

    # Links 1Gbs
    net.addLink(switch1, switchag1, bw=1000)
    net.addLink(switch2, switchag1, bw=1000)
    net.addLink(switch3, switchag1, bw=1000)
    net.addLink(switch4, switchag1, bw=1000)
    net.addLink(switch5, switchag1, bw=1000)

    # Links 100Mbs

    # Bloco 1

    net.addLink(ap01, switch1, bw=100)
    net.addLink(ap02, switch1, bw=100)

    # Bloco 2
    net.addLink(ap03, switch2, bw=100)
    net.addLink(ap04, switch2, bw=100)

    # Bloco 3
    net.addLink(ap05, switch3, bw=100)
    net.addLink(ap06, switch3, bw=100)

    # Bloco 4
    net.addLink(ap07, switch4, bw=100)
    net.addLink(ap08, switch4, bw=100)

    # Bloco 5
    net.addLink(ap09, switch5, bw=100)
    net.addLink(ap10, switch5, bw=100)

    # Links Ap-Stations

    # Bloco 1
    net.addLink(sta01, ap01)
    net.addLink(sta02, ap01)
    net.addLink(sta03, ap02)
    net.addLink(sta04, ap02)

    # Bloco 2
    net.addLink(sta05, ap03)
    net.addLink(sta06, ap03)
    net.addLink(sta07, ap04)
    net.addLink(sta08, ap04)

    # Bloco 3
    net.addLink(sta09, ap05)
    net.addLink(sta10, ap05)
    net.addLink(sta11, ap06)
    net.addLink(sta12, ap06)

    # Bloco 4
    net.addLink(sta13, ap07)
    net.addLink(sta14, ap07)
    net.addLink(sta15, ap08)
    net.addLink(sta16, ap08)

    # Bloco 5
    net.addLink(sta17, ap09)
    net.addLink(sta18, ap09)
    net.addLink(sta19, ap10)
    net.addLink(sta20, ap10)

    info("* Iniciando rede\n")
    net.plotGraph(max_x=500, max_y=500)
    net.start()
    net.staticArp()

    info("* Applying switches configurations\n")

    switchag1.cmd(
        "ovs-ofctl add-flow {} \"actions=output:NORMAL\"".format(switchag1.name))
    switchdc0.cmd(
        "ovs-ofctl add-flow {} \"actions=output:NORMAL\"".format(switchdc0.name))
    switch1.cmd(
        "ovs-ofctl add-flow {} \"actions=output:NORMAL\"".format(switch1.name))
    switch2.cmd(
        "ovs-ofctl add-flow {} \"actions=output:NORMAL\"".format(switch2.name))
    switch3.cmd(
        "ovs-ofctl add-flow {} \"actions=output:NORMAL\"".format(switch3.name))
    switch4.cmd(
        "ovs-ofctl add-flow {} \"actions=output:NORMAL\"".format(switch4.name))
    switch5.cmd(
        "ovs-ofctl add-flow {} \"actions=output:NORMAL\"".format(switch5.name))

    info("* Running CLI\n")
    CLI(net)

    info("* Stopping network\n")
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    remote_controller = False
    topology(remote_controller)
