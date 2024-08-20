import inet.applications.udpapp.UdpBasicApp;
import inet.node.inet.StandardHost;
import inet.node.ethernet.EthernetSwitch;
import inet.node.wireless.AccessPoint;
import inet.physicallayer.wireless.ieee80211.packetlevel.Ieee80211ScalarRadioMedium;
import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.linklayer.ieee80211.Ieee80211Interface;
import inet.node.inet.WirelessHost;
import inet.node.inet.Router;
import inet.node.base.LinkLayerNodeBase;


simple RtpOverUdpApp extends UdpBasicApp
{
    parameters:
        @class(RtpOverUdpApp);
        double maxEndToEndDelay @unit(s);
        double maxLossRate;
}


network LunarNetwork
{
    parameters:
        int numWebClients = 1;
    submodules:
        configurator: Ipv4NetworkConfigurator {
            parameters:
                @display("p=35.502964,62.7219");
        }

        radioMedium: Ieee80211ScalarRadioMedium {
            @display("p=395,146");
        }

        // Science Station
        wlanAP: AccessPoint {
            @display("p=200,100");
        }

        lunarWebBrowsing[numWebClients]: WirelessHost {
            @display("p=172.78108,41.420124;r=100");
        }

        ftpUploadScience: WirelessHost {
            @display("p=234.91127,17.751482");
        }

        videoConference: WirelessHost {
            @display("p=149.70416,81.065094");
        }

        scienceStationRouter: Router {
            @display("p=200,200");
        }

        cctvCamera: StandardHost {
            @display("p=314.2012,138.46155");
        }

        // Control Station
        controlStationRouter: Router {
            @display("p=500,200");
        }

        cctvMonitoringStation: StandardHost {
            @display("p=649,105");
        }

        videoConferenceRoom: StandardHost {
            @display("p=568,300");
        }

        httpServer: StandardHost {
            @display("p=721,200");
        }

        ftpServer: StandardHost {
            @display("p=700,300");
        }

    connections allowunconnected:
        //Science station connections
        wlanAP.ethg++ <--> { @display("m=s"); datarate = 100Mbps; } <--> scienceStationRouter.ethg++;
        scienceStationRouter.pppg++ <--> {  delay = 10ms; datarate = 12Mbps; } <--> controlStationRouter.pppg++;
        cctvCamera.pppg++ <--> { @display("m=s"); datarate = 100Mbps; } <--> scienceStationRouter.pppg++;

        // Control Station Connections
        cctvMonitoringStation.pppg++ <--> { @display("m=s"); datarate = 100Mbps; } <--> controlStationRouter.pppg++;
        videoConferenceRoom.pppg++ <--> { @display("m=s"); datarate = 100Mbps; delay = 5ms; } <--> controlStationRouter.pppg++;
        httpServer.pppg++ <--> { @display("m=s"); delay = exponential(30ms); datarate = 100Mbps; } <--> controlStationRouter.pppg++;
        ftpServer.pppg++ <--> { @display("m=s"); delay = exponential(30ms); datarate = 100Mbps; } <--> controlStationRouter.pppg++;

}
