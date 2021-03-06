# encoding: UTF-8

control 'V-92809' do
  title 'The Apache web server must set an absolute timeout for sessions.'
  desc  "Leaving sessions open indefinitely is a major security risk. An
attacker can easily use an already authenticated session to access the hosted
application as the previously authenticated user. By closing sessions after an
absolute period of time, the user is forced to reauthenticate, guaranteeing the
session is still in use. Enabling an absolute timeout for sessions closes
sessions that are still active. Examples would be a runaway process accessing
the Apache web server or an attacker using a hijacked session to slowly probe
the Apache web server."
  desc  'rationale', ''
  desc  'check', "
    Determine the location of the \"HTTPD_ROOT\" directory and the
\"httpd.conf\" file:

    # httpd -V | egrep -i 'httpd_root|server_config_file'
    -D HTTPD_ROOT=\"/etc/httpd\"
    -D SERVER_CONFIG_FILE=\"conf/httpd.conf\"

    Verify the \"SessionMaxAge\" directive exists and is set to \"600\".

    If the \"SessionMaxAge\" directive does not exist, this is a finding.

    If the \"SessionMaxAge\" directive exists but is not set to \"600\", this
is a finding.
  "
  desc  'fix', "
    Determine the location of the \"HTTPD_ROOT\" directory and the
\"httpd.conf\" file:

    # httpd -V | egrep -i 'httpd_root|server_config_file'
    -D HTTPD_ROOT=\"/etc/httpd\"
    -D SERVER_CONFIG_FILE=\"conf/httpd.conf\"

    Add or set the \"SessionMaxAge\" directive to \"600\".
  "
  impact 0.5
  tag severity: 'medium'
  tag gtitle: 'SRG-APP-000295-WSR-000012'
  tag gid: 'V-92809'
  tag rid: 'SV-102897r1_rule'
  tag stig_id: 'AS24-U2-000650'
  tag fix_id: 'F-99053r1_fix'
  tag cci: ['CCI-002361']
  tag nist: ['AC-12']
end

