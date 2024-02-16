# Bots & Bento Rulebook

- Dr.-Ing. Edwin Babaians (TUM)
- Dr.-Ing. Mojtaba Karimi (TUM)

#### Release 

- Versionv 0.7: 15 Feb 2024

#### 1. Acknowledgments

We would like to acknowledge the following people for contributing to the development
of the Bots & Bento compition:

- Dr.-Ing. Arne Rost 
- Saori Ozawa
- Benjamin Felbrich
- Prof. Dr.-Ing. Eckehard Steinbach

##### 1.1 How to cite the rulebook

```
@misc{bots_bento_2024,
author = {Edwin Babaians, Mojtaba Karimi, Eckehard Steinbach},
title = {Bots & Bento 2024 - Rulebook},
year = 2024,
howpublished = {\url{https://github.com/olive-robotics/olv_bots_bento_icra24/docs/rulbook.md}},
}
```

#### 2. Introduction
Within the Bots & Bento Challenge, competitors are tasked with designing and programming a robot that is able to locate, transport and sort standardized palettes containing the Japanese delicacy Bento. The rules are simple: given a pre-defined set of available hardware components, design your own robot and let it carry and sort palettes as high and as efficiently as possible.

##### 2.1 Organization of the League

A panel of judges from Olive Robotics, TUM Venture Lab Robotics / AI, and UTokyoIPC will evaluate the competitors’ performance based on the above mentioned criteria and reserve the right to grant extra points or penalties based on transparent criteria.

###### 2.1.1 Executive Committee (EC)

- Dr.-Ing. Arne Rost (TUM Venture Lab Robotics)
- Saori Ozawa (UTIPC)

###### 2.1.2 Technical Committee (TC)

- Dr.-Ing. Mojtaba Karimi (Technical University of Munich)
- Dr.-Ing. Edwin Babaians (Technical University of Munich)

#### 3. General Rules

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

##### 3.1 Robots
###### 3.1.1 Design and Contraints

Maximum allowed robot size: 65x65x90 cm
Palette size: 40x30x12cm

Robot hardware is temporarily provided by the challenge organizers (Olive Robotics supported by TUM VL RAI and UTokyo IPC) for the selected teams in the form of comprehensive robotic hardware kits of modular sensors, actuators and respective standardized connectors and power units. These modular robot components (servo motors, cameras, IMUs) are designed as interoperable and reconfigurable robot building blocks and natively speak ROS2 out-of-the-box. They can be treated as standalone Linux-based SMBs. Challenge participants are provided with the required documentation (datasheets, CAD, URDF, API docs, manuals) of the hardware along with a default robot design. However, participants are encouraged and rewarded for coming up with their own improved robot designs using the hardware. The hardware kits will be provided two months before the competition so that teams can start designing and programming their competition bots.

Aside from the provided hardware, teams are allowed to 3D print passive parts to amend their robot designs as well as using off-the-shelf transmission gears and belts. Furthermore teams are free to either use any stationary computer to control the hardware wirelessly and / or use additional mobile compute units like Intel NUCs, Laptops, compute sticks and so on directly on the robot.

###### 3.1.2 Given Robotic Components

| Name     | Image                                               |
|-------------|-----------------------------------------------------|
| 6x oliveTM [SERVO OLV-SRV01-S64](https://docs.olive-robotics.com/hardware/servo/servo.html) | ![5.png](/images/5.png "5.png") |
| 2x oliveTM [CAMERA OLV-CAM01-TP](https://docs.olive-robotics.com/hardware/camera/camera_01_tp.html) | <img src="/images/6.png" alt="6.png" width="190" /> |
| 1x oliveTM [IMU OLV-IMU01-13D](https://docs.olive-robotics.com/hardware/imu/imu_01_13d_10x.html) | <img src="/images/7.png" alt="7.png" width="80" /> |
| 4x oliveTM Omni Directional Wheels | ![8.png](/images/8.png "8.png") |
| 12x oliveTM X-Bolt Module Connector | ![9.png](/images/9.png "9.png") |
| 1x T-Slot Kit 20x20mm w/ connectors | ![10.png](/images/10.png "10.png") |
| 1x T-Slot Kit 10x10mm w/ connectors | ![11.png](/images/11.png "11.png") |
| 1x Set of USB-C Cables various lengths and 1x USB-C Hub | ![12.png](/images/12.png "12.png") |
| 1x USB-C 65W PD Power Bank | ![13.png](/images/13.png "13.png") |

###### 3.1.3 Simulation Content

To be able to simulate the components in any simulation software the Universal Robot Description (URDF) files are available from this git repository.

https://github.com/olive-robotics/olv_module_descriptions
https://github.com/olive-robotics/olv_brackets_descriptions
https://github.com/olive-robotics/olv_kit_descriptions

###### 3.1.4 Documentation

For more technical information regarding each olive components you can visit:

https://docs.olive-robotics.com

###### 3.1.3 Preliminary requirements per team

Each team should have a working laptop with [Ubuntu 22.04 Desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview) and [ROS 2 Humble](https://docs.ros.org/en/humble/Installation.html) installed. The laptop should have at least one USB-C or USB 3.0 slot.

###### 3.1.4 Example Robot

![2.png](/images/2.png "2.png")

###### 3.1.5 Behavior and Safety

In general, all robots shall be operated with maximum safety in mind. Any robot operation must be such that a robot neither harms humans nor damages the environment. The used batteries shall be handled with care and all team members must be educated in the correct usage, charging and storage of the batteries of the team.

All robots must have an emergency stop button. The emergency stop has to be a hard stop mechanism, that ensures that the energy transfer to all actuators is stopped immediately and the robot halts. The mechanism must be a red emergency stop button that is clearly visible, easily accessible and per wire attached to the robot. It has to be easy accessible from at least 3 sides of the robot. A wireless emergency stop button is optional but not sufficient.

##### 3.2 Arena Example Environemnt

![3.png](/images/3.png "3.png")

###### 3.2.1 Floor

The floor is made of some firm material. This includes among others floors made of concrete, screed, timber, plywood, chipboard, laminated boards, linoleum, PVC flooring, or carpet.

###### 3.2.2 Virtual Walls

Virtual Walls are made of yellow/black tape and may never be crossed during a run. The arena doesn't contain Walls.

###### 3.2.3 Obstacles
###### 3.2.4 Tapes

<img src="/images/14.png" alt="7.png" width="200" />

###### 3.2.4.1 Red/white Tape:
The red/white Tape (Tesa signal 5cm width) is considered as a Virtual Wall and has an zero height. 

###### 3.2.4.2 Yellow/black Tape:
The yellow/black Tape (Tesa signal 5cm width) is considered as a Virtual Obstacles and has an infinite height. 

###### 3.2.5 Zones

We will have start/end zone in the middle and on the edge of arena. It will be several placement zones for pallets which robot has to bring them there. The receive the extra score points the pallets has to match the location id. This zones will be marked with the red/white tape.

###### 3.2.6 Arena Layout

The competition arena is a 5x5 meter clear space with barriers on its sides. It has designated starting and stacking areas. Standardized pallets are randomly scattered within the arena, each measuring 40x30 cm and labeled with localisation tags on top and sides indicatinguniqueids. Atfirsttheareaisclearandwithoutfurtherobstacles.Inthesecond challenge run, however, small obstacles with a size of up to 30x30x30cm are introduced into the area and must be avoided.

<img src="/images/Competition_A1_v0.png" alt="7.png" width="400" />


###### 3.2.7 Start and Finish


The robot's operation commences and concludes in the same square zone, strategically positioned on the arena's edge. This designated area serves as both the launching point for the robot's mission and the final destination where it returns to mark the completion of its tasks, emphasizing the significance of this singular location for both the beginning and end of the operation.

###### 3.2.8 Pallets

During the competition, there will be a maximum of six pallets, each supported by three wheels for ease of movement. The robot's task involves either pushing or pulling these pallets to sort them into predefined locations. The starting position of each pallet within the arena is determined randomly, adding an element of unpredictability to the challenge. To facilitate identification and sorting, each pallet is equipped with an April Tag on both its front and back sides. These tags contain unique IDs, enabling the robot to accurately recognize and handle the pallets according to the competition's requirements.


 |a     | b           |  c |
 |-------------|-------------------------|----------------------------|
 | <img src="/images/Wheel_PlasticBox_400х300_v2.png" alt="7.png" width="150" />         |       <img src="/images/2xWheel_PlasticBox_400х300_v2.png" alt="7.png" width="150" />                   |          <img src="/images/3xWheel_PlasticBox_400х300_v2.png" alt="7.png" width="150" />                   |

###### 3.2.9 April Tag 

April tags might be used in the competition. This should allow teams to focus on other areas than object recognition by simplifying the detection of pallets. 

The April Tags measure 40mm × 40mm and have an encoding taken from the 36h11 April Tag family, including a 1bit black and 1bit white border.

<img src="/images/15.png" alt="7.png" width="200" />

April Tags can be easy generated. The usage of any ROS package to identify the April Tag is allowed. For example the April Tag ROS package can easy be adapted to be used within the competition. Example April Tags out of the April Tag Family 36h11 are shown:

<img src="/images/16.png" alt="7.png" width="500" />

#### 4. Competition
The competition is split into two runs for each team. In the first run, the arena is free of obstacles (other than the palettes themselves). The task is for the robot to collect a palette and carry to a predefined location. 

In the second run, small obstacles are introduced into the arena and the task is to sort 4 palettes to 4 predefined locations acroding to their id. The challenge is evaluated and awarded in two categories: “Fastest Sorting” and “Overall Champion" with the latter merging both runs into a single score. Extra points are granted if the robot manages to stack pallets in order of their id.
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

<img src="/images/17.png" alt="7.png" width="500" />

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
- The emergency stop button had to be pressed before a restart call
- A team was identified to be cheating

The end of a run phase must be announced by the EC by saying ’end’. Once this happened, the
team may touch and control their robot to bring it to a full stop.

###### 4.7.3 End Phase

In the resulting end phase the team is expected to move their robot back to parc ferm´e. Referees gather and discuss their performance rating afterwards. Once they agree on the performing team’s
result, the teamleader is required to accept this score. Teams are allowed to make their case if they do not agree with the refs decision, but cannot force changes and are expected to be understanding.

Special cases will be decided by the TC if the rulebook leaves room for interpretation. Once the score has been accepted by a team, the arena must be set up for the next run if necessary.
The prep time of the next team begins once the arena state is declared as ready by all refs.

##### 4.10 Restarting a Run

During a run, the teamleader can restart the test execution once. Therefore he/she must say ’restart’, which stops the current run phase. The robot must be stopped using the emergency switches, which then allows the refs to reset the arena state. The remaining run time will be noted and used after the restart. Once the refs have finished resetting the arena, the performing team is brought back to their prep phase, which allows them to move the robot back to the start area and prepare it for the restarted run. A so called tactical call of a restart (e.g. to prevent a major collision) is allowed, because this rewards the teams knowledge about the robot. Note: When the first major collision occurs, the team can decide whether they stop the run or they restart the run

##### 4.11 Challenges
###### 4.11.1 Pallet Ordering
###### 4.11.2 Technical Challenge 
###### 4.11.3 Presentation

#### 5. Scoring and Raking
##### 5.1 Scoring
###### 5.1.1 Scores
###### 5.1.1 Penalties
###### 5.1.2 Colissions
###### 5.1.3 Restarts
##### 5.5 Ranking

#### 6. References

https://docs.olive-robotics.com
www.olive-robotics.com
www.ros.org
www.2024.ieee-icra.org









