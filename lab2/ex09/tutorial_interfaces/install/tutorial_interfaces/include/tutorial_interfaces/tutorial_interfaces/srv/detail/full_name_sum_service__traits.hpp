// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from tutorial_interfaces:srv/FullNameSumService.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__SRV__DETAIL__FULL_NAME_SUM_SERVICE__TRAITS_HPP_
#define TUTORIAL_INTERFACES__SRV__DETAIL__FULL_NAME_SUM_SERVICE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "tutorial_interfaces/srv/detail/full_name_sum_service__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace tutorial_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const FullNameSumService_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: last_name
  {
    out << "last_name: ";
    rosidl_generator_traits::value_to_yaml(msg.last_name, out);
    out << ", ";
  }

  // member: name
  {
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << ", ";
  }

  // member: first_name
  {
    out << "first_name: ";
    rosidl_generator_traits::value_to_yaml(msg.first_name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FullNameSumService_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: last_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "last_name: ";
    rosidl_generator_traits::value_to_yaml(msg.last_name, out);
    out << "\n";
  }

  // member: name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << "\n";
  }

  // member: first_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "first_name: ";
    rosidl_generator_traits::value_to_yaml(msg.first_name, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FullNameSumService_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace tutorial_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use tutorial_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const tutorial_interfaces::srv::FullNameSumService_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  tutorial_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use tutorial_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const tutorial_interfaces::srv::FullNameSumService_Request & msg)
{
  return tutorial_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<tutorial_interfaces::srv::FullNameSumService_Request>()
{
  return "tutorial_interfaces::srv::FullNameSumService_Request";
}

template<>
inline const char * name<tutorial_interfaces::srv::FullNameSumService_Request>()
{
  return "tutorial_interfaces/srv/FullNameSumService_Request";
}

template<>
struct has_fixed_size<tutorial_interfaces::srv::FullNameSumService_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<tutorial_interfaces::srv::FullNameSumService_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<tutorial_interfaces::srv::FullNameSumService_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace tutorial_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const FullNameSumService_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: full_name
  {
    out << "full_name: ";
    rosidl_generator_traits::value_to_yaml(msg.full_name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FullNameSumService_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: full_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "full_name: ";
    rosidl_generator_traits::value_to_yaml(msg.full_name, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FullNameSumService_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace tutorial_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use tutorial_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const tutorial_interfaces::srv::FullNameSumService_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  tutorial_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use tutorial_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const tutorial_interfaces::srv::FullNameSumService_Response & msg)
{
  return tutorial_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<tutorial_interfaces::srv::FullNameSumService_Response>()
{
  return "tutorial_interfaces::srv::FullNameSumService_Response";
}

template<>
inline const char * name<tutorial_interfaces::srv::FullNameSumService_Response>()
{
  return "tutorial_interfaces/srv/FullNameSumService_Response";
}

template<>
struct has_fixed_size<tutorial_interfaces::srv::FullNameSumService_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<tutorial_interfaces::srv::FullNameSumService_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<tutorial_interfaces::srv::FullNameSumService_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<tutorial_interfaces::srv::FullNameSumService>()
{
  return "tutorial_interfaces::srv::FullNameSumService";
}

template<>
inline const char * name<tutorial_interfaces::srv::FullNameSumService>()
{
  return "tutorial_interfaces/srv/FullNameSumService";
}

template<>
struct has_fixed_size<tutorial_interfaces::srv::FullNameSumService>
  : std::integral_constant<
    bool,
    has_fixed_size<tutorial_interfaces::srv::FullNameSumService_Request>::value &&
    has_fixed_size<tutorial_interfaces::srv::FullNameSumService_Response>::value
  >
{
};

template<>
struct has_bounded_size<tutorial_interfaces::srv::FullNameSumService>
  : std::integral_constant<
    bool,
    has_bounded_size<tutorial_interfaces::srv::FullNameSumService_Request>::value &&
    has_bounded_size<tutorial_interfaces::srv::FullNameSumService_Response>::value
  >
{
};

template<>
struct is_service<tutorial_interfaces::srv::FullNameSumService>
  : std::true_type
{
};

template<>
struct is_service_request<tutorial_interfaces::srv::FullNameSumService_Request>
  : std::true_type
{
};

template<>
struct is_service_response<tutorial_interfaces::srv::FullNameSumService_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // TUTORIAL_INTERFACES__SRV__DETAIL__FULL_NAME_SUM_SERVICE__TRAITS_HPP_
