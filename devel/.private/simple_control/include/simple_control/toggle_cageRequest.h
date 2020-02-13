// Generated by gencpp from file simple_control/toggle_cageRequest.msg
// DO NOT EDIT!


#ifndef SIMPLE_CONTROL_MESSAGE_TOGGLE_CAGEREQUEST_H
#define SIMPLE_CONTROL_MESSAGE_TOGGLE_CAGEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace simple_control
{
template <class ContainerAllocator>
struct toggle_cageRequest_
{
  typedef toggle_cageRequest_<ContainerAllocator> Type;

  toggle_cageRequest_()
    : cage_on(false)  {
    }
  toggle_cageRequest_(const ContainerAllocator& _alloc)
    : cage_on(false)  {
  (void)_alloc;
    }



   typedef uint8_t _cage_on_type;
  _cage_on_type cage_on;





  typedef boost::shared_ptr< ::simple_control::toggle_cageRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::simple_control::toggle_cageRequest_<ContainerAllocator> const> ConstPtr;

}; // struct toggle_cageRequest_

typedef ::simple_control::toggle_cageRequest_<std::allocator<void> > toggle_cageRequest;

typedef boost::shared_ptr< ::simple_control::toggle_cageRequest > toggle_cageRequestPtr;
typedef boost::shared_ptr< ::simple_control::toggle_cageRequest const> toggle_cageRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::simple_control::toggle_cageRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::simple_control::toggle_cageRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace simple_control

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::simple_control::toggle_cageRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::simple_control::toggle_cageRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::simple_control::toggle_cageRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::simple_control::toggle_cageRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::simple_control::toggle_cageRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::simple_control::toggle_cageRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::simple_control::toggle_cageRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "820030dea9a8caa8250c04fcd974f946";
  }

  static const char* value(const ::simple_control::toggle_cageRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x820030dea9a8caa8ULL;
  static const uint64_t static_value2 = 0x250c04fcd974f946ULL;
};

template<class ContainerAllocator>
struct DataType< ::simple_control::toggle_cageRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "simple_control/toggle_cageRequest";
  }

  static const char* value(const ::simple_control::toggle_cageRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::simple_control::toggle_cageRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool cage_on\n\
";
  }

  static const char* value(const ::simple_control::toggle_cageRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::simple_control::toggle_cageRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.cage_on);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct toggle_cageRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::simple_control::toggle_cageRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::simple_control::toggle_cageRequest_<ContainerAllocator>& v)
  {
    s << indent << "cage_on: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.cage_on);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SIMPLE_CONTROL_MESSAGE_TOGGLE_CAGEREQUEST_H
