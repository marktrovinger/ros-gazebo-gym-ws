// Generated by gencpp from file panda_gazebo/AddBox.msg
// DO NOT EDIT!


#ifndef PANDA_GAZEBO_MESSAGE_ADDBOX_H
#define PANDA_GAZEBO_MESSAGE_ADDBOX_H

#include <ros/service_traits.h>


#include <panda_gazebo/AddBoxRequest.h>
#include <panda_gazebo/AddBoxResponse.h>


namespace panda_gazebo
{

struct AddBox
{

typedef AddBoxRequest Request;
typedef AddBoxResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct AddBox
} // namespace panda_gazebo


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::panda_gazebo::AddBox > {
  static const char* value()
  {
    return "33a045cab11c556ad20e54d951c3d3de";
  }

  static const char* value(const ::panda_gazebo::AddBox&) { return value(); }
};

template<>
struct DataType< ::panda_gazebo::AddBox > {
  static const char* value()
  {
    return "panda_gazebo/AddBox";
  }

  static const char* value(const ::panda_gazebo::AddBox&) { return value(); }
};


// service_traits::MD5Sum< ::panda_gazebo::AddBoxRequest> should match
// service_traits::MD5Sum< ::panda_gazebo::AddBox >
template<>
struct MD5Sum< ::panda_gazebo::AddBoxRequest>
{
  static const char* value()
  {
    return MD5Sum< ::panda_gazebo::AddBox >::value();
  }
  static const char* value(const ::panda_gazebo::AddBoxRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::panda_gazebo::AddBoxRequest> should match
// service_traits::DataType< ::panda_gazebo::AddBox >
template<>
struct DataType< ::panda_gazebo::AddBoxRequest>
{
  static const char* value()
  {
    return DataType< ::panda_gazebo::AddBox >::value();
  }
  static const char* value(const ::panda_gazebo::AddBoxRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::panda_gazebo::AddBoxResponse> should match
// service_traits::MD5Sum< ::panda_gazebo::AddBox >
template<>
struct MD5Sum< ::panda_gazebo::AddBoxResponse>
{
  static const char* value()
  {
    return MD5Sum< ::panda_gazebo::AddBox >::value();
  }
  static const char* value(const ::panda_gazebo::AddBoxResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::panda_gazebo::AddBoxResponse> should match
// service_traits::DataType< ::panda_gazebo::AddBox >
template<>
struct DataType< ::panda_gazebo::AddBoxResponse>
{
  static const char* value()
  {
    return DataType< ::panda_gazebo::AddBox >::value();
  }
  static const char* value(const ::panda_gazebo::AddBoxResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // PANDA_GAZEBO_MESSAGE_ADDBOX_H
