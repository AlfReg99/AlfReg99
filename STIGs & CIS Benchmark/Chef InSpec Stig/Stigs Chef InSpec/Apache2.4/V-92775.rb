# encoding: UTF-8

control 'V-92775' do
  title "The Apache web server must allow mappings to unused and vulnerable
scripts to be removed."
  desc  "Scripts allow server-side processing on behalf of the hosted
application user or as processes needed in the implementation of hosted
applications. Removing scripts not needed for application operation or deemed
vulnerable helps to secure the web server.

    To ensure scripts are not added to the web server and run maliciously,
script mappings that are not needed or used by the web server for hosted
application operation must be removed.
  "
  desc  'rationale', ''
  desc  'check', "
    Determine the location of the \"HTTPD_ROOT\" directory and the
\"httpd.conf\" file:

    # httpd -V | egrep -i 'httpd_root|server_config_file'
    -D HTTPD_ROOT=\"/etc/httpd\"
    -D SERVER_CONFIG_FILE=\"conf/httpd.conf\"

    Review \"Script\", \"ScriptAlias\" or \"ScriptAliasMatch\", or
\"ScriptInterpreterSource\" directives.

    Go into each directory and locate \"cgi-bin\" files.

    If any scripts are present that are not needed for application operation,
this is a finding.

    If this is not documented and approved by the Information System Security
Officer (ISSO), this is a finding.
  "
  desc  'fix', "
    Determine the location of the \"HTTPD_ROOT\" directory and the
\"httpd.conf\" file:

    # httpd -V | egrep -i 'httpd_root|server_config_file'
    -D HTTPD_ROOT=\"/etc/httpd\"
    -D SERVER_CONFIG_FILE=\"conf/httpd.conf\"

    Remove any scripts in \"cgi-bin\" directory if they are not needed for
application operation.

    Ensure this process is documented and approved by the ISSO.
  "
  impact 0.5
  tag severity: 'medium'
  tag gtitle: 'SRG-APP-000141-WSR-000082'
  tag gid: 'V-92775'
  tag rid: 'SV-102863r1_rule'
  tag stig_id: 'AS24-U2-000310'
  tag fix_id: 'F-99019r1_fix'
  tag cci: ['CCI-000381']
  tag nist: ['CM-7 a']
end

