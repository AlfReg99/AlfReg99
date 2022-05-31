# encoding: utf-8

control "V-92675" do
	title "The Apache web server must separate the hosted applications from hosted Apache web server management functionality."
	desc "The separation of user functionality from web server management can be accomplished by moving management functions to a separate IP address or port. To further separate the management functions, separate authentication methods and certificates should be used.

By moving the management functionality, the possibility of accidental discovery of the management functions by non-privileged users during hosted application use is minimized.false"
	impact 0.5
	tag "check": "Review the web server documentation and deployed configuration to determine whether hosted application functionality is separated from web server management functions.

If the functions are not separated, this is a finding."
	tag "fix": "Configure Apache to separate the hosted applications from web server management functionality."

	# Write Check Logic Here

end