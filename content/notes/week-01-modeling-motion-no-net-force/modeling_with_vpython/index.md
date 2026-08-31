---
title: "Modeling Motion with VPython"
weight: 3
textbook_ref: "Section 1.7 and 1.11 in Matter and Interactions (4th edition)"
---

There is a restricted class of motion that can be modeled or explained with analytical tools (i.e., algebra and calculus). Most modern scientific research (and, indeed, engineering work) uses computational modeling as a significant part of the scientific endeavor. VPython is a Python-based programming language that allows you to create short programs that model the motion of physical systems. **In these notes, you will read about how to write your programs so that they follow a common structure, which will make it easier to write new programs in the future.** You will develop these computational models in class with the help of your classmates and the guidance of instructors.

## Lecture Video

{{< youtube vzof--LEJw4 >}}

## Structuring your programs

Below is the code that was written in the lecture video above. There are 4 major components to this code that you will repeat in each program that you write:

1.  **Objects** - Each program that you write is modeling the motion of some physical objects. So you will need to set up and place those objects in the scene. A big list of objects is [available online](http://vpython.org/contents/docs/primitives.html).
2.  **Parameters & Initial Conditions** - Each program will have associated physical quantities for one or more of the objects in the scene. These might be the object's mass, velocity, momentum, etc. The selection of these parameters and initial conditions depends on the problem you are trying to solve (and are often informed by analytical calculations).
3.  **Time conditions** - The initial time and time step are needed in each program. The time step is particularly important because it controls how often the calculations occur. Typically, [the more frequent the calculations are, the more accurate the solutions will be](/notes/week-04-05-springs-contact-interactions/springmotion/#modeling_motion_with_spring_forces). But there's a tradeoff; the computer has to do more calculations – making the program take longer to run.
4.  **Calculation loop** - Your job in mechanics is to predict or explain the motion of systems and the calculation loop is where that happens. In the loop is where the [iterative prediction of motion](/notes/week-02-modeling-motion-net-force/iterativepredict/) really plays out. In any calculation loop you will,
    - [Calculate all the forces acting on the system, and determine the net force.](/notes/week-02-modeling-motion-net-force/momentum_principle/#net_force)
    - [Update the momentum using this net force.](/notes/week-02-modeling-motion-net-force/motionpredict/)
    - [Update the position using this new momentum (velocity).](/notes/week-01-modeling-motion-no-net-force/displacement_and_velocity/#predicting_the_motion_of_objects)

Note that in this example, the cart was moving at constant velocity, so we didn't need to do much step 4 above. In future weeks, there will be examples of how to use Glowscript to model motion when there is nonzero net force.

<div class="Definition-Term">

[videoexample.py](https://msuperl.org/wikis/pcubed/doku.php?do=export_code&id=183_notes:modeling_with_vpython&codeblock=0)

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
