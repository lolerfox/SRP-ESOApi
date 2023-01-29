#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

F1::
WinActivate , SRP ESO
return
F2::
WinSet, AlwaysOnTop, On, SRP ESO
WinActivate , SRP ESO
return
F3::
WinActivate , SRP ESO
WinSet, AlwaysOnTop, Off, SRP ESO
WinMinimize , SRP ESO
return