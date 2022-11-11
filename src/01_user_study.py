import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
from pathlib import Path
from math import ceil
import sys
from termcolor import colored

global id
id = int(sys.argv[1]) if len(sys.argv) > 1 else 0


def get_scroll(event):
    global id
    id += 1 if event.button == 'down' else -1
    global anim
    anim.event_source.start()


def show_init():
    plt.get_current_fig_manager().full_screen_toggle()


def show_imgs(_frame_id):
    subfolder = get_subfolder()
    global id
    plt.clf()
    if subfolder == 0:
        plt.axis('off')
        plt.text(0.4, 0.5, 'No More Images! Press Enter in Terminal to Exit.')
    else:
        imgs = list(subfolder.glob('*.jpg'))
        print(colored(str(id) + ':\t' + str(subfolder), 'green'),
              [x.name for x in imgs], sep='\n')
        n = len(imgs)
        area = 0, 0
        for i, img_path in enumerate(imgs):
            plt.subplot(ceil(n/4), 4, i+1)
            plt.axis('off')
            img = mpimg.imread(str(img_path))
            area_rate = 1.0
            if i == 0:
                area = img.shape[0] * img.shape[1]
            else:
                area_rate = img.shape[0] * img.shape[1] / area
            plt.title(img_path.name + ', ' + str(round(area_rate, 3)))

            plt.imshow(img)
        plt.gcf().canvas.manager.set_window_title(
            'Folder Index: ' + str(id) + ', Name: ' + subfolder.name)
    plt.draw()

    global anim
    anim.event_source.stop()


def get_subfolder():
    global subfolders
    global id
    return subfolders[id]


if __name__ == "__main__":
    folder = Path('images/')
    print('Dataset Root Directory:',
          colored(str(folder.resolve()), 'green'), sep='\n')
    print('Start at index:', colored(id, 'blue'))
    assert folder.is_dir()
    global subfolders
    subfolders = [x for x in folder.glob('*') if x.is_dir()]
    subfolders.append(0)
    print('Subfolder Number:', colored(len(subfolders), 'green'))
    print('Subfolder Name:')
    for i, subfolder in enumerate(subfolders[:-1]):
        print(subfolder.name, end='\t' if i % 10 != 9 else '\n')

    print(colored('\nPress Enter to Start and Press Aagin to Exit', 'yellow'))
    input()

    plt.ion()
    fig = plt.figure(figsize=(10, 10))
    fig.canvas.mpl_connect('scroll_event', get_scroll)
    fig.patch.set_facecolor('tab:gray')

    global anim
    anim = animation.FuncAnimation(fig, show_imgs,
                                   interval=10, repeat=False,
                                   init_func=show_init)  # lambda: None
    input()
