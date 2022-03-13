For this challenge we need to go index patterns and search for ip logs:

```
10.0.2.15
```

For the new user that was created we look down and check various logs:

```
malware_attacker
```

We were asked to provide the payload use by the attacker. When searching
on pattern discover with:

```
event.action : "Process Create (rule: ProcessCreate)" and winlog.event_data.ParentUser : *malware*
```

We are seeing this command which was the answer:

```
"C:\Windows\System32\Wbem\WMIC.exe" process call create malware
```

We are asked to provide the name of the utility used by our security team. Looking into logs
we notice various stuff with `winlogbeat` and `sysmon`. Googling them we notice that those are
monitoring utilities we try `Winlogbeat` and `Sysmon`. The latter was the answer.
