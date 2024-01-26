# therembone<!-- omit in toc -->

prog_jissen3

## Table of Content<!-- omit in toc -->

- [Execution Environment](#execution-environment)
- [Setup](#setup)
  - [Setup VGG\_Demo](#setup-vgg_demo)
  - [Setup VL53L0X-python](#setup-vl53l0x-python)
  - [Install Library](#install-library)
  - [Setup Pygame.midi](#setup-pygamemidi)
- [References](#references)


## Execution Environment

- jetson(jetpack4.6.2)
- python3.10.13

## Setup

Note. This is only for Jetson.

### Setup VGG_Demo

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

3. Place the learned weights file in the VGG_Demo directory.

### Setup VL53L0X-python

1. Clone the repository.

```bash
pip3 install git+https://github.com/pimoroni/VL53L0X-python.git
```

2. Install all packages.

```bash
cd [your repository]
git clone https://github.com/pimoroni/VL53L0X_rasp_python.git
cd VL53L0X-python
make
```

### Install Library

1. Install from requirements.txt

```bash
pip install -r requirements.txt
```

2. Please refer to the following to install Pytorch

[Building the Project from Source](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md)

### Setup Pygame.midi

Please refer to the following

[Jetson NanoでMIDIを使うためにカーネルビルド](https://qiita.com/karaage0703/items/9bef6aeec9ad24f647c6)

## References

[Pygame.midi](https://www.pygame.org/docs/ref/midi.html)

[VGG_Demo](https://github.com/s-ito0621/VGG_Demo/tree/main)

[VL53L0X-python](https://github.com/juehess/VL53L0X-python)
