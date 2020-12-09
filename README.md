# QGC_plan_fix
QGroundControl flight plan with fixed angle for multirotor.
# Short description
Program modifies .plan Flight Plan file, saved from [QGroundControl](qgroundcontrol.com)
<br>related issue: https://github.com/mavlink/qgroundcontrol/issues/7140
<br>related discussion: https://discuss.px4.io/t/heading-fixed-flight-path-for-multicopters/1591/21

Usage: `python plan_fix_heading.py <filename> <angle>`
<br>Generates <filename_fixed> flight plan
<br>Angle, if ommited - will be taken from survey parameter Angle, if any
