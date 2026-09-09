---
title: 'Modeling Motion with VPython'
weight: 3
textbook_ref: 'Reference: Sections 1.7 and 1.11 in Matter and Interactions (4th edition)'
---

Relatively simple types of motion can be analyzed using analytic tools – algebra and calculus – but applying them to more complicated (realistic) situations rapidly becomes quite difficult. Most modern scientific and engineering work uses computational models extensively for all but the simplest problems, and in this course we will see how those computational models are built up from the analytic tools.

Glowscript is a VPython-based programming package that allows you to create short programs that model the motion of physical systems. **In these notes, you will read about how to write your programs so that they follow a common structure, which will make it easier to write new programs in the future.** You will develop these computational models in class with the help of your classmates and the guidance of instructors over the course of the semester.

## Lecture Video

{{< youtube vzof--LEJw4 >}}

# Structuring Your Programs

Below is the code that was written in the lecture video above. There are 4 major pieces to this code that you will need to include in each program that you write:

1.  **Creating Objects** - Each program that you write is modeling the motion of some physical objects. First, you need to set up these objects and place them in the scene. A big list of objects is [available online](http://vpython.org/contents/docs/primitives.html).
2.  **Parameters & Initial Conditions** - Each program will have associated physical quantities for one or more of the objects in the scene, such as the object's mass, initial position, velocity, or momentum. The values of these parameters and initial conditions depends on the problem you are trying to solve (and are often informed by analytical calculations). Note that we only set the *initial* conditions by hand, we don’t try to tell the computer what the final conditions will be. The point of the code is to have the computer do the work of figuring out what will happen.
3.  **Time Conditions** – Our programs will model what happens to the objects based on the initial conditions and physical principles. We’ll set an initial (starting) time and a *time step* in each program. The time step is the size of the time interval $\Delta t$ the computer uses for its calculations: internally, the computer model assumes everything about the system is constant over that time interval, and only updates positions, velocities, etc. at the end of the time step (like the frame rate in a video game).
4.  **Calculation Loop** – This is where the computer actually predicts what happens to the system as time goes by: an [iterative prediction of motion](/notes/week-02-modeling-motion-net-force/iterativepredict/). In general, in a calculation loop you will
    - [Calculate all the forces acting on the system, and determine the net force.](/notes/week-02-modeling-motion-net-force/momentum_principle/#net-force)
    - [Update the momentum using this net force.](/notes/week-02-modeling-motion-net-force/motionpredict/)
    - [Update the position using this new momentum (velocity).](/notes/week-01-modeling-motion-no-net-force/displacement_and_velocity/#predicting-the-motion-of-objects)

It’s worth emphasizing the fundamental approximation behind this method: we assume the force, momentum, and velocity are constant within each time step $\Delta t$, then instantly change to new values at the end of the time step. Typically, [the shorter the time step, the more accurate the solutions will be](/notes/week-04-05-springs-contact-interactions/springmotion/#modeling-motion-with-spring-forces), since values are updated more frequently and the computer “follows” the motion more closely. But there's a tradeoff; the computer has to do more calculations, making the program slower.

Note that in this example, the cart was moving at constant velocity, so we didn't need to do much in step 4 – not much actually got updated in each step through the loop. In future weeks, there will be examples of how to use Glowscript to model motion when the net force is not zero.

<div class="Definition-Term">

videoexample.py (you can copy this code into Glowscript if you want to run it yourself)

</div>

    Web VPython 3.2

    # object setup 
    road = box(pos = vec(0,0,0), size = vec(10,0.5,1))
    cart = box(pos = vec(-4,0.5,0), size = vec(1,1,0.9), color = color.red, velocity = vec(0,0,0))

    # parameters and initial conditions
    cart.velocity = vec(5,0,0) # m/s

    # time setup 
    t = 0
    dt = 0.01
    tf = 2

    # loop to do physics
    while cart.pos.x < 4:
        rate(100)
        cart.pos = cart.pos + cart.velocity*dt

        t = t + dt
    print('t = ', t, 's')
