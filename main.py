"""Copy the bundled PNG using only the Python standard library."""

import os
import shutil


MINIMAL_PNG = bytes.fromhex(
    '89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c489'
    '0000000b49444154789c6360000200000500017a5eab3f0000000049454e44ae426082'
)


def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR') or '/output'
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, 'entry.png')
    source_dir = os.path.dirname(os.path.abspath(__file__))

    for name in ('entry.png', 'news.png'):
        source = os.path.join(source_dir, name)
        if os.path.isfile(source):
            if not (os.path.exists(target) and os.path.samefile(source, target)):
                shutil.copyfile(source, target)
            return

    with open(target, 'wb') as image:
        image.write(MINIMAL_PNG)


if __name__ == '__main__':
    main()
