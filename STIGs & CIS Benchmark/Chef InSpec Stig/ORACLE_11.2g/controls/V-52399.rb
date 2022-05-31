# encoding: utf-8

control "V-52399" do
	title "OS accounts utilized to run external procedures called by the DBMS must have limited privileges."
	desc "This requirement is intended to limit exposure due to operating from within a privileged account or role. The inclusion of role is intended to address those situations where an access control policy, such as Role Based Access Control (RBAC) is being implemented and where a change of role provides the same degree of assurance in the change of access authorizations for both the user and all processes acting on behalf of the user as would be provided by a change between a privileged and non-privileged account. 

To limit exposure when operating from within a privileged account or role, the application must support organizational requirements that users of information system accounts, or roles, with access to organization-defined lists of security functions or security-relevant information, use non-privileged accounts, or roles, when accessing other (non-security) system functions.

Use of privileged accounts for non-administrative purposes puts data at risk of unintended or unauthorized loss, modification, or exposure. In particular, DBA accounts if used for non-administration application development or application maintenance can lead to miss-assignment of privileges where privileges are inherited by object owners. It may also lead to loss or compromise of application data where the elevated privileges bypass controls designed in and provided by applications.

External applications called or spawned by the DBMS process may be executed under OS accounts with unnecessary privileges. This can lead to unauthorized access to OS resources and compromise of the OS, the DBMS or any other services provided by the host platform.false"
	impact 0.5
	tag "check": "Determine which OS accounts are used by the DBMS to run external procedures. Validate that these OS accounts have only the privileges necessary to perform the required functionality. If any OS accounts, utilized by the database for running external procedures, have privileges beyond those required for running the external procedures, this is a finding.

System views providing privilege information are:
DBA_SYS_PRIVS
DBA_TAB_PRIVS
DBA_ROLE_PRIVS"
	tag "fix": "Limit privileges to DBMS-related OS accounts to those required to perform their DBMS specific functionality."

	# Write Check Logic Here

end