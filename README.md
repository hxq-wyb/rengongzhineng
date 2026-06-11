# 大模型多媒体生成项目
基于开源AIGC大模型，实现**文生绘画、文生音频、文生视频**三大功能，《人工智能导论》课程期末项目。

## 一、运行环境
### 硬件要求
- 推荐：NVIDIA独立显卡（显存≥4GB），CUDA加速，运行速度快
- 最低：CPU设备（可运行，生成速度较慢）

### 软件环境
- Python：3.9 ~ 3.10
- 系统：Windows / Linux / MacOS
- 必备工具：FFmpeg（音视频编解码依赖）

## 二、依赖库安装
打开CMD，进入项目根目录，执行以下命令：
```cmd
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install diffusers transformers accelerate pillow safetensors
pip install audiocraft soundfile
pip install modelscope opencv-python