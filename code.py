Web VPython 3.2

#creates graphs for energy
scene = canvas(align="left")
gd = graph(align = "right", title='<b>Energy Plots</b>',
      xtitle='<i>Time (s)</i>', ytitle='<i>Energy (J)</i>',
      xmin=0, ymin=0)
kinetic_graph = gcurve(color=color.blue,label="kinetic energy (J)") # kinetic energy graph
potential_graph = gcurve(color = color.green, label = "potential energy (J)") #potential energy graph
total_energy_graph = gcurve(color = color.purple, label = "total energy (J)") #total energy graph

#user-controllable variables
dlength = 50 #range: 5 m -100 m, length of inital downward ramp
rad = 10 #range: 1 m - 20 m, radius of loop
g = 9.8 #range: 1 m/s^2 - 20 m/s^2, gravity
m = 1 #range: 1 kg - 10 kg, mass
mew = 0.9 #range: 0.5-0.9

#helpful value to store
corva = dlength/2/sqrt(2) #CORVA CORVA

#creates visual components of track
initial_ramp = box(size = vector(dlength, 0.1, 3), pos = vector(0, 0, 0)) #creates horizontal box
initial_ramp.rotate(angle = -pi/4, axis = vector(0, 0, 1)) #rotates so it is downward sloping
flat_connector = box(size = vector(20, 0.1, 3), pos = vector(corva+10, -corva, 0)) #creates horizontal slope connecting loop to inital ramp

#creates 3 arcs so it looks like the curve is helixy (moving in the z direction)
loop1 = shapes.arc(angle1 = -pi/2, angle2 = pi/2, radius = rad)
loop1ex = extrusion(path = [vec(corva + 20, -corva + rad, 1.5), vec(corva + 20, -corva + rad, 0.5)], shape = loop1, color = color.red) #extrusion of semicircle

loop2 = shapes.arc(angle1 = pi/2, angle2 = -pi/2, radius = rad)
loop2ex = extrusion(path = [vec(corva + 20, -corva + rad, -1.5), vec(corva + 20, -corva + rad, -0.5)], shape = loop2, color = color.red) #extrusion of semicircle

loop3 = shapes.circle(radius = rad, thickness = 0.001)
loop3ex = extrusion(path = [vec(corva + 20, -corva + rad, -0.5), vec(corva + 20, -corva + rad, 0.5)], shape = loop3, color = color.blue) #extrusion of circle

#sets up visible frictional path
friction_length = 200
friction = box(size = vector(friction_length, 0.1, 3), pos = vec(corva + 20 + (friction_length/2), -corva, 0), color = color.yellow)

#create cart, and rotate it so it lines up with track
cart = box(size = vector(2, 2, 1),pos = vector(-corva, corva, 0.5), color = color.red, mass = m) #attribute of mass
cart.rotate(angle = -pi/4, axis = vector(0, 0, 1))

zoom = 50 #sets initial camera zoom
scene.range = zoom

sliders = [] #create slider array
wts = [] #create text array (to correspond with sliders)

#sets up sliders (default values, steps, ranges)
sliders.append(slider(length=300, left=10, bind = settings, min=5, max = 100, value = 50, step = 5, id = 0)) #adds dlength slider
wts.append(wtext(text=sliders[0].value + ' m [Length of Initial Frictionless Ramp] \n')) #dlength caption
sliders.append(slider(length=300, left=10, bind = settings, min=1, max = 20, value = 10, step = 1, id = 1)) #adds radius slider
wts.append(wtext(text=sliders[1].value + ' m [Radius of Circular Frictionless Loop] \n')) #radius caption
sliders.append(slider(length=300, left=10, bind = settings, min=1, max = 20, step = 0.1, value=9.8)) #adds gravity slider
wts.append(wtext(text=sliders[2].value + ' m/s^2 [Acceleration Due to Gravity]: \n Interesting gravitys to explore (m/s^2) \n Earth: 9.8, Moon: 1.6, Mars: 3.7, Venus: 8.9, Saturn: 11.1, Uranus: 10.7, Neptune: 14.1 \n')) #gravity caption
sliders.append(slider(length=300, left=10, bind = settings, min=1, max = 10, value = 1, step = 0.5, id = 3)) #adds mass slider
wts.append(wtext(text=sliders[3].value + ' kg [Mass of Cart] \n')) #mass caption
sliders.append(slider(length=300, left=10, bind = settings, min=0.5, max=0.9, value = 0.9, step = 0.1, id = 4)) #adds mew slider
wts.append(wtext(text=sliders[4].value + ' [Friction Coefficient of Flat Track After Loop] \n')) #friction coefficient

running = False #is the program running? at the beginning, no

def Run(b):
    global running
    running = not running #switch the running var to the opposite of whatever it currently is
    if running: 
        st.text = 'pause' #button now shows pause if we pressed run
        rs.disabled = True
        cart.axis = vec(-2,2,0)
        kinetic_graph.delete()
        potential_graph.delete()
        total_energy_graph.delete()
        for i in range(5):
            sliders[i].disabled = True #stops the sliders from being edited in the middle
    else: 
        st.text = 'run (from beginning)' #button now shows run if we pressed pause
        rs.disabled = False
        if time is 0: #not sure if lines 67-69 are doing anything, but we are scared to delete bc too many things have broken already
            for i in range(5):
                sliders[i].disabled = False #allows the sliders to be edited
    
st = button(bind=Run, text='run (from beginning)') #run/pause button

def Reset(c):
    kinetic_graph.delete()
    potential_graph.delete()
    total_energy_graph.delete()
    if running:
        Run(st) #execute the button (b/c we need to pause if we want to reset)
    for i in range(5):
        sliders[i].disabled = False #allows the sliders to be edited
    global time, dlength, rad, g, m, corva, mew #make sure we're referencing the GLOBAL variables
    cart.axis = vec(-2,2,0)
    time = 0 #start time at 0 again
    dlength = 50 #range: 5 m - 100 m, length of inital downward ramp
    rad = 10 #range: 1 m - 20 m, radius of loop
    g = 9.8 #range: 1 m/s^2 - 20 m/s^2, gravity
    m = 1 #range: 1 kg - 10 kg, mass
    mew = 0.9 #range: 0.5 - 0.9, mew
    corva = dlength/2/sqrt(2) #CORVA CORVA
    #update sliders to indicate default values again
    sliders[0].value = dlength
    sliders[1].value = rad
    sliders[2].value = g
    sliders[3].value = m
    sliders[4].value = mew
    wts[0].text = sliders[0].value + ' m [Length of Initial Frictionless Ramp] \n'
    wts[1].text = sliders[1].value + ' m [Radius of Circular Frictionless Loop] \n'
    wts[2].text = sliders[2].value + ' m/s^2 [Acceleration Due to Gravity]: \n Interesting gravitys to explore (m/s^2) \n Earth: 9.8, Moon: 1.6, Mars: 3.7, Venus: 8.9, Saturn: 11.1, Uranus: 10.7, Neptune: 14.1 \n'
    wts[3].text = sliders[3].value + ' kg [Mass of Cart] \n'
    wts[4].text = sliders[4].value + ' [Friction Coefficient of Flat Track After Loop] \n'
    
    initial_ramp.size = vector(dlength, 0.1, 3) #update size of ramp based on sliders
    flat_connector.pos = vector(corva+10, -corva, 0) #update position of flat part based on sliders
    
    #update positions and sizes of loop extrusions based on sliders
    loop1ex.pos = vec(corva + 20 + rad/2, -corva + rad, 1)
    loop1ex.size = vec(rad, 2*rad, 1)

    loop2ex.pos = vec(corva + 20 - rad/2, -corva + rad, -1)
    loop2ex.size = vec(rad, 2*rad, 1)
    
    loop3ex.pos = vec(corva + 20, -corva + rad, 0)
    loop3ex.size = vec(2*rad, 2*rad, 1)
    
    #update position of frictional part based on sliders
    friction.pos = vec(corva + 20 + (friction_length/2), -corva, 0)
    
    #update position and mass of cart
    cart.pos = vec(-corva,corva,0.5)
    cart.mass = m

rs = button(bind = Reset, text = 'reset') #reset button

def settings(sl): #function to assign variables using slider information
    #keep the slider values updated
    wts[0].text = sliders[0].value + ' m [Length of Initial Frictionless Ramp] \n' 
    wts[1].text = sliders[1].value + ' m [Radius of Circular Frictionless Loop] \n'
    wts[2].text = sliders[2].value + ' m/s^2 [Acceleration Due to Gravity]: \n Interesting gravitys to explore (m/s^2) \n Earth: 9.8, Moon: 1.6, Mars: 3.7, Venus: 8.9, Saturn: 11.1, Uranus: 10.7, Neptune: 14.1 \n'
    wts[3].text = sliders[3].value + ' kg [Mass of Cart] \n'
    wts[4].text = sliders[4].value + ' [Friction Coefficient of Flat Track After Loop] \n'
    
    #assigning values
    dlength = sliders[0].value 
    rad = sliders[1].value
    g = sliders[2].value
    m = sliders[3].value
    mew = sliders[4].value
    corva = dlength/2/sqrt(2) #redefine corva
    #print("old corva " + corva) #CORVA CORVA

    #update sizes and positions of track components based on sliders
    initial_ramp.size = vector(dlength, 0.1, 3) 
    flat_connector.pos = vector(corva+10, -corva, 0) 
    
    loop1ex.pos = vec(corva + 20 + rad/2, -corva + rad, 1)
    loop1ex.size = vec(rad, 2*rad, 1)

    loop2ex.pos = vec(corva + 20 - rad/2, -corva + rad, -1)
    loop2ex.size = vec(rad, 2*rad, 1)
    
    loop3ex.pos = vec(corva + 20, -corva + rad, 0)
    loop3ex.size = vec(2*rad, 2*rad, 1)

    friction.pos = vec(corva + 20 + (friction_length/2), -corva, 0)

    #update position and mass of cart based on sliders
    cart.pos = vector(-corva, corva, 0.5)
    cart.mass = m

while True: #constantly checking
    rate(100)
    if running: #only run the simulation if the running boolean is true
        
        #updating values based on sliders
        dlength = sliders[0].value
        rad = sliders[1].value
        g = sliders[2].value
        m = sliders[3].value
        mew = sliders[4].value
        corva = dlength/2/sqrt(2) 
            
        #camera stuff
        zoom = 50 #sets zoom
        scene.camera.follow(cart)
        scene.range = zoom
        scene.camera.axis = vector(-zoom / 2,0,-zoom)
        
        #setting up variables 
        time = 0 #time
        dt = 0.01 #time change
        K = 0 #don't know if we actually use this variable later, but we'll keep it in just in case everything falls apart
        U_max = (corva*2) * cart.mass * g #total energy
        init_cart_y = cart.pos.y #store the current height of the cart so we can check later if potential energy is high enough
        U_current = corva*2 * cart.mass * g #initialize potential energy
        K_current = 0 #initialize kinetic energy
        biggest_velocity = sqrt(dlength / sqrt(2) * 2 * g) #biggest velocity
        startrotatetime = 0.2 #variable used to create the slow rotation thingy
        
        #PART 1
        #on the downward ramp
        
        while(running and time >= 0 and time <= sqrt(2 * dlength / sqrt(2) / g)): #while the cart is on the downward ramp
            rate(100)

            if time >= sqrt(2 * dlength / sqrt(2) / g) - startrotatetime: #while the cart is near the change to the flat part, start to rotate a little
                cart.rotate(angle = (pi / 8) / (100 * startrotatetime), axis = vector(0, 0, 1)) 
            cart.pos.y = corva + 0.5 * -g * time * time #change y position (based on kinematics)
            cart.pos.x = -corva + 0.5 * g * time * time #change x position
            U_current = (cart.pos.y + corva) * cart.mass * g # update potential energy
            K_current = U_max - U_current #update kinetic energy
            
            #updating plots on graph
            kinetic_graph.plot(time, K_current)
            potential_graph.plot(time, U_current)
            total_energy_graph.plot(time, K_current + U_current)
            
            time += dt
        time1 = time #saves time that it ends at           
        
        #on the first flat part
        vx = sqrt(2 * g * dlength / sqrt(2)) #define x velocity (since there is no y movement while on the flat part)
        while(running and time >= sqrt(2 * dlength / sqrt(2) / g) and time <= 20 / vx + time1): #while on the horizontal track
            rate(100)
            cart.pos.y = -corva #correct for any small offset (due to dt value) to make sure the cart is centered on the track
            if time <= sqrt(2 * dlength / sqrt(2) / g) + startrotatetime: #while near the change btw ramp and flat part, rotate the rest so it is flat
                cart.rotate(angle = (pi / 8) / ( 100 * startrotatetime), axis = vector(0, 0, 1))    
            cart.pos.x = corva + vx * (time - time1) #change x position, constant velocity because track is frictionless here

            U_current = (cart.pos.y + corva) * m * g # update potential energy
            K_current = U_max - U_current #update kinetic energy
            
            #update graphs
            kinetic_graph.plot(time, K_current)
            potential_graph.plot(time, U_current)
            total_energy_graph.plot(time, K_current + U_current)
            
            time += dt
            
        time2 = time #saves time that it ends at
        CCW = True #boolean is true if cart will fully make it around the loop, assume it's true at the beginning
        anglesavething = 0 #shhh it works
        #ON LOOP
        while(running and time >= time2 and CCW):
            rate(100)
            total_velocity = sqrt(K_current * 2 / cart.mass) #obtain the velocity from the kinetic energy
            cartx = cart.pos.x #why did we do this? we could have just used cart.pos.x by itself... :)))
            carty = cart.pos.y
            
            #store the center of the loop
            centerx = corva + 20 
            centery = -corva + rad
            
            if(abs(centerx - cartx) < 0.001): #edge case where the cart is only going in the x direction
                cart.pos.x = centerx
                if(centery > carty): #bottom of loop
                    cart.velocity = vec(total_velocity, 0, 0) 
                else: #top of loop
                    cart.velocity = vec(-total_velocity, 0, 0)
                cart.pos.x += cart.velocity.x * dt
                cart.pos.y += cart.velocity.y * dt
            elif(centery - carty < 0.001 and centery - carty > -0.001): #edge case where the cart is only going in the y direction
                cart.pos.y = centery
                cart.velocity = vec(0, total_velocity, 0)
                cart.pos.x += cart.velocity.x * dt
                cart.pos.y += cart.velocity.y * dt
            else: #all non-edge cases
                slope = (centery - cart.pos.y) / (centerx - cart.pos.x) #slope between center of loop and cart's position
                slope = -1 / slope #slope now stores the slope of the velocity
                if(carty < centery): #if cart is in the bottom half of the loop, cart should be moving to the right
                    cart.velocity = vec(cos(atan(slope)) * total_velocity, sin(atan(slope)) * total_velocity, 0)
                    cart.pos.x += cart.velocity.x * dt
                else: #if cart is in the top half of the loop, cart should be moving to the left
                    cart.velocity = vec(cos(atan(slope)) * total_velocity, -sin(atan(slope)) * total_velocity, 0)
                    cart.pos.x -= cart.velocity.x * dt
                if(cartx > centerx): #if cart is in the right half of the loop, cart should be moving upwards
                    cart.pos.y += cart.velocity.y * dt
                    cart.velocity = vec(cos(atan(slope)) * total_velocity, sin(atan(slope)) * total_velocity, 0)
                else: #if cart is in the left half of the loop, cart should be moving downwards
                    cart.pos.y += cart.velocity.y * dt
                    cart.velocity = vec(cos(atan(slope)) * total_velocity, sin(atan(slope)) * total_velocity, 0)
           
            #rotate the cart so that it goes along the track
            cart.rotate(angle = -anglesavething, axis=vector(0,0,1))
            cart.rotate(angle = atan(slope), axis=vector(0,0,1))
            anglesavething = atan(slope)
            
            #move the cart in the z-direction
            Zfactor = abs(total_velocity / biggest_velocity)
            if cart.pos.x >= centerx:
                cart.pos.z = -1 + 1.5*Zfactor
            else:
                cart.pos.z = 1 - 1.5* Zfactor  
                
            #if the cart is beginning to slow down
            if abs(total_velocity) < 1 and cart.pos.y > -corva + 0.5:
                CCW = False #the cart needs to start reversing
                break #break out of this while loop
            
            #if the cart is at the bottom of the loop and near the biggest velocity, it means we've completed a loop, so BREAK!
            if cart.pos.z + 0.5 < 0.01 and abs(total_velocity - biggest_velocity) < 0.5:
                break

            U_current = (cart.pos.y + corva) * m * g # update potential energy
            K_current = U_max - U_current #update kinetic energy
            #update graphs
            kinetic_graph.plot(time, K_current)
            potential_graph.plot(time, U_current)
            total_energy_graph.plot(time, K_current + U_current)

            time += dt
        time3 = time #store the time it stops at
        time += dt #move the time a little
        
        if(running and CCW is False and time >= time3): #if the cart can't make it around the loop, it goes here
            time += dt #move the time a little
            DirectionRight = False #at the beginning, the cart moves to the left
            ramptoflat = False #the cart will not go from ramp to flat yet
            flattoramp = True #the cart WILL go from flat to ramp first
            while(running and time >= time3):
                rate(100)
                if running and corva <= cart.pos.x and cart.pos.x < centerx: #if the cart is on the flat part
                    vx = sqrt(U_max * 2 / cart.mass) #x velocity
                    cart.pos.y = -corva #correct the y position to make sure imprecision caused by dt doesn't accumulate
                    if running and flattoramp and abs(cart.pos.x-corva) < 0.4 and DirectionRight is False: #if the cart is going to go from flat to ramp, AND it's going to the left, AND it's getting close to the bottom of the ramp
                        cart.rotate(angle = -2*pi/8, axis = vector(0,0,1)) #rotate the cart to align with the ramp
                        cart.pos.y = -corva + 0.1 #bump the cart a little upwards
                        cart.pos.x = corva - 0.1 #bump the cart a little leftwards
                        #print("going flat to ramp!!!")
                        #switch the booleans, because the cart is now preparing to go ramp to flat
                        flattoramp = False
                        ramptoflat = True
                    if running and DirectionRight: #if the cart is going to the right, just keep it going to the right
                        cart.pos.x += vx * dt
                    else: #keep cart going to the left if it's going to the left
                        cart.pos.x -= vx * dt
                    time4 = time 
                elif running and ramptoflat and cart.pos.y > -corva: #if the cart is on the ramp
                    vx -= g * dt
                    cart.pos.y += (vx - g * dt)*dt #change y and x based on kinematics
                    cart.pos.x -= (vx - g * dt)*dt
        
                    if running and ramptoflat and abs(cart.pos.x-corva) < 0.1 and DirectionRight: #if the cart is prepared to go from ramp to flat AND it's getting close to the flat part AND it's going to the right
                        cart.rotate(angle = 2*pi/8, axis = vector(0,0,1)) #rotate the cart
                        cart.pos.y -= 0.1 #give cart a little bump downwards
                        cart.pos.x += 0.1 #little bump rightwards
                        #switch the booleans, because the cart is now preparing to go flat to ramp
                        ramptoflat = False
                        flattoramp = True
                    DirectionRight = True
                    
                elif running and cart.pos.x >= centerx: #if the cart is on the loop
                    slope = (centery - cart.pos.y) / (centerx - cart.pos.x) #slope between center of loop and cart's position
                    slope = -1 / slope #perpendicular of slope
                    #rotate cart so it goes with the loop
                    cart.rotate(angle = -anglesavething, axis=vector(0,0,1))
                    cart.rotate(angle = atan(slope), axis=vector(0,0,1))
                    anglesavething = atan(slope)
                    
                    total_velocity = sqrt(K_current * 2 / cart.mass) #get total velocity from kinetic energy
                    if DirectionRight: #if the cart is going up
                        cart.velocity = vec(cos(atan(slope)) * total_velocity, sin(atan(slope)) * total_velocity, 0)
                        if(cart.pos.y > centery): #if the cart is in the top half, it comes back down
                            cart.pos.x -= cart.velocity.x * dt
                            cart.pos.y -= cart.velocity.y * dt
                        else: #keep going up
                            cart.pos.x += cart.velocity.x * dt
                            cart.pos.y += cart.velocity.y * dt
        
                        if abs(cart.pos.y - init_cart_y) < 0.3: #if the cart is getting close to its original height, it doesn't go in that direction anymore
                            DirectionRight = False
                    else: #if the cart is going down
                        cart.velocity = vec(cos(atan(slope)) * total_velocity, sin(atan(slope)) * total_velocity, 0)
                        if(cart.pos.y > centery):  
                            cart.pos.x += cart.velocity.x * dt
                            cart.pos.y += cart.velocity.y * dt
                            
                        else:
                            cart.pos.x -= cart.velocity.x * dt
                            cart.pos.y -= cart.velocity.y * dt
                            
                U_current = (cart.pos.y + corva) * m * g # update potential energy
                K_current = U_max - U_current #update kinetic energy
                
                #update graphs
                kinetic_graph.plot(time, K_current)
                potential_graph.plot(time, U_current)
                total_energy_graph.plot(time, K_current + U_current)
                
                time += dt
                
        #friction part
        else:
            if(running):
                cart.rotate(angle = -anglesavething, axis=vector(0,0,1)) 
                timewow = time #smart variable naming
                time += dt
                mew = 0.9 #friction coefficient (MEOW)
                cart.pos.y = -corva #correct the y so that imprecision doesn't accumulate
                total_velocity = sqrt(K_current * 2 / cart.mass) #obtain velocity from kinetic
                while time > timewow:
                    rate(100)
                    total_velocity += (-m * g * mew) * dt #calculate velocity, derivative of position
                    cart.pos.x += total_velocity * dt
                    U_current = (cart.pos.y + corva) * m * g # update potential energy
                    K_current = 0.5 * cart.mass * total_velocity * total_velocity #update kinetic energy
                    #update graphs
                    kinetic_graph.plot(time, K_current)
                    potential_graph.plot(time, U_current)
                    total_energy_graph.plot(time, K_current + U_current)
                    time += dt
                    if abs(total_velocity) < 3: #once cart is REALLY slow, stop!!!
                        Run(st)
                        break
