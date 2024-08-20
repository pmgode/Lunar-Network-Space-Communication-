# Team 3 (Simulation of Communication Network)


## OMNET++ Network Simulation Project (Lunar Network Scenario)

Overview: 
This project simulates a network scenario using OMNET++, based on a problem statement that involves the communication network of a lunar base. The primary focus is on understanding bottlenecks in the system during FTP uploads while other HTTP and UDP-based applications are active. The network includes components such as an IEEE 802.11g WLAN, Ethernet, point-to-point radio links, and VDSL connections.


## Tasks and Objectives

**TASK 1 :** Modeling HTTP Request Inter-Arrival Times
- Objective: To model the inter-arrival times of HTTP requests based on a given trace file.
- **Approach :** 
    - Extracted inter-arrival times from the trace file.
    - Performed a statistical analysis to determine the best-fitting distribution.
    - Validated the statistical distribution using the chi-square goodness-of-fit test.
    - Plotted the inter-arrival times for visualization.

**TASK 2 :** Impact of HTTP Users on Video Connection QoS
- Objective: To evaluate how the number of active HTTP users influences the QoS of the video connection between the science station and the control station.
- **Approach :** 
    - Simulated the network with varying numbers of HTTP users (from 0 up to 30).
    - Calculated the packet loss rate for the video connection.
    - Analyzed the QoS impact in the absence and presence of HTTP users on both the science station and control station sides.
    - Plotted the results to show the relationship between the number of HTTP users and the video connection QoS.

**TASK 3 :** Impact of Receiver Advertised Window Size
- Objective: To assess the impact of reducing the receiver advertised window size to 10 times the maximum segment size (MSS) on the 
             network's performance.
- **Approach :** 
    - Simulated the scenario with the reduced window size for 1 and 0 HTTP users.
    - Analyzed the packet loss rate and other relevant metrics.
    - Justified the findings with reference to TCP flow control mechanisms.
    - Plotted the results to visualize the impact of the reduced window size.

## Simulation Setup

**Tools and Technologies: :** 
  - Network Model: Custom model based on IEEE 802.11g, IEEE 802.3, and other specified network components.
  - Traffic Modeling: HTTP requests, FTP uploads, UDP streams (CCTV camera, video conference).
  - Statistical Analysis: Chi-square test for distribution fitting.

## Scenario Details

- Area: 20 m × 20 m around the access point.
- Devices: Stationary astronauts’ computers, CCTV camera, video conference computers.
- Connections: Fast Ethernet, point-to-point radio link, VDSL with propagation delays.
- Protocols: TCP New Reno, UDP, RTP over IPv4.

## Results and Analysis

- Inter-Arrival Time Distribution: Identified the best-fitting distribution for HTTP request inter-arrival times.
- Packet Loss Rate: Analyzed the impact of HTTP user load on packet loss for video connections.
- QoS Analysis: Evaluated the impact on QoS under different scenarios, including the presence of multiple HTTP users and reduced receiver window size.

## Conclusion

- The simulation results highlight the bottlenecks in the network when handling simultaneous FTP uploads and HTTP requests. The QoS of the video connection is significantly impacted by the number of active HTTP users, and reducing the receiver advertised window size affects TCP performance.


## Authors and acknowledgment
Prashant Gode (prashant.gode@tuhh.de) and Rohan Mandal(rohan.mandal@tuhh.de)
- Special thanks to Dr.-Ing. Koojana Kuladinithi, Yevhenii Shudrenko, Aliyu Makama and Frank Laue for providing resources and support.
