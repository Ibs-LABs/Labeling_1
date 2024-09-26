import cv2
import json
import os

for for_a in os.listdir(os.path.join('.', 'raw')):
    if for_a == 'test':
        pass

    img = cv2.imread(os.path.join('.', 'raw', for_a), cv2.IMREAD_COLOR)
    cv2.imshow(for_a, img)
    print(for_a)

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

cv2.destroyAllWindows()

if len(os.listdir(os.path.join('.', 'raw'))) == 0:
    file_list = os.listdir(os.path.join('.', 'in'))

    with open(os.path.join('.', 'result.json')) as f:
        f.write(json.dumps(file_list))

    print(file_list)