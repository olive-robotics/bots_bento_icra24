# IEEE ICRA 2024 | Bots & Bento | The first Robotic Pallet Handling Competition

Germany and Japan have excellent robotics researchers and industrial robotics companies. To further foster collaboration, the TUM Venture Lab Robotics / AI and the UTokyoIPC are hosting a new ICRA competition focusing on entrepreneurship and the goal of translating excellent research into new industrial applications.

![1.png](/images/1.png "1.png")

## Challenge Description
Within the Bots & Bento Challenge, competitors are tasked with designing and programming a robot that is able to locate, transport and stack standardized palettes containing the Japanese delicacy Bento. The rules are simple: given a pre-defined set of available hardware components, design your own robot and let it stack palettes as high and as efficiently as possible.

- 🗓️ Duration: 4 days
- 📍 Place: Yokohama, Japan
- 🗒️ Registeration Open: February 29, 2024 11:59 pm
- 🗒️ Start: May 13, 2024 12:00 am GMT+2
- 🔗 Apply: [Here](https://docs.google.com/forms/d/e/1FAIpQLSfIDB8EHTKZsTSxabpzjz0qU7LuDq8VqgYfEWqWLxOi16SeZA/viewform) 
- 📧 General Contact: arne.rost@tum-venture-labs.de
- 📧 Technical Contact: edwin@olive-robotics.com

## Rulebook

- 📘 [Rulebook 2024](docs/rulebook.md)

## Intorduction
Our goal is to drive innovation in autonomous material handling through a competition in which teams design and build robots using identical, pre-supplied robotics kits to perform pallet handling tasks within a specified area as part of our first challenge. 

This first inaugural competition, co-organized by Olive Robotics, UTokyoIPC and TUM Venture Lab Robotics / AI, is a competitive platform for IEEE ICRA 2024, and is designed to foster innovation and practical skills among budding robotics professionals in the field of autonomous material handling. Within the Bots & Bento Challenge, competitors are tasked with designing and programming a robot that is able to locate, transport and stack standardized palettes containing the Japanese delicacy Bento. The rules are simple: given a pre-defined set of available hardware components, design your own robot and let it stack palettes as high and as efficiently as possible.

The Bots & Bento Challenge at IEEE ICRA 2024 will be held from May 13th to May 17th in Yokohama, Japan. Acting as the local partner in Japan, UTokyoIPC will be responsible for handling most of the on-site organizational tasks, whereas the Germany-based team takes care of supporting participants and shipping hardware and providing the simulation environment and later on be onsite to manage the competition itself. To ensure first-class support to all challenge participants, the number of teams allowed to participate is limited to six teams with up to six team members each.

Challenge preparation and training in virtual environments
In order to streamline processes and reduce the burden to participants of shipping large, bulky robotic setups to Japan with potential complications in customs, freight and clearance and thus delayed hardware deliveries, the challenge preparation phase is streamlined to be quite lean. The participants will receive a reduced-size “sample kit” approx. two months in advance with the most important components to get their hands on the actual hardware. The entirety of competition hardware needed is sent to Japan by the challenge organizers instead. This guarantees smooth transport of hardware and improves logistics handling.
Additionally, we introduce a virtual simulation environment with a detailed representation of the challenge arena and the robot hardware (eg. given in Gazebo, URDF) already sent approx. three months in advance. In this virtual representation participants are able to design and train their robots to handle and stack the Bento boxes. At ICRA, participants will then get two days of time upfront to assemble their own robots based on their virtual designs.

### 1-Arena
The competition arena is a 5x5 meter clear space with barriers on its sides. It has designated starting and stacking areas. Standardized pallets are randomly scattered within the arena, each measuring 40x30 cm and labeled with localisation tags on top and sides indicatinguniqueids. Atfirsttheareaisclearandwithoutfurtherobstacles.Inthesecond challenge run, however, small obstacles with a size of up to 30x30x30cm are introduced into the area and must be avoided.

### 2-Robotic Hardware

Maximum allowed robot size: 65x65x90 cm
Palette size: 40x30x12cm

Robot hardware is temporarily provided by the challenge organizers (Olive Robotics supported by TUM VL RAI and UTokyo IPC) for the selected teams in the form of comprehensive robotic hardware kits of modular sensors, actuators and respective standardized connectors and power units. These modular robot components (servo motors, cameras, IMUs) are designed as interoperable and reconfigurable robot building blocks and natively speak ROS2 out-of-the-box. They can be treated as standalone Linux-based SMBs. Challenge participants are provided with the required documentation (datasheets, CAD, URDF, API docs, manuals) of the hardware along with a default robot design. However, participants are encouraged and rewarded for coming up with their own improved robot designs using the hardware. The hardware kits will be provided two months before the competition so that teams can start designing and programming their competition bots.

Aside from the provided hardware, teams are allowed to 3D print passive parts to amend their robot designs as well as using off-the-shelf transmission gears and belts. Furthermore teams are free to either use any stationary computer to control the hardware wirelessly and / or use additional mobile compute units like Intel NUCs, Laptops, compute sticks and so on directly on the robot.

### 3-Competition Tasks
The competition is split into two runs for each team. In the first run, the arena is free of obstacles (other than the palettes themselves). The task is for the robot to collect palettes and build a single palette tower as high as possible. In the second run, small obstacles are introduced into the arena and the task is to build a tower of six palettes in the shortest time possible. The challenge is evaluated and awarded in three categories: “Highest Tower”, “Fastest Stacking” and “Overall Champion'' with the latter merging both runs into a single score. Extra points are granted if the robot manages to stack pallets in order of their id.

A panel of judges from Olive Robotics, TUM Venture Lab Robotics / AI, and UTokyoIPC will evaluate the competitors’ performance based on the above mentioned criteria and reserve the right to grant extra points or penalties based on transparent criteria.
Rules and Regulations
Start and Boundary Compliance:
- Robots must initiate from the specified starting area.
- Robots are not permitted to exit the arena at any point.
Hardware Compliance:
- Only components listed in the “Hardware” section are permitted for robot construction.
- Alteration or modification of provided hardware is prohibited. Time Constraints:
- Each run has a time limit of maximum ten minutes.
- Any uncompleted tasks post timeout will not be scored.
Submission and Disassembly:
- Teams must bring their assembled robots to the competition venue.
- Post-competition, robots must be disassembled and provided hardware returned in the initial condition to the respective co-organizers (TUM VL RAI and UTokyo IPC)
latest in two weeks after the competition. Scoring Criteria:
- Points awarded based on the number (height) of the collected pallet tower, speed of stacking, order of pallet IDs, and adherence to design constraints.
- Specific point values for each criterion will be disclosed prior to competition.
Safety Compliance:
- Robots must operate safely to ensure the welfare of all present.
- Any unsafe behavior may result in disqualification.
Judging and Appeals:
- A panel of judges will evaluate the performance based on predefined criteria.
- Teams have the right to appeal and must do so within a specified timeframe post
scoring announcement. Technical Support and Troubleshooting:
- Limited technical support may be available during the competition.
- Teams are expected to handle troubleshooting autonomously.

## Awards & Budget
TUM Venture Lab Robotics / AI and UTokyo IPC will both share the burden of supplying the 12 teams with rented robotics kits, which will be returned by the teams to the hosts after the competition. TUM VL RAI will supply four complete kits and eight kits will be rented additionally for the teams. We will further sponsor a joint award for the best team. All qualified and participating teams will receive certificates of participation. Optionally, a visit to one or both entities in Munich and/or Tokyo for the winning team is under consideration.

## Schedule 2024

| Date     | Event                                               |
|-------------|-----------------------------------------------------|
| Jan.4th | - Public call for challenge participation<br>- Challenge info website online<br>- Application process starts |
| Feb.29th  | - Application deadline for competitors             |
| Mar.4th   | - Notification to participating teams<br>- Starting preparation to send out robot sample kits |
| Mar.15th  | - Shipment of sample kits to participants          |
| Apr.15th  | - Shipment of full robotics challenge kits to Japan and local storage |
| May.12th   | - Venue setup by challenge organizers              |
| May.13th   | - Welcoming challenge participants in Yokohama<br>- Day one of robot assembly |
| May.14th   | - Day two of robot assembly                        |
| May.15th   | - Challenge Session 1             |
| May.16th   | - Challenge Session 2 <br>- Award Ceremony |
| May.17th   | - Disassembly of robots by challenge organizers and preparation of return of kits |

## Safety Considerations
The safety considerations for this challenge are relatively straightforward: as the arena is walled with robust barriers on each side and the machines will move at relatively low speed (~1m/s at max), it is very unlikely for a robot to escape the arena. Within the arena safety hazards might be represented by the robot or stacks of pallets falling over. Thus to avoid harm to visitors and the contestants, no one is allowed to enter the arena while a competition run is under way.

## Competition History
TUM Venture Lab Robotics / AI and UTokyo IPC want to set up a permanent competition that will hopefully become part of ICRA. The goal is to strengthen future ICRAs in the EU by offering a similar second competition, and then to host a Japanese challenge. The idea came up during the exchange of ideas between the TUM Venture Lab Robotics / AI and UTokyo IPC in June and October 2023.

## Alignment with ICRA
The "Bots & Bento" challenge embodies cutting-edge robotics and AI technologies pivotal in modern autonomous systems. SLAM algorithms are honed for accurate robot localization amidst dynamic environments, while efficient path planning is crucial for optimizing the collection and stacking of pallets. Precise motion control ensures safe and accurate handling of pallets for stable stacking. The competition leverages ROS and ROS2 frameworks for orchestrating a seamless choreography between perception, decision-making, and control, fostering modular, collaborative robotics development. Additionally, sensor fusion and machine learning for perception are crucial for a holistic understanding of the environment and advanced object recognition, respectively.

The competition further promotes real-time systems ensuring robustness in dynamic, unstructured environments, a core theme in contemporary robotics research. The provision of a hardware kit encourages hardware-software co-design, fostering innovation in integrated solutions for autonomous material handling. AI-driven decision-making enables adaptive strategies for stacking pallets based on their IDs, optimizing the process further. Although not explicitly mentioned, potential Human-Robot Interaction elements could be integrated to ensure safety and collaboration in shared spaces. Through a practical, industrially-relevant challenge, this competition provides a platform for the ICRA community to showcase, test, and advance the state-of-the-art in robotics and AI, aligning perfectly with ICRA's mission of propelling the global robotics community forward.

## Challenge Participants
The organizing team is well connected to the international robotics community and has close scientific & industrial contacts to potential teams at TU Munich / MIRMI, University of Stuttgart / Fraunhofer IPA, ETH Zurich, EPFL Lausanne, Odense & Denmark, the robotics community in Basque Area in Spain, University of Bonn, University of Tokyo as well as the Yokohama ecosystem and others.
Based on our network reach we expect a large number of applicants. The overall estimated teams to be qualified is 12 teams and with max. up to four members per team. So the maximum number of participants will be 48.

## Organizers
1) **TUM Venture Lab Robotics / AI :** This early-stage robotics and artificial intelligence (AI) incubator of Technical University of Munich and UnternehmerTUM provides a unique, networked hub specifically tailored to scalable startups. We provide comprehensive support, including mentoring, access to industry experts, state-of-the-art facilities and tools, funding opportunities, and a vibrant community of like-minded innovators. By combining deep industry knowledge with a hands-on approach, we empower startups to rapidly develop and refine their technologies, gain a foothold in the marketplace, and successfully navigate the challenges of scaling. Our unique selling point lies in our commitment to disruptive deep-tech innovation and advancing the future of robotics and AI through our dedicated support ecosystem.

- Link: https://www.tum-venture-labs.de/labs/robotics-ai/


 2) **UTIPC:** UTokyo Innovation Platform Co., Ltd.(UTokyo IPC for short) supports various startups in deep tech fields, which have the potential to significantly change society, including life science and medicine, robotics and hardware, IT services and artificial intelligence (AI) to enhance the innovation ecosystem around universities. UTokyo IPC provides not only funding support but comprehensive mentoring support for academic technology seeds to deliver it to society and also consulting for team building. It operates the largest incubation program "1stRound", which is dedicated for pre-seed startups, entrepreneurs and researchers spin-out from universities and R&D entities. 1stRound is co-hosted by 13 of the most prominent universities and sponsored by 24 of industrial leading companies in Japan.

- Link: https://www.utokyo-ipc.co.jp/en/

3) **OR:** Olive Robotics GmbH is a leading provider of interoperable, software-defined robot hardware based in Munich, Germany. Within this challenge Olive Robotics will provide robotic kits, technical expertise, co-organizing and competition evaluation on-site.
- Link: https://olive-robotics.com/