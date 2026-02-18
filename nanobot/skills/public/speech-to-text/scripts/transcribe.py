#!/usr/bin/env python3
"""
语音转文本脚本
使用 OpenAI Whisper 进行本地语音识别
"""

import sys
import os

def transcribe(audio_path: str, model: str = "base") -> str:
    """
    转录语音文件为文本
    
    Args:
        audio_path: 语音文件路径
        model: Whisper 模型 (tiny, base, small, medium, large)
    
    Returns:
        转录的文本内容
    """
    try:
        # 尝试使用 faster-whisper（更快）
        try:
            from faster_whisper import WhisperModel
            model = WhisperModel(model, device="cpu", compute_type="int8")
            segments, info = model.transcribe(audio_path, language="zh")
            text = " ".join([segment.text for segment in segments])
            return text.strip()
        except ImportError:
            pass
        
        # 回退到标准 whisper
        try:
            import whisper
            model = whisper.load_model(model)
            result = model.transcribe(audio_path, language="zh")
            return result["text"].strip()
        except ImportError:
            print("错误：未安装 whisper 或 faster-whisper", file=sys.stderr)
            print("请运行：pip install openai-whisper 或 pip install faster-whisper", file=sys.stderr)
            sys.exit(1)
            
    except Exception as e:
        print(f"转录失败：{e}", file=sys.stderr)
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("用法：python transcribe.py <语音文件路径> [模型]", file=sys.stderr)
        print("模型选项：tiny, base, small, medium, large (默认：base)", file=sys.stderr)
        sys.exit(1)
    
    audio_path = sys.argv[1]
    model = sys.argv[2] if len(sys.argv) > 2 else "base"
    
    if not os.path.exists(audio_path):
        print(f"错误：文件不存在 - {audio_path}", file=sys.stderr)
        sys.exit(1)
    
    text = transcribe(audio_path, model)
    print(text)


if __name__ == "__main__":
    main()
