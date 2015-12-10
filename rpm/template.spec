Name:           ros-indigo-moveit-simple-grasps
Version:        1.3.1
Release:        1%{?dist}
Summary:        ROS moveit_simple_grasps package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/davetcoleman/moveit_simple_grasps/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-moveit-msgs
Requires:       ros-indigo-moveit-visual-tools
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-eigen-conversions
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-moveit-core
BuildRequires:  ros-indigo-moveit-msgs
BuildRequires:  ros-indigo-moveit-ros-planning
BuildRequires:  ros-indigo-moveit-ros-planning-interface
BuildRequires:  ros-indigo-moveit-visual-tools
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-tf-conversions
BuildRequires:  ros-indigo-trajectory-msgs

%description
A basic grasp generator for simple objects such as blocks or cylinders for use
with the MoveIt! pick and place pipeline. Does not consider friction cones or
other dynamics.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Dec 10 2015 Dave Coleman <davetcoleman@gmail.com> - 1.3.1-1
- Autogenerated by Bloom

* Mon Dec 07 2015 Dave Coleman <davetcoleman@gmail.com> - 1.3.1-0
- Autogenerated by Bloom

* Sat Dec 05 2015 Dave Coleman <davetcoleman@gmail.com> - 1.3.0-0
- Autogenerated by Bloom

* Mon Oct 27 2014 Dave Coleman <davetcoleman@gmail.com> - 1.2.1-0
- Autogenerated by Bloom

* Fri Sep 19 2014 Dave Coleman <davetcoleman@gmail.com> - 1.2.0-1
- Autogenerated by Bloom

* Fri Sep 19 2014 Dave Coleman <davetcoleman@gmail.com> - 1.2.0-0
- Autogenerated by Bloom

* Thu Jul 31 2014 Dave Coleman <davetcoleman@gmail.com> - 1.1.0-0
- Autogenerated by Bloom

