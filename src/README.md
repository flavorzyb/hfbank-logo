# 恒丰银行LOGO识别

使用TensorFlow的目标检测模块进行恒丰银行LOGO的识别

## 环境需求

- **Python** >= 2.7.15
- **tensorflow** >= 1.12.0
- **Cython** >= 0.29.1
- **contextlib2** >= 0.5.5
- **pillow** >= 5.3.0
- **lxml** >= 4.2.5
- **jupyter** >= 1.0.0
- **matplotlib** >= 2.2.3

### 安装Python

Python官方网址: [https://www.python.org](https://www.python.org)

下载地址: [https://www.python.org/downloads/](https://www.python.org/downloads/)

**注意:**  Python 需要安装 <= 3.0.0 版本

### 安装Python依赖库:

```bash
$ pip install --user tensorflow
$ pip install --user Cython
$ pip install --user contextlib2
$ pip install --user pillow
$ pip install --user lxml
$ pip install --user jupyter
$ pip install --user matplotlib
```

### 安装protoc

protoc官方网址: [https://developers.google.com/protocol-buffers/](https://developers.google.com/protocol-buffers/)

**注意:** 官方网址需翻墙

下载地址: [https://github.com/protocolbuffers/protobuf/releases](https://github.com/protocolbuffers/protobuf/releases)

下载最新的源码版本:

```bash
$ wget https://github.com/protocolbuffers/protobuf/releases/download/v3.6.1/protobuf-all-3.6.1.tar.gz
```

**注意:** 至2018-12-10最新版本为 **3.6.1**

#### 编译依赖

编译protobuf需要先安装如下软件

- **autoconf**
- **automake**
- **libtool**
- **make**
- **g++**
- **unzip**

**注意:** 上述依赖软件请自行安装

#### 编译及安装

```bash
$ tar zxvf protobuf-all-3.6.1.tar.gz
$ cd protobuf-all-3.6.1
$ ./autogen.sh
$ ./configure
$ make
$ make check
$ sudo make install
```
