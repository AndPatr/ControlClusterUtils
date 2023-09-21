# ControlClusterUtils

Utilities to bridge parallel simulations (typically GPU-based simulators, e.g. [Omniverse Isaac Sim](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim.html)), with a cluster of CPU-based receding-horizon controllers (developed, for example, with tools like [horizon-casadi](https://github.com/ADVRHumanoids/horizon)). 

<center><img src="control_cluster_utils/docs/images/overview/architecture.png" alt="drawing" width="1000"/> </center>

At its core, the package is made of the following components:
- A `ControlClusterSrvr` object is in charge of loading and spawning a number of controllers over separate child processes. Each controller must inherit from a base `RHController` class. Controllers are added to the server via the `add_controller` method.
- A `ControlClusterClient` object represents the interface between the controllers and the parallel simulation environment (e.g. Omniverse Isaac Sim). 
- Data is shared and passed between *cluster server*, *cluster client* and the *control cluster* employing shared memory, for minimum latency (no need for serialization/deserialization and/or messages exchange) and maximum flexibility. 
The low-level implementation of the shared data mechanism is hosted in `utilities/shared_mem.py`. At its core, the package uses [posix_ipc](https://github.com/osvenskan/posix_ipc) and [mmap](https://docs.python.org/3.7/library/mmap.html) to build shared memory clients and servers which create and manage views of specific memory regions. 

- When `ControlClusterClient`'s `solve` is called, the shared cluster state is synched with the one from the simulator (this might require a copy from GPU to CPU), all the controllers in the cluster run the solution of their associated control problem and fill a shared solution object with updated data. By design, the client's `solve` will block until all controllers have returned. This way, the cluster is alwayss synchronized with the simulator.

- Additionally, a debugging Qt5-based gui is also provided:

    <center><img src="control_cluster_utils/docs/images/overview/debugger_gui.png" alt="drawing" width="500"/> </center>

    At its current state, the GUI has the following main features:
    - selection of which shared data to monitor (all or a subset of them).
    - arbitrary plot resizing and window collapsing
    - online window length resizing
    - online sample and update rate selection
    - for each window, line selection/deselection
    - pause/unpause of all or individual plots for better debugging
    - control cluster solution triggering
    - day/night mode
Some notes: 
- The package is also available through Anaconda at [control_cluster_utils](https://anaconda.org/AndrePatri/control_cluster_utils). `ControlClusterUtils` is under active development, so its Anaconda version might not be always updated with the tip of this repo. For cutting-edge features, always refer to the source code hosted here.
- The reasons for using the third party library `posix_ipc` instead of the newest [multiprocessing.shared_memory](https://docs.python.org/3/library/multiprocessing.shared_memory.html) are twofold. First, `posix_ipc` is more flexible since it allows potentially communication with non-python applications. Second, and more importantly, `multiprocessing.shared_memory` is available only from Python 3.8 onwards and this might cause issues if interfacing with a simulator supporting earlier versions of Python (like IsaacSim 2022.2.1, which is only compatible with Python 3.7). Choosing `posix_ipc` thus enables maximum compatibility.

#### ToDo:

- [] RhcTaskRef setting throrugh keyboard commands for controller debugging.  