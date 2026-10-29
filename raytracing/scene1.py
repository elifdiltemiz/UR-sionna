from sionna.rt import (
    load_scene,
    scene,
    Transmitter,
    Receiver,
    PlanarArray,
    PathSolver,
)

# 1. Load the built-in Munich scene
my_scene = load_scene(scene.munich)

# 2. Set carrier frequency to 3.5 GHz
my_scene.frequency = 3.5e9

# 3. Configure antenna arrays
my_scene.tx_array = PlanarArray(
    num_rows=1,
    num_cols=1,
    vertical_spacing=0.5,
    horizontal_spacing=0.5,
    pattern="iso",
    polarization="V"
)

my_scene.rx_array = PlanarArray(
    num_rows=1,
    num_cols=1,
    vertical_spacing=0.5,
    horizontal_spacing=0.5,
    pattern="iso",
    polarization="V"
)

# 4. Add a transmitter
tx = Transmitter(
    name="base_station",
    position=[8.5, 21.0, 27.0]
)
my_scene.add(tx)

# 5. Add a receiver
rx = Receiver(
    name="user",
    position=[45.0, 90.0, 1.5]
)
my_scene.add(rx)

# Point transmitter towards receiver
tx.look_at(rx)

# Create the ray-tracing solver
solver = PathSolver()

# Compute propagation paths
paths = solver(
    scene=my_scene,
    max_depth=3,
    los=True,
    specular_reflection=True,
    diffuse_reflection=False,
    refraction=False,
    synthetic_array=True
)

print("Frequency:", my_scene.frequency / 1e9, "GHz")
print("Transmitter:", tx.position)
print("Receiver:", rx.position)

print("Paths calculated successfully!")
print(paths)