# encoding: utf-8
#
control "V-72283" do
  title "The system must not forward Internet Protocol version 4 (IPv4)
source-routed packets."
  desc  "Source-routed packets allow the source of the packet to suggest that
routers forward the packet along a different path than configured on the
router, which can be used to bypass network security measures. This requirement
applies only to the forwarding of source-routed traffic, such as when IPv4
forwarding is enabled and the system is functioning as a router."
  impact 0.5
  tag "check": "Verify the system does not accept IPv4 source-routed packets.

Check the value of the accept source route variable with the following command:

# /sbin/sysctl -a | grep  net.ipv4.conf.all.accept_source_route
net.ipv4.conf.all.accept_source_route=0

If the returned line does not have a value of \"0\", a line is not returned, or
the returned line is commented out, this is a finding."
  tag "fix": "Set the system to the required kernel parameter by adding the
following line to \"/etc/sysctl.conf\" (or modify the line to have the required
value):

net.ipv4.conf.all.accept_source_route = 0"

  describe kernel_parameter('net.ipv4.conf.all.accept_source_route') do
    its('value') { should eq 0 }
  end
end