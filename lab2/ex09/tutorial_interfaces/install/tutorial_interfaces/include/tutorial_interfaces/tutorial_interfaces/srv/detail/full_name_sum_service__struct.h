// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from tutorial_interfaces:srv/FullNameSumService.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__SRV__DETAIL__FULL_NAME_SUM_SERVICE__STRUCT_H_
#define TUTORIAL_INTERFACES__SRV__DETAIL__FULL_NAME_SUM_SERVICE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'last_name'
// Member 'name'
// Member 'first_name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/FullNameSumService in the package tutorial_interfaces.
typedef struct tutorial_interfaces__srv__FullNameSumService_Request
{
  rosidl_runtime_c__String last_name;
  rosidl_runtime_c__String name;
  rosidl_runtime_c__String first_name;
} tutorial_interfaces__srv__FullNameSumService_Request;

// Struct for a sequence of tutorial_interfaces__srv__FullNameSumService_Request.
typedef struct tutorial_interfaces__srv__FullNameSumService_Request__Sequence
{
  tutorial_interfaces__srv__FullNameSumService_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__srv__FullNameSumService_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'full_name'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/FullNameSumService in the package tutorial_interfaces.
typedef struct tutorial_interfaces__srv__FullNameSumService_Response
{
  rosidl_runtime_c__String full_name;
} tutorial_interfaces__srv__FullNameSumService_Response;

// Struct for a sequence of tutorial_interfaces__srv__FullNameSumService_Response.
typedef struct tutorial_interfaces__srv__FullNameSumService_Response__Sequence
{
  tutorial_interfaces__srv__FullNameSumService_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__srv__FullNameSumService_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TUTORIAL_INTERFACES__SRV__DETAIL__FULL_NAME_SUM_SERVICE__STRUCT_H_
