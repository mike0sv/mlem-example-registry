import random

from mlem.api import init, save
from mlem.core.artifacts import md5_fileobj


def pet_face_recognition(filename):
    return "It's a pet face probably"

def mlem_blep_classifier(filename):
    return "mlem" if random.randint(0, 1) % 2 else "blep"

def dog_bark_translator(filename):
    emojis = ["😺", "🐶", "🐕", "😁", "🤗", "🥰"]
    size = len(emojis)
    with open(filename, "rb") as f:
        md5_digest = int(md5_fileobj(f), 16)
        return "".join(emojis[md5_digest % (i * 100) % size] for i in range(1, md5_digest % 4 + 3))


def main():
    init()
    save(dog_bark_translator, "dog-bark-translator", tmp_sample_data="train.py", description="""- 📖 Translates dog barks in emoji.
- 📦 Pytorch 1.10.0, Torchaudio 0.10.0, Emoji 1.6.1
- 🎯 Accuracy 87.3%""")
    save(mlem_blep_classifier, "mlem-blep-classifier", description="""- 📖 Classifies images as `mlem` or `blep`
- 📦 Pytorch 1.10.0
- 🎯 Accuracy 50%""")
    save(pet_face_recognition, "pet-face-recognition", description="""- 📖 Tries to recognize pet face on a photo
- 📦 Pytorch 1.10.0
- 🎯 Accuracy 100%""")

if __name__ == '__main__':
    main()