"""
AIGC多媒体生成项目 - 主入口
功能：整合绘画、音频、视频三大模块，命令行菜单交互
编码规范：PEP8，逻辑清晰，异常友好提示
"""
from image_generator import generate_image
from audio_generator import generate_audio
from video_generator import generate_video


def show_menu():
    """打印功能选择菜单"""
    print("=" * 55)
    print("      大模型多媒体生成工具（绘画/音频/视频）")
    print("=" * 55)
    print("1. AI 文生绘画（图片生成）")
    print("2. AI 文生音频（音乐/音效生成）")
    print("3. AI 文生视频（短视频生成）")
    print("0. 退出程序")
    print("=" * 55)


def main():
    while True:
        show_menu()
        choice = input("请输入功能编号(0-3)：").strip()
        if choice == "0":
            print("程序已退出！")
            break
        elif choice == "1":
            prompt = input("请输入图片描述词：")
            generate_image(prompt)
        elif choice == "2":
            prompt = input("请输入音频描述词：")
            generate_audio(prompt)
        elif choice == "3":
            prompt = input("请输入视频场景描述词：")
            generate_video(prompt)
        else:
            print("输入错误，请选择 0~3 之间的数字！")
        print("\n")


if __name__ == "__main__":
    main()