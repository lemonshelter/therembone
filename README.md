# therembone

prog_jissen3

## Setup

Note. This is only for Jetson.

### Setup VGG_Demo

Note. This is only for Jetson.

1. Clone the repository.

```bash
cd [your repository]
git clone https://github.com/s-ito0621/VGG_Demo.git
```

2. Install all packages.

```bash
cd VGG_Demo
bash setup.sh

#check
python3
>>import jetcam
```

### Setup VL53L0X-python

1. Clone the repository.

```bash
# Python2
pip2 install git+https://github.com/pimoroni/VL53L0X-python.git
# Python3
pip3 install git+https://github.com/pimoroni/VL53L0X-python.git
```

2. Install all packages.

```bash
cd [your repository]
git clone https://github.com/pimoroni/VL53L0X_rasp_python.git
cd VL53L0X-python
make
```

