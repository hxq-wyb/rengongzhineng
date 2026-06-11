"""
AI文生音频模块
基于MusicGen大模型实现文本转音乐/音效
"""
import os
import torch
import soundfile as sf
from audiocraft.models import MusicGen

OUTPUT_DIR = "./output"
MODEL_SIZE = "small"


def init_audio_model():
    """初始化音频模型"""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[音频模块] 运行设备: {device}")
    model = MusicGen.get_pretrained(MODEL_SIZE, device=device)
    model.set_generation_params(duration=8)  # 生成8秒音频
    return model


def generate_audio(prompt: str, audio_name: str = "ai_audio.wav"):
    """根据文本生成音频并保存"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    model = init_audio_model()
    try:
        print(f"[音频模块] 正在生成音频...")
        wav = model.generate([prompt])
        save_path = os.path.join(OUTPUT_DIR, audio_name)
        sf.write(save_path, wav[0].cpu().numpy().T, 32000)
        print(f"[音频模块] 生成完成！文件路径：{save_path}")
        return save_path
    except Exception as e:
        print(f"[音频模块] 生成失败：{str(e)}")
        return None


if __name__ == "__main__":
    generate_audio("轻快钢琴音乐，治愈放松风格")