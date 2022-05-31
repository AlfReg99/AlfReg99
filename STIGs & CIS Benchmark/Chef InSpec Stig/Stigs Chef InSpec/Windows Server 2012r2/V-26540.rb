# encoding: utf-8
# copyright: 2016, you
# license: All rights reserved
# date: 2016-06-08
# description: The Windows Server 2012 / 2012 R2 Member Server Security Technical Implementation Guide (STIG) is published as a tool to improve the security of Department of Defense (DoD) information systems. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.
# impacts
title 'V-26540 - The system must be configured to audit Logon/Logoff - Logoff successes.'
control 'V-26540' do
  impact 0.5
  title 'The system must be configured to audit Logon/Logoff - Logoff successes.'
  desc 'Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks.  Audit logs are necessary to provide a trail of evidence in case the system or network is compromised.  Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior.  Logoff records user logoffs.  If this is an interactive logoff, it is recorded on the local system.  If it is to a network share, it is recorded on the system accessed.'
  tag 'stig', 'V-26540'
  tag severity: 'medium'
  tag checkid: 'C-47303r1_chk'
  tag fixid: 'F-45923r1_fix'
  tag version: 'WN12-AU-000045'
  tag ruleid: 'SV-52996r2_rule'
  tag fixtext: 'Configure the policy value for Computer Configuration -> Windows Settings -> Security Settings -> Advanced Audit Policy Configuration -> System Audit Policies -> Logon/Logoff -> "Audit Logoff" with "Success" selected.'
  tag checktext: 'Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (V-14230) for the detailed auditing subcategories to be effective. 

Use the AuditPol tool to review the current Audit Policy configuration:
-Open a Command Prompt with elevated privileges ("Run as Administrator").
-Enter "AuditPol /get /category:*".

Compare the AuditPol settings with the following.  If the system does not audit the following, this is a finding.

Logon/Logoff -> Logoff - Success'

# START_DESCRIBE V-26540
      describe file('') do
      it "is a pending example"
    end

# STOP_DESCRIBE V-26540

end

