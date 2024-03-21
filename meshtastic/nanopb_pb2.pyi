"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Custom options for defining:
- Maximum size of string/bytes
- Maximum number of elements in array

These are used by nanopb to generate statically allocable structures
for memory-limited environments.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.descriptor_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.internal.extension_dict
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _FieldType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FieldTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FieldType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    FT_DEFAULT: _FieldType.ValueType  # 0
    """Automatically decide field type, generate static field if possible."""
    FT_CALLBACK: _FieldType.ValueType  # 1
    """Always generate a callback field."""
    FT_POINTER: _FieldType.ValueType  # 4
    """Always generate a dynamically allocated field."""
    FT_STATIC: _FieldType.ValueType  # 2
    """Generate a static field or raise an exception if not possible."""
    FT_IGNORE: _FieldType.ValueType  # 3
    """Ignore the field completely."""
    FT_INLINE: _FieldType.ValueType  # 5
    """Legacy option, use the separate 'fixed_length' option instead"""

class FieldType(_FieldType, metaclass=_FieldTypeEnumTypeWrapper): ...

FT_DEFAULT: FieldType.ValueType  # 0
"""Automatically decide field type, generate static field if possible."""
FT_CALLBACK: FieldType.ValueType  # 1
"""Always generate a callback field."""
FT_POINTER: FieldType.ValueType  # 4
"""Always generate a dynamically allocated field."""
FT_STATIC: FieldType.ValueType  # 2
"""Generate a static field or raise an exception if not possible."""
FT_IGNORE: FieldType.ValueType  # 3
"""Ignore the field completely."""
FT_INLINE: FieldType.ValueType  # 5
"""Legacy option, use the separate 'fixed_length' option instead"""
global___FieldType = FieldType

class _IntSize:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _IntSizeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_IntSize.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    IS_DEFAULT: _IntSize.ValueType  # 0
    """Default, 32/64bit based on type in .proto"""
    IS_8: _IntSize.ValueType  # 8
    IS_16: _IntSize.ValueType  # 16
    IS_32: _IntSize.ValueType  # 32
    IS_64: _IntSize.ValueType  # 64

class IntSize(_IntSize, metaclass=_IntSizeEnumTypeWrapper): ...

IS_DEFAULT: IntSize.ValueType  # 0
"""Default, 32/64bit based on type in .proto"""
IS_8: IntSize.ValueType  # 8
IS_16: IntSize.ValueType  # 16
IS_32: IntSize.ValueType  # 32
IS_64: IntSize.ValueType  # 64
global___IntSize = IntSize

class _TypenameMangling:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _TypenameManglingEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TypenameMangling.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    M_NONE: _TypenameMangling.ValueType  # 0
    """Default, no typename mangling"""
    M_STRIP_PACKAGE: _TypenameMangling.ValueType  # 1
    """Strip current package name"""
    M_FLATTEN: _TypenameMangling.ValueType  # 2
    """Only use last path component"""
    M_PACKAGE_INITIALS: _TypenameMangling.ValueType  # 3
    """Replace the package name by the initials"""

class TypenameMangling(_TypenameMangling, metaclass=_TypenameManglingEnumTypeWrapper): ...

M_NONE: TypenameMangling.ValueType  # 0
"""Default, no typename mangling"""
M_STRIP_PACKAGE: TypenameMangling.ValueType  # 1
"""Strip current package name"""
M_FLATTEN: TypenameMangling.ValueType  # 2
"""Only use last path component"""
M_PACKAGE_INITIALS: TypenameMangling.ValueType  # 3
"""Replace the package name by the initials"""
global___TypenameMangling = TypenameMangling

class _DescriptorSize:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DescriptorSizeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DescriptorSize.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DS_AUTO: _DescriptorSize.ValueType  # 0
    """Select minimal size based on field type"""
    DS_1: _DescriptorSize.ValueType  # 1
    """1 word; up to 15 byte fields, no arrays"""
    DS_2: _DescriptorSize.ValueType  # 2
    """2 words; up to 4095 byte fields, 4095 entry arrays"""
    DS_4: _DescriptorSize.ValueType  # 4
    """4 words; up to 2^32-1 byte fields, 2^16-1 entry arrays"""
    DS_8: _DescriptorSize.ValueType  # 8
    """8 words; up to 2^32-1 entry arrays"""

class DescriptorSize(_DescriptorSize, metaclass=_DescriptorSizeEnumTypeWrapper): ...

DS_AUTO: DescriptorSize.ValueType  # 0
"""Select minimal size based on field type"""
DS_1: DescriptorSize.ValueType  # 1
"""1 word; up to 15 byte fields, no arrays"""
DS_2: DescriptorSize.ValueType  # 2
"""2 words; up to 4095 byte fields, 4095 entry arrays"""
DS_4: DescriptorSize.ValueType  # 4
"""4 words; up to 2^32-1 byte fields, 2^16-1 entry arrays"""
DS_8: DescriptorSize.ValueType  # 8
"""8 words; up to 2^32-1 entry arrays"""
global___DescriptorSize = DescriptorSize

@typing_extensions.final
class NanoPBOptions(google.protobuf.message.Message):
    """This is the inner options message, which basically defines options for
    a field. When it is used in message or file scope, it applies to all
    fields.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAX_SIZE_FIELD_NUMBER: builtins.int
    MAX_LENGTH_FIELD_NUMBER: builtins.int
    MAX_COUNT_FIELD_NUMBER: builtins.int
    INT_SIZE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    LONG_NAMES_FIELD_NUMBER: builtins.int
    PACKED_STRUCT_FIELD_NUMBER: builtins.int
    PACKED_ENUM_FIELD_NUMBER: builtins.int
    SKIP_MESSAGE_FIELD_NUMBER: builtins.int
    NO_UNIONS_FIELD_NUMBER: builtins.int
    MSGID_FIELD_NUMBER: builtins.int
    ANONYMOUS_ONEOF_FIELD_NUMBER: builtins.int
    PROTO3_FIELD_NUMBER: builtins.int
    PROTO3_SINGULAR_MSGS_FIELD_NUMBER: builtins.int
    ENUM_TO_STRING_FIELD_NUMBER: builtins.int
    FIXED_LENGTH_FIELD_NUMBER: builtins.int
    FIXED_COUNT_FIELD_NUMBER: builtins.int
    SUBMSG_CALLBACK_FIELD_NUMBER: builtins.int
    MANGLE_NAMES_FIELD_NUMBER: builtins.int
    CALLBACK_DATATYPE_FIELD_NUMBER: builtins.int
    CALLBACK_FUNCTION_FIELD_NUMBER: builtins.int
    DESCRIPTORSIZE_FIELD_NUMBER: builtins.int
    DEFAULT_HAS_FIELD_NUMBER: builtins.int
    INCLUDE_FIELD_NUMBER: builtins.int
    EXCLUDE_FIELD_NUMBER: builtins.int
    PACKAGE_FIELD_NUMBER: builtins.int
    TYPE_OVERRIDE_FIELD_NUMBER: builtins.int
    SORT_BY_TAG_FIELD_NUMBER: builtins.int
    FALLBACK_TYPE_FIELD_NUMBER: builtins.int
    max_size: builtins.int
    """Allocated size for 'bytes' and 'string' fields.
    For string fields, this should include the space for null terminator.
    """
    max_length: builtins.int
    """Maximum length for 'string' fields. Setting this is equivalent
    to setting max_size to a value of length+1.
    """
    max_count: builtins.int
    """Allocated number of entries in arrays ('repeated' fields)"""
    int_size: global___IntSize.ValueType
    """Size of integer fields. Can save some memory if you don't need
    full 32 bits for the value.
    """
    type: global___FieldType.ValueType
    """Force type of field (callback or static allocation)"""
    long_names: builtins.bool
    """Use long names for enums, i.e. EnumName_EnumValue."""
    packed_struct: builtins.bool
    """Add 'packed' attribute to generated structs.
    Note: this cannot be used on CPUs that break on unaligned
    accesses to variables.
    """
    packed_enum: builtins.bool
    """Add 'packed' attribute to generated enums."""
    skip_message: builtins.bool
    """Skip this message"""
    no_unions: builtins.bool
    """Generate oneof fields as normal optional fields instead of union."""
    msgid: builtins.int
    """integer type tag for a message"""
    anonymous_oneof: builtins.bool
    """decode oneof as anonymous union"""
    proto3: builtins.bool
    """Proto3 singular field does not generate a "has_" flag"""
    proto3_singular_msgs: builtins.bool
    """Force proto3 messages to have no "has_" flag.
    This was default behavior until nanopb-0.4.0.
    """
    enum_to_string: builtins.bool
    """Generate an enum->string mapping function (can take up lots of space)."""
    fixed_length: builtins.bool
    """Generate bytes arrays with fixed length"""
    fixed_count: builtins.bool
    """Generate repeated field with fixed count"""
    submsg_callback: builtins.bool
    """Generate message-level callback that is called before decoding submessages.
    This can be used to set callback fields for submsgs inside oneofs.
    """
    mangle_names: global___TypenameMangling.ValueType
    """Shorten or remove package names from type names.
    This option applies only on the file level.
    """
    callback_datatype: builtins.str
    """Data type for storage associated with callback fields."""
    callback_function: builtins.str
    """Callback function used for encoding and decoding.
    Prior to nanopb-0.4.0, the callback was specified in per-field pb_callback_t
    structure. This is still supported, but does not work inside e.g. oneof or pointer
    fields. Instead, a new method allows specifying a per-message callback that
    will be called for all callback fields in a message type.
    """
    descriptorsize: global___DescriptorSize.ValueType
    """Select the size of field descriptors. This option has to be defined
    for the whole message, not per-field. Usually automatic selection is
    ok, but if it results in compilation errors you can increase the field
    size here.
    """
    default_has: builtins.bool
    """Set default value for has_ fields."""
    @property
    def include(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Extra files to include in generated `.pb.h`"""
    @property
    def exclude(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Automatic includes to exclude from generated `.pb.h`
        Same as nanopb_generator.py command line flag -x.
        """
    package: builtins.str
    """Package name that applies only for nanopb."""
    type_override: google.protobuf.descriptor_pb2.FieldDescriptorProto.Type.ValueType
    """Override type of the field in generated C code. Only to be used with related field types"""
    sort_by_tag: builtins.bool
    """Due to historical reasons, nanopb orders fields in structs by their tag number
    instead of the order in .proto. Set this to false to keep the .proto order.
    The default value will probably change to false in nanopb-0.5.0.
    """
    fallback_type: global___FieldType.ValueType
    """Set the FT_DEFAULT field conversion strategy.
    A field that can become a static member of a c struct (e.g. int, bool, etc)
    will be a a static field.
    Fields with dynamic length are converted to either a pointer or a callback.
    """
    def __init__(
        self,
        *,
        max_size: builtins.int | None = ...,
        max_length: builtins.int | None = ...,
        max_count: builtins.int | None = ...,
        int_size: global___IntSize.ValueType | None = ...,
        type: global___FieldType.ValueType | None = ...,
        long_names: builtins.bool | None = ...,
        packed_struct: builtins.bool | None = ...,
        packed_enum: builtins.bool | None = ...,
        skip_message: builtins.bool | None = ...,
        no_unions: builtins.bool | None = ...,
        msgid: builtins.int | None = ...,
        anonymous_oneof: builtins.bool | None = ...,
        proto3: builtins.bool | None = ...,
        proto3_singular_msgs: builtins.bool | None = ...,
        enum_to_string: builtins.bool | None = ...,
        fixed_length: builtins.bool | None = ...,
        fixed_count: builtins.bool | None = ...,
        submsg_callback: builtins.bool | None = ...,
        mangle_names: global___TypenameMangling.ValueType | None = ...,
        callback_datatype: builtins.str | None = ...,
        callback_function: builtins.str | None = ...,
        descriptorsize: global___DescriptorSize.ValueType | None = ...,
        default_has: builtins.bool | None = ...,
        include: collections.abc.Iterable[builtins.str] | None = ...,
        exclude: collections.abc.Iterable[builtins.str] | None = ...,
        package: builtins.str | None = ...,
        type_override: google.protobuf.descriptor_pb2.FieldDescriptorProto.Type.ValueType | None = ...,
        sort_by_tag: builtins.bool | None = ...,
        fallback_type: global___FieldType.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["anonymous_oneof", b"anonymous_oneof", "callback_datatype", b"callback_datatype", "callback_function", b"callback_function", "default_has", b"default_has", "descriptorsize", b"descriptorsize", "enum_to_string", b"enum_to_string", "fallback_type", b"fallback_type", "fixed_count", b"fixed_count", "fixed_length", b"fixed_length", "int_size", b"int_size", "long_names", b"long_names", "mangle_names", b"mangle_names", "max_count", b"max_count", "max_length", b"max_length", "max_size", b"max_size", "msgid", b"msgid", "no_unions", b"no_unions", "package", b"package", "packed_enum", b"packed_enum", "packed_struct", b"packed_struct", "proto3", b"proto3", "proto3_singular_msgs", b"proto3_singular_msgs", "skip_message", b"skip_message", "sort_by_tag", b"sort_by_tag", "submsg_callback", b"submsg_callback", "type", b"type", "type_override", b"type_override"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["anonymous_oneof", b"anonymous_oneof", "callback_datatype", b"callback_datatype", "callback_function", b"callback_function", "default_has", b"default_has", "descriptorsize", b"descriptorsize", "enum_to_string", b"enum_to_string", "exclude", b"exclude", "fallback_type", b"fallback_type", "fixed_count", b"fixed_count", "fixed_length", b"fixed_length", "include", b"include", "int_size", b"int_size", "long_names", b"long_names", "mangle_names", b"mangle_names", "max_count", b"max_count", "max_length", b"max_length", "max_size", b"max_size", "msgid", b"msgid", "no_unions", b"no_unions", "package", b"package", "packed_enum", b"packed_enum", "packed_struct", b"packed_struct", "proto3", b"proto3", "proto3_singular_msgs", b"proto3_singular_msgs", "skip_message", b"skip_message", "sort_by_tag", b"sort_by_tag", "submsg_callback", b"submsg_callback", "type", b"type", "type_override", b"type_override"]) -> None: ...

global___NanoPBOptions = NanoPBOptions

NANOPB_FILEOPT_FIELD_NUMBER: builtins.int
NANOPB_MSGOPT_FIELD_NUMBER: builtins.int
NANOPB_ENUMOPT_FIELD_NUMBER: builtins.int
NANOPB_FIELD_NUMBER: builtins.int
nanopb_fileopt: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[google.protobuf.descriptor_pb2.FileOptions, global___NanoPBOptions]
nanopb_msgopt: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[google.protobuf.descriptor_pb2.MessageOptions, global___NanoPBOptions]
nanopb_enumopt: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[google.protobuf.descriptor_pb2.EnumOptions, global___NanoPBOptions]
nanopb: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[google.protobuf.descriptor_pb2.FieldOptions, global___NanoPBOptions]
