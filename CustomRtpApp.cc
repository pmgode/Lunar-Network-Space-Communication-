/*
 * MyRtpApplication.cc
 *
 *  Created on: 17-Jul-2024
 *      Author: Prashant Gode
 */

#include <stdio.h>
#include <string.h>
#include <math.h>
#include "inet/applications/udpapp/UdpBasicApp.h"
#include "inet/applications/base/ApplicationPacket_m.h"
#include "inet/networklayer/common/L3AddressResolver.h"
#include "inet/common/clock/ClockUserModuleMixin.h"
#include "inet/transportlayer/contract/udp/UdpSocket.h"
#include <omnetpp.h>

using namespace omnetpp;
using namespace inet;

class RtpOverUdpApp : public UdpBasicApp
{
private:
    cMessage *selfMsg;
    double maxEndToEndDelay;
    double maxLossRate;
    int numLost;
    int numReceived;

public:
    RtpOverUdpApp();
    virtual ~RtpOverUdpApp();

protected:
    virtual void initialize(int stage) override;
    virtual void processPacket(Packet *pk) override;
};

Define_Module(RtpOverUdpApp);

RtpOverUdpApp::RtpOverUdpApp()
{
    selfMsg = nullptr;
    numLost = 0;
    numReceived = 0;
}

RtpOverUdpApp::~RtpOverUdpApp()
{
    cancelAndDelete(selfMsg);
}

void RtpOverUdpApp::initialize(int stage)
{
    UdpBasicApp::initialize(stage);
    if (stage == INITSTAGE_LOCAL) {
        maxEndToEndDelay = par("maxEndToEndDelay").doubleValue();
        maxLossRate = par("maxLossRate").doubleValue();
    }
}

void RtpOverUdpApp::processPacket(Packet *pk)
{
    numReceived++;

    simtime_t endToEndDelay = simTime() - pk->getCreationTime();
    if (endToEndDelay >= maxEndToEndDelay) {
        numLost++;
    }

    double lossRate = (double)numLost / numReceived;
    if (lossRate > maxLossRate) {
        EV_WARN << "Loss Rate Exceeded Limit: " << lossRate << endl;
    }

    delete pk;
}
