# 语音识别依赖安装

## 方案一：本地 Whisper（推荐）

完全离线运行，无需 API 密钥。

### 安装 faster-whisper（更快，更省资源）

```bash
pip install faster-whisper
```

### 或安装标准 whisper

```bash
pip install openai-whisper
```

### 模型说明

| 模型 | 大小 | 速度 | 准确率 | 适用场景 |
|------|------|------|--------|----------|
| tiny | 39M | 最快 | 一般 | 快速测试 |
| base | 74M | 快 | 良好 | 日常使用 |
| small | 244M | 中等 | 很好 | 高质量需求 |
| medium | 769M | 慢 | 优秀 | 专业场景 |
| large | 1550M | 最慢 | 最佳 | 最高质量 |

## 方案二：OpenAI Whisper API

需要 API 密钥，按使用量计费。

```bash
pip install openai
export OPENAI_API_KEY="your-api-key"
```

## 测试安装

```bash
python scripts/transcribe.py /path/to/voice-message.ogg
```

## 支持格式

- .ogg
- .wav
- .mp3
- .m4a
- .flac
- 以及其他常见音频格式
