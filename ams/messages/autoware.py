#!/usr/bin/env python
# coding: utf-8

from ams.structures import get_base_class

timestamp_template = {
    "secs": 0,
    "nsecs": 0
}

timestamp_schema = {
    "secs": {
        "type": "integer",
        "required": True,
        "nullable": False,
    },
    "nsecs": {
        "type": "integer",
        "required": True,
        "nullable": False,
    }
}


class Timestamp(get_base_class(timestamp_template, timestamp_schema)):
    pass


header_template = {
    "seq": 0,
    "stamp": Timestamp.get_template(),
    "frame_id": ""
}

header_schema = {
    "seq": {
        "type": "integer",
        "required": True,
        "nullable": False,
    },
    "stamp": {
        "type": "dict",
        "schema": Timestamp.get_schema(),
        "required": True,
        "nullable": False,
    },
    "frame_id": {
        "type": "string",
        "required": True,
        "nullable": False,
    }
}


class Header(get_base_class(header_template, header_schema)):
    pass


vector3_template = {
    "x": 0.0,
    "y": 0.0,
    "z": 0.0,
}

vector3_schema = {
    "x": {
        "type": "number",
        "required": True,
        "nullable": False,
    },
    "y": {
        "type": "number",
        "required": True,
        "nullable": False,
    },
    "z": {
        "type": "number",
        "required": True,
        "nullable": False,
    }
}


class Vector3(get_base_class(vector3_template, vector3_schema)):
    pass


pose_template = {
    "position": Vector3.get_template(),
    "orientation": {
        "w": 0.0,
        "x": 0.0,
        "y": 0.0,
        "z": 0.0
    }
}

pose_schema = {
    "position": {
        "type": "dict",
        "schema": Vector3.get_schema(),
        "required": True,
        "nullable": False,
    },
    "orientation": {
        "type": "dict",
        "schema": {
            "w": {
                "type": "number",
                "required": True,
                "nullable": False,
            },
            "x": {
                "type": "number",
                "required": True,
                "nullable": False,
            },
            "y": {
                "type": "number",
                "required": True,
                "nullable": False,
            },
            "z": {
                "type": "number",
                "required": True,
                "nullable": False,
            }
        },
        "required": True,
        "nullable": False,
    }
}


class Pose(get_base_class(pose_template, pose_schema)):
    pass


current_pose_template = {
    "header": Header.get_template(),
    "pose": Pose.get_template()
}

current_pose_schema = {
    "header": {
        "type": "dict",
        "schema": Header.get_schema(),
        "required": True,
        "nullable": False
    },
    "pose": {
        "type": "dict",
        "schema": Pose.get_schema(),
        "required": True,
        "nullable": False
    },
}


class CurrentPose(get_base_class(current_pose_template, current_pose_schema)):
    pass


twist_template = {
    "linear": Vector3.get_template(),
    "angular": Vector3.get_template()
}

twist_schema = {
    "linear": {
        "type": "dict",
        "schema": Vector3.get_schema(),
        "required": True,
        "nullable": False,
    },
    "angular": {
        "type": "dict",
        "schema": Vector3.get_schema(),
        "required": True,
        "nullable": False,
    }
}


class Twist(get_base_class(twist_template, twist_schema)):
    pass


twist_stamped_template = {
    "header": Header.get_template(),
    "twist": Twist.get_template()
}

twist_stamped_schema = {
    "header": {
        "type": "dict",
        "schema": Header.get_schema(),
        "required": True,
        "nullable": False,
    },
    "twist": {
        "type": "dict",
        "schema": Twist.get_schema(),
        "required": True,
        "nullable": False,
    }
}


class TwistStamped(get_base_class(twist_stamped_template, twist_stamped_schema)):
    pass


dtlane_template = {
    "dist": 0.0,
    "dir": 0.0,
    "apara": 0.0,
    "r": 0.0,
    "slope": 0.0,
    "cant": 0.0,
    "lw": 0.0,
    "rw": 0.0
}

dtlane_schema = {
    "dist": {
        "type": "number",
        "required": True,
        "nullable": False,
    },
    "dir": {
        "type": "number",
        "required": True,
        "nullable": False,
    },
    "apara": {
        "type": "number",
        "required": True,
        "nullable": False,
    },
    "r": {
        "type": "number",
        "required": True,
        "nullable": False,
    },
    "slope": {
        "type": "number",
        "required": True,
        "nullable": False,
    },
    "cant": {
        "type": "number",
        "required": True,
        "nullable": False,
    },
    "lw": {
        "type": "number",
        "required": True,
        "nullable": False,
    },
    "rw": {
        "type": "number",
        "required": True,
        "nullable": False,
    }
}


class Dtlane(get_base_class(dtlane_template, dtlane_schema)):
    pass


waypoint_state_template = {
    "aid": 0,
    "lanechange_state": 0,
    "steering_state": 0,
    "accel_state": 0,
    "stop_state": 0,
    "event_state": 0
}

waypoint_state_schema = {
    "aid": {
        "type": "integer",
        "required": True,
        "nullable": False,
    },
    "lanechange_state": {
        "type": "integer",
        "required": True,
        "nullable": False,
    },
    "steering_state": {
        "type": "integer",
        "required": True,
        "nullable": False,
    },
    "accel_state": {
        "type": "integer",
        "required": True,
        "nullable": False,
    },
    "stop_state": {
        "type": "integer",
        "required": True,
        "nullable": False,
    },
    "event_state": {
        "type": "integer",
        "required": True,
        "nullable": False,
    }

}


class WaypointState(get_base_class(waypoint_state_template, waypoint_state_schema)):
    pass


closest_waypoint_template = {
    "data": 0
}

closest_waypoint_schema = {
    "data": {
        "type": "integer",
        "required": True,
        "nullable": False,
    }
}


class ClosestWaypoint(get_base_class(closest_waypoint_template, closest_waypoint_schema)):
    pass


dicision_maker_states_template = {
    "header": Header.get_template(),
    "main_state": "default",
    "acc_state": "default",
    "str_state": "default",
    "behavior_state": "default"
}

dicision_maker_states_schema = {
    "header": {
        "type": "dict",
        "schema": Header.get_schema(),
        "required": True,
        "nullable": False
    },
    "main_state": {
        "type": "string",
        "required": True,
        "nullable": False
    },
    "acc_state": {
        "type": "string",
        "required": True,
        "nullable": False
    },
    "str_state": {
        "type": "string",
        "required": True,
        "nullable": False
    },
    "behavior_state": {
        "type": "string",
        "required": True,
        "nullable": False
    }
}


class DecisionMakerStates(get_base_class(dicision_maker_states_template, dicision_maker_states_schema)):
    pass


status_template = {
    "route_code": "0:0_1:1",
    "time": 0.0,
    "state": "default"
}

status_schema = {
    "route_code": {
        "type": "string",
        "required": True,
        "nullable": False
    },
    "time": {
        "type": "number",
        "required": True,
        "nullable": False
    },
    "state": {
        "type": "string",
        "required": True,
        "nullable": False,
    }
}


class Status(get_base_class(status_template, status_schema)):
    pass


pose_stamped_template = {
    "header": Header.get_template(),
    "pose": Pose.get_template()
}

pose_stamped_schema = {
    "header": {
        "type": "dict",
        "schema": Header.get_schema(),
        "required": True,
        "nullable": False,
    },
    "pose": {
        "type": "dict",
        "schema": Pose.get_schema(),
        "required": True,
        "nullable": False,
    }
}


class PoseStamped(get_base_class(pose_stamped_template, pose_stamped_schema)):
    pass


waypoint_template = {
    "gid": 0,
    "lid": 0,
    "pose": PoseStamped.get_template(),
    "twist": TwistStamped.get_template(),
    "dtlane": Dtlane.get_template(),
    "change_flag": 0,
    "wpstate": WaypointState.get_template()

}

waypoint_schema = {
    "gid": {
        "type": "integer",
        "required": True,
        "nullable": False,
    },
    "lid": {
        "type": "integer",
        "required": True,
        "nullable": False,
    },
    "pose": {
        "type": "dict",
        "schema": PoseStamped.get_schema(),
        "required": True,
        "nullable": False,
    },
    "twist": {
        "type": "dict",
        "schema": TwistStamped.get_schema(),
        "required": True,
        "nullable": False,
    },
    "dtlane": {
        "type": "dict",
        "schema": Dtlane.get_schema(),
        "required": True,
        "nullable": False,
    },
    "change_flag": {
        "type": "integer",
        "required": True,
        "nullable": False,
    },
    "wpstate": {
        "type": "dict",
        "schema": WaypointState.get_schema(),
        "required": True,
        "nullable": False,
    },
}


class Waypoint(get_base_class(waypoint_template, waypoint_schema)):
    pass


lane_template = {
    "header": Header.get_template(),
    "increment": 0,
    "lane_id": 0,
    "waypoints": [Waypoint.get_template()]
}

lane_schema = {
    "header": {
        "type": "dict",
        "schema": Header.get_schema(),
        "required": True,
        "nullable": False,
    },
    "increment": {
        "type": "integer",
        "required": True,
        "nullable": False,
    },
    "lane_id": {
        "type": "integer",
        "required": True,
        "nullable": False,
    },
    "waypoints": {
        "type": "list",
        "valueschema": {
            "type": "dict",
            "schema": Waypoint.get_schema(),
            "required": True,
            "nullable": False
        },
        "required": True,
        "nullable": False
    }
}


class Lane(get_base_class(lane_template, lane_schema)):
    pass


lane_array_template = {
    "lanes": [Lane.get_template()]
}

lane_array_schema = {
    "lanes": {
        "type": "list",
        "valueschema": {
            "type": "dict",
            "schema": Lane.get_schema(),
            "required": True,
            "nullable": False
        },
        "required": True,
        "nullable": False
    }
}


class LaneArray(get_base_class(lane_array_template, lane_array_schema)):
    pass


state_command_template = {
    "data": 14
}

state_command_schema = {
    "data": {
        "type": "integer",
        "required": True,
        "nullable": False
    }
}


class StateCommand(get_base_class(state_command_template, state_command_schema)):
    pass


light_color_template = {
    "header": Header.get_template(),
    "traffic_light": 0
}

light_color_schema = {
    "header": {
        "type": "dict",
        "schema": Header.get_schema(),
        "required": True,
        "nullable": False
    },
    "traffic_light": {
        "type": "integer",
        "required": True,
        "nullable": False
    }
}


class LightColor(get_base_class(light_color_template, light_color_schema)):
    pass


pose_with_covariance_template = {
    "pose": Pose.get_template(),
    "convariance": [
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
}

pose_with_covariance_schema = {
    "position": {
        "type": "dict",
        "schema": Pose.get_schema(),
        "required": True,
        "nullable": False,
    },
    "convariance": {
        "type": "list",
        "valueschema": {
            "type": "number",
            "required": True,
            "nullable": False
        },
        "required": True,
        "nullable": False,
    }
}


class PoseWithCovariance(get_base_class(pose_with_covariance_template, pose_with_covariance_schema)):
    pass


initial_pose_template = {
    "header": Header.get_template(),
    "pose": PoseWithCovariance.get_template()
}

initial_pose_schema = {
    "header": {
        "type": "dict",
        "schema": Header.get_schema(),
        "required": True,
        "nullable": False
    },
    "pose": {
        "type": "dict",
        "schema": PoseWithCovariance.get_schema(),
        "required": True,
        "nullable": False
    },
}


class InitialPose(get_base_class(initial_pose_template, initial_pose_schema)):
    pass


class ROSMessage(object):
    Header = Header
    CurrentPose = CurrentPose
    ClosestWaypoint = ClosestWaypoint
    DecisionMakerStates = DecisionMakerStates
    LaneArray = LaneArray
    StateCommand = StateCommand
    LightColor = LightColor
    LaneArray = LaneArray
    Lane = Lane
    Waypoint = Waypoint
