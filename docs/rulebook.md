# Bots & Bento Rulebook

- Dr.-Ing. Edwin Babaians (TUM)
- Dr.-Ing. Mojtaba Karimi (TUM)

#### 📖 Release 

- Version 1.3: 08 May 2024
- Version 1.2: 24 April 2024
- Version 1.1: 20 April 2024
- Version 1.0: 05 March 2024
- Version 0.7: 15 Feb 2024

#### 1. Acknowledgments

We would like to acknowledge the following people for contributing to the development
of the Bots & Bento compition:

- Dr.-Ing. Arne Rost 
- Saori Ozawa
- Shogo Sawaguchi
- Benjamin Felbrich
- Prof. Dr.-Ing. Eckehard Steinbach

##### 1.1 How to cite the rulebook

```
@misc{bots_bento_2024,
author = {Edwin Babaians, Mojtaba Karimi, Shogo Sawaguchi, Eckehard Steinbach},
title = {Bots & Bento 2024 - Rulebook},
year = 2024,
howpublished = {\url{https://github.com/olive-robotics/olv_bots_bento_icra24/docs/rulbook.md}},
}
```

#### 2. Introduction
Within the Bots & Bento Challenge, competitors are tasked with designing and programming a robot that is able to locate, transport and sort standardized KLTs ([also called Eurobox, or KLT box](https://en.wikipedia.org/wiki/Euro_container), is an industrial stacking container conforming to the VDA 4500 standard.) containing the Japanese delicacy Bento. The rules are simple: given a pre-defined set of available hardware components, design your own robot and let it carry and sort KLTs as high and as efficiently as possible.

##### History

<img src="/images/klt.jpg" alt="7.png" width="350" />

In a world where technology and culinary arts blend into the fabric of daily life, a cutting-edge competition emerges, set in the near future where dense warehouse management systems are the norm. This competition, known as "Bots & Bento", is not just a contest; it's a visionary project designed to revolutionize how food is managed in warehouses across the globe, using advanced robotics and artificial intelligence.

The warehouses are vast, filled with stacks upon stacks of KLTs, each bearing bento boxes of different types: vegetarian, seafood, beef, and chicken. Each category must be sorted accurately, a task that would be daunting for humans alone. But this is the age of robotics, where precision and efficiency are paramount.

"The Great Bento Sort in Bots & Bento" challenges teams to develop sophisticated robots equipped with the latest in motion planning, computer vision, and AI development. These robots must navigate the labyrinthine aisles of the warehouse, identifying and sorting bento boxes with unerring accuracy. The competition's objective is two-fold: to advance the technology of automated systems in large-scale food management and to foster innovation in AI that can discern between food types, understanding textures, colors, and packaging with the same discernment as a human expert.

In this scenario, the imaginative use of bento-filled KLTs is a metaphor for the diverse range of products that such robots will handle in the real world. It's a testbed for innovation, a showcase of human ingenuity, and a tantalizing glimpse into a future where technology and tradition combine to create a world that is more organized, more efficient, and more delicious.

##### Example Demo

![1.png](/images/cover.gif "1.png")

##### 2.1 Organization of the League

A panel of judges from Olive Robotics, TUM Venture Lab Robotics / AI, and UTokyoIPC will evaluate the competitors’ performance based on the above mentioned criteria and reserve the right to grant extra points or penalties based on transparent criteria.

###### 2.1.1 Executive Committee (EC)

- Dr.-Ing. Arne Rost (TUM Venture Lab Robotics)
- Saori Ozawa (UTIPC)

###### 2.1.2 Technical Committee (TC)

- Dr.-Ing. Mojtaba Karimi (Technical University of Munich)
- Dr.-Ing. Edwin Babaians (Technical University of Munich)

#### 3. General Rules

General:
- Robots must initiate from the specified starting area.
- Robots are permitted to partially exit the arena, but are not allowed to leave the arena entirely at any point.

Hardware Compliance:
- Only components listed in the “Hardware” section are permitted for robot construction.
- Alteration or modification of provided hardware is prohibited. 

Time Constraints:
- Each run has a time limit of maximum 15 minutes.
- Any uncompleted tasks post timeout will not be scored.

Submission and Disassembly:
- Teams must bring their assembled robots to the competition venue.
- Post-competition, robots must be disassembled and provided hardware returned in the initial condition to the respective co-organizers (TUM VL RAI and UTokyo IPC)

Safety Compliance:
- Robots must operate safely to ensure the welfare of all present.
- Any unsafe behavior may result in disqualification.

Judging and Appeals:
- A panel of judges will evaluate the performance based on predefined criteria.

Technical Support and Troubleshooting:
- Limited technical support may be available during the competition.
- Teams are expected to handle troubleshooting autonomously.

##### 3.1 Robots
###### 3.1.1 Design and Contraints

Maximum allowed robot size: 65x65x90 cm
[KLT](https://en.wikipedia.org/wiki/Euro_container) size: 40x30x12cm

Robot hardware is temporarily provided by the challenge organizers (Olive Robotics supported by TUM VL RAI and UTokyo IPC) for the selected teams in the form of comprehensive robotic hardware kits of modular sensors, actuators and respective standardized connectors and power units. These modular robot components (servo motors, cameras, IMUs) are designed as interoperable and reconfigurable robot building blocks and natively speak ROS2 out-of-the-box. They can be treated as standalone Linux-based SMBs. Challenge participants are provided with the required documentation (datasheets, CAD, URDF, API docs, manuals) of the hardware along with a default robot design. However, participants are encouraged and rewarded for coming up with their own improved robot designs using the hardware. 

Aside from the provided hardware, teams are allowed to 3D print passive parts to amend their robot designs as well as using off-the-shelf transmission gears and belts.

Furthermore teams are free to either use any stationary computer to control the hardware wirelessly and / or use additional mobile compute units like Laptops, compute sticks and so on directly on the robot.

###### 3.1.2 Given Robotic Components

| Name     | Image                                               |
|-------------|-----------------------------------------------------|
| 5x oliveTM [SERVO OLV-SRV01-S64](https://docs.olive-robotics.com/hardware/servo/servo.html) | ![5.png](/images/5.png "5.png") |
| 2x oliveTM [CAMERA OLV-CAM01-S](https://docs.olive-robotics.com/hardware/camera/camera_01_s.html) | <img src="/images/6.png" alt="6.png" width="190" /> |
| 1x oliveTM [OLVX™-IMU01-9D](https://docs.olive-robotics.com/hardware/imu/OLVX™-IMU01-9D_10x.html) | <img src="/images/7.png" alt="7.png" width="80" /> |
| 4x oliveTM Omni Directional Wheels | ![8.png](/images/8.png "8.png") |
| 12x oliveTM X-Bolt Module Connector | ![9.png](/images/9.png "9.png") |
| 1x T-Slot Kit 20x20mm w/ connectors | ![10.png](/images/10.png "10.png") |
| 1x T-Slot Kit 10x10mm w/ connectors | ![11.png](/images/11.png "11.png") |
| 1x passive part for the hook system | ![passive.png](/images/passive.png "passive.png") |
| 1x Set of USB-C Cables various lengths and 1x USB-C Hub | ![12.png](/images/12.png "12.png") |
| 2x USB-C 100W PD Power Bank | <img src="/images/battery_v2.png" alt="13.png" width="150" /> |

![set.png](/images/set.png "set.png")

In the picture we have 6 servo motors. One is backup.

###### 3.1.3 Simulation Content

To be able to simulate the components in any simulation software the Universal Robot Description (URDF) files are available from this git repository.

- https://github.com/olive-robotics/olv_module_descriptions
- https://github.com/olive-robotics/olv_brackets_descriptions
- https://github.com/olive-robotics/olv_kit_descriptions

Example URDF of the robot base:

<img src="/images/ANT.gif" alt="ANT.gif" width="400" />

###### 3.1.4 Documentation

For more technical information regarding each olive components you can visit:

- https://docs.olive-robotics.com

###### 3.1.5 ⚠️ Preliminary requirements per team

Each team should have a working laptop with [Ubuntu 22.04 Desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview) and [ROS 2 Humble](https://docs.ros.org/en/humble/Installation.html) installed. The laptop should have at least one USB-C or USB-A 2.0/3.0 slot.

###### 3.1.6 Example Robot

![2.png](/images/2.png "2.png")

You will be provided with the Olive [ANT kit](https://docs.olive-robotics.com/kits/ant/ant.html) as the base for your robot. To enhance its capabilities, you are tasked with creatively installing an additional 2 cameras and 2 actuators. This modification aims to transform the passive base into a robot with high-level understanding and picking capabilities, enabling it to effectively transport and sort KLTs within the competition arena. Your innovative integration of these components will be crucial in equipping the robot with the necessary tools to navigate, identify, and manipulate objects according to the competition's requirements.

<img src="/images/robot.png" alt="ant.png" width="400" />

<img src="/images/antm.gif" alt="ant.png" width="400" />

###### 3.1.6.1

- 📘 [Please follow this tutorial to build the base](tutorial.md)

###### 3.1.6.2

Example robot with laptop, cameras, and hooking system

![2.png](/images/a3.png "2.png")

![2.png](/images/a2.png "2.png")

###### 3.1.7 Behavior and Safety

In general, all robots shall be operated with maximum safety in mind. Any robot operation must be such that a robot neither harms humans nor damages the environment. The used batteries shall be handled with care and all team members must be educated in the correct usage, charging and storage of the batteries of the team.

##### 3.2 Arena Example Environemnt

![3.png](/images/a1-3.png "3.png")

###### 3.2.1 Floor

The floor is made of some firm material. This includes among others floors made of concrete, screed, timber, plywood, chipboard, laminated boards, linoleum, PVC flooring, or carpet. 

###### 3.2.2 Virtual Walls

Virtual Walls are made of yellow/black tape and may never be crossed during a run. The arena doesn't contain Walls.


Robots may cross over the red/white tapes but must not entirely cross the boundaries of the main area delineated by the yellow/black tape. Partial crossing of the yellow/black tape area is permissible.

###### 3.2.3 Obstacles

The arena will initially be free of obstacles, providing a clear path for the robots to navigate. However, for an added technical challenge, red paper packaging boxes can be introduced into the arena. This is up to teams and an idea for showcasing a demo for the technical challenge session.

###### 3.2.4 Tapes

<img src="/images/14.png" alt="7.png" width="200" />

###### 3.2.4.1 Red/white Tape:
The red/white Tape (Tesa signal 5cm width) is considered as a virtual seperator and has an zero height. 

###### 3.2.4.2 Yellow/black Tape:
The yellow/black Tape (Tesa signal 5cm width) is considered as a virtual wall and has an infinite height. 

###### 3.2.5 Zones

We will have start/end zone in the middle and on the edge of arena. It will be several placement zones for KLTs which robot has to bring them there. The receive the extra score points the KLTs has to match the location id. This zones will be marked with the red/white tape. The ground will be white.

###### 3.2.6 Arena Layout

The competition arena is a 〜5x6 meter clear space. It has designated starting and sorting areas. 

Standardized KLTs with free wheels are randomly scattered within the arena, each measuring 40x30 cm and labeled with localisation tags on top and sides indicating unique ids. 

![3.png](/images/a5.png "3.png")


###### 3.2.7 Start and Finish


The robot's operation commences and concludes in the same square zone, strategically positioned on the arena's edge. This designated area serves as both the launching point for the robot's mission and the final destination where it returns to mark the completion of its tasks, emphasizing the significance of this singular location for both the beginning and end of the operation.

###### 3.2.8 KLTs

During the competition, there will be a maximum of six KLTs, each supported by 4x wheels for ease of movement. The robot's task involves pulling these KLTs to sort them into predefined locations. The starting position of each KLT within the arena is determined randomly, adding an element of unpredictability to the challenge. To facilitate identification and sorting, each KLT is equipped with overal 8x AprilTags. These tags contain unique IDs, enabling the robot to accurately recognize and handle the KLTs according to the competition's requirements.

Example of the KLT:



<img src="/images/klt/2.jpg" alt="klt_real.jpg" width="350" />

<img src="/images/klt/3.jpg" alt="7.png" width="350" />

<img src="/images/klt/4.jpg" alt="klt_real.jpg" width="350" />

To carry the KLT we suggest you build your own hook like the picture below (in the picture the KLT is the bigger one, but we will use the small version):

![3.png](/images/hook_example.JPG "4.png")

###### 3.2.9 AprilTag 

AprilTags will be used in the competition. This should allow teams to focus on other areas than object recognition by simplifying the detection of KLTs. 

The AprilTags measur [100mm x 100mm](https://github.com/rgov/apriltag-pdfs/tree/main/tag36h11/a4/100mm) or smaller and have an encoding taken from the 36h11 AprilTag family, including a 1bit black and 1bit white border.

We will use the small tags for the KLTs and depeneds on the situation (big or small) for the grid of the ground.

AprilTags can be easy generated. Example AprilTags out of the AprilTag Family 36h11 are shown:

<img src="/images/16.png" alt="7.png" width="500" />

⚠️ Pritable A4 size (36h11):
https://github.com/rgov/apriltag-pdfs

Open source implementation for Olive Camera is available in the camera playground repo:

https://github.com/olive-robotics/olv_camera_tpu_playground_py

<img src="/images/tag.gif" alt="7tag.gif" width="400" />

AprilTag detection will be preinstalled in the cameras and they will publish the tag information by default. The message type for AprilTags will be standard [apriltag_msgs](https://github.com/christianrauch/apriltag_msgs).

```
string family
int32 id
int32 hamming
float32 goodness
float32 decision_margin
Point centre                    # centre in (x,y) pixel coordinates
Point[4] corners                # corners of tag ((x1,y1),(x2,y2),...)
float64[9] homography           # 3x3 row-major homography matrix
```

It is also possible to change the camera lenses. Here we compaired different supported lenses:

## Supported Camera Lenses 

| Lens                               | Focal Length (mm) | Max Aperture | Sensor Size  | Features            | Predicted FOV (°) |
|------------------------------------|--------------------|--------------|--------------|---------------------|-------------------|
| 2.8-12mm 1:1.4 IR                  | 2.8-12             | f/1.4        | 1/2.7"       | Manual focus, zoom  | ~28° - ~90°       |
| Far-view                           | 2.6                | f/2.6        | 1/4"         | N/A                 | ~55°              |
| Low-distortion Lens                | 3.6                | N/A          | 1/2.7"       | N/A                 | ~60°              |
| Fisheye Lens                       | 10 (estimated)     | f/2.8 (estimated) | 1/2.3" (estimated) | N/A              | 187°              |

###### 3.2.9.1 

⚠️ 2x AprilTags will be installed on each side and on each KLT. In this example for a KLT it will be 8 Tags. The id for all Tags will be same and you can identify the side or front from distance between each AprilTag. 

![3.png](/images/klt_simple.png "4.png")

⚠️ We will extend the tags to make the localization easier. We will use either small or big tags for the ground.

![3.png](/images/grid.png "3.png")

#### 4. Competition
The competition is split into three runs for each team. In the first run, the arena is free of obstacles (other than the KLTs themselves). The task is for the robot to collect a KLT and carry to a predefined location. 

In the second run, each team will show a technical challenge achivement. Extra points are granted if the robot manages to transport KLTs in order of their id.

In the third round, each team will have a short presentation, pitching their inovative idea and algorithm to public.

##### 4.1 Teams and Roles
##### 4.2 Meetings and Language of Communication

Both the TC and the EC may organize several special meetings during a competition, such as referee meetings, teamleader meetings, etc. The meetings are held in english and will be planned and announced locally. They are used to clarify rules, assign timeslots, request test participation or for any other exchange of information between teams and commitee members. It is the responsibility of each team to inform themselves about the organization and scheduling of such meetings. Each team is expected to send at least one representative to such meetings. If the meeting refers to specific roles, such as ’referee’ or ’team leader’, the person designated by the team to fill this role is expected
to participate.

##### 4.3 Code of Conduct and Disqualification

Teams and team members are expected to maintain a friendly and cooperative atmosphere throughout a competition and contribute to a vivid work environment and to scientific exchange before, during and after a competition. The TC may disqualify individual team members or a whole teams during a competition for severe reasons, such as repeated breach of rules.

##### 4.4 Competition Procedure
##### 4.5 Time Schedule

A detailed schedule for sessions will be available locally, providing teams with their specific time slots for robot testing and main run.

##### 4.6 Practice Slots

Scheduled practice time slots will be made available for each team, allowing them the opportunity to test their robots in the competition environment. These practice sessions will be announced locally, providing teams with the necessary information to plan and prepare for their designated testing times. This arrangement ensures that all participants have equal access to the arena for fine-tuning their robots and strategizing based on the actual competition setup.

##### 4.7 Competition Phases

| Phase      | Do                                   | Do Not                                     |
|------------|--------------------------------------|--------------------------------------------|
| Prep Phase | move robot to start pose           |  hardcode solutions                       |
|            | prepare task execution             |  record test-specific data                |
|            | clear robot memory                 |                                            |
| Run Phase  | nothing / watch the run            |  control the robot                        |
|            |                  | interfere with the robot                 |
|            |                                      | enter the arena                          |
| End Phase  | stop robot autonomy                |                                      |
|            | move robot out           |            |


###### 4.7.1 Preparation Phase
During the prep phase, teams are allowed to move their robot from the parc ferm´e to the defined start pose in the arena either by hand or by carefully driving manually. They should prepare their robot for their run and can therefore remote access the robot and/or make minor changes. It is explicitly forbidden to hardcode solutions for specific requirements of a test during this phase (e.g. drawing position of obstacles in the map). Also, if the robot passes and detects obstacles during this phase, they must be erased from the memory (e.g. clear costmap) unless they can be detected from the START location. The TC might disqualify teams that try to gain unfair advantages from the current or even the following tests.

###### 4.7.2 Run Phase

The run phase begins once the preparation time is up or when the teamleader announces that the team is ready. The task is then sent to the robot and from there on, the robot must act fully autonomously. It is forbidden to interact or control the robot in any human kind (keyboard/mouse
actions, gestures, voice). 

During the run phase, the robot must not leave, nor may any person enter the arena. Teammembers of the performing team are allowed to enter the arena to prevent damage in case of an error (e.g. remove a dropped object from the robots path), but receive a penalty for each interaction. If a robot behaves uncontrolled and poses a potential threat to the environment, any person may approach the robot and press the emergency stop. However, it is requested and strongly advised that only the developers touch their robot.

The run phase regularly ends when:

- The robot has reached the FINISH location of the arena
- The run time is up
- The teamleader says ’stop’
The run phase ends early when:
- The robot has caused a second major collision
- A team was identified to be cheating

The end of a run phase must be announced by the EC by saying ’end’. Once this happened, the
team may touch and control their robot to bring it to a full stop.

###### 4.7.3 End Phase

In the resulting end phase the team is expected to move their robot back to parc ferm´e. Referees gather and discuss their performance rating afterwards. Once they agree on the performing team’s
result, the teamleader is required to accept this score. Teams are allowed to make their case if they do not agree with the refs decision, but cannot force changes and are expected to be understanding.

Special cases will be decided by the TC if the rulebook leaves room for interpretation. Once the score has been accepted by a team, the arena must be set up for the next run if necessary.
The prep time of the next team begins once the arena state is declared as ready by all refs.

##### 4.10 Restarting a Run

During a run, the teamleader can restart the test execution once. Therefore he/she must say ’restart’, which stops the current run phase. The robot must be stopped using the emergency switches, which then allows the refs to reset the arena state. The remaining run time will be noted and used after the restart. Once the refs have finished resetting the arena, the performing team is brought back to their prep phase, which allows them to move the robot back to the start area and prepare it for the restarted run. A so called tactical call of a restart (e.g. to prevent a major collision) is allowed, because this rewards the teams knowledge about the robot.

##### 4.11 Challenges
###### 4.11.1 🏁 KLT Transport
In the first run, teams will navigate their Autonomous Mobile Robot (AMR) in an arena free of obstacles, except for the KLTs themselves. The robot must select any one of the six KLTs and transport it to a designated park zone. The task is to be completed within a maximum time of 15 minutes. Completing this task will grant the team the full score for this challenge, with time efficiency being a crucial factor.

While placing the KLTs in any park zone is required, teams will earn extra points for parking the KLTs in order of their ID. 

###### 4.11.2 🏁 Technical Challenge
Teams have the opportunity to present a technical showcase demonstrating a key feature or creative aspect of their system. Proposals can include handling static or dynamic obstacles, such as people moving within the arena, to exhibit the robot's capabilities in max 10 minutes. The creativity and problem solving has 40%, running a complete task is 30%, and robot design is in general has 30%. 

###### 4.11.3 🧑‍💻 Presentation
Each team has 10 minutes to pitch their approach to solving the challenges. They will introduce their team and explain their strategies and solutions. The presentation may be recorded and published online to highlight the open nature of the competition and share findings and results. Scientific achivement / engineering solution 30%, overal presentation skills 30%, Teamwork has 40% of the points. 

#### 5. Scoring and Ranking 
The competition spans two days, with a total of 12 hours available for all runs and the award ceremony. There are six teams in total.

##### 5.1 Scoring
###### 5.1.1 Scores
Teams will be scored on the speed and efficiency of completing the KLT Transport and KLT Sorting challenges. Extra points are awarded for stacking KLTs in order of their ID during the sorting challenge. 

| Challenge                | Task Completion Score | Extra Points for Sorting |
|--------------------------|---------------------------------------------|--------------------------|
| 6 KLTs Transport / Sorting           | if the team sort all 6 KLTs, **200** points extra            | **25** points per KLT  or **50** points per KLT with correct ID | 
| Technical Challenge      | **150** points            |                                          |                       | 
| Presentation             | **150** points            |                                          |                       | 

###### 5.1.2 🚫 Penalties
Penalties are incurred for various infractions, including:
- The robot exiting the competition arena, marked by yellow and black tape.
- Multiple requests for resets. One reset is permitted without penalty, but subsequent resets will result in score deductions.

| Infraction               | Penalty Points |
|--------------------------|----------------|
| Exiting the arena (and come back)       | -25 points      |
| Up to three reset     | 0 points      |
| Each additional reset    | -25 points each |

*Note: The first reset request does not incur a penalty.*

###### 5.1.3 Restarts
Teams are allowed one restart without penalty. Additional restarts will incur penalties, which will impact the team's total score.

##### 5.2 🏅 Ranking
Teams will be ranked based on their overall total score accumulated over the two days of competition. The top three teams will be announced and awarded as the best in the competition.

"GOOD LUCK! ;)"

#### 6. References

- https://docs.olive-robotics.com
- https://www.olive-robotics.com/
- https://www.ros.org/
- https://2024.ieee-icra.org/









