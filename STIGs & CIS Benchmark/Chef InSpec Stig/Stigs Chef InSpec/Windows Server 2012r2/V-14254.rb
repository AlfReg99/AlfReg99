# encoding: utf-8
# copyright: 2016, you
# license: All rights reserved
# date: 2016-06-08
# description: The Windows Server 2012 / 2012 R2 Member Server Security Technical Implementation Guide (STIG) is published as a tool to improve the security of Department of Defense (DoD) information systems. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.
# impacts
title 'V-14254 - Client computers must be required to authenticate for RPC communication.'
control 'V-14254' do
  impact 0.5
  title 'Client computers must be required to authenticate for RPC communication.'
  desc 'Configuring RPC to require authentication to the RPC Endpoint Mapper will force clients to provide authentication before RPC communication is established.'
  tag 'stig', 'V-14254'
  tag severity: 'medium'
  tag checkid: 'C-47295r3_chk'
  tag fixid: 'F-45915r3_fix'
  tag version: 'WN12-CC-000063-MS'
  tag ruleid: 'SV-52989r2_rule'
  tag fixtext: 'Configure the policy value for Computer Configuration >> Administrative Templates >> System >> Remote Procedure Call >> "Enable RPC Endpoint Mapper Client Authentication" to "Enabled".'
  tag checktext: 'If the following registry value does not exist or is not configured as specified, this is a finding:

Registry Hive: HKEY_LOCAL_MACHINE
Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Rpc\

Value Name: EnableAuthEpResolution

Value Type: REG_DWORD
Value: 1'

# START_DESCRIBE V-14254
  
    describe registry_key({
      hive: 'HKEY_LOCAL_MACHINE',
      key:  'SOFTWARE\Policies\Microsoft\Windows NT\Rpc',
    }) do
      its("EnableAuthEpResolution") { should eq 1 }
    end

# STOP_DESCRIBE V-14254

end

