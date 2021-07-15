<p align="center">
  <img width=900 src="https://i.imgur.com/lQxRb0Q.png">
</p>

This library implements various optimal control algorithms that are particularly suited for aerospace applications.

## Guidance and Control Algorithms

 * Efficient Successive Convexification, a real-time guidance algorithm for optimal trajectory planning of constrained dynamical systems
 * Generic linear receding-horizon SOCP MPC algorithm
 * Linear Quadratic Regulator

## Features

 * JIT derivative code generation with CppAD/CppADCodegen
 * Intuitive interface to implement custom models
 * Rapid iteration with parameters files
 

## Current Models

 * 2D Rocket Model
 * Rocket Landing Model with Quaternion
 * Rocket Landing Model with Euler Angles

## Instructions

### Install

Replace `E:\Code` with wherever you want to download the files below.
```
cd E:\Code
git clone https://github.com/Zentrik/SCpp
cd docker
docker build . -t scpp
docker run -it -v E:\Code\SCpp:/home/SCpp scpp:latest
cd SCpp
mkdir build
cd build
cmake ..
make
```

If you are using wsl2 I would suggest doing the below instead to improve speed significantly by not using the windows file system.
```
cd E:\Code
git clone https://github.com/Zentrik/SCpp
cd docker
docker build . -t scpp
docker run -it -v E:\Code\SCpp:/home/SCpp scpp:latest
mkdir local
cd /home/SCpp
mkdir build
tar cf - --exclude=evaluation --exclude=.git . | (cd /home/local && tar xvf - )
cd /home/local/build
cmake ..
make
rm -rf /home/SCpp/build/*
cp -r * /home/SCpp/build/
cd /home/SCpp/build/
```
Then run the executable, e.g. `./sc_oneshot`

To get 3d video, open the .blend file in blender and render it. For `starship sc_tracking.blend`, use Camera.002 to track the rocket and Camera.001 to have a stationary camera. If you change the code to `body_ob.location = x[1:4] / 100` you can use Camera (it is also stationary).
`animate_landing.blend` and `landingVisualisation.blend` are from https://github.com/EmbersArc/SuccessiveConvexificationFreeFinalTime, only included so you don't have to go look into the history of that repo to find them. The trajectory files from that repo are included so you can test the blend files and `model_6dof_plot.py`.
Using `animate_landing.blend` and `landingVisualisation.blend` I have added falcon 9 blend files, the v1 is a white falcon 9, whilst the other has the black rings later Falcon 9 versions have.

To plot trajectories, numpy, matplotlib and mpl_toolkits may need to be installed, then just run the file e.g. `python plot_rocket2d.py`. If you get python errors about file not being found make sure you are in E:\Code\Scpp when running the python command.

To change which model is used (3d/quaternion vs 2d) edit scpp_core/include/activeModel.hpp
To change which method is used (lqr vs sc_oneshot ...) edit CMakeLists.txt

If `CMake Error: The current CMakeCache.txt directory /home/SCpp/build/CMakeCache.txt is different than the directory /home/build where CMakeCache.txt was created.` then search for all CMakeCache.txt and in SCpp and delete all. Command to do this is `find . -name "CMakeCache.txt" -delete`, make sure you are in build directory when you do this.

X is [mass, position, velocity, quaternion, angular velocity] (https://github.com/EmbersArc/SCpp/blob/master/scpp_models/src/rocketQuat.cpp#L20).

U is [Thrust, roll_torque] (https://github.com/EmbersArc/SCpp/blob/master/scpp_models/src/rocketQuat.cpp#L27).
### Run

Available executables are:

* **LQR_sim** to simulate a trajectory with the classic MPC controller
                
    This didn't work with RocketQuat either for me.

* **MPC_sim** to simulate a trajectory with the classic MPC controller

  I don't think this can be used with RocketQuat as scpp_models/config/RocketQuat/MPC.info is nonexistent.

* **SC_oneshot** to calculate one trajectory with Successive Convexification

* **SC_sim** to simulate a trajectory with Successive Convexification

Calculated trajectories are written to the `output/<modelname>` directory.

### Create a Custom Model

See existing models in the `socp_models` folder for some examples.

## Papers

* [Successive Convexification: A Superlinearly Convergent Algorithm for Non-convex Optimal Control Problems](https://arxiv.org/abs/1804.06539)

* [Successive Convexification for 6-DoF Mars Rocket Powered Landing with Free-Final-Time](https://arxiv.org/abs/1802.03827)

## Examples

(click on videos for higher quality versions)

### Rocket Trajectory Model with Free-Final-Time

<p align="center">
<a href="https://thumbs.gfycat.com/DeliriousCandidAldabratortoise-mobile.mp4">
  <img width="400" src="https://thumbs.gfycat.com/DeliriousCandidAldabratortoise-size_restricted.gif">
</a>
</p>

### SpaceX Starship Landing Trajectory

<p align="center">
<a href="https://giant.gfycat.com/RecklessBountifulKillifish.webm">
  <img width="400" src="https://thumbs.gfycat.com/RecklessBountifulKillifish-small.gif">
</a>
</p>
<p align="center">
  <img width="400" src="https://user-images.githubusercontent.com/1352472/66057427-f736be00-e538-11e9-8078-727282910f54.png">
</p>

### My SpaceX Starship Landing Trajectory using sc_tracking

<p align="center">
<a href="https://giant.gfycat.com/WelltodoCoarseBird.mp4">
  <img width="400" src="https://thumbs.gfycat.com/WelltodoCoarseBird-size_restricted.gif">
</a>
</p>

<p align="center">
<a href="https://giant.gfycat.com/nimblezanydairycow.mp4"> <!--  High res, when you upload a file you get a link gfycat.com/slimydistantgoldfish, go to gfycat.com/slimydistantgoldfish.gif inspect the video and you will see two link the giant .mp4 and the thumbs .gif. Alternatively just replace slimydistantgoldfish with your one. -->
  <img width="400" src="https://thumbs.gfycat.com/nimblezanydairycow-size_restricted.gif"> <!--  Low res -->
</a>
</p>

### 2D Rocket Landing Problem

feed-forward input tested in a box2d physics simulation

<p align="center">
<a href="https://thumbs.gfycat.com/DaringPortlyBlacklab-mobile.mp4">
  <img width="400" src="https://thumbs.gfycat.com/DaringPortlyBlacklab-small.gif">
</a>
</p>

### Cartpole

<p align="center">
<a href="https://thumbs.gfycat.com/KnobbyFlatCanvasback-mobile.mp4">
  <img src="https://thumbs.gfycat.com/KnobbyFlatCanvasback-small.gif">
</a>
</p>

## Contributing

I'm looking forward to contributions, both problem formulations and improvements to the core library.
