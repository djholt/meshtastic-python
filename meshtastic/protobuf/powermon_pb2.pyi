"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class PowerMon(google.protobuf.message.Message):
    """Note: There are no 'PowerMon' messages normally in use (PowerMons are sent only as structured logs - slogs).
    But we wrap our State enum in this message to effectively nest a namespace (without our linter yelling at us)
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _State:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PowerMon._State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CPU_DeepSleep: PowerMon._State.ValueType  # 1
        CPU_LightSleep: PowerMon._State.ValueType  # 2
        Vext1_On: PowerMon._State.ValueType  # 4
        """
        The external Vext1 power is on.  Many boards have auxillary power rails that the CPU turns on only
        occasionally.  In cases where that rail has multiple devices on it we usually want to have logging on
        the state of that rail as an independent record.
        For instance on the Heltec Tracker 1.1 board, this rail is the power source for the GPS and screen.

        The log messages will be short and complete (see PowerMon.Event in the protobufs for details).
        something like "S:PM:C,0x00001234,REASON" where the hex number is the bitmask of all current states.
        (We use a bitmask for states so that if a log message gets lost it won't be fatal)
        """
        Lora_RXOn: PowerMon._State.ValueType  # 8
        Lora_TXOn: PowerMon._State.ValueType  # 16
        Lora_RXActive: PowerMon._State.ValueType  # 32
        BT_On: PowerMon._State.ValueType  # 64
        LED_On: PowerMon._State.ValueType  # 128
        Screen_On: PowerMon._State.ValueType  # 256
        Screen_Drawing: PowerMon._State.ValueType  # 512
        Wifi_On: PowerMon._State.ValueType  # 1024
        GPS_Active: PowerMon._State.ValueType  # 2048
        """
        GPS is actively trying to find our location
        See GPSPowerState for more details
        """

    class State(_State, metaclass=_StateEnumTypeWrapper):
        """Any significant power changing event in meshtastic should be tagged with a powermon state transition.
        If you are making new meshtastic features feel free to add new entries at the end of this definition.
        """

    CPU_DeepSleep: PowerMon.State.ValueType  # 1
    CPU_LightSleep: PowerMon.State.ValueType  # 2
    Vext1_On: PowerMon.State.ValueType  # 4
    """
    The external Vext1 power is on.  Many boards have auxillary power rails that the CPU turns on only
    occasionally.  In cases where that rail has multiple devices on it we usually want to have logging on
    the state of that rail as an independent record.
    For instance on the Heltec Tracker 1.1 board, this rail is the power source for the GPS and screen.

    The log messages will be short and complete (see PowerMon.Event in the protobufs for details).
    something like "S:PM:C,0x00001234,REASON" where the hex number is the bitmask of all current states.
    (We use a bitmask for states so that if a log message gets lost it won't be fatal)
    """
    Lora_RXOn: PowerMon.State.ValueType  # 8
    Lora_TXOn: PowerMon.State.ValueType  # 16
    Lora_RXActive: PowerMon.State.ValueType  # 32
    BT_On: PowerMon.State.ValueType  # 64
    LED_On: PowerMon.State.ValueType  # 128
    Screen_On: PowerMon.State.ValueType  # 256
    Screen_Drawing: PowerMon.State.ValueType  # 512
    Wifi_On: PowerMon.State.ValueType  # 1024
    GPS_Active: PowerMon.State.ValueType  # 2048
    """
    GPS is actively trying to find our location
    See GPSPowerState for more details
    """

    def __init__(
        self,
    ) -> None: ...

global___PowerMon = PowerMon

@typing.final
class PowerStressMessage(google.protobuf.message.Message):
    """
    PowerStress testing support via the C++ PowerStress module
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Opcode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _OpcodeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PowerStressMessage._Opcode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNSET: PowerStressMessage._Opcode.ValueType  # 0
        """
        Unset/unused
        """
        PRINT_INFO: PowerStressMessage._Opcode.ValueType  # 1
        """Print board version slog and send an ack that we are alive and ready to process commands"""
        FORCE_QUIET: PowerStressMessage._Opcode.ValueType  # 2
        """Try to turn off all automatic processing of packets, screen, sleeping, etc (to make it easier to measure in isolation)"""
        END_QUIET: PowerStressMessage._Opcode.ValueType  # 3
        """Stop powerstress processing - probably by just rebooting the board"""
        SCREEN_ON: PowerStressMessage._Opcode.ValueType  # 16
        """Turn the screen on"""
        SCREEN_OFF: PowerStressMessage._Opcode.ValueType  # 17
        """Turn the screen off"""
        CPU_IDLE: PowerStressMessage._Opcode.ValueType  # 32
        """Let the CPU run but we assume mostly idling for num_seconds"""
        CPU_DEEPSLEEP: PowerStressMessage._Opcode.ValueType  # 33
        """Force deep sleep for FIXME seconds"""
        CPU_FULLON: PowerStressMessage._Opcode.ValueType  # 34
        """Spin the CPU as fast as possible for num_seconds"""
        LED_ON: PowerStressMessage._Opcode.ValueType  # 48
        """Turn the LED on for num_seconds (and leave it on - for baseline power measurement purposes)"""
        LED_OFF: PowerStressMessage._Opcode.ValueType  # 49
        """Force the LED off for num_seconds"""
        LORA_OFF: PowerStressMessage._Opcode.ValueType  # 64
        """Completely turn off the LORA radio for num_seconds"""
        LORA_TX: PowerStressMessage._Opcode.ValueType  # 65
        """Send Lora packets for num_seconds"""
        LORA_RX: PowerStressMessage._Opcode.ValueType  # 66
        """Receive Lora packets for num_seconds (node will be mostly just listening, unless an external agent is helping stress this by sending packets on the current channel)"""
        BT_OFF: PowerStressMessage._Opcode.ValueType  # 80
        """Turn off the BT radio for num_seconds"""
        BT_ON: PowerStressMessage._Opcode.ValueType  # 81
        """Turn on the BT radio for num_seconds"""
        WIFI_OFF: PowerStressMessage._Opcode.ValueType  # 96
        """Turn off the WIFI radio for num_seconds"""
        WIFI_ON: PowerStressMessage._Opcode.ValueType  # 97
        """Turn on the WIFI radio for num_seconds"""
        GPS_OFF: PowerStressMessage._Opcode.ValueType  # 112
        """Turn off the GPS radio for num_seconds"""
        GPS_ON: PowerStressMessage._Opcode.ValueType  # 113
        """Turn on the GPS radio for num_seconds"""

    class Opcode(_Opcode, metaclass=_OpcodeEnumTypeWrapper):
        """
        What operation would we like the UUT to perform.
        note: senders should probably set want_response in their request packets, so that they can know when the state
        machine has started processing their request
        """

    UNSET: PowerStressMessage.Opcode.ValueType  # 0
    """
    Unset/unused
    """
    PRINT_INFO: PowerStressMessage.Opcode.ValueType  # 1
    """Print board version slog and send an ack that we are alive and ready to process commands"""
    FORCE_QUIET: PowerStressMessage.Opcode.ValueType  # 2
    """Try to turn off all automatic processing of packets, screen, sleeping, etc (to make it easier to measure in isolation)"""
    END_QUIET: PowerStressMessage.Opcode.ValueType  # 3
    """Stop powerstress processing - probably by just rebooting the board"""
    SCREEN_ON: PowerStressMessage.Opcode.ValueType  # 16
    """Turn the screen on"""
    SCREEN_OFF: PowerStressMessage.Opcode.ValueType  # 17
    """Turn the screen off"""
    CPU_IDLE: PowerStressMessage.Opcode.ValueType  # 32
    """Let the CPU run but we assume mostly idling for num_seconds"""
    CPU_DEEPSLEEP: PowerStressMessage.Opcode.ValueType  # 33
    """Force deep sleep for FIXME seconds"""
    CPU_FULLON: PowerStressMessage.Opcode.ValueType  # 34
    """Spin the CPU as fast as possible for num_seconds"""
    LED_ON: PowerStressMessage.Opcode.ValueType  # 48
    """Turn the LED on for num_seconds (and leave it on - for baseline power measurement purposes)"""
    LED_OFF: PowerStressMessage.Opcode.ValueType  # 49
    """Force the LED off for num_seconds"""
    LORA_OFF: PowerStressMessage.Opcode.ValueType  # 64
    """Completely turn off the LORA radio for num_seconds"""
    LORA_TX: PowerStressMessage.Opcode.ValueType  # 65
    """Send Lora packets for num_seconds"""
    LORA_RX: PowerStressMessage.Opcode.ValueType  # 66
    """Receive Lora packets for num_seconds (node will be mostly just listening, unless an external agent is helping stress this by sending packets on the current channel)"""
    BT_OFF: PowerStressMessage.Opcode.ValueType  # 80
    """Turn off the BT radio for num_seconds"""
    BT_ON: PowerStressMessage.Opcode.ValueType  # 81
    """Turn on the BT radio for num_seconds"""
    WIFI_OFF: PowerStressMessage.Opcode.ValueType  # 96
    """Turn off the WIFI radio for num_seconds"""
    WIFI_ON: PowerStressMessage.Opcode.ValueType  # 97
    """Turn on the WIFI radio for num_seconds"""
    GPS_OFF: PowerStressMessage.Opcode.ValueType  # 112
    """Turn off the GPS radio for num_seconds"""
    GPS_ON: PowerStressMessage.Opcode.ValueType  # 113
    """Turn on the GPS radio for num_seconds"""

    CMD_FIELD_NUMBER: builtins.int
    NUM_SECONDS_FIELD_NUMBER: builtins.int
    cmd: global___PowerStressMessage.Opcode.ValueType
    """
    What type of HardwareMessage is this?
    """
    num_seconds: builtins.float
    def __init__(
        self,
        *,
        cmd: global___PowerStressMessage.Opcode.ValueType = ...,
        num_seconds: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cmd", b"cmd", "num_seconds", b"num_seconds"]) -> None: ...

global___PowerStressMessage = PowerStressMessage
