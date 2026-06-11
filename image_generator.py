"""
AI文生绘画模块
基于Stable Diffusion大模型实现文本转图片
"""
import os
import torch
from diffusers import StableDiffusionPipeline

# 全局配置
OUTPUT_DIR = "./output"
MODEL_ID = "runwayml/stable-diffusion-v1-5"


def init_image_pipeline():
    """初始化绘图模型，自动适配GPU/CPU设备"""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[绘画模块] 运行设备: {device}")

    pipe = StableDiffusionPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        safety_checker=None
    )
    pipe = pipe.to(device)
    return pipe


def generate_image(prompt: str, img_name: str = "ai_image.png"):
    """根据文本生成图片并保存"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    pipe = init_image_pipeline()
    try:
        print(f"[绘画模块] 正在生成图片...")
        image = pipe(prompt).images[0]
        save_path = os.path.join(OUTPUT_DIR, img_name)
        image.save(save_path)
        print(f"[绘画模块] 生成完成！文件路径：{save_path}")
        return save_path
    except Exception as e:
        print(f"[绘画模块] 生成失败：{str(e)}")
        return None


if __name__ == "__main__":
    generate_image("古风山水，水墨风格，唯美意境")