# QGroundControl flight plan with fixed angle for multirotor
# related issue: https://github.com/mavlink/qgroundcontrol/issues/7140
# related discussion: https://discuss.px4.io/t/heading-fixed-flight-path-for-multicopters/1591/21 
# Author: Petrov Ilya, www.copter.space, ipetrov@byte-1c.ru, mail@copter.space

import json
import sys

# Constants from https://mavlink.io/en/messages/common.html
MAV_CMD_NAV_WAYPOINT=16
MAV_CMD_SET_CAMERA_MODE=530
MAV_CMD_DO_SET_CAM_TRIGG_DIST=206
CAMERA_MODE_IMAGE=0
CAMERA_MODE_VIDEO=1
CAMERA_MODE_IMAGE_SURVEY=2

def fix_item(i, angle):
    if i['command'] == MAV_CMD_NAV_WAYPOINT and i['params'][3] == None:
        i['params'][3] = angle

def main():
    if len(sys.argv)<2:
        print('Usage: python plan_fix_heading.py <filename> <angle>')
        print('Generates <filename_fixed> flight plan')
        print('Angle, if ommited - will be taken from survey parameter Angle, if any')
        return

    filename=sys.argv[1]
    if len(sys.argv)>2:
        angle = int(sys.argv[2])
    else:
        angle = None

    with open(filename, 'r') as myfile:
        plan = json.loads(myfile.read())

    for item in plan['mission']['items']:
        if item['type']=='SimpleItem':
            fix_item(item, angle)
        elif item['type']=='ComplexItem':
            if angle==None:
                angle = item['angle']
            mission_items = item['TransectStyleComplexItem']['Items']
            for i in mission_items:
                fix_item(i, angle)
    outfilename = filename.split('.')[0]+'_fixed.plan'
    with open(outfilename, 'w') as outfile:
        outfile.write(json.dumps(plan, sort_keys=False, indent=4))

if __name__ == "__main__":
    main()