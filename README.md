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

    For Windows only:
    
     ``pip install tensorflow-1.5.0-cp27-cp27m-win_amd64.whl``

## Step 2, run the experiment:
- ``python main.py``

    - Additional customization options
        - ``--Student_number``, tell us your student number for testing purposes
        - ``--MARLAlgorithm``, choice in 'IQL', 'VDN' (to be completed) and 'QMIX'
        - ``--agents-number``, an int number, which represents the number of agents in experiment
        - For other options, please refer to lines 168-219 in the ``main.py``
    - Example
        - ``python main.py --agents-number 2 --MARLAlgorithm IQL --Student_number 100``, where you set three agents and train them with IQL algorithm, and your student number is 100 (for example).
## Step 3, Modify the code ```MARL_agent.py``` and submit everything in a zip/rar file, name it "FirstName_LastName_Project2.zip".
Test the neural network by ``python main.py --agents-number 2 --MARLAlgorithm IQL --Student_number 100``.

Test the VDN algorithm by ``python main.py --agents-number 2 --MARLAlgorithm VDN --Student_number 100``.

Test the prey strategy by ``python main.py --agents-number 2 --MARLAlgorithm IQL --Student_number 100 -evm 3``.

Test the training strategy by ``python main.py --agents-number 2 --MARLAlgorithm VDN --Student_number 100 ... (--agrs in main.py)``.