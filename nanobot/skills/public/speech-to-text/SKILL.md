---
name: speech-to-text
description: 语音消息识别和转录。当收到语音附件（.ogg, .wav, .mp3 等）时，自动将其转换为文本以便后续对话。
---

# Speech to Text

语音识别技能，将语音消息转换为文本。

## 触发场景

- 用户发送了语音附件（.ogg, .wav, .mp3, .m4a 等格式）
- 用户明确要求转录语音内容

## 使用方法

### 自动处理

当检测到消息中包含语音附件时，调用 `scripts/transcribe.py` 脚本进行转录：

```bash
python scripts/transcribe.py <语音文件路径>
```

### 手动转录

用户也可以明确要求转录某个语音文件。

## 脚本说明

- `scripts/transcribe.py` - 主转录脚本，使用本地语音识别服务或 API

## 依赖

需要安装以下依赖之一：

1. **本地方案**（推荐，离线可用）：
   - `whisper` (OpenAI Whisper)
   - 或 `faster-whisper`

2. **API 方案**：
   - OpenAI Whisper API
   - Google Speech-to-Text API

## 安装

```bash
# 本地 Whisper（推荐）
pip install openai-whisper

# 或更快的版本
pip install faster-whisper
```

## 注意事项

- 语音文件路径从附件中提取
- 转录结果用于后续对话理解
- 支持中文和英文识别
