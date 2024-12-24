# roller-coaster-simulator
by Max Yenlee & Raven (Ruiwen) Tang

Hello!!! You may access our project [here]([https://glowscript.org/#/user/mavenphysics/folder/MyPrograms/program/FinalProject]). You can find our source code within this repository, in the code.py file.

Our project models a rollercoaster with the following components:
    1. An initial fricitionless downward ramp (at an angle of 45 degrees)
    2. A flat fricitonless track
    3. A frictionless circular loop
    4. A frictional flat track
    
We aim to demonstrate conservation of energy and friction.

Here are a few important physical things about our project:
    1. Air resistance is ignored.
    2. The cart is bolted/attached to the track, meaning it will not fall off 
        the track if it runs out of kinetic energy on its way up the loop. 
        Instead, it will simply progress back down the loop.
    3. We incorporated 3-dimensionality into our model. As such, the loop does 
        not end and begin at the same z-coordinate, and the cart progresses in 
        the z-direction during its time on the loop.
    4. The cart appears to be "in" the track, because creating an offset that 
        places the cart exactly on the surface messes with the potential energy. 
        We felt that it would be more physically accurate if the cart's motion 
        was modeled correctly, so we chose to prioritize the energy behavior of 
        our simulation over a visual offset.

How to use our program!
    The following sliders are included for the user to control:
        1. Length of initial frictionless ramp (from 5 m to 100 m)
        2. Radius of circular frictionless loop (from 1 m to 20 m)
        3. Acceleration due to gravity (from 1 m/s^2 to 20 m/s^2)
        4. Mass of cart (from 1 kg to 10 kg)
        5. Friction coefficient for last flat part (from 0.5 to 0.9)
    After beginning the program, the user can adjust the sliders and then press 
    the start button to see the cart begin its journey down the track. At this
    time, the start button will switch to a pause button. At any time, the user 
    can press this pause button to freeze the current frame. The pause button 
    will switch to a start button, which will start the animation from the 
    beginning. The user can also interact with the reset button, which will 
    only be available if the animation is paused. The reset button will bring
    the animation back to its default measurements:
        1. Length of initial frictionless ramp = 50 m
        2. Radius of circular frictionless loop = 10 m
        3. Acceleration due to gravity = 9.8 m/s^2
        4. Mass of cart = 1 kg
        5. Friction coefficient of last flat part = 0.9
    The sliders can only be modified in 2 situations: 1) before the start button 
    is pressed for the first time, and 2) when the simulation has been reset.
    Enjoy the graphs displaying kinetic, potential, and total energy of the cart!
