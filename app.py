import cv2
import json
import os
import natsort
from random import shuffle

all_file_list = natsort.natsorted(os.listdir(os.path.join('.', 'in')) + os.listdir(os.path.join('.', 'out')) + os.listdir(os.path.join('.', 'raw')))
file_search = natsort.natsorted(os.listdir(os.path.join('.', 'in')) + os.listdir(os.path.join('.', 'out')))

print(all_file_list)
print(file_search)

if len(file_search) > 1:
    file_search_name = file_search[-1]

    count = all_file_list.index(file_search_name) + 1
else:
    count = 0

while count < len(all_file_list):
    for_a = all_file_list[count]

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    print(for_a)
    img = cv2.imread(os.path.join('.', 'raw', for_a), cv2.IMREAD_COLOR)
    cv2.imshow('image', img)

    key = cv2.waitKey()
    if key == ord('a'):
        os.rename(os.path.join('.', 'raw', for_a), os.path.join('.', 'out', for_a))
    
        print('out')
    elif key == ord('q'):
        os.rename(os.path.join('.', 'raw', for_a), os.path.join('.', 'in', for_a))

        print('in')
    elif key == 27:
        break

        print('exit')
    elif key == ord('b'):
        if count != 0:
            count -= 1
            for_a = all_file_list[count]

            try:
                os.rename(os.path.join('.', 'out', for_a), os.path.join('.', 'raw', for_a))
            except Exception as e:
                print(e)

            try:
                os.rename(os.path.join('.', 'in', for_a), os.path.join('.', 'raw', for_a))
            except Exception as e:
                print(e)

        print('back')

        continue
    else:
        continue

    count += 1

cv2.destroyAllWindows()

if len(os.listdir(os.path.join('.', 'raw'))) == 0:
    file_list = os.listdir(os.path.join('.', 'in'))

    with open(os.path.join('.', 'result.json')) as f:
        f.write(json.dumps(file_list))

    print(file_list)