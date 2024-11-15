// Generated by gencpp from file panda_gazebo/AddPlane.msg
// DO NOT EDIT!


#ifndef PANDA_GAZEBO_MESSAGE_ADDPLANE_H
#define PANDA_GAZEBO_MESSAGE_ADDPLANE_H

#include <ros/service_traits.h>


#include <panda_gazebo/AddPlaneRequest.h>
#include <panda_gazebo/AddPlaneResponse.h>


namespace panda_gazebo
{

struct AddPlane
{

typedef AddPlaneRequest Request;
typedef AddPlaneResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct AddPlane
} // namespace panda_gazebo


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::panda_gazebo::AddPlane > {
  static const char* value()
  {
    return "df1995ac0ca0010f12d98c831ff22d85";
  }

  static const char* value(const ::panda_gazebo::AddPlane&) { return value(); }
};

template<>
struct DataType< ::panda_gazebo::AddPlane > {
  static const char* value()
  {
    return "panda_gazebo/AddPlane";
  }

  static const char* value(const ::panda_gazebo::AddPlane&) { return value(); }
};


// service_traits::MD5Sum< ::panda_gazebo::AddPlaneRequest> should match
// service_traits::MD5Sum< ::panda_gazebo::AddPlane >
template<>
struct MD5Sum< ::panda_gazebo::AddPlaneRequest>
{
  static const char* value()
  {
    return MD5Sum< ::panda_gazebo::AddPlane >::value();
  }
  static const char* value(const ::panda_gazebo::AddPlaneRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::panda_gazebo::AddPlaneRequest> should match
// service_traits::DataType< ::panda_gazebo::AddPlane >
template<>
struct DataType< ::panda_gazebo::AddPlaneRequest>
{
  static const char* value()
  {
    return DataType< ::panda_gazebo::AddPlane >::value();
  }
  static const char* value(const ::panda_gazebo::AddPlaneRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::panda_gazebo::AddPlaneResponse> should match
// service_traits::MD5Sum< ::panda_gazebo::AddPlane >
template<>
struct MD5Sum< ::panda_gazebo::AddPlaneResponse>
{
  static const char* value()
  {
    return MD5Sum< ::panda_gazebo::AddPlane >::value();
  }
  static const char* value(const ::panda_gazebo::AddPlaneResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::panda_gazebo::AddPlaneResponse> should match
// service_traits::DataType< ::panda_gazebo::AddPlane >
template<>
struct DataType< ::panda_gazebo::AddPlaneResponse>
{
  static const char* value()
  {
    return DataType< ::panda_gazebo::AddPlane >::value();
  }
  static const char* value(const ::panda_gazebo::AddPlaneResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // PANDA_GAZEBO_MESSAGE_ADDPLANE_H
