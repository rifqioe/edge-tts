import asyncio
import edge_tts

async def main():
    voices = {
        "id": "id-ID-GadisNeural",
        "en": "en-US-GuyNeural",
        "jp": "ja-JP-NanamiNeural"
    }

    texts = {
        "id": "Halo Rifqi, semoga harimu menyenangkan!",
        "en": "Hello Rifqi, hope you're having a great day!",
        "jp": "リフキさん、素敵な一日をお過ごしください。"
    }

    for lang, voice in voices.items():
        communicate = edge_tts.Communicate(texts[lang], voice)
        await communicate.save(f"{lang}.mp3")
        print(f"✅ Generated {lang}.mp3 using {voice}")

if __name__ == "__main__":
    asyncio.run(main())
