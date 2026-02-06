' VBS Script to setup AI Attendance System as auto-start task
' Right-click and choose "Run as administrator" 
' Or double-click if you have admin privileges

Dim objFSO, objShell, taskName, scriptPath, workDir

Set objShell = CreateObject("WScript.Shell")

taskName = "AI_Attendance_System"
scriptPath = """C:\AI_Attendance_App\start-background.bat"""
workDir = "C:\AI_Attendance_App"

' Create the scheduled task command
Dim cmd
cmd = "schtasks /create /tn " & taskName & " /tr " & scriptPath & " /sc onstart /rl highest /f"

' Execute the command
On Error Resume Next
objShell.Run cmd, 0, True

If Err.Number <> 0 Then
    MsgBox "Error: " & Err.Description & vbCrLf & "Please run as Administrator!", vbCritical, "Error"
    Err.Clear
Else
    MsgBox "✅ Task Scheduler configured successfully!" & vbCrLf & vbCrLf & "AI Attendance System will now start automatically on boot.", vbInformation, "Success"
End If

On Error Goto 0
