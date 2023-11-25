This tutorial provides an efficient guide to configuring your Python environment for multi-agent reinforcement learning (MARL) experiment. We recommend [Anaconda](https://www.anaconda.com/) for its robust package management capabilities.

For installing Anaconda on different platforms:
- Windows: Refer to [Windows Installation Guide](https://docs.anaconda.com/free/anaconda/install/windows/).
- MAC: Refer to [MAC Installation Guide](https://docs.anaconda.com/free/anaconda/install/mac-os/).
- Linux: Refer to [Linux Installation Guide](https://docs.anaconda.com/free/anaconda/install/linux/).

After installing Anaconda, you can get started with conda by referring to the [guide](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#starting-conda).

## Step 1, install python requirement:
### Create New "MARL" Environment:
macOS/Linux/Windows (using Anaconda Prompt)
- ``conda create -y -n MARL python=2.7``
### Activate the "MARL" Environment:
- ``conda activate MARL``
### Install Dependencies:
- ``cd xxx/MARL``
- ``pip install -r requirement.txt``

Windows (for TensorFlow):

- ``pip install tensorflow-1.5.0-cp27-cp27m-win_amd64.whl``

## Step 2, run the experiment:
- ``python predators_prey_multiagent.py``

    - Additional customization options
        - ``--Student_number``, tell us your student number for testing purposes
        - ``--MARLAlgorithm``, choice in 'QMIX', 'VDN' and 'IQL'
        - ``--agents-number``, an int number, which represents the number of agents in experiment
        - For other options, please refer to lines 168-219 in the ``predators_prey_multiagent.py``
    - Example
        - ``python predators_prey_multiagent.py --agents-number 2 --MARLAlgorithm VDN --Student_number 100``, where you set three agents and train them with VDN algorithm, and your student number is 100 (for example).
## Step 3, Modify the agent code ```MARL_agent.py``` and submit the network structure you designed for testing. We offer two options as follows: 
### Online testing:
* You must connect to http://10.112.4.51:5000/. (部署需要查看ip地址)

Upload your network structure file on the http://10.112.4.51:5000/, and wait for the return result.


### Local testing:

Test your network structure by using ``python predators_prey_multiagent.py --agents-number 2 --MARLAlgorithm VDN --Student_number 100 -test``.

## Appendix - Main code structure
```
MARL
│  brain.py # Agent design
│  controller.py # MultiAgent reinforcement learning methods
│  MARL_agent.py # Agent funcation
│  predators_prey_multiagent.py # main function
│  prioritized_experience_replay.py # Experience playback function
│  README.md
│  requirement.txt
│  sum_tree.py
│  uniform_experience_replay.py # Memory design
├─environments
│  └─predators_prey
│      └─env.py # MultiAgent environment
├─results_predators_prey
│    └─weights_files
│            100_5e-05_RMSProp_100_32_10000_100000_100_0_10_256_DQN_UER_0.5_False_3_5_1_1_0.h5
│            100_5e-05_RMSProp_100_32_10000_100000_100_0_10_256_DQN_UER_0.5_False_3_5_1_1_1.h5
│            100_5e-05_RMSProp_100_32_10000_100000_100_0_10_256_DQN_UER_0.5_False_3_5_1_1_2.h5
```



