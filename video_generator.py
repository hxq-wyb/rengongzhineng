"""
AI文生视频模块
基于ModelScope文生视频模型实现文本转短视频
"""
import os
import shutil
from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys

OUTPUT_DIR = "./output"


def generate_video(prompt: str, video_name: str = "ai_video.mp4"):
    """根据文本生成短视频并保存"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    try:
        print(f"[视频模块] 正在生成视频...")
        text_to_video = pipeline(
            task='text-to-video-synthesis',
            model='damo/text-to-video-synthesis'
        )
        result = text_to_video(prompt)
        video_path = result[OutputKeys.OUTPUT_VIDEO]
        target_path = os.path.join(OUTPUT_DIR, video_name)
        shutil.copy(video_path, target_path)
        print(f"[视频模块] 生成完成！文件路径：{target_path}")
        return target_path
    except Exception as e:
        print(f"[视频模块] 生成失败：{str(e)}")
        return None


if __name__ == "__main__":
    generate_video("海边日出，海浪流动，暖色调风景")