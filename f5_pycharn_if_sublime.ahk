;160903 press f5, chrome will refresh


;whether S.T. is active, if yes, f5 will save and send f5 to Chrome
#IfWinActive, ahk_class PX_WINDOW_CLASS

	F4::
	send,^a
	sleep,100
	send,^v
	return

	F5::
	st_save()
	sleep, 500
	run()
	return
#If

st_save(){
	send,^s
}

run(){
	win_title = ahk_class SunAwtFrame
	;win_title = ahk_class Chrome_WidgetWin_1


	IfWinExist, %win_title%
	{
		WinActivate, %win_title%
		send,{esc}
		send,^+{f10}
 
		WinActivate, ahk_class PX_WINDOW_CLASS
	    
	}else{
		MsgBox "Window >>>"+%win_title%+"<<< not exist"
	}
}