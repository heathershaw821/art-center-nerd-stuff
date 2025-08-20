# 8-Week Robotics Curriculum (16 Sessions)

![Robot car built](images/robot.jpeg)

## Week 1: Assembly & Orientation

* **Day 1:** Build the chassis. Identify each part and what it does.
* **Day 2:** Finish building. Power test. Upload a “blink” to confirm wiring works.



---

## Week 2: Arduino Fundamentals

- **Day 1 (Code):** Intro to C. Serial basics: `Serial.print()`, Hello World, debugging. Digital output with LED blink patterns.
- **Day 2 (Robot):** Video presentation + lecture on robotics funamentals

  - [An Introduction To Robotics 🤖 By Teach Kids Robotics](https://www.youtube.com/watch?v=HvMQONnCXbE)
  - [Valkyrie: NASA's Superhero Robot](https://www.youtube.com/watch?v=IE-YBaYjbqY)


---

## Week 3: Motors & Basic Motion

- **Day 1 (Code):** HIGH/LOW digital writes, `delay()`, sequencing. Build motor control functions: `forward()`, `backward()`, `stop()`.
  - [Controlling Self Driving Cars](https://youtu.be/4Y7zG48uHRo)
- **Day 2 (Robot):** Make the robot drive forward, reverse, turn left/right using those functions.

---

## Week 4: Loops & Motion Patterns

- **Day 1 (Code):** `for` loops, `while` loops, `millis()` timing instead of delay. Practice LED sequences with loops.
- **Day 2 (Robot):** Write a robot “dance routine” — forward 2s, spin, reverse, pause. Use loops for repetition.

---

## Week 5: Inputs & Remote Control

- **Day 1 (Code):** Read IR remote signals using a library. Print codes to Serial Monitor. Introduce `if` statements.
- **Day 2 (Robot):** Remote control mode: UP = forward, DOWN = backward, LEFT = spin left, RIGHT = spin right. (Reward = they can drive their robot like an RC car).

---

## Week 6: Ultrasonic Distance Sensor

- **Day 1 (Code):** Variables & functions. Use ultrasonic sensor on breadboard first. Print distances to Serial.
- **Day 2 (Robot):** Robot drives forward until an obstacle < 20cm, then stops. Add LED warning when too close.

---

## Week 7: Conditionals & Obstacle Avoidance

- **Day 1 (Code):** Nested `if/else`. Practice with LED logic (red/green/yellow = stop/go/warning).
- **Day 2 (Robot):** Robot avoids collisions: if wall < 20cm, stop and turn. Teach **autonomy = decision-making**.

---

## Week 8: Servo & Scanning Radar

- **Day 1 (Code):** Servo basics. Sweep servo 0–180° with `for` loop. Print angle values. Combine with ultrasonic sensor to log distances. (Mini radar scanner in Serial).
- **Day 2 (Robot):** Full-featured robot: servo scans left, center, right → robot chooses best direction automatically.

  - Example: if obstacle ahead, check left vs right → turn where there’s more space.

---

# Capstone Project Week (Optional Week 9 if time allows)

- Teams design **autonomous robot demos**:
  - Maze-solving.
  - Obstacle race.
  - “Robot dance battle” (sync servo sweeps & motion).
  - Remote-vs-autonomous switch mode.
- Students present their robots, explain their code, and show creativity.

---

# Learning Outcomes

By the end, each student can:

- Assemble and wire a robot from scratch.
- Use **Arduino libraries** (Servo, IRremote, etc.).
- Write modular functions (`forward()`, `scanLeft()`, etc.).
- Implement **sensor-based autonomy** with ultrasonic + servo scanning.
- Debug and troubleshoot using Serial Monitor.
- Create a final project that’s personal and rewarding.

---

To keep it **rewarding**:

- Every session ends with something **moving or visual** (LED blink, wheel spin, sensor print, robot turning).
- Students **see the robot get smarter** each week: from blinking → moving → controlled → sensing → thinking.

