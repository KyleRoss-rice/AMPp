## Build
1. Pull Singularity container 

`singularity pull library://kyleross/default/ampp:0.1`

2. Clone repo

3. Shell into container
`singularity shell ampp_0.1.sif`

4. cd into `src` directory from cloned repo
`cd src`

5. build C++ library and Python wrapper
`make python`

This also creates a `DeepMimic.py` in the root directory of the project.
This file is used for running simulations. `mpi_run.py` is used for training.

## How to Use
Once the python wrapper has been built, training is done entirely in python using Tensorflow.
`DeepMimic.py` runs the visualizer used to view the simulation. Training is done with `mpi_run.py`, 
which uses MPI to parallelize training across multiple processes.

`DeepMimic.py` is run by specifying an argument file that provides the configurations for a scene.
For example,
```
python DeepMimic.py --arg_file args/run_humanoid3d_spinkick_args.txt
```

will run a pre-trained policy for a spinkick. Similarly,
```
python DeepMimic.py --arg_file args/play_motion_humanoid3d_args.txt
```

will load and play a mocap clip. To run a pre-trained policy for a simulated dog, use this command
```
python DeepMimic.py --arg_file args/run_dog3d_pace_args.txt
```

To train a policy, use `mpi_run.py` by specifying an argument file and the number of worker processes.
For example,
```
python mpi_run.py --arg_file args/train_humanoid3d_spinkick_args.txt --num_workers 16
```

will train a policy to perform a spinkick using 16 workers. As training progresses, it will regularly
print out statistics and log them to `output/` along with a `.ckpt` of the latest policy.
It typically takes about 60 millions samples to train one policy, which can take a day
when training with 16 workers. 16 workers is likely the max number of workers that the
framework can support, and it can get overwhelmed if too many workers are used.

A number of argument files are already provided in `args/` for the different skills. 
`train_[something]_args.txt` files are setup for `mpi_run.py` to train a policy, and 
`run_[something]_args.txt` files are setup for `DeepMimic.py` to run one of the pretrained policies.
To run your own policies, take one of the `run_[something]_args.txt` files and specify
the policy you want to run with `--model_file`. Make sure that the reference motion `--motion_file`
corresponds to the motion that your policy was trained for, otherwise the policy will not run properly.

Similarly, to train a policy using amp, run with the corresponding argument files:
```
python mpi_run.py --arg_file args/train_amp_target_humanoid3d_locomotion_args.txt --num_workers 16
```

Pretrained AMP models can be evaluated using:
```
python DeepMimic.py --arg_file args/run_amp_target_humanoid3d_locomotion_args.txt
```

## Interface
- the plot on the top-right shows the predictions of the value function
- right click and drag will pan the camera
- left click and drag will apply a force on the character at a particular location
- scrollwheel will zoom in/out
- pressing 'r' will reset the episode
- pressing 'l' will reload the argument file and rebuild everything
- pressing 'x' will pelt the character with random boxes
- pressing space will pause/resume the simulation
- pressing '>' will step the simulation one step at a time


## Mocap Data
Mocap clips are located in `data/motions/`. To play a clip, first modify 
`args/play_motion_humanoid3d_args.txt` and specify the file to play with
`--motion_file`, then run
```
python DeepMimic.py --arg_file args/play_motion_humanoid3d_args.txt
```

The motion files follow the JSON format. The `"Loop"` field specifies whether or not the motion is cyclic.
`"wrap"` specifies a cyclic motion that will wrap back to the start at the end, while `"none"` specifies an
acyclic motion that will stop once it reaches the end of the motion. Each vector in the `"Frames"` list
specifies a keyframe in the motion. Each frame has the following format:
```
[
	duration of frame in seconds (1D),
	root position (3D),
	root rotation (4D),
	chest rotation (4D),
	neck rotation (4D),
	right hip rotation (4D),
	right knee rotation (1D),
	right ankle rotation (4D),
	right shoulder rotation (4D),
	right elbow rotation (1D),
	left hip rotation (4D),
	left knee rotation (1D),
	left ankle rotation (4D),
	left shoulder rotation (4D),
	left elbow rotation (1D)
]
```

Positions are specified in meters, 3D rotations for spherical joints are specified as quaternions `(w, x, y ,z)`,
and 1D rotations for revolute joints (e.g. knees and elbows) are represented with a scalar rotation in radians. The root
positions and rotations are in world coordinates, but all other joint rotations are in the joint's local coordinates.
To use your own motion clip, convert it to a similar style JSON file.
